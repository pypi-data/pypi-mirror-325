from pathlib import Path
import pandas

from ..abstract.dataset_base import DatasetBase


class CsvDataset(DatasetBase):
    """
    CsvDataset is a class that handles a dataset stored in a CSV file, where the file contains columns for
    timestamps and data. It provides methods for accessing data by index, extracting timestamps,
    and validating the structure of the CSV file.
    """

    def __init__(self, path: str | Path, cols: list[str] | str | None = None, sep=";"):
        super().__init__()

        self.path = Path(path)
        self.data = pandas.read_csv(self.path, sep=sep)
        self.data["timestamp"] = (
            self.data["timestamp"].apply(self.convert_timestamp).apply(int)
        )

        self.cols = (
            cols if isinstance(cols, list) else [cols] if cols else self.data.columns
        )
        self.cols = [col for col in self.cols if not col == "timestamp"]

    def convert_timestamp(self, timestamp: str | int) -> int:
        raise NotImplementedError

    def __len__(self):
        return len(self.data)

    def get_data(self, idx):
        data = {f"{col}": self.data[col].values[idx] for col in self.cols}
        return data

    @property
    def sensor_ids(self):
        return self.cols

    def get_timestamp(self, idx):
        return self.data["timestamp"].values[idx]

    def get_timestamp_idx(self, timestamp):
        return self.data[self.data["timestamp"] == timestamp].index[0]

    @property
    def timestamps(self):
        return self.data["timestamp"].values.tolist()
