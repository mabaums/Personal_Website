
from swagger_server.models.game import Game  # noqa: E501
from swagger_server.models.team import Team  # noqa: E501
from swagger_server import util


def get_teams():
    f = open('C:/Users/Mark/Documents/website/backend/teams.json', encoding='utf-8')
    data = json.load(f)
    teams = []
    for team in data:
        teams.append(Team.from_dict(team))
    return teams


def predict(home_id=None, away_id=None):
    game = Game(1, 100, "Manchester City", "Chelsea ")
    return game