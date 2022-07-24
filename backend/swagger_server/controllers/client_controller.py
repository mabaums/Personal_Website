import connexion
import six

from swagger_server.models.fixture import Fixture  # noqa: E501
from swagger_server.models.player import Player  # noqa: E501
from swagger_server.models.predicted_game import PredictedGame  # noqa: E501
from swagger_server.models.team import Team  # noqa: E501
from swagger_server.models.team_standing import TeamStanding  # noqa: E501
from swagger_server import util

import controllers

def get_fixture(fixture_id=None):  # noqa: E501
    """Get basic info about a fixture

     # noqa: E501

    :param fixture_id: 
    :type fixture_id: int

    :rtype: Fixture
    """
    return controllers.get_fixture(fixture_id)


def get_player(player_id=None):  # noqa: E501
    """get basic info about a player

     # noqa: E501

    :param player_id: 
    :type player_id: int

    :rtype: Player
    """
    return controllers.get_player(player_id)


def get_squad(team_id=None):  # noqa: E501
    """get list of players from a team

     # noqa: E501

    :param team_id: 
    :type team_id: int

    :rtype: List[Player]
    """
    return controllers.get_squad(team_id)


def get_standing(league_id=None, season=None):  # noqa: E501
    """Get standings from the selected league

     # noqa: E501

    :param league_id: 
    :type league_id: int
    :param season: 
    :type season: int

    :rtype: List[TeamStanding]
    """
    return controllers.get_standing(league_id, season)


def get_team(team_id=None):  # noqa: E501
    """get team of specified id

     # noqa: E501

    :param team_id: 
    :type team_id: int

    :rtype: Team
    """
    return controllers.get_team(team_id)


def predict_game(home_id=None, away_id=None, algo_id=None):  # noqa: E501
    """Predict the outcome of two teams playing

     # noqa: E501

    :param home_id: 
    :type home_id: int
    :param away_id: 
    :type away_id: int
    :param algo_id: 
    :type algo_id: int

    :rtype: PredictedGame
    """

    #TODO: Change predicted game yaml to be the two id's of the team you moron
    return PredictedGame(1,2,'Chelsea', 'Man city?')


def predict_round(round_number=None, algo_id=None):  # noqa: E501
    """Predict a certain round based on the previous weeks.

     # noqa: E501

    :param round_number: 
    :type round_number: int
    :param algo_id: 
    :type algo_id: int

    :rtype: List[PredictedGame]
    """
    return controllers.predict_round(round_number)
