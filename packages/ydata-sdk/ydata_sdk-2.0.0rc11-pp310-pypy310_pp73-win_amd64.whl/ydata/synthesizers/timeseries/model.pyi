from _typeshed import Incomplete
from pandas import DataFrame as pdDataFrame
from pathlib import Path
from typing import Callable
from ydata.connectors.storages.big_query_connector import BigQueryConnector as BigQueryConnector
from ydata.connectors.storages.object_storage_connector import ObjectStorageConnector as ObjectStorageConnector
from ydata.connectors.storages.rdbms_connector import RDBMSConnector as RDBMSConnector
from ydata.datascience.common import PrivacyLevel
from ydata.dataset import Dataset
from ydata.metadata import Metadata
from ydata.preprocessors.methods.anonymization import AnonymizerConfigurationBuilder
from ydata.synthesizers.base_model import BaseModel, SegmentByType
from ydata.synthesizers.conditional import ConditionalFeature
from ydata.synthesizers.entity_augmenter import FidelityConfig, SmoothingConfig
from ydata.utils.random import RandomSeed as RandomSeed

logger: Incomplete

class TimeSeriesSynthesizer(BaseModel):
    sortbykey: Incomplete
    bypass_entities_anonymization: Incomplete
    def __init__(self, tmppath: str | Path = None) -> None:
        """Initializes the SYNTHESIZER."""
    @property
    def SUPPORTED_DTYPES(self): ...
    anonymize: Incomplete
    entity_merged_col: Incomplete
    entities_type: Incomplete
    is_fitted_: bool
    def fit(self, X: Dataset, metadata: Metadata, extracted_cols: list = None, calculated_features: list[dict[str, str | Callable | list[str]]] | None = None, missing_values: list | None = None, anonymize: dict | AnonymizerConfigurationBuilder | None = None, privacy_level: PrivacyLevel | str = ..., condition_on: str | list[str] | None = None, anonymize_ids: bool = False, segment_by: SegmentByType = 'auto', random_state: RandomSeed = None): ...
    def sample(self, n_entities: int | None = None, smoothing: bool | dict | SmoothingConfig = False, fidelity: float | dict | FidelityConfig | None = None, sort_result: bool = True, condition_on: list[ConditionalFeature] | dict | pdDataFrame | None = None, balancing: bool = False, random_state: RandomSeed = None, connector: BigQueryConnector | ObjectStorageConnector | RDBMSConnector | None = None, **kwargs) -> Dataset:
        '''Generate a time series.

        This method generates a new time series. The instance should be trained via the method `fit` before calling `sample`.
        The generated time series has the same length of the training data. However, in the case of multi-entity time series, it is possible
        to augment the number of entities by specifying the parameter `n_entities`.

        A multi-entity time series requires the metadata dataset attributes to specify at least one column corresponding to an entity ID.
        For instance, the following example specify two columns as entity ID columns:
        ```python

        dataset_attrs = {
            "sortbykey": "sate",
            "entities": [\'entity\', \'entity_2\']
        }

        m = metadata(dataset, dataset_type=DatasetType.TIMESERIES, dataset_attrs=dataset_attrs)
        ```

        For a multi-entity sample, there are two major arguments that can be used to modify the results: fidelity and smoothing.

        1. Fidelity: It defines how close the new entities should be from the original ones.
                     When a `float`, it represents the behavioral noise to be added to the entity expressed as a percentage of its variance.
                     See `ydata.synthesizer.entity_augmenter.FidelityConfig` for more details.
        2. Smoothing: It defines if and how the new entities trajectory should be smoothed.
                    See `ydata.synthesizer.entity_augmenter.SmoothingConfig` for more details.

        Args:
            n_entities (Optional[int]): Number of entities to sample. If None, generates as many entities as in the training data. By default None.
            smoothing (Union[bool, dict, SmoothingConfig]): Define how the smoothing should be done. `True` uses the `auto` configuration.
            fidelity Optional[Union[float, dict, FidelityConfig]]: Define the fidely policy.
            sort_result (bool): True if the sample should be sorted by sortbykey, False otherwise.
            condition_on (list[ConditionalFeature] | dict | pdDataFrame | None): Conditional rules to be applied.
            balancing (bool): If True, the categorical features included in the conditional rules have equally distributed percentages.

        Returns:
            PipelinePrototype: Pipeline prototype to use to build the synthesizer
        '''
