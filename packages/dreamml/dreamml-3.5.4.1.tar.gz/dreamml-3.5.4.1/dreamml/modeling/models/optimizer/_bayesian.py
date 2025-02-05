"""
Модуль с реализацией оптимизатора BayesianOptimization, для
ML-моделей с зафиксированным для DreamML, API.

Доступные классы:
- BayesianOptimizationModel: реализация оптимизатора BayesianOptimization.

"""

from typing import Tuple

import pandas as pd
from bayes_opt import BayesianOptimization

from dreamml.logging import get_logger
from dreamml.modeling.models.estimators import BoostingBaseModel
from dreamml.modeling.cv import make_cv
from dreamml.modeling.metrics import BaseMetric

_logger = get_logger(__name__)


class BayesianOptimizator:
    def __init__(self, params_bounds, model):
        self.model = model
        self.params_bounds = params_bounds
        self._logger = model._logger or _logger

    @staticmethod
    def check_param_value(params: dict) -> dict:
        """
        Проверка значений гиперпараметров на валидность.
        Некоторые гиперпараметры могут принимать только целые
        значений, для таких гиперпараметров - проверяется их
        значение и, при необходимости, происходит преобразованье
        в int-тип.

        Parameters
        ----------
        params: dict
            Словарь гиперпараметров, ключ словаря - название
            гиперпараметра, значение - значение гиперпараметра.

        Returns
        -------
        valid_params: dict
            Провалидированный словарь гиперпараметров.

        """
        check_params = [
            "max_depth",
            "num_leaves",
            "min_data_in_leaf",
            "min_child_samples",
            "subsample_for_bin",
            "n_estimators",
        ]
        for name in check_params:
            if params.get(name, None):
                params[name] = int(params[name])
        return params


class BayesianOptimizationModel(BayesianOptimizator):
    """
    Байесовская оптимизация ML-моделей для DreamML.

    Parameters
    ----------
    model: BoostingBaseModel
        Экземпляр модели со стандартизованным API для DreamML.

    metric: BaseMetric
        Метрика для оценки качества модели.

    eval_set: Tuple[pd.DataFrame, pd.Series]
        Набор данных для валидации и подбора гиперпараметров.

    params_bounds: dict
        Словарь c границами оптимизируемых параметров,
        ключ словаря - название гиперпараметра, значение - кортеж
        с минимальным и максимальным значением.

    maximize: bool, optional, default = True
        Флаг максимизации метрики. Опциональный параметр,
        по умолчанию True. Если равен True, то цель оптимизации -
        максимизация metric, если равен False, то цель
        оптимизации - минимизация metric.

    n_iter: int, optional, default = 30
        Количество итераций работы оптимизатора.

    seed: int, optional, default = 27
        it's random_state position.

    Attributes
    ----------
    init_points: int
        Количество итераций для инициализации оптимизатора.
        Принимается равным 30% от общего числа итераций.

    optimizer: bayes_opt.bayesian_optimization.BayesianOptimization
        Экземпляр оптимизатора bayes_opt.

    """

    def __init__(
        self,
        model: BoostingBaseModel,
        metric: BaseMetric,
        eval_set: Tuple[pd.DataFrame, pd.Series],
        params_bounds: dict,
        maximize: bool = True,
        n_iter: int = 30,
        seed: int = 27,
    ) -> None:
        super().__init__(params_bounds, model)
        self.metric = metric
        self.optimizer = None
        self.train_set = None
        self.maximize = maximize
        self.eval_set = eval_set
        self.init_points = int(n_iter * 0.2)
        self.n_iter = n_iter
        self.seed = seed

    def objective(self, **fit_params) -> float:
        """
        Функция оптимизации.
        """
        valid_params = self.check_param_value(fit_params)
        params = self.model.params
        params.update(valid_params)

        self.model.params = params
        self.model.fit(*self.train_set, *self.eval_set)
        y_pred = self.model.transform(self.eval_set[0])
        self._logger.info("=" * 78)
        if self.maximize:
            return self.metric(self.eval_set[1], y_pred)
        else:
            return -self.metric(self.eval_set[1], y_pred)

    def fit(self, data, target) -> None:
        """
        Обучение оптимизатора.

        Parameters
        ----------
        data: pandas.DataFrame, shape = [n_samples, n_features]
            матрица признаков для обучения.

        target: pandas.Series, shape = [n_samples, ]
            вектор истинных ответов.

        """
        self.train_set = (data, target)
        self.optimizer = BayesianOptimization(
            self.objective, self.params_bounds, self.seed
        )
        self.optimizer.maximize(
            self.init_points, self.n_iter, alpha=1e-6, acq="ucb", xi=0.0
        )
        max_params = self.optimizer.max["params"]
        max_params = self.check_param_value(max_params)
        self.model.params.update(max_params)
        self.model.fit(*self.train_set, *self.eval_set)


