import os

import numpy as np
from plotly import graph_objects as go
from sklearn.metrics import (
    precision_recall_fscore_support,
    accuracy_score,
    det_curve,
    matthews_corrcoef,
)


class Evaluator:

    def __init__(self, decimal_places=3, name=""):
        self.decimal_places = decimal_places
        self.name = name

        self.far = []
        self.frr = []
        self.thresholds = []

    def evaluate(self, authenticator, test_data, adver_data, verbose=1, plots=False):
        self.identification(authenticator, test_data)
        self.authentication(authenticator, adver_data)
        name = str(authenticator) if not self.name else self.name

        if verbose:
            print(
                "============================================================================="
            )
            print(f"Evaluation of {name} with the medba dataset.")
            print(
                "============================================================================="
            )
            print(
                "Classification Accuracy:",
                round(self.acc, self.decimal_places),
            )
            print("Precision:", round(self.prec, self.decimal_places))
            print("Recall:", round(self.rec, self.decimal_places))
            print("F1 Score:", round(self.f1, self.decimal_places))
            print("Equal Error Rate:", round(self.err, self.decimal_places))
            print(
                "============================================================================="
            )
        if plots:
            fig = go.Figure(
                data=[
                    go.Scatter(
                        x=self.thresholds, y=self.far, name="False Acceptance Rate"
                    ),
                    go.Scatter(
                        x=self.thresholds, y=self.frr, name="False Rejection Rate"
                    ),
                ]
            )
            fig.update_layout(
                xaxis_title="Confidence Threshold",
                yaxis_title="False Rates",
            )
            fig.show()

            fig = go.Figure(
                data=[
                    go.Scatter(x=self.far, y=1 - self.frr),
                ]
            )
            fig.update_layout(
                xaxis_title="False Acceptance Rate",
                yaxis_title="False Rejection Rate",
            )
            fig.show()
        return (
            self.acc,
            self.prec,
            self.rec,
            self.f1,
            # self.mcc,
            self.far,
            self.frr,
            self.thresholds,
            self.eer,
        )

    def identification(self, authenticator, test_data):
        X_test = test_data.X
        y_test = list(np.argmax(test_data.y, axis=1))

        y_pred = np.argmax(authenticator.identification(X_test), axis=1)
        acc = accuracy_score(y_test, y_pred)
        prec, rec, f1, _ = precision_recall_fscore_support(
            y_test, y_pred, average="macro", zero_division=0
        )
        mcc = matthews_corrcoef(y_test, y_pred)
        self.acc = acc
        self.prec = prec
        self.rec = rec
        self.f1 = f1
        self.mcc = mcc

    def authentication(self, authenticator, adver_data):
        # 0, 1 vector of ground truth (0 — auth user, 1 attackers)
        y_true = np.argmax(adver_data.y, axis=1)
        # Probability of positive class (auth user) as required by det_curve.
        y_scores = authenticator.authentication(adver_data.X)
        y_pred = [x[0] for x in y_scores]
        far, frr, thresholds = det_curve(y_true, y_pred, pos_label=0)
        self.far = far
        self.frr = frr
        self.thresholds = thresholds

        deltas = [abs(x - y) for x, y in zip(far, frr)]
        min_i = np.argmin(deltas)
        self.eer = (far[min_i] + frr[min_i]) / 2


class Comparator:

    def __init__(self, evaluators):
        self.evaluators = evaluators

    def compare(self):
        data = []
        for evaluator in self.evaluators:
            data.append(
                go.Scatter(
                    x=evaluator.far,
                    y=1 - evaluator.frr,
                    name=evaluator.name,
                ),
            )
        fig = go.Figure(data=data)
        fig.update_layout(
            xaxis_title="False Acceptance Rate",
            yaxis_title="1 - False Rejection Rate",
        )
        fig.show()
