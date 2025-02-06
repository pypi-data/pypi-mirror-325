from typing import Iterable, Union
from abc import ABC, abstractmethod
from jk_soccer_core.models import Match


class MatchCalculation(ABC):
    @abstractmethod
    def calculate(
        self, matches: Iterable[Match]
    ) -> Union[int, float]:  # pragma: no cover
        pass
