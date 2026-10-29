from typing import List, Optional


class DataProcessor:
    """Class for data preprocessing.

    Attributes
    ----------
    data : List[float]
        Source data.
    processed_data_ : Optional[List[float]]
        Deviations from the mean, None until process() is called.
    """

    def __init__(self, data: List[float]):
        self.data = data
        self.processed_data_: Optional[List[float]] = None

    def process(self) -> None:
        """Compute deviation from the mean for each value in data."""
        mean = sum(self.data) / len(self.data)
        self.processed_data_ = [x - mean for x in self.data]

    def save_to_file(self, filename: str) -> None:
        """Save processed data to a file, one value per line.

        Nothing is saved if the data has not been processed.
        """
        if self.processed_data_ is None:
            return
        with open(filename, "w") as file:
            for value in self.processed_data_:
                file.write(f"{value}\n")
