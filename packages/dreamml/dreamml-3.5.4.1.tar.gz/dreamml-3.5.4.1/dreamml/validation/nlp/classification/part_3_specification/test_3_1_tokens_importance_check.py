from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelBinarizer

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from typing import List, Any, Optional


class ModelTokensImportanceAnalysis:
    """
    Тест 3.1: Проверка значимости токенов в модели (информативный тест)
    """

    def __init__(self, artifacts_config, images_dir_path: str) -> None:
        self.binarizer = LabelBinarizer()
        self.images_dir_path = images_dir_path

    def _plot_token_importance(
        self,
        chi_square: pd.DataFrame,
        class_name: str,
        feature_name: Optional[str] = None,
    ):
        title = (
            f"{feature_name}_{class_name}" if feature_name is not None else class_name
        )
        fig, axes = plt.subplots(1, 1, figsize=(12, 8))
        fig.subplots_adjust(wspace=0.3)
        axes.set_title(title)
        plt.barh(chi_square["token"], chi_square[class_name], color="b", align="center")
        axes.set_ylabel("token name", size=15)
        axes.set_xlabel("importance")
        axes.legend(loc="best")
        plt.grid(True)
        plt.savefig(
            f"{self.images_dir_path}/{title}.png",
            bbox_inches="tight",
            pad_inches=0.1,
        )
        plt.close()

    def calculate_stats(self, data, feature_name: Optional[str] = None):
        train_texts, train_target = data["train"][0], self.binarizer.fit_transform(
            data["train"][1].values
        )
        oos_texts, oos_target = data["test"][0], self.binarizer.transform(
            data["test"][1].values
        )

        vectorizer = CountVectorizer()
        train_vec = vectorizer.fit_transform(train_texts)
        oos_vec = vectorizer.transform(oos_texts)

        train_bow = train_vec.toarray()
        oos_bow = oos_vec.toarray()

        E_i_oos = oos_bow.mean(axis=1) @ oos_target.reshape(
            -1, oos_target.shape[1]
        ).mean(axis=1)
        O_i_train_matrix = train_target.reshape(-1, train_target.shape[1]).T @ train_bow

        chi_square = np.power((O_i_train_matrix - E_i_oos) / E_i_oos, 2) / len(
            train_texts
        )

        chi_results = []
        results = pd.DataFrame(
            {
                "token": vectorizer.get_feature_names_out(),
            }
        )
        _classes = np.unique(self.binarizer.inverse_transform(train_target)).tolist()
        for i, _class in enumerate(_classes):
            if i < chi_square.shape[0]:
                name = f"chi_square_class_{_class}"
                importance = (
                    pd.DataFrame({"token": results["token"], name: chi_square[i, :]})
                    .sort_values(by=name, ascending=False)
                    .head(n=20)
                )
                chi_results.append(importance)
                self._plot_token_importance(
                    importance, class_name=name, feature_name=feature_name
                )

        results = [pd.DataFrame({"Результат теста": ["-"]}), *chi_results]
        return results