import copy
import pandas as pd
import numpy as np
import numpy.typing as npt
from typing import Callable

# this is an edit placed here in notepad.


class ConfusionMatrix:
    """
    Confusion matrix class for multi-class problems.
    """
    def __init__(self, table: dict[str, list[int]]={}):
        """
        The class constructor.

        An example of a confusion matrix for multiple classes ('a', 'b', and 'c')
        is given below::

                          (pred)
                         a   b   c
                       ____________
                    a  | ta  fb  fc
             (real) b  | fa  tb  fc
                    c  | fa  fb  tc

        which should be input as a dictionary as follows::

             {'a': [ta, fb, fc],
              'b': [fa, tb, fc],
              'c': [fa, fb, tc]}



        :param __table: a dictionary with all class names as keys and their corresponding frequencies
        as values.
        """
        
        self.__table = copy.deepcopy(table)
        self.__num_classes = len(self.__table)
        
        for row in self.__table.values():
            if len(row) != self.__num_classes:
                raise ValueError('Length of each row must be equal to the number of classes.')
        
        self.class_freqs = {}
        for k, v in self.__table.items():
            self.class_freqs.update({k: int(np.sum(np.array(v)))})
        self.dim = len(self.class_freqs.keys())

    def add_class(self, cls: str, values: list[int]) -> None:
        """Adds a row to the matrix. Do not use this function unless you are building
        a matrix from scratch.

        Args:
            cls (str): The name of the class being added.
            values (list[int]): Values of the row.
        """
        self.__table.update({cls: values})
        self.class_freqs.update({cls: int(np.sum(np.array(values)))})
        self.__num_classes += 1
        
    def normalize(self):
        """
        Normalizes all entries of the confusion matrix::
        
                           (pred)                           (pred)
                         a   b   c                        a   b   c
                       ____________                      ____________
                    a  | 30  60  10      =>          a  |0.3 0.6 0.1
             (real) b  | 60  20  20      =>   (real) b  |0.6 0.2 0.2
                    c  | 30  20  50      =>          c  |0.3 0.2 0.5
        """
        
        
        cm_normalized = {}
        for k, freqs in self.__table.items():
            norm_freqs = [e / self.class_freqs[k] if self.class_freqs[k] != 0 else 0 for e in freqs]
            cm_normalized.update({k: norm_freqs})
        self.__init__(cm_normalized)

    def get_total_true(self, per_class: bool = False) -> int | dict[str, int]:
        """ Returns the total number of true classifications in the matrix.
        
        Args:
            per_class (bool): Whether to return the number of true classifications per class. Defaults to False.
        Returns:
            int: sum of the counts along the diagonal of the table.
        """
        a = np.array(list(self.__table.values()))
        
        match per_class:
            case True:
                
                return_dict: dict[str, int] = {}
                
                preds = a.diagonal()
                for cls, val in zip(self.__table.keys(), preds):
                    return_dict.update({cls: val})
                
                return return_dict
            case False:
                return np.sum(a.diagonal())
            case _:
                raise ValueError('per_class must be either True or False.')

    def get_wrong_classifications(self, cls: str = None) -> dict[str, int] | int:
        """
        For each class i, the total amount of false classifications is the sum of the counts in column i, except the one on the diagonal. 
        For binary classification, this will return the number of false positives in the matrix.
        
        In terms of a classification problem, this is the number of times that the model predicted a class, when the real value was a different one. 
        
        For example, given a matrix::
        
                           (pred)
                         a   b   c
                       ____________
                    a  | ta  fba fca
             (real) b  | fab tb  fcb
                    c  | fac fbc tc
                    
        The values would be returned like so::
        
                    {'a': (fab + fac),
                     'b': (fba + fbc),
                     'c': (fca + fcb)}

        Args:
            cls (str, optional): 
                The class for which you wish to find the number of false classifications. If left blank, this function will return a list of false classifications by class.

        Returns:
            list[int] | int: 
                -list[int]: List of the number of false classifications by class.
                -int:       The total number of false classifications for the specified class.
        """
        
        
        matrix = np.array(list(self.__table.values()))
        keys = list(self.__table.keys())
        
        diagonal_mask = np.eye(len(matrix), dtype=bool) #create a mask for the diagonal of the matrix.
        
        if cls is None:
            
            #return the sum of all values in the matrix, except for the diagonal.
            matrix_without_hits = matrix * (1 - diagonal_mask)
            
            summed_list = np.sum(matrix_without_hits, axis=0)
            
            summed_dict = {cls: value for cls, value in zip(self.__table.keys(), summed_list)}
            
            return summed_dict
        else:
            try:
                column_index = keys.index(cls)
            except:
                raise ValueError(f'The class {cls} was not found in this matrix.')
            
            
            #return the sum of all values in the matrix, except for the diagonal.
            return matrix[:, column_index][~diagonal_mask[:, column_index]].sum()
            
    def get_missed_classifications(self, cls: str = None) -> list[int] | int:
        """
        For each class i, the total amount of missed classifications is the sum of the counts in row i, except the one on the diagonal. 
        For binary classification, this will return the number of false negatives in the matrix.
        
        In terms of a classification problem, this is the number of times that the model a different class than the one given. 
        
        For example, given a matrix::
        
                           (pred)
                         a   b   c
                       ____________
                    a  | ta  fba fca
             (real) b  | fab tb  fcb
                    c  | fac fbc tc
                    
        The values would like like so::
        
                    {'a': (fba + fca),
                     'b': (fab + fcb),
                     'c': (fac + fbc)}

        Args:
            cls (str, optional): 
                The class for which you wish to find the number of missed classifications. If left blank, this function will return a list of missed classifications by class. Defaults to None.

        Returns:
            result: list[int] | int: 
                -list[int]: List of the number of missed classifications by class.
                -int:       The total number of missed classifications for the specified class.
        """
        
        matrix = np.array(list(self.__table.values()))
        keys = list(self.__table.keys())
        
        #create a diagonal mask for the matrix
        diagonal_mask = np.eye(len(matrix), dtype=bool)
        
        if cls is None:
            
            #return list of misses per class.
            
            matrix_without_hits = matrix * (1 - diagonal_mask)
            
            return np.sum(matrix_without_hits, axis=1)
        else:
            try:
                row_index = keys.index(cls)
            except:
                raise ValueError(f'The class {cls} was not found in this matrix.')
                
            #return sum of all values within the row, excluding the diagonal
            return matrix[row_index, :][~diagonal_mask[row_index, :]].sum()

    def get_matrix(self):
        return np.array(list(self.__table.values()))

    def vector(self, return_type: tuple | list = tuple, metric: Callable[[], float]=None) -> tuple[float, ...] | list[float]:
        """Returns a tuple representing the position of the confusion matrix within a contingency space. 
        
        Args:
        
            return_type (tuple | list): 
                The type of structure you wish the point to be returned as. Defaults to tuple.
            metric: (Callable[[ConfusionMatrix], float]): 
                A function that takes in a ConfusionMatrix, and returns a float representing an evaluation score for the metric. 

        Returns:
            c (tuple[int, ...] | list[int]): The tuple taking the form (x1, x2, ..., xk), where k is the number of classes.
        """
        
        rates = []
        cm = np.array(list(self.__table.values()))
        
        total_real = np.sum(cm, axis=1) #the total # of instances of each class.
        true_pred = cm.diagonal() #the list of # of times the model classifications each class correctly.
        
        
        for real, pred in zip(total_real, true_pred): #create each coordinate
            rates.append(pred / real)
            
        rates.reverse() # flip to (tnr, tpr)
            
        if metric is not None:
            if metric.__module__.startswith('sklearn'):
                true_labels, predicted_labels = self.labels()
                rates.append(true_labels, predicted_labels)
            else:
                rates.append(metric(self))
        
        return return_type(rates)
    
    def num_samples(self, per_class:bool = False):
        """Returns the total number of samples in the matrix.

        Args:
            per_class (bool, optional): Whether or not to return the number of samples per class. Defaults to False.
        """
        
        arr = np.array(list(self.__table.values()))
        
        if per_class == True:
            return np.sum(arr, axis=1)
        return np.sum(np.array(list(self.__table.values())))
    
    def array(self) -> npt.NDArray:
        """Returns the matrix as a numpy array.

        Returns:
            npt.NDArray: A numpy array representation of the ConfusionMatrix.
        """
        return np.array(list(self.__table.values()))
    
    def labels(self) -> tuple[list[int], list[int]]:
        """
        Returns the true and predicted labels in the form of a tuple.
        
        Extracts and returns the true and predicted labels from the confusion matrix.
        The method iterates over the confusion matrix stored in `self.table`, where the keys are the actual labels and the values are lists of counts corresponding to predicted labels. It constructs two lists: one for the true labels and one for the predicted labels, by repeating each label according to its count in the confusion matrix.

        Returns:
            tuple[list[int], list[int]]: A tuple containing two lists: the first list contains the true labels, and the second list contains the predicted labels.
        """
        
        
        true_labels = []
        predicted_labels = []

        for actual_label, counts in self.table.items():
            for predicted_index, count in enumerate(counts):
                predicted_label = list(self.table.keys())[predicted_index]
                true_labels.extend([actual_label] * count)
                predicted_labels.extend([predicted_label] * count)

        return true_labels, predicted_labels

    
    @property
    def matrix(self):
        return self.__table
    @matrix.getter
    def matrix(self):
        return self.__table
    @matrix.setter
    def matrix(self, new_table = dict[str, list[int]]):
        if len(new_table) != len(self.__table):
            raise ValueError("New matrix must be the same size as the old matrix.")
        if set(self.__table.keys()) != set(new_table.keys()):
            raise ValueError("New matrix must contain the same classes as the previous matrix.")
        for row in new_table.values():
            if len(row) != self.__num_classes:
                raise ValueError("Number of elements in each row must match the number of classes in the original matrix.")
            
        self.__table = new_table
    
    @property
    def num_classes(self):
        return self.__num_classes
        

    def __repr__(self) -> str:
        #called when printing the object
        df = pd.DataFrame.from_dict(self.__table, orient='index', columns=self.__table.keys())
        df.index = self.__table.keys()
        return str(df)
    
    def __getitem__(self, index: str, give_index: bool = False):
        
        if index in self.__table:
            return self.__table[index]
        
        if self.num_classes == 2:
            if index.__contains__('t') or index.__contains__('p'):
                for i, cls in enumerate(self.__table.keys()):
                    if cls.__contains__('t') or cls.__contains__('p'):
                        if give_index == True:
                            return (self.__table[cls], i)
                        return self.__table[cls]
            if index.__contains__('f') or index.__contains__('n'):
                for i, cls in enumerate(self.__table.keys()):
                    if cls.__contains__('f') or cls.__contains('n'):
                        if give_index == True:
                            return (self.__table[cls], i)
                        return self.__table[cls]
                    
        raise IndexError(f'Class "{index}" not found within the confusion matrix.')
    
    def __eq__(self, other) -> bool:
        """Compares this CM with another CM. 
        
        Returns whether the frequencies in this matrix match the frequencies of
        another matrix.

        Args:
            other (CM): 
                The other matrix that will be compared with this one.

        Returns:
            bool: 
                Returns True if the frequencies of the given matrices match, and
                False if they do not.
        """
        if other.__class__ is self.__class__:
            for this_freq, that_freq in zip(self.class_freqs, other.class_freqs):
                if this_freq != that_freq:
                    return False
            return True
        else:
            return NotImplemented
        
    
if __name__ == "__main__":
    matrix_1 = ConfusionMatrix({
        'a': [30, 60, 10],
        'b': [20, 70, 10],
        'c': [40, 20, 40]
    })
    
    matrix_1.vector()
    