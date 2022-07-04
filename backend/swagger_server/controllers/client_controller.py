import connexion
import six

from swagger_server.models.game import Game  # noqa: E501
from swagger_server.models.team import Team  # noqa: E501
from swagger_server import util

import controllers

def get_standing():  # noqa: E501
    """Get standings of premier league

     # noqa: E501


    :rtype: None
    """
    return controllers.get_standing()


def get_team(team_id=None):  # noqa: E501
    """Get team

     # noqa: E501

    :param team_id: 
    :type team_id: int

    :rtype: None
    """
    return controllers.get_team()

def get_teams():  # noqa: E501
    """returns Teams

    Returns all of the teams in the EPL and their rank.  # noqa: E501


    :rtype: List[Team]
    """
    return controllers.get_teams()


def predict_game(home_id=None, away_id=None):  # noqa: E501
    """Predict the outcome of two teams playing

     # noqa: E501

    :param home_id: 
    :type home_id: int
    :param away_id: 
    :type away_id: int

    :rtype: Game
    """
    return controllers.predict_game(10,10)


def predict_round(round_number=38):  # noqa: E501
    """predict every game of a certain round

     # noqa: E501

    :param round_number: 
    :type round_number: int

    :rtype: None
    """
    return controllers.predict_round(round_number)
