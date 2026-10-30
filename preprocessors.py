from abc import ABC, abstractmethod
import pandas as pd


class DataPreprocessor(ABC):

  @abstractmethod
  def preprocess(self, data):
    pass


class OutlierRemover(DataPreprocessor):

  def preprocess(self, data):
    data = pd.Series(data)
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - (1.5 * IQR)
    upper_bound = Q3 + (1.5 * IQR)
    return data[(data >= lower_bound) & (data <= upper_bound)].tolist()


class Normalizer(DataPreprocessor):

  def preprocess(self, data):
    data = pd.Series(data)
    mean = data.mean()
    max_value = data.max()
    min_value = data.min()
    normalized_data = (data - mean) / (max_value - min_value)
    return normalized_data.tolist()


class Encoder(DataPreprocessor):

  def __init__(self, encoding_dict: dict):
    self.encoding_dict = encoding_dict

  def preprocess(self, data):
    data = pd.Series(data)
    encoded_data = data.map(self.encoding_dict)
    return encoded_data.tolist()
