from collections import Counter

import numpy as np


from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import datasets
from mpl_toolkits.mplot3d import Axes3D




class ClassificationMetrics:
    def accuracy(y_true, y_pred):
        accuracy = np.sum(y_true == y_pred) / len(y_true)  # Calculate accuracy as ratio of correct predictions
        return accuracy


class RegressionMetrics:
    def mean_squared_error(y_true, y_pred):
        return np.mean((np.array(y_true) - np.array(y_pred)) ** 2)