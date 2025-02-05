from abc import ABC, abstractmethod


class FoldingAlgorithm(ABC):
    @abstractmethod
    def _load(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def fold(self, sequence: str) -> None:
        raise NotImplementedError
