import json
from swagger_server.models.game import Game  # noqa: E501
from swagger_server.models.team import Team  # noqa: E501


def get_standing():
    f = open('C:/Users/Mark/Documents/website/backend/data/39-2021.json', encoding='utf-8')
    json_standings = json.load(f)
    return json_standings


def get_teams():
    f = open('teams.json', encoding='utf-8')
    data = json.load(f)
    teams = []
    for team in data:
        teams.append(Team.from_dict(team))
    return teams


def predict_game():
    game = Game(1, 100, "Manchester City", "Chelsea ")
    return game
