import json
from swagger_server.models.game import Game  # noqa: E501
from swagger_server.models.team import Team  # noqa: E501
import pandas as pd

class DataStore:
    def __int__(self):
        self.teams = {}
        self.standings = {}
        self.fixtures = {}

        self.__load_teams()
        self.__load_standings()

    def get_data(self):
        data_set = "data/prem.csv"
        data = pd.read_csv(data_set)
        return data

    def get_teams(self):
        f = open('data/teams.json', encoding='utf-8')
        data = json.load(f)
        teams = []
        for team in data:
            teams.append(Team.from_dict(team))
        return teams

    def get_standings(self):
        f = open('data/39-2021.json', encoding='utf-8')
        json_standings = json.load(f)
        return json_standings

    def get_fixture(self, fixture_id=0):
        return self.fixtures[fixture_id]

    def get_team(self, team_id=0):
        f = open('data/50-39-2021.json', encoding='utf-8')
        team_info = json.load(f)
        return team_info

    def __load_standings(self):
        """

        @rtype: object
        """
        f = open('Cdata/39-2021.json', encoding='utf-8')
        self.standings = json.load(f)
        f.close()

    def __load_teams(self):
        f = open('teams.json', encoding='utf-8')
        data = json.load(f)
        teams = []
        for team in data:
            teams.append(Team.from_dict(team))
        self.teams = teams
        f.close()