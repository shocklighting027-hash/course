import numpy as np
import pandas as pd


class RandomSampler:
    """Randomly samples data from a dataframe."""

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def get_num_rows(self):
        """Returns the number of rows in the dataframe."""
        return len(self.dataframe)

    def sample_data(self, num_samples):
        """Samples a specified number of rows from the dataframe."""
        return self.dataframe.sample(num_samples)


class UniqueColumnSampler(RandomSampler):
    """Samples unique values from a specified column in the dataframe."""

    def __init__(self, dataframe, column_name):
        super().__init__(dataframe)
        self.column_name = column_name

    def sample_data(self, num_samples):
        """Samples unique values from the specified column."""
        column_data = self.dataframe[self.column_name].unique()
        sampled_values = np.random.choice(
            column_data, size=num_samples, replace=False
        )
        return pd.DataFrame({self.column_name: sampled_values})