class CVBayesianOptimizationModel(BayesianOptimizator):
    """
    Байесовская оптимизация ML-моделей для DreamML.

    Parameters
    ----------
    model: dreamml.modeling.models.estimators.boosting_base.BoostingBaseModel
        Экземпляр модели со стандартизованным API для DreamML.

    metric: BaseMetric
        Метрика для оценки качества модели.

    eval_set: Tuple[pd.DataFrame, pd.Series]
        Набор данных для валидации и подбора гиперпараметров.

    params_bounds: dict
        Словарь c границами оптимизируемых параметров,
        ключ словаря - название гиперпараметра, значение - кортеж
        с минимальным и максимальным значением.

    maximize: bool, optional, default = True
        Флаг максимизации метрики. Опциональный параметр,
        по умолчанию True. Если равен True, то цель оптимизации -
        максимизация metric, если равен False, то цель
        оптимизации - минимизация metric.

    n_iter: int, optional, default = 30
        Количество итераций работы оптимизатора.

    seed: int, optional, default = 27
        it's random_state position.

    Attributes
    ----------
    init_points: int
        Количество итераций для инициализации оптимизатора.
        Принимается равным 30% от общего числа итераций.

    optimizer: bayes_opt.bayesian_optimization.BayesianOptimization
        Экземпляр оптимизатора bayes_opt.

    """

    def __init__(
        self,
        model,
        cv,
        metric: BaseMetric,
        params_bounds: dict,
        splitter_df: pd.DataFrame,
        maximize: bool = True,
        n_iter: int = 30,
        timeout: int = 7200,
        seed: int = 27,
    ) -> None:
        super().__init__(params_bounds, model)
        self.cv = cv
        self.splitter_df = splitter_df
        self.metric = metric
        self.optimizer = None
        self.train_set = None
        self.maximize = maximize
        self.init_points = int(n_iter * 0.2)
        self.n_iter = n_iter
        self.timeout = timeout
        self.seed = seed

    def objective(self, **fit_params) -> float:
        """
        Функция оптимизации.
        """
        valid_params = self.check_param_value(fit_params)
        params = self.model.params
        params.update(valid_params)

        self.model.params = params
        _, cv_score, _, _, _, _ = make_cv(
            estimator=self.model,
            x_train_cv=self.train_set[0],
            y_train_cv=self.train_set[1],
            cv=self.cv,
            splitter_df=self.splitter_df,
            metric=self.metric,
        )
        self._logger.info("=" * 111)

        if self.maximize:
            return cv_score
        return -cv_score

    def fit(self, data, target) -> None:
        """
        Обучение оптимизатора.

        Parameters
        ----------
        data: pandas.DataFrame, shape = [n_samples, n_features]
            матрица признаков для обучения.

        target: pandas.Series, shape = [n_samples, ]
            вектор истинных ответов.

        """
        self.train_set = (data, target)
        self.optimizer = BayesianOptimization(
            self.objective, self.params_bounds, self.seed
        )
        self.optimizer.maximize(
            self.init_points, self.n_iter, alpha=1e-6, acq="ucb", xi=0.0
        )
        max_params = self.optimizer.max["params"]
        max_params = self.check_param_value(max_params)

        return max_params