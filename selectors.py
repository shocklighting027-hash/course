from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Self

import numpy as np
import pandas as pd


@dataclass
class BaseSelector(ABC):

  @abstractmethod
  def fit(self, X: pd.DataFrame, y: pd.Series | None = None) -> Self:
    pass

  def transform(self, X: pd.DataFrame) -> pd.DataFrame:
    return X[self.selected_features]

  def fit_transform(self, X: pd.DataFrame, y: pd.Series | None = None):
    self.fit(X, y)
    return self.transform(X)

  @property
  def n_features_(self) -> int:
    return len(self.selected_features)

  @property
  def original_features_(self) -> list:
    return self.original_features

  @property
  def selected_features_(self) -> list:
    return self.selected_features


@dataclass
class PearsonSelector(BaseSelector):
  threshold: float = 0.5

  def fit(self, X: pd.DataFrame, y: pd.Series) -> Self:
    corr = pd.concat([X, y], axis=1).corr(method='pearson')
    corr_target = corr.iloc[:-1, -1]
    self.original_features = X.columns.tolist()
    self.selected_features = corr_target[
        abs(corr_target) >= self.threshold
    ].index.tolist()
    return self  


@dataclass
class SpearmanSelector(BaseSelector):
  threshold: float = 0.5

  def fit(self, X: pd.DataFrame, y: pd.Series) -> Self:
    corr = pd.concat([X, y], axis=1).corr(method='spearman')  #
    corr_target = corr.iloc[:-1, -1]

    self.original_features = X.columns.tolist()
    self.selected_features = corr_target[
        abs(corr_target) >= self.threshold
    ].index.tolist()
    return self  


@dataclass
class VarianceSelector(BaseSelector):
  min_var: float = 0.4

  def fit(self, X: pd.DataFrame, y: pd.Series | None = None) -> Self:
    variances = np.var(X, axis=0)
    self.original_features = X.columns.tolist()
    self.selected_features = X.columns[variances > self.min_var].tolist()
    return self
