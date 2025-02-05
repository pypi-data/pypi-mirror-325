# core/experiment_stores/IExperimentStore.py
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Union
from swarmauri_core.documents.IExperimentDocument import IExperimentDocument

class IExperimentStore(ABC):
    """
    Interface for an Experiment Store that manages experimental documents and supports
    operations related to experimenting, evaluating, testing, and benchmarking.
    """
    @abstractmethod
    def add_experiment(self, experiment: IExperimentDocument) -> None:
        """
        Stores a single experiment in the experiment store.

        Parameters:
        - experiment (IExperimentDocument): The experimental document to be stored.
        """
        pass

    @abstractmethod
    def add_experiments(self, experiments: List[IExperimentDocument]) -> None:
        """
        Stores multiple experiments in the experiment store.

        Parameters:
        - experiments (List[IExperimentDocument]): The list of experimental documents to be stored.
        """
        pass

    @abstractmethod
    def get_experiment(self, experiment_id: str) -> Union[IExperimentDocument, None]:
        """
        Retrieves an experimental document by its ID.

        Parameters:
        - id (str): The unique identifier of the experiment.

        Returns:
        - Union[IExperimentDocument, None]: The requested experimental document, or None if not found.
        """
        pass

    @abstractmethod
    def get_all_experiments(self) -> List[IExperimentDocument]:
        """
        Retrieves all experimental documents stored in the experiment store.

        Returns:
        - List[IExperimentDocument]: A list of all experimental documents.
        """
        pass

    @abstractmethod
    def update_experiment(self, experiment_id: str, updated_experiment: IExperimentDocument) -> None:
        """
        Updates an experimental document in the experiment store.

        Parameters:
        - id (str): The unique identifier of the experiment to update.
        - updated_experiment (IExperimentDocument): The updated experimental document.
        """
        pass

    @abstractmethod
    def delete_experiment(self, experiment_id: str) -> None:
        """
        Deletes an experimental document from the experiment store by its ID.

        Parameters:
        - id (str): The unique identifier of the experimental document to be deleted.
        """
        pass

    @abstractmethod
    def evaluate_experiments(self, evaluation_criteria: Dict[str, Any]) -> Any:
        """
        Evaluates the experiments stored in the experiment store based on given criteria and measurements.

        Parameters:
        - evaluation_criteria (Dict[str, Any]): The criteria and measurements to evaluate the experiments.

        Returns:
        - Any: The evaluation results, which may vary depending on the evaluation criteria.
        """
        pass

    @abstractmethod
    def benchmark_experiments(self, benchmarking_data: Dict[str, Any]) -> Any:
        """
        Benchmarks the experiments against each other or predefined standards.

        Parameters:
        - benchmarking_data (Dict[str, Any]): Data and parameters for benchmarking the experiments.

        Returns:
        - Any: The benchmark results, which may vary depending on the benchmarking methodology.
        """
        pass