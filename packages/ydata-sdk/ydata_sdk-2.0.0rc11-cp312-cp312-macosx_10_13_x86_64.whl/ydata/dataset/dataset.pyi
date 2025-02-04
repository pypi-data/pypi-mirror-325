import dask
from dask.dataframe import DataFrame as ddDataframe, Series as ddSeries
from dask.dataframe.core import Scalar as ddScalar
from dask.delayed import Delayed as Delayed
from numpy import ndarray as ndarray
from pandas import DataFrame as pdDataframe, Series as pdSeries
from typing import Literal
from ydata.dataset.engines import VALID_ENGINES
from ydata.dataset.schemas import DatasetSchema as Schema
from ydata.utils.data_types import VariableType

class Dataset:
    """Dataset class provides the interface to handle data within YData's
    platform.

    Arguments:
        df (Union[pd.DataFrame, dd.DataFrame]): Dataset
        schema (Optional[Dict]): Mapping of column names to datatypes
        sample (float): Fraction of the sampled dataset
        index (str): Name of the column to be used as index
        missing_values (list or value): list of markers for missing values

    Properties:
        columns (list[str]): list of column names
        nrows (tuple): number of rows from the training and test datasets
        ncols (int): number of columns
        shape (tuple): tuple of (nrows, ncols)
        memory_usage (int): number of bytes consumed by the underlying dataframe
        nmissings (int): total number of missings in Dataset
        infered_dtypes_count (Dict[str, Dict]): infered data types per column
        infered_dtypes (Dict[str, str]): infered data type per column
        dtypes (Dict[str, str]): mapping of data type per column, either provided or inferred
        index (str): Returns the name of the index column

    Methods:
        enforce_dtypes: enforces a schema of data types, defaults to inferred
        select_dtypes: subset Dataset column based on features' data types
        to_pandas, to_numpy, to_dask: returns a Dataset as a pandas dataframe, numpy array or dask dataframe
        value_counts: number of value occurrences for given column
        uniques: number of unique values for given column
        drop_columns: drops specific columns from a Dataset
        select_columns: select specific columns from a Dataset
        reorder_columns: defines the order of columns for underlying data
        sample: returns a sample from the original Dataset

    Magic Methods:
        __len__: equal to nrows
        __contains__: checks whether a column is in a Dataset
        __getitem__: equal to select_columns
    """
    def __init__(self, df: VALID_ENGINES, schema: dict[str, Schema] | None = None, sample: float = 0.2, index: str | dask.dataframe.core.Index | None = None, divisions: list | tuple | None = None) -> None: ...
    def copy(self) -> Dataset:
        """Copy a Dataset instance.

        Returns:
            dataset (Dataset): A new Dataset instance with the scame schema and index.
        """
    @property
    def ncols(self) -> int:
        """Return the number of columns"""
    @property
    def nrows(self) -> int:
        """Return the number of rows"""
    @property
    def columns(self) -> list[str | int]:
        """Return dataset columns."""
    @property
    def index(self) -> str | None:
        """Returns the name of the index column"""
    @property
    def loc(self):
        '''Label location based indexer for selection. This method is inherited
        from Dask original LocIndexer implementation.

        >>> df.loc["b"]
        >>> df.loc["b":"d"]
        '''
    @property
    def schema(self) -> dict: ...
    @schema.setter
    def schema(self, new_value: dict[str, VariableType | str]): ...
    def apply(self, function: callable, axis: int | str = 1, raw: bool = False, args: tuple | None = None, meta: dict | list[tuple] | tuple | Dataset | None | str = '__no_default__') -> Dataset:
        """Parallelized version of apply.

        Only supported on the rows axis.
        To guarantee results with expected format, output metadata should be provided with meta argument.
        Arguments:
            function (callable): Function to apply to each row
            axis (Union[int, str]): 1/'columns' apply function to each row.
                0/'index' apply function to each column is not supported.
            raw (bool): Passed function operates on Pandas Series objects (False), or numpy arrays (True)
            args (Optional[Tuple]): Positional arguments to pass to function in addition to the array/series
            meta (Optional[Union[Dict, List[Tuple], Tuple, Dataset]]): A dictionary, list of tuples, tuple or dataset
                that matches the dtypes and column names of the output. This is an optional argument since it only
                certifies that Dask will use the correct metadata instead of infering which may lead to unexpected
                results.
        Returns:
            df (Dataset): A dataset object output of function.
        """
    def shape(self, lazy_eval: bool = True, delayed: bool = False) -> tuple[int | Delayed | None, int]:
        """Returns dataset shape as a tuple (rows, columns).

        Supports lazy evaluation of nrows, ncols is unexpensive and
        returned directly
        """
    @property
    def memory_usage(self) -> ddSeries:
        """Calculates the memory usage of the Dataset."""
    def missings(self, compute: bool = False) -> ddSeries | pdSeries:
        """Calculates the number of missing values in a Dataset.

        #TODO: Define missing as not-parsed from string_parser
                instead of native Dask computation.
        """
    @property
    def nmissings(self) -> int:
        """Returns the total count of missings in a Dataset"""
    def infer_dtypes(self, schema: dict | None = None):
        """Infers the schema based on the dtypes count.

        A feature is assigned to a dtype if its values represent the
        majority of its values.
        """
    def select_dtypes(self, include: str | list | None = None, exclude: str | list | None = None) -> Dataset:
        """Returns a subset of the original Dataset based on the data types."""
    def astype(self, column: str, vartype: VariableType | str, format: str | None = None): ...
    def update_types(self, dtypes: list): ...
    def to_pandas(self) -> pdDataframe:
        """Returns a Dataset as a Pandas DataFrame."""
    def to_numpy(self) -> ndarray:
        """Returns a Dataset as a Numpy Array."""
    def to_dask(self) -> ddDataframe:
        """Returns a Dataset as a Dask Dataframe."""
    def value_counts(self, col: str, compute: bool = True) -> ddSeries | pdSeries:
        """Calculates the exact number of value occurrences for a given column."""
    def uniques(self, col: str, approx: bool = True, delayed: bool = False) -> int | ddScalar:
        """Calculates the (exact/approximate) number of unique values in a column."""
    def drop_columns(self, columns: str | list, inplace: bool = False) -> Dataset | None:
        """Drops specified columns from a Dataset.

        Args:
            columns (str or list): column labels to drop
            inplace (bool): if False, return a copy. Otherwise, drop inplace and return None.
        """
    def select_columns(self, columns: str | list, copy: bool = True) -> Dataset:
        """Returns a Dataset containing only the subset of specified columns.
        If columns is a single feature, returns a Dataset with a single column.

        Args:
            columns (str or list): column labels to select
            copy (bool): if True, return a copy. Otherwise, select inplace and return self.
        """
    def query(self, query: str) -> Dataset: ...
    def sample(self, size: float | int, strategy: Literal['random', 'stratified'] = 'random', **strategy_params) -> Dataset:
        """Returns a sample from the original Dataset"""
    def reorder_columns(self, columns: list[str]) -> Dataset:
        """Defines the order of the underlying data based on provided 'columns'
        list of column names.

        Usage:
            >>> data.columns
            ['colA', 'colB', colC']
            >>> data.reorder_columns(['colB', 'colC']).columns
            ['colB', 'colC']
        """
    def divisions(self) -> tuple: ...
    def sort_values(self, by: list[str], ignore_index: bool = True, inplace: bool = False) -> Dataset | None: ...
    def sorted_index(self, by: list[str]) -> pdSeries: ...
    @property
    def known_divisions(self) -> bool: ...
    def head(self, n: int = 5) -> pdDataframe:
        """Return the `n` first rows of a dataset.

        If the number of rows in the first partition is lower than `n`,
        Dask will not return the requested number of rows (see
        `dask.dataframe.core.head` and `dask.dataframe.core.safe_head`).
        To avoid this corner case, we retry using all partitions -1.
        """
    def tail(self, n: int = 5) -> pdDataframe: ...
    def __len__(self) -> int:
        """Implements utility to call len(Dataset) directly, returning the
        number of rows.

        Usage:
        >>> len(data)
        """
    def __contains__(self, key) -> bool:
        """True if key is in Dataset columns.

        Usage:
        >>> 'my_column' in data
        """
    def __getitem__(self, key) -> Dataset:
        """
        Usage:
        >>> data[ ['columnA', 'columnB'] ]
        """
