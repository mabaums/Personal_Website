import http.client
import json

class ApiHandler:
    def __init__(self):
        self.conn = None

        self.__connect_api()

    def get_fixtures(self, fixture_ids=None, season_year=2021, live=False):
        if fixture_ids is not None:
            self.conn.request("GET", "/fixtures?")
        elif live:
            self.conn.request("GET", "/fixtures?live=all", headers=self.headers)
            res = self.conn.getresponse()
            data = json.loads(res.read())
        else:
            return "WHAT DO YOU WANT"

    def get_fixture(self, fixture_id):
        if fixture_id is not None:
            self.conn.request()
        else:
            return "WHAT?"

    def list_fixtures(self, league_id=39, season_year=2021, live=False):
        if live:
            self.conn.request
        else:
            self.conn.request

    def get_player(self, player_id, season_year):
        self.conn.request("GET", "/players?id={}&season={}".format(player_id, season_year), headers=self.headers)
        res = self.conn.getresponse()
        data = json.loads(res.read())

        if len(data['response']) > 0:
            print('Requested player_id: {} season: {}'.format(player_id, season_year))
            # print(data['response'])
            return data['response'][0]
        else:
            print('ERROR MORON')
            return None

    def __connect_api(self):
        self.conn = http.client.HTTPSConnection("v3.football.api-sports.io")

        self.headers = {
            'x-rapidapi-host': "v3.football.api-sports.io",
            'x-rapidapi-key': "93e03c58cd2dcde693cc96a47ed67a71"
        }
