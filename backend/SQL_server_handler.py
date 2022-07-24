import os
import pg8000
import sqlalchemy
from google.cloud.sql.connector import Connector
import json
import http.client
import time

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "93e03c58cd2dcde693cc96a47ed67a71"
    }



# The Cloud SQL Python Connector can be used along with SQLAlchemy using the
# 'creator' argument to 'create_engine'
def init_connection_engine() -> sqlalchemy.engine.Engine:
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


if __name__ == '__main__':
    pool = init_connection_engine()
    stmt = sqlalchemy.text("select * from player where player_id=184")
    result = pool.execute(stmt)
    print(result.fetchone())
    '''
    for player_id in result.fetchall():
        time.sleep(0.25)
        print(player_id[0])
        conn.request("GET", "/players?id={}&season=2021".format(player_id[0]), headers=headers)
        res = conn.getresponse()
        data = res.read()
        player_info = json.loads(data.decode("utf-8"))
        res = player_info['response'][0]

        player_id = res['player']['id']
        name = res['player']['name']
        name = name.replace('\'', '\'\'')
        print(name)
        lastname = res['player']['lastname']
        lastname = lastname.replace('\'', '\'\'')
        firstname = res['player']['firstname']
        firstname = firstname.replace('\'', '\'\'')
        age = res['player']['age']
        team_id = res['statistics'][0]['team']['id']
        photo = res['player']['photo']

        stmt = sqlalchemy.text("INSERT INTO player (player_id, name, lastname, firstname, age,"
                               " team_id, photo) VALUES ({}, \'{}\', \'{}\', \'{}\', {}, {}, \'{}\')".format(player_id, name, lastname,
                                                                   firstname, age, team_id, photo))
        result = pool.execute(stmt)
    
    f = open('data/fixtures.json')
    j_f = json.load(f)
    resp = j_f['response']
    for data in resp:
        fixture = data['fixture']
        league = data['league']
        teams = data['teams']
        goals = data['goals']

        fixture_id = fixture['id']
        ref = fixture['referee']
        date = fixture['timestamp']
        venue_id = fixture['venue']['id']
        league_id = league['id']
        home_team_id = teams['home']['id']
        away_team_id = teams['away']['id']
        home_goals = goals['home']
        away_goals = goals['away']
        round_number = league['round']
        season_year = league['season']

        stmt = sqlalchemy.text("INSERT INTO fixture (fixture_id, referee, date, home_team_id, away_team_id,"
                               " home_goals, away_goals, round_number, season_year, league_id) VALUES"
                               " ({}, \'{}\', {}, {}, {}, {}, {}, \'{}\', {} ,{})"
                               "".format(fixture_id, ref, date, home_team_id, away_team_id, home_goals, away_goals,
                                         round_number, season_year, league_id))
        result = pool.execute(stmt)
    '''
    '''
    files = os.listdir('data/fixtures-39-2021')
    for file in files:
        f = open('data/fixtures-39-2021/{}'.format(file))
        j_f = json.load(f)
        resp = j_f['response']
        fixture_id = file.split('.')[0]
        for team in resp:
            team_id = team['team']['id']
            for player in team['players']:
                statistics = player['statistics'][0]
                minutes = statistics['games']['minutes']
                shots_total = statistics['shots']['total']
                goals_conceded = statistics['goals']['conceded']
                goals_scored = statistics['goals']['total']
                assists = statistics['goals']['assists']
                passes_total = statistics['passes']['total']
                passes_key = statistics['passes']['key']
                passes_accuracy = statistics['passes']['accuracy']
                tackles = statistics['tackles']['total']

                player_id = player['player']['id']
                player_rating = statistics['games']['rating']
                player_position = statistics['games']['position']
                stmt = sqlalchemy.text("INSERT INTO player_fixture (player_id, rating, position, fixture_id, team_id,"
                                       " minutes, shots_total, goals_conceded, goals_scored, assists, passes_total, passes_key,"
                                       " passes_accuracy, tackles) VALUES ({}, {}, \'{}\', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})".format(player_id,
                                                                                                           player_rating if player_rating is not None else 0,
                                                                                                           player_position,
                                                                                                           fixture_id,
                                                                                                           team_id,
                                                                                                           minutes if minutes is not None else 0,
                                                                                                           shots_total if shots_total is not None else 0,
                                                                                                           goals_conceded if goals_conceded is not None else 0,
                                                                                                        goals_scored if goals_scored is not None else 0,
                                                                                                           assists if assists is not None else 0,
                                                                                                           passes_total if passes_total is not None else 0,
                                                                                                           passes_key if passes_key is not None else 0,
                                                                                                           passes_accuracy if passes_accuracy is not None else 0,
                                                                                                           tackles if tackles is not None else 0))
                result = pool.execute(stmt)
                # print(result)
        print('Fixture : {} done'.format(fixture_id))
    '''