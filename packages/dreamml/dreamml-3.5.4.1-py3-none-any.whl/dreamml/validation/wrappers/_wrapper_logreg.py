from typing import Optional, List

import json

import shap
import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import LogisticRegression


class _LogRegWrapper(BaseEstimator, TransformerMixin):
    """
    Универсальный объект `estimator` для LogReg.
    Используется для вычисления валидационных тестов и
    подготовки отчета.

    Parameters
    ----------
    estimator: callable
        Объект типа estimator, после применения метода `fit`.

    used_features: List[str], optional = None
        Список используемых признаков.

    categorical_features: List[str], optional = None
        Список используемых категориальных признаков.

    """

    def __init__(
        self,
        estimator: callable,
        used_features: Optional[List[str]] = None,
        categorical_features: Optional[List[str]] = None,
        task: str = "binary",
        metric_name: str = "gini",
    ):
        self.estimator = estimator
        self.used_features = used_features
        self.categorical_features = categorical_features
        self.task = task
        self.metric_name = metric_name

    def _validate_input_data(self, X):
        """
        Подготовка данных для передачи в модель.
        Подготовка данных заключается в отборе требуемых
        признаков для применения модели.

        Parameters
        ----------
        X: pandas.core.frame.DataFrame
            Матрица признаков для применения модели.

        Returns
        -------
        X_transformed: pandas.core.frame
            Матрица признаков для передачи в модель.

        """
        if self.used_features:
            X_ = X[self.used_features]
        else:
            X_ = X.copy()

        return X_

    @property
    def get_estimator_params(self):
        """
        Получение гиперпараметров модели.

        Returns
        -------
        params: dict
            Словарь гиперпараметров модели.

        """
        params = self.estimator.get_params()
        params["eval_metric"] = self.metric_name.upper()
        return params

    def transform(self, X):
        """
        Применение модели к данным X.

        Parameters
        ----------
        X: pandas.core.frame.DataFrame
            Матрица признаков для применения модели.

        Returns
        -------
        y_pred: np.array
            Прогнозы модели на выборке Х.

        """
        data = self._validate_input_data(X)
        data = self._fill_nan_values(data)
        if hasattr(self.estimator, "transform"):
            return self.estimator.transform(data)
        elif hasattr(self.estimator, "predict_proba"):
            predicts = self.estimator.predict_proba(data)
            return (
                predicts
                if self.task in ("multiclass", "multilabel")
                else predicts[:, 1]
            )
        else:
            return self.estimator.predict(data)

    def _fill_nan_values(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Метод для заполнения NaN значений.
        Используем для log_reg, linear_reg, поскольку данные модели
        не имеют автоматической предобработки NaN значений, в отличие
        от catboost, xgboost, lightgbm
        """
        self.fillna_strategy = "mean"
        used_features = self.used_features if self.used_features else data.columns
        for feature in used_features:
            if isinstance(self.fillna_strategy, (int, float)):
                fill_value = self.fillna_strategy
            elif self.fillna_strategy == "mean":
                fill_value = float(data[feature].fillna(value=0).mean())
            elif self.fillna_strategy == "median":
                fill_value = float(data[feature].fillna(value=0).median())
            else:
                fill_value = 0
            data[feature] = data[feature].fillna(value=fill_value)
        return data