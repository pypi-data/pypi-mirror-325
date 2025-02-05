from typing import Optional, List

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from dreamml.validation.wrappers._wrapper_catboost import _CatBoostWrapper
from dreamml.validation.wrappers._wrapper_lightgbm import _LightGBMWrapper
from dreamml.validation.wrappers._wrapper_xgboost import _XGBoostWrapper
from dreamml.validation.wrappers._wrapper_automl import _WBAutoMLWrapper

models_wrappers = dict(
    lightgbm=_LightGBMWrapper,
    xgboost=_XGBoostWrapper,
    catboost=_CatBoostWrapper,
    autowoe=_WBAutoMLWrapper,
)


class _CalibrationWrapper(BaseEstimator, TransformerMixin):
    """
    Универсальный объект `estimator` для откалиброванной модели.
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
        self.model = estimator.model.estimator
        self.model_wrapper_class = [
            v for k, v in models_wrappers.items() if k in self.model.__module__
        ][-1]
        self.model_wrapper = self.model_wrapper_class(
            self.model, used_features, categorical_features
        )
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
        X_ = self.model_wrapper._validate_input_data(X)

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
        params = self.model_wrapper.get_estimator_params

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

        shap_values, shap_importance = self.model_wrapper.get_shap_importance(X)

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
        if type(data) == tuple:
            data = data[0]
        if hasattr(self.estimator, "transform"):
            return self.estimator.transform(data)