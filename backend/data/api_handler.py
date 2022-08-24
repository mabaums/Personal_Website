import http.client
import json
import logging


class ApiHandler:
    def __init__(self):
        self.conn = None
        # TODO: check if connection is open

        self.__connect_api()
        self.logger = logging.getLogger(__name__)
        self.logger.info('ApiHandler object created')

    def get_fixture_stats(self, fixture_id=None):
        return self.make_call("GET", f"/fixtures/players?fixture={fixture_id}")

    def get_fixtures(self, league_id=None, season=2021, live=True):
        if league_id is None:
            return self.make_call("GET", f'/fixtures?live=all')
        else:
            return self.make_call("GET", f'/fixtures?league={league_id}&season={season}')

    def get_fixture(self, fixture_id):
        return self.make_call("GET", f'/fixtures?id={fixture_id}')

    def get_player(self, player_id, season_year):
        return self.make_call("GET", "/players?id={}&season={}".format(player_id, season_year))

    def get_standing(self, league_id=39, season_id=2021):
        return self.make_call("GET", f"/standings?league={league_id}&season={season_id}")



    def make_call(self, method, query):
        self.conn.request(method, query, headers=self.headers)
        res = self.conn.getresponse()
        data = json.loads(res.read())

        if res.status != 200:
            self.logger.error(f'HTTP ERROR: {res.status} call {method} {query}')
            raise Exception(f"HTTP request to API ERROR {res.status}")

        self.logger.info(f'API-FOOTBALL CALL - {method} {query} Errors ({len(data["errors"])}),'
                         f' Responses ({len(data["response"])})')

        if len(data['errors']):
            raise Exception(f"Errors in query {data['errors']}")

        return data['response']

    def __connect_api(self):
        self.conn = http.client.HTTPSConnection("v3.football.api-sports.io")

        self.headers = {
            'x-rapidapi-host': "v3.football.api-sports.io",
            'x-rapidapi-key': "93e03c58cd2dcde693cc96a47ed67a71"
        }
