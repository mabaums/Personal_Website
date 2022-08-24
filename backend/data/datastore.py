from data.api_handler import ApiHandler
import logging
import pandas as pd
import os
from swagger_server.models.player import Player
from swagger_server.models.fixture import Fixture


class DataStore:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info('DataStore object created')
        self.api_handler = ApiHandler()

        self.__players = pd.DataFrame(columns=['name', 'age', 'lastname', 'firstname', 'photo', 'player_id', 'team_id'])
        self.__fixtures = pd.DataFrame()
        self.__player_fixtures = {}
        self.__team_fixtures = {}
        self.__fixture_list = pd.DataFrame()

    def get_standing(self, league_id=39, season_id=2021):
        standings_json = self.api_handler.get_standing(league_id, season_id)
        print(standings_json)
        return None

    def get_player(self, player_id=184, season=2021):
        if (self.__players['player_id'] == player_id).any():
            player = self.__players.loc[self.__players['player_id'] == player_id]
            return Player.from_dict(player.to_dict('records')[0])
        else:
            response = self.api_handler.get_player(player_id, season)
            player_json = response[0]['player']
            # statistics = response[0]['statistics']
            player_dict = {
                'name': player_json['name'],
                'player_id': player_json['id'],
                'firstname': player_json['firstname'],
                'lastname': player_json['lastname'],
                'photo': player_json['photo'],
                'age': player_json['age'],
                'team_id': None
            }

            player_pd = pd.DataFrame(player_dict, index=[0])
            self.__players = pd.concat([self.__players, player_pd])
        return Player.from_dict(player_dict)

    def get_dataframe_player_fixture(self, league_id=39, seasons=None):
        if seasons is None:
            seasons = [2021]
        if league_id in self.__team_fixtures:
            return self.__player_fixtures[league_id], self.__team_fixtures[league_id]
        for season in seasons:
            fixtures_json = self.api_handler.get_fixtures(league_id, season)

            player_fixtures = []
            fixtures = []
            for fixture in fixtures_json:
                fixtures.append([fixture['fixture']['id'], fixture['teams']['home']['id'],
                                 fixture['teams']['away']['id'],
                                 fixture['fixture']['timestamp'],
                                 fixture['goals']['home'],
                                 fixture['goals']['away'],
                                 int(fixture['league']['round'].split(' - ')[1])])
                fixture_stats_json = self.api_handler.get_fixture_stats(fixture['fixture']['id'])
                for team in fixture_stats_json:
                    for player in team['players']:
                        stats = player['statistics'][0]
                        player_fixtures.append([
                            player['player']['id'],
                            team['team']['id'],
                            fixture['fixture']['id'],
                            stats['games']['minutes'],
                            stats['games']['position'],
                            stats['games']['rating'],
                            stats['goals']['total'],
                            stats['passes']['total'],
                            stats['tackles']['total'],
                            stats['duels']['total'],
                            stats['dribbles']['attempts']
                        ])
            player_fixture_df = pd.DataFrame(player_fixtures,
                                             columns=['player_id', 'team_id', 'fixture_id', 'minutes', 'position',
                                                      'rating', 'goals', 'passes',
                                                      'tackles', 'duels',
                                                      'dribbles'])
            fixture_df = pd.DataFrame(fixtures,
                                      columns=['fixture_id', 'home_id', 'away_id', 'timestamp', 'home_goals',
                                               'away_goals', 'round_number']
                                      )
            player_fixture_df.to_csv('player_fixture.csv')
            fixture_df.to_csv('fixture.csv')
            self.__team_fixtures[league_id] = fixture_df
            self.__player_fixtures[league_id] = player_fixture_df
            return player_fixture_df, fixture_df
