from sql_classes import *
from google.cloud.sql.connector import Connector
from sqlalchemy.orm import Session
from sqlalchemy import select, insert
import pg8000
import sqlalchemy
from api_handler import ApiHandler


class DataStore:
    def __init__(self):
        self.engine = self.__init_connection_engine()
        self.handler = ApiHandler()

        Base.metadata.create_all(self.engine)
        print('__init__ called')

    def push_objs(self, objects):
        session = Session(self.engine)
        session.add_all(objects)
        session.commit()

    def get_fixture(self, fixture_ids=None, live=False, season=2021):
        if fixture_ids is None:
            self.handler.get_fixture(live=True)
        else:
            for fixture in fixture_ids:
                self.handler.get_fixture(fixture_id=fixture)

    def get_player(self, player_id=184, season_year=2021):
        session = Session(self.engine)

        player_req = session.query(Player).get(player_id)

        if player_req is None:
            print('Player id and season combo not found')
            player_json = self.handler.get_player(player_id, season_year)
            if player_json is None:
                return "No player with Id or other error"
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

            session.add(new_player)
            session.commit()
            return new_player.__repr__()
            '''
            for stats in player_json['statistics']:
                goals = stats['goals']['total']
                team_id = stats['team']['id']
                league_id = stats['league']['id']

                new_player = Player(
                    player_id=player_id,
                    season_year=season_year,
                    name=name,
                    firstname=firstname,
                    lastname=lastname,
                    photo=photo,
                    age=age,
                    birthdate=birthdate,
                    league_id=league_id,
                    goals=goals,
                    team_id=team_id
                )
                session.add(new_player)
                session.commit()
                '''
        session.commit()
        return player_req.__repr__()

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
            pool_size=20,
            max_overflow=20
        )
        pool.dialect.description_encoding = None
        return pool


if __name__ == "__main__":
    datastore = DataStore()
    for i in range(1000, 1500):
        player_req = datastore.get_player(i, 2021)
        print(player_req)
