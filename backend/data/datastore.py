import json
from swagger_server.models.game import Game  # noqa: E501
from swagger_server.models.team import Team  # noqa: E501
from swagger_server.models.player import Player
from swagger_server.models.fixture import Fixture
from swagger_server.models.team_standing import TeamStanding
from swagger_server.models.predicted_game import PredictedGame
import pandas as pd
import os
import pg8000
import sqlalchemy
from google.cloud.sql.connector import Connector
import http.client
import time


class DataStore:
    def __init__(self):
        self.teams = {}
        self.pool = None
        self.players = {}
        self.leagues = {}
        self.headers = {}
        self.conn = None

        self.__connect_api()
        self.pool = self.__init_connection_engine()

    def get_team_list(self):
        return None

    def get_seasons(self):
        return None

    def get_team(self, team_id=0):
        return None

    def get_fixture(self, fixture_id):
        return None

    def get_fixtures(self, team_id):
        return None

    def get_player_fixture(self, p_id, f_id):
        return None

    def get_squad(self, team_id=0):
        return [Player()]

    def get_player(self, player_id=0, season_year=2021):
        """
        If the player is in the database return it otherwise attempts to get data from api,
        if that also fails return an error
        @param player_id: id of player
        @return: Player model
        """
        # TODO: Update database and then this code to include the season. Not necessary for now
        stmt = sqlalchemy.text("select * from player where player_id={}".format(player_id))
        res = self.pool.execute(stmt).fetchone()
        if len(res):
            return Player(name=res[1], firstname=res[4], player_id=res[0], lastname=res[2], team_id=res[3],
                          photo=res[5])
        else:
            self.conn.request("GET", "/players?id={}&season={}".format(player_id, season_year), headers=self.headers)
            res = self.conn.getresponse()
            data = res.read()
            player_info = json.loads(data.decode("utf-8"))

            res = player_info['response'][0]

            player_id = res['player']['id']
            name = res['player']['name']
            name = name.replace('\'', '\'\'')

            lastname = res['player']['lastname']
            lastname = lastname.replace('\'', '\'\'')

            firstname = res['player']['firstname']
            firstname = firstname.replace('\'', '\'\'')

            age = res['player']['age']
            team_id = res['statistics'][0]['team']['id']
            photo = res['player']['photo']
            if len(data['errors']):
                return Exception
            else:
                stmt = sqlalchemy.text("INSERT INTO player (player_id, name, lastname, firstname, age,"
                               " team_id, photo) VALUES ({}, \'{}\', \'{}\', \'{}\', {}, {}, \'{}\'"..format(player_id, name, lastname,
                                                                   firstname, age, team_id, photo))
                result = self.pool.execute(stmt)

    def execute_sql_query(self, stmt):
        # TODO: add error catching etc in here
        result = self.pool.execute(stmt)
        return result.fetchall()

    def get_teams(self, league_id=39, season_year=2021):
        self.conn.request("GET", "/teams/statistics?season=2021&team={}&league=39".format(team_id), headers=headers)

        res = self.conn.getresponse()
        data = res.read()
        return data['response'][0]

    def get_standings(self, league_id=39, season_year=2021):
        '''
        TODO: Maybe keep this in DB?? Create table for each or just one large table with standings
        @param league_id: id of league requested
        @param season_year: year of standings to get
        @return: A json of the standings with basic info.
        '''
        self.conn.request("GET", "/standings?league={}&season={}".format(league_id, season_year), headers=self.headers)
        res = self.conn.getresponse()
        data = json.loads(res.read())
        data = data['response'][0]['league']['standings'][0]

        # print(data)
        standings = []

        for team in data:
            print(team['rank'])
            standings.append(TeamStanding(rank=team['rank'], team_id=team['team']['id'], team_name=team['team']['name'],
                                          team_logo=team['team']['logo'], points=team['points'],
                                          goals_diff=team['goalsDiff'], form=team['form'],
                                          description=team['description']))

        return standings

    def __connect_api(self):
        self.conn = http.client.HTTPSConnection("v3.football.api-sports.io")

        self.headers = {
            'x-rapidapi-host': "v3.football.api-sports.io",
            'x-rapidapi-key': "93e03c58cd2dcde693cc96a47ed67a71"
        }

    def __init_connection_engine(self) -> sqlalchemy.engine.Engine:
        def getconn() -> pg8000.dbapi.Connection:
            # initialize Connector object for connections to Cloud SQL
            with Connector() as connector:
                conn: pg8000.dbapi.Connection = connector.connect(
                    "mark-website-355321:us-central1:football-database",  # os.environ["POSTGRES_CONNECTION_NAME"],
                    "pg8000",
                    user="postgres",  # os.environ["POSTGRES_USER"],
                    password="Marik123",  # os.environ["POSTGRES_PASS"],
                    db="postgres",  # os.environ["POSTGRES_DB"],
                )
                return conn

        # create SQLAlchemy connection pool
        pool = sqlalchemy.create_engine(
            "postgresql+pg8000://",
            creator=getconn,
        )
        pool.dialect.description_encoding = None
        return pool
