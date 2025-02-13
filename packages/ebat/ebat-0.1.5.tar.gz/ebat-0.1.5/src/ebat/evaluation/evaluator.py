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

    def evaluate(
        self, authenticator, id_data=None, auth_data=None, verbose=1, plots=False
    ):
        results = {}
        if id_data:
            results |= self.identification(authenticator, id_data)
        if auth_data:
            results |= self.authentication(authenticator, auth_data)
        return results

    def identification(self, authenticator, id_data):
        X_test = id_data.X
        y_test = list(np.argmax(id_data.y, axis=1))

        y_pred = np.argmax(authenticator.identification(X_test), axis=1)
        acc = accuracy_score(y_test, y_pred)
        prec, rec, f1, _ = precision_recall_fscore_support(
            y_test, y_pred, average="macro", zero_division=0
        )
        mcc = matthews_corrcoef(y_test, y_pred)
        return {"acc": acc, "prec": prec, "rec": rec, "f1": f1, "mcc": mcc}

    def authentication(self, authenticator, auth_data):
        # 0, 1 vector of ground truth (0 — auth user, 1 attackers)
        y_true = np.argmax(auth_data.y, axis=1)
        # Probability of positive class (auth user) as required by det_curve.
        y_scores = authenticator.authentication(auth_data.X)
        y_pred = [x[0] for x in y_scores]
        far, frr, thresholds = det_curve(y_true, y_pred, pos_label=0)

        deltas = [abs(x - y) for x, y in zip(far, frr)]
        min_i = np.argmin(deltas)
        eer = (far[min_i] + frr[min_i]) / 2
        return {"far": far, "frr": frr, "thresholds": thresholds, "eer": eer}
