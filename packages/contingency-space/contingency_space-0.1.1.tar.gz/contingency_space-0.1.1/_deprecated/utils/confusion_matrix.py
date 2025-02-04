import pandas as pd


class CM:
    """
    Confusion matrix class for binary problems.
    """
    def __init__(self, table: dict):
        """
        The class constructor.

        :param table: a dictionary with 4 keys (tp, fn, tn, fp) and their corresponding
        values representing a confusion matrix.
        """
        self.table = table #the matrix with all 4 values
        self.tp = table['tp'] #true positives
        self.fn = table['fn'] #false negatives
        self.tn = table['tn'] #true negatives
        self.fp = table['fp'] #false positives
        self.n = self.tn + self.fp #all negatives
        self.p = self.tp + self.fn #all positives

    def normalize(self):
        """
        normalizes all entries of the confusion matrix.

        :return: None.
        """
        cm_normalized = {
            'tn': self.tn / self.n if self.n != 0 else 0,
            'fp': self.fp / self.n if self.n != 0 else 0,
            'tp': self.tp / self.p if self.p != 0 else 0,
            'fn': self.fn / self.p if self.p != 0 else 0
        }
        self.__init__(cm_normalized)

    def __repr__(self):
        d = {'TP': self.tp, 'FN': self.fn, 'TN': self.tn, 'FP': self.fp}
        return str(pd.DataFrame.from_dict(d, orient='index').T)

