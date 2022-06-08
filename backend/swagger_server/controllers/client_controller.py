import json

import connexion
import six

from swagger_server.models.game import Game  # noqa: E501
from swagger_server.models.team import Team  # noqa: E501
from swagger_server import util


def get_teams():  # noqa: E501
    """returns Teams

    Returns all of the teams in the EPL and their rank.  # noqa: E501


    :rtype: List[Team]
    """
    f = open('C:/Users/Mark/Documents/website/backend/teams.json', encoding='utf-8')
    data = json.load(f)
    teams = []
    for team in data:
        teams.append(Team.from_dict(team))
    return teams


def predict_game(home_id=None, away_id=None):  # noqa: E501
    """Predict the outcome of two teams playing

     # noqa: E501

    :param home_id: 
    :type home_id: int
    :param away_id: 
    :type away_id: int

    :rtype: Game
    """
    game = Game(1, 100,"Manchester City", "Chelsea")
    return game
