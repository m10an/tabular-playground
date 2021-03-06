from typing import Any
from sklearn.linear_model import LinearRegression
from numpy import ndarray
import numpy as np

__all__ = ['ConstantModel', 'LinearRegressionModel']


class Model:
    def train(self, x: ndarray, y: ndarray, **kwargs):
        ...

    def predict(self, x: ndarray, **kwargs):
        ...


class SciKitModel(Model):
    _model: Any

    def train(self, x: ndarray, y: ndarray, **kwargs):
        self._model.fit(x, y, **kwargs)

    def predict(self, x: ndarray, **kwargs):
        return self._model.predict(x, **kwargs)


class ConstantModel(Model):
    def __init__(self, constant=0.5):
        self._constant = constant

    def train(self, x: ndarray, y: ndarray, **kwargs):
        pass

    def predict(self, x: ndarray, **kwargs):
        return np.zeros(x.shape[0]) + self._constant


class LinearRegressionModel(SciKitModel):
    def __init__(self, **kwargs):
        self._model = LinearRegression(**kwargs)
