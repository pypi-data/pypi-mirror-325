from _typeshed import Incomplete
from dask.distributed import Future
from dataclasses import dataclass
from pandas import DataFrame as pdDataframe
from ydata.characteristics import ColumnCharacteristic
from ydata.dataset import Dataset, DatasetType
from ydata.metadata.builder import MetadataConfigurationBuilder
from ydata.metadata.column import Column
from ydata.metadata.compute import ComputeConfig

logger: Incomplete
DEFAULT_PARTITION_SIZE: int

def assign_correlation(data: Future | pdDataframe, m: Metadata): ...
def assign_characteristics(data: Future | tuple, m: Metadata, schema, columns: dict | None = None): ...

@dataclass
class DatasetAttr:
    sortbykey: list[str] = ...
    entities: list[str] = ...
    @staticmethod
    def fields(): ...
    def empty(self): ...
    def __init__(self, sortbykey=..., entities=...) -> None: ...

def istype(d: dict, inputtype=...):
    """Validate wether all the values from a dict are of a provided type."""
def valid_input_col(d: dict):
    """Validate input column."""

class Metadata:
    """Metadata contains data about a Dataset.

    Properties:
        columns (List[str]): list of feature names
        ncols (int): number of features
        shape (Tuple[int, int]): tuple of (nrows, ncols)
        uniques (Dict[str, int]): number of unique values per feature.
        skewness (Dict[str, float]): skewness metric per continuous feature.
        schema (Dict[str, str]): feature type (VariableTypes), based on data types.
    """
    DATASET_WARNINGS: list[str]
    MIN_ROWS_FOR_SAMPLING: int
    MAX_CORR_CARDINALITY: int
    status: Incomplete
    def __init__(self, dataset: Dataset | None = None, dataset_attrs: dict | None = None, columns: dict | None = None, dataset_type: DatasetType | str = ..., infer_characteristics: bool = False, characteristics: dict | None = None, pairwise_metrics: bool = True, partition_size: int = ..., intercolumns_warnings: bool = True, compute_config: ComputeConfig | dict | None = None, configuration_builder: MetadataConfigurationBuilder | None = None) -> None: ...
    def __call__(self, dataset: Dataset, dataset_attrs: dict | DatasetAttr | None = None, columns: dict | None = None, dataset_type: DatasetType | str = ...) -> Metadata: ...
    def set_dataset_type(self, dataset_type: DatasetType | str, dataset_attrs: dict | None = None):
        """Update dataset type and optionaly dataset attrs.

        Args:
            dataset_type (DatasetType | str): new dataset type
            dataset_attrs (dict | None, optional): Dataset attrs for TIMESERIES dataset. Defaults to None.
        """
    def set_dataset_attrs(self, sortby: str | list[str], entities: str | list[str] | None = None):
        """Update dataset attributes.

        Args:
            sortby (str | List[str]): Column(s) that express the temporal component
            entities (str | List[str] | None, optional): Column(s) that identify the entities. Defaults to None
        """
    def clean_characteristics(self, matched_dictionary: dict, threshold: float, confidence_level: float) -> dict: ...
    def compute_characteristics(self, dataset: Dataset, columns: dict | None = None, deferred: bool = False) -> dict | Future:
        """Compute the dataset's characteristics.

        The method returns the characteristics and update the metadata instance's summary accordingly.

        Args:
            dataset: dataset corresponding to the Metadata instance
            columns: columns dictionary
            deferred: defer the computation if True, else compute now

        Returns:
            dict if deferred is False, Future otherwise
        """
    def compute_correlation(self, dataset: Dataset, columns: dict | None = None, deferred: bool = False) -> pdDataframe | Future:
        """Compute the dataset's correlation matrix.

        The method returns the correlation matrix and update the metadata instance's summary accordingly.

        Args:
            dataset: dataset corresponding to the Metadata instance
            columns: columns dictionary
            deferred: defer the computation if True, else compute now

        Returns:
            pandas dataframe if deferred is False, Future otherwise
        """
    def add_characteristics(self, characteristics: dict[str, list[ColumnCharacteristic | str] | ColumnCharacteristic | str]):
        """Add characteristics to the specified columns.

        The argument `characteristics` is dictionary indexed on the columns that accept two syntaxes:
            1. a characteristic
            2. a list of characteristics

        Example:

            ```python
            characteristics = {
                'col1': 'phone',
                'col2': ['uuid', 'name']
            }
            metadata.add_characteristics(characteristics)
        ```

        Args:
            characteristics (dict[str, list[ColumnCharacteristic | str] | ColumnCharacteristic | str]): characteristics to add
        """
    def add_characteristic(self, column: str, characteristic: ColumnCharacteristic | str):
        """Add new characteristic to a column.

        Args:
            column (str): column name
            characteristic (ColumnCharacteristic): characteristic to add
        """
    def remove_characteristics(self, characteristics: dict[str, list[ColumnCharacteristic | str] | ColumnCharacteristic | str]):
        """Remove characteristics to the specified columns.

        The argument `characteristics` is dictionary indexed on the columns that accept two syntaxes:
            1. a characteristic
            2. a list of characteristics

        Example:

            ```python
            characteristics = {
                'col1': 'phone',
                'col2': ['uuid', 'name']
            }
            metadata.remove_characteristics(characteristics)
        ```

        Args:
            characteristics (dict[str, list[ColumnCharacteristic | str] | ColumnCharacteristic | str]): characteristics to add
        """
    def remove_characteristic(self, column: str, characteristic: ColumnCharacteristic | str):
        """Remove a characteristic from a column.

        Args:
            column (str): column name
            characteristic (ColumnCharacteristic): characteristic to remove
        """
    def get_characteristics(self) -> dict[str, list[ColumnCharacteristic]]:
        """Get the characteristics for all columns.

        Returns:
            dict[str, list[ColumnCharacteristic]]: characteristics dictionary
        """
    def set_characteristics(self, characteristics: dict[str, list[ColumnCharacteristic | str]]):
        """Define the characteristics for all columns.

        Obs.: this will overwrite any previous definition for characteristics

        Args:
            characteristics (dict[str, list[ColumnCharacteristic]]): the new set of characteristics
        """
    def get_possible_targets(self): ...
    @property
    def columns(self) -> dict | None: ...
    def update_datatypes(self, value: dict, dataset: Dataset | None = None):
        '''Method to update the data types set during the Metadata automatic
        datatype inference.

        Valid datatypes to update the columns are: "longtext",
        "categorical", "numerical", "date" and "id". value (dict): A
        dictionary with the name: datatype value to be assigned to the
        column. Provide only the names of the columns that need a
        datatype update.
        '''
    @property
    def cardinality(self) -> dict:
        """Returns a tuple with a dict with categorical variables approximated
        cardinality and the sum of the total cardinality."""
    @property
    def isconstant(self) -> list:
        """Returns a list with the name of the columns that are constant
        throughout the dataset, i.e., always assume the same value."""
    @property
    def warnings(self) -> dict: ...
    @property
    def summary(self): ...
    @property
    def shape(self) -> tuple: ...
    @property
    def ncols(self): ...
    @property
    def target(self): ...
    @target.setter
    def target(self, value: str | Column): ...
    def get_numerical_columns(self):
        """List columns with numerical VariableType."""
    @property
    def numerical_vars(self):
        """List of continuous variables."""
    @property
    def date_vars(self):
        """List of integer numerical variables."""
    @property
    def categorical_vars(self):
        """List of categorical variables."""
    @property
    def id_vars(self):
        """List of columns that are unique identifiers variables."""
    @property
    def longtext_vars(self):
        """List of columns of longtext data type."""
    @property
    def string_vars(self):
        """List of columns with string data type."""
    @property
    def dataset_attrs(self):
        """Dataset attributes."""
    @dataset_attrs.setter
    def dataset_attrs(self, attrs: dict):
        """Set dataset attributes."""
    def save(self, path: str):
        """Creates a pickle of the metadata object stored in the provided path."""
    @staticmethod
    def load(path: str) -> Metadata:
        """Loads a metadata object from a path to a pickle."""
    def __getitem__(self, key):
        """
        Usage:
        >>> data[ ['columnA', 'columnB'] ]
        """
    def combine(self, other: Metadata): ...
