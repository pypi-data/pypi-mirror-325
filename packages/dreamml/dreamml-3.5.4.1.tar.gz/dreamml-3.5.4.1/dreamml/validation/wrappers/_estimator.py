from typing import Optional, List

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

from dreamml.validation.wrappers._wrapper_catboost import _CatBoostWrapper
from dreamml.validation.wrappers._wrapper_lightgbm import _LightGBMWrapper
from dreamml.validation.wrappers._wrapper_xgboost import _XGBoostWrapper
from dreamml.validation.wrappers._wrapper_automl import _WBAutoMLWrapper
from dreamml.validation.wrappers._wrapper_calibration import _CalibrationWrapper
from dreamml.validation.wrappers._wrapper_pyboost import _PyBoostWrapper
from dreamml.validation.wrappers._wrapper_logreg import _LogRegWrapper


# FIXME: выглядит как лишний уровень абстракции, уже имеются классы estimator для каждой модели
class Estimator(BaseEstimator, TransformerMixin):
    """
    Универсальный объект `estimator` для вычисления
    валидационных тестов и подготовки отчета.

    Parameters
    ----------
    estimator: callable
        Объект типа estimator, после применения метода `fit`.

    log_target_transformer: dreamml.features.feature_extraction.__transformers
        LogTargetTransformer - трансформер целевой переменной.

    images_dir_path: str, optional, default = None
        Путь для сохранения изображений.

    used_features: List[str], optional = None
        Список используемых признаков.

    categorical_features: List[str], optional = None
        Список используемых категориальных признаков.

    """

    def __init__(
        self,
        estimator: callable,
        vectorizer: callable = None,
        log_target_transformer=None,
        used_features: Optional[List[str]] = None,
        categorical_features: Optional[List[str]] = None,
        task: str = "binary",
        metric_name: str = "gini",
    ):
        self.estimator = estimator
        self.vectorizer = vectorizer
        self.used_features = used_features
        self.categorical_features = categorical_features
        self.task = task
        self.metric_name = metric_name
        self.log_target_transformer = log_target_transformer
        self.wrapper = self._init_wrapper()

    def _init_wrapper(self):
        """
        Инициализация конкретного объекта `estimator`.
        Инициализация проводится на основе типа аргумента
        self.estimator.

        """
        if "lightgbm" in self.estimator.__module__:
            return _LightGBMWrapper(
                self.estimator,
                self.used_features,
                self.categorical_features,
                self.task,
                self.metric_name,
            )
        elif "xgboost" in self.estimator.__module__:
            return _XGBoostWrapper(
                self.estimator,
                self.used_features,
                self.categorical_features,
                self.task,
                self.metric_name,
            )
        elif "catboost" in self.estimator.__module__:
            return _CatBoostWrapper(
                self.estimator,
                self.used_features,
                self.categorical_features,
                self.task,
                self.metric_name,
            )
        elif "calibration" in self.estimator.__module__:
            return _CalibrationWrapper(
                self.estimator,
                self.used_features,
                self.categorical_features,
                self.task,
                self.metric_name,
            )
        elif "py_boost" in self.estimator.__module__:
            return _PyBoostWrapper(
                self.estimator,
                self.used_features,
                self.categorical_features,
                self.task,
            )
        elif "logistic" in self.estimator.__module__ or "pipeline" in self.estimator.__module__:
            return _LogRegWrapper(
                self.estimator,
                self.used_features,
                self.categorical_features,
                self.task,
                self.metric_name,
            )
        else:
            return _WBAutoMLWrapper(
                self.estimator,
                self.used_features,
                self.categorical_features,
                self.task,
                self.metric_name,
            )

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
        return self.wrapper.get_shap_importance(X)

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

        if self.vectorizer is not None and hasattr(self.vectorizer, "transform"):
            X = self.vectorizer.transform(X)

        y_pred_raw = self.wrapper.transform(X)
        if (
            self.log_target_transformer is not None
            and self.log_target_transformer.fitted
        ):
            y_pred = self.log_target_transformer.inverse_transform(y_pred_raw)
            return y_pred
        else:
            return y_pred_raw

    @property
    def get_estimator_params(self):
        params = pd.Series(self.wrapper.get_estimator_params)
        params = pd.DataFrame(
            {"Гиперпараметр": params.index, "Значение": params.values}
        )
        params["Значение"] = params["Значение"].astype(str)
        return params