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

    def get_fixtures(self, league_id=None, season=2021, live=True):
        if self.conn.sock is None:
            self.__connect_api()

        if league_id is None and live:
            res, suc = self.make_call("GET", f'/fixtures?live=all')
            if suc:
                if res is not None:
                    self.logger.info(f'API returned success fixture list league_id: {league_id} season_year: {season}')
                else:
                    self.logger.info(f'No fixtures available')
            return res, suc
        else:
            res, suc = self.make_call("GET", f'/fixtures?league={league_id}&season={season}')
            if suc:
                if res is not None:
                    self.logger.info(f'API returned success fixture list league_id: {league_id} season_year: {season}')
                else:
                    self.logger.info(f'No fixtures available')
            return res, suc

    def get_fixture(self, fixture_id):
        res, suc = self.make_call("GET", f'/fixtures?id={fixture_id}')
        if suc:
            if res is None:
                self.logger.info(f'No fixture found fixture_id: {fixture_id}')
            else:
                self.logger.info(f'Success fixture_id: {fixture_id}')
        return res, suc

    def get_player(self, player_id, season_year):
        res, suc = self.make_call("GET", "/players?id={}&season={}".format(player_id, season_year))
        if suc:
            if res is not None:
                self.logger.info(f'No player found (player_id: {player_id}, season_year: {season_year})')
            else:
                self.logger.info(
                    f'Requested successfully from API for player_id: {player_id}, season_year: {season_year}')
        return res, suc

    def make_call(self, method, query):
        self.conn.request(method, query, headers=self.headers)
        res = self.conn.getresponse()
        data = json.loads(res.read())
        if len(data['response']) > 0:
            return data['response'], True
        elif data['results'] == 0:
            return None, True
        elif len(data['errors']) > 0:
            self.logger.error(f'Erorr in API call, {data["errors"]}')
            return None, False

    def __connect_api(self):
        self.conn = http.client.HTTPSConnection("v3.football.api-sports.io")

        self.headers = {
            'x-rapidapi-host': "v3.football.api-sports.io",
            'x-rapidapi-key': "93e03c58cd2dcde693cc96a47ed67a71"
        }
