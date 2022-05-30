import json

import connexion
import six

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
