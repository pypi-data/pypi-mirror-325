from typing import Optional, List

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

from lightautoml.dataset.np_pd_dataset import NumpyDataset


class _WBAutoMLWrapper(BaseEstimator, TransformerMixin):
    """
    Универсальный объект `estimator` для WhiteBox AutoML.
    Используется для вычисления валидационных тестов и
    подготовки отчета.

    Parameters
    ----------
    estimator: callable
        Объект типа estimator, после применения метода `fit`.

    used_features: List[str], optional, default = None
        Список используемых признаков.

    categorical_features: List[str], optional, default = None
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

    @property
    def get_estimator_params(self):
        params_dict = self.estimator.__dict__
        estimator_params = params_dict["_params"]

        return estimator_params

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
            Пустой список, не используется, поскольку метод SHAP-values
            не адаптирован для WhiteBox AutoML.

        shap_importance: pd.DataFrame, shape = [n_features, 2]
            Матрица важности признаков.

        """
        shap_values = []

        shap_importance = pd.DataFrame(
            {
                "feature": self.estimator.features_fit.index,
                "importance": self.estimator.features_fit.values,
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
        if hasattr(self.estimator, "transform"):
            prediction = self.estimator.transform(X)
        elif hasattr(self.estimator, "predict_proba"):
            try:
                prediction = self.estimator.predict_proba(X)
            except AssertionError:
                prediction = self.estimator.predict(X)
        else:
            prediction = self.estimator.predict(X)

        prediction = prediction.data if isinstance(prediction, NumpyDataset) else prediction

        if self.task in ["binary", "regression"]:
            return prediction[:, 0]
        elif self.task == "multiclass":
            return prediction
        else:
            raise ValueError(f"Задача {self.task} не поддерживается.")