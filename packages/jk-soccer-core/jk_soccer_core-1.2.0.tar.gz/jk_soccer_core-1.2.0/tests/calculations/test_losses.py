import pytest
from jk_soccer_core.models import Match, Team
from jk_soccer_core.calculations.losses import LossesCalculation


@pytest.fixture
def team_a():
    return Team(name="Team A")


@pytest.fixture
def team_b():
    return Team(name="Team B")


@pytest.fixture
def team_c():
    return Team(name="Team C")


@pytest.fixture
def matches(team_a, team_b, team_c):
    return [
        Match(home=team_a, away=team_b, home_score=2, away_score=1),
        Match(home=team_a, away=team_c, home_score=1, away_score=1),
        Match(home=team_b, away=team_a, home_score=0, away_score=3),
        Match(home=team_c, away=team_a, home_score=2, away_score=2),
    ]


def test_losses_calculation_team_a(matches, team_a):
    calc = LossesCalculation(team_a.name)
    assert calc.calculate(matches) == 0


def test_losses_calculation_team_b(matches, team_b):
    calc = LossesCalculation(team_b.name)
    assert calc.calculate(matches) == 2


def test_losses_calculation_team_c(matches, team_c):
    calc = LossesCalculation(team_c.name)
    assert calc.calculate(matches) == 0


def test_losses_calculation_empty_team_name(matches):
    calc = LossesCalculation("")
    assert calc.calculate(matches) == 0


def test_losses_calculation_none_team_name(matches):
    calc = LossesCalculation(None)
    assert calc.calculate(matches) == 0


def test_losses_calculation_empty_matches(team_a):
    calc = LossesCalculation(team_a.name)
    assert calc.calculate([]) == 0


def test_losses_calculation_no_teams():
    match = Match(home=None, away=None, home_score=1, away_score=1)
    calc = LossesCalculation("Team A")
    assert calc.calculate([match]) == 0
