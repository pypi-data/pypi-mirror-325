from typing import Optional, List

import shap
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class _LightGBMWrapper(BaseEstimator, TransformerMixin):
    """
    Универсальный объект `estimator` для LightGBM.
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
        try:
            params = self.estimator.get_params()
            params["n_estimators"] = self.estimator.n_estimators
        except AttributeError:
            params = self.estimator.params
            params["n_estimators"] = self.estimator.current_iteration()

        return params

    def get_shap_importance(self, X: pd.DataFrame) -> pd.DataFrame:
        """
        Вычисление важности признаков на основе SHAP-values.

        Parameters
        ----------
        X: pandas.core.frame.DataFrame
            Матрица признаков для вычисления важности признаков.

        Returns
        -------
        shap_values: np.array, shape = [n_samples, n_features]
            Матрица SHAP-values.

        shap_importance: pd.DataFrame, shape = [n_features, 2]
            Матрица важности признаков на основе SHAP-values.

        """
        if hasattr(self.estimator, "booster_"):
            self.estimator.booster_.params["objective"] = self.estimator.objective

        x = self._validate_input_data(X)
        explainer = shap.TreeExplainer(self.estimator)
        shap_values = explainer.shap_values(x)

        if isinstance(shap_values, list):
            shap_values = shap_values[0]

        shap_importance = pd.DataFrame(
            {
                "feature": list(x.columns),
                "importance": np.round(np.abs(shap_values).mean(axis=0), 5),
            }
        )
        shap_importance = shap_importance.sort_values(by="importance", ascending=False)
        shap_importance = shap_importance.reset_index(drop=True)

        return shap_values, shap_importance

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