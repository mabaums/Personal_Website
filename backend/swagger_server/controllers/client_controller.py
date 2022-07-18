import connexion
import six

from swagger_server.models.predicted_game import PredictedGame  # noqa: E501
from swagger_server.models.team import Team  # noqa: E501
from swagger_server import util

import controllers

def get_standing(league_id=None):  # noqa: E501
    """Get standings from the selected league

     # noqa: E501

    :param league_id: 
    :type league_id: int

    :rtype: List[Team]
    """
    #print(controllers.get_standing())
    return controllers.get_standing()


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
    return controllers.predict_game(home_id, away_id)


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
