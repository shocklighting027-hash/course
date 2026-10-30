import numpy as np
import pandas as pd
from preprocessing import fill_missing_values

# Test functions for filling missing values


def test_mean_value_filling():
    """Test that the fill_missing_values function correctly fills missing values with the mean of the column."""
    test_data = pd.DataFrame(np.random.normal(
        loc=2, scale=1, size=10), columns=['numeric_col'])
    test_data.iloc[[1, 6, 9]] = None
    mean = test_data['numeric_col'].mean()
    process_data = fill_missing_values(test_data, strategy="mean")
    assert process_data.iloc[1].item() == mean
    assert process_data.iloc[6].item() == mean
    assert process_data.iloc[9].item() == mean


def test_median_value_filling():
    """Test that the fill_missing_values function correctly fills missing values with the median of the column."""
    test_data = pd.DataFrame(np.random.normal(
        loc=2, scale=1, size=10), columns=['numeric_col'])
    test_data.iloc[[1, 6, 9]] = None
    median = test_data['numeric_col'].median()
    process_data = fill_missing_values(test_data, strategy="median")
    assert process_data.iloc[1].item() == median
    assert process_data.iloc[6].item() == median
    assert process_data.iloc[9].item() == median


def test_zero_value_filling():
    """Test that the fill_missing_values function correctly fills missing values with zero."""
    test_data = pd.DataFrame(np.random.normal(
        loc=2, scale=1, size=10), columns=['numeric_col'])
    test_data.iloc[[1, 6, 9]] = None
    process_data = fill_missing_values(test_data, strategy="zero")
    assert process_data.iloc[1].item() == 0
    assert process_data.iloc[6].item() == 0
    assert process_data.iloc[9].item() == 0


def test_fill_without_missing_values():
    """Test that the fill_missing_values function does not modify a DataFrame without missing values."""
    test_data = pd.DataFrame(np.random.normal(
        loc=2, scale=1, size=10), columns=['numeric_col'])
    process_data_mean = fill_missing_values(test_data, strategy="mean")
    process_data_median = fill_missing_values(test_data, strategy="median")
    process_data_zero = fill_missing_values(test_data, strategy="zero")
    assert process_data_mean.equals(test_data)
    assert process_data_median.equals(test_data)
    assert process_data_zero.equals(test_data)


def test_fill_with_empty_dataframe():
    """Test that the fill_missing_values function handles an empty DataFrame without errors."""
    test_data = pd.DataFrame(columns=['numeric_col'])
    process_data_mean = fill_missing_values(test_data, strategy="mean")
    process_data_median = fill_missing_values(test_data, strategy="median")
    process_data_zero = fill_missing_values(test_data, strategy="zero")
    assert process_data_mean.equals(test_data)
    assert process_data_median.equals(test_data)
    assert process_data_zero.equals(test_data)
