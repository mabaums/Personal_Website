from data.sql_classes import *
from google.cloud.sql.connector import Connector
from sqlalchemy.orm import Session
from sqlalchemy import select, insert
import pg8000
import sqlalchemy
from data.api_handler import ApiHandler
import logging
import os


class DataStore:
    def __init__(self):
        self.engine = self.__init_connection_engine()
        self.handler = ApiHandler()
        self.session = None

        Base.metadata.create_all(self.engine)
        self.logger = logging.getLogger(__name__)
        self.logger.info('DataStore object created')

    def push_objs(self, objects):
        session = Session(self.engine)
        session.add_all(objects)
        session.commit()

    def get_fixtures(self, league=None, season=2021, live=True):
        if self.session is None:
            self.session = Session(self.engine)

        return self.handler.get_fixtures(league, season, live)


    def get_fixture(self, fixture_id):
        if self.session is None:
            self.session = Session(self.engine)

        fixture = self.session.query(Fixture).get(fixture_id)

        if fixture is None:
            self.logger.info(f'Fixture_id: {fixture_id} not found, attempting to get from API')
            fixture_json, success = self.handler.get_fixture(fixture_id)
            if success:
                fixture_json = fixture_json[0]
                new_fixture = Fixture(
                    fixture_id=fixture_id,
                    referee=fixture_json['fixture']['referee'],
                    league_id=fixture_json['league']['id'],
                    round=fixture_json['league']['round'],
                    goals_ft_home=fixture_json['score']['fulltime']['home'],
                    goals_ht_home=fixture_json['score']['halftime']['home'],
                    goals_ft_away=fixture_json['score']['fulltime   ']['away'],
                    goals_ht_away=fixture_json['score']['halftime']['away'],
                    away_id=fixture_json['teams']['away']['id'],
                    home_id=fixture_json['teams']['home']['id']
                )

                self.session.add(new_fixture)
                self.session.commit()
                return new_fixture.__repr__(), True
            else:
                return None, False
        self.logger.info(f'Got fixture id: {fixture_id}')
        return fixture.__repr__(), True

    def get_player(self, player_id=184, season_year=2021):
        if self.session is None:
            self.session = Session(self.engine)

        player_json = self.session.query(Player).get(player_id)

        if player_json is None:
            self.logger.info(f'Player_id: {player_id}, season_year={season_year} not found in database, attempting to '
                             f'get '
                             f'from API.')
            player_json, success = self.handler.get_player(player_id, season_year)
            if player_json is None:
                return self.logger.warning(
                    f'API did not return a player for player_id={player_id}, season_year={season_year}.')
            photo = player_json['player']['photo']
            name = player_json['player']['name']
            firstname = player_json['player']['firstname']
            lastname = player_json['player']['lastname']
            age = player_json['player']['age']
            birthdate = player_json['player']['birth']['date']

            new_player = Player(
                player_id=player_id,
                season_year=season_year,
                name=name,
                firstname=firstname,
                lastname=lastname,
                age=age,
                birthdate=birthdate,
                photo=photo
            )

            self.session.add(new_player)
            self.session.commit()
            return new_player.__repr__()
        self.logger.info(f"Player with id {player_id} and season {season_year} found in DB, successfully returned")
        return player_json.__repr__()

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
            creator=getconn
        )
        pool.dialect.description_encoding = None
        return pool
