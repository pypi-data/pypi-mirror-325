from copy import deepcopy
import pandas as pd
from sklearn.preprocessing import LabelEncoder


class DmlLabelEncoder:
    """Кастомный LabelEncoder для работы с DataFrame.

    Этот класс предоставляет интерфейс для кодирования категориальных признаков
    в DataFrame с использованием LabelEncoder из scikit-learn.

    Attributes:
        encoder (LabelEncoder): Экземпляр LabelEncoder из scikit-learn.
    """

    def __init__(self):
        """Инициализирует DmlLabelEncoder.

        Создаёт экземпляр LabelEncoder для кодирования категориальных признаков.
        """
        self.encoder = LabelEncoder()

    def fit(self, data: pd.DataFrame, feature: str):
        """Обучает кодировщик на данных.

        Args:
            data (pd.DataFrame): DataFrame, содержащий данные для обучения.
            feature (str): Название столбца, который нужно закодировать.

        Returns:
            self (DmlLabelEncoder): Возвращает экземпляр класса для цепочки вызовов.
        """
        self.encoder = self.encoder.fit(data[feature])
        return self

    def transform(self, data: pd.DataFrame, feature: str) -> pd.DataFrame:
        """Применяет кодировку к данным.

        Args:
            data (pd.DataFrame): DataFrame, содержащий данные для кодирования.
            feature (str): Название столбца, который нужно закодировать.

        Returns:
            pd.DataFrame: DataFrame с закодированным признаком.
        """
        x_transformed = deepcopy(data)
        x_transformed[feature] = self.encoder.transform(x_transformed[feature])
        return x_transformed

    def inverse_transform(self, data: pd.DataFrame, feature: str) -> pd.DataFrame:
        """Обратное преобразование закодированных данных.

        Args:
            data (pd.DataFrame): DataFrame, содержащий закодированные данные.
            feature (str): Название столбца, который нужно декодировать.

        Returns:
            pd.DataFrame: DataFrame с декодированным признаком.
        """
        x_transformed = deepcopy(data)
        if feature in x_transformed.columns:
            x_transformed[feature] = self.encoder.inverse_transform(
                x_transformed[feature]
            )
        return x_transformed