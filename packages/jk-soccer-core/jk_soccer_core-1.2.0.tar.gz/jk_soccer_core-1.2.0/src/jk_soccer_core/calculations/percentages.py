from typing import Iterable, Optional
from .match import MatchCalculation
from jk_soccer_core.models import Match

from jk_soccer_core.calculations.wins import WinsCalculation
from jk_soccer_core.calculations.losses import LossesCalculation
from jk_soccer_core.calculations.draws import DrawsCalculation


class WinningPercentageCalculation(MatchCalculation):
    """
    Calculate the winning percentage for a specific team
    """

    def __init__(
        self,
        team_name: Optional[str],
        skip_team_name: Optional[str],
        number_of_digits: int = 2,
    ):
        self.__team_name = team_name
        self.__skip_team_name = skip_team_name
        self.__number_of_digits = number_of_digits

    def calculate(self, matches: Iterable[Match]) -> float:
        """
        Calculate the winning percentage for a specific team
        """
        if self.__team_name is None:
            return 0.0

        if self.__team_name == "":
            return 0.0

        filtered_matches = matches
        if self.__skip_team_name is not None:
            filtered_matches = [
                match
                for match in matches
                if not match.contains_team_name(self.__skip_team_name)
            ]

        wins = WinsCalculation(self.__team_name).calculate(filtered_matches)
        losses = LossesCalculation(self.__team_name).calculate(filtered_matches)
        draws = DrawsCalculation(self.__team_name).calculate(filtered_matches)
        matches_played = wins + losses + draws

        if matches_played == 0:
            return 0.0

        result = (float(wins) + (float(draws) / 2)) / float(matches_played)
        result = round(result, self.__number_of_digits)

        return result
