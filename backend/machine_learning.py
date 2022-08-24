from data.datastore import DataStore
import json
from swagger_server.models.game import Game  # noqa: E501
from swagger_server.models.team import Team  # noqa: E501
from swagger_server.models.predicted_game import PredictedGame
from sklearn.ensemble import RandomForestRegressor

import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Embedding, Dropout, Dense
from sklearn.preprocessing import RobustScaler
import numpy as np
from data.datastore import DataStore


class MachineLearning:

    def __init__(self, dataStore=None):
        self.dataStore = dataStore if dataStore is not None else DataStore()
        self.data = []
        self.model = None
        self.score_transformer = RobustScaler()
        self.y_pred = None

    def RFN_predict(self, round_number=38, league_id=39):

        X_train = [[[1, 3, 5] for x in range(10)] for _ in range(10)]
        y_train = [[1] for _ in range(10)]
        rf = RandomForestRegressor(n_estimators=1000, random_state=42)
        rf.fit(X_train, y_train)

        print(X_train)
        '''
        player_fixtures_df, fixture_df = pd.read_csv('player_fixture.csv'), pd.read_csv(
            'fixture.csv')  # self.dataStore.get_dataframe_player_fixture(league_id)
        fixture_df['FTR'] = fixture_df['home_goals'] - fixture_df['away_goals']
        rating_avgs = player_fixtures_df.groupby(['fixture_id', 'team_id']).rating.mean()
        # print(rating_avgs.to_dict())
        fixture_df['h_a_r'] = [rating_avgs[(row['fixture_id'], row['home_id'])] for i, row in fixture_df.iterrows()] # home average rating
        fixture_df['a_a_r'] = [rating_avgs[(row['fixture_id'], row['away_id'])] for i, row in fixture_df.iterrows()] # away average rating

        training_data = fixture_df[fixture_df['round_number'] < round_number]
        testing_data = fixture_df[fixture_df['round_number'] == round_number]


        # fixture_df['h_avg_rating'] = rating_team_avgs[(fixture_df['fixture_id'], fixture_df['home_id'])]

        # print(fixture_df)
        # print(player_fixtures_df[player_fixtures_df['fixture_id'].isin(training_data['fixture_id'])])

        X_train = np.array(training_data[['home_id', 'away_id']])
        y_train = np.array(training_data[['home_goals', 'away_goals']])

        X_test = np.array(testing_data[['home_id', 'away_id', 'home_avg_rating', 'away_avg_rating']])
        y_test = np.array(testing_data[['home_goals', 'away_goals']])
        rf = RandomForestRegressor(n_estimators=1000, random_state=42)
        rf.fit(X_train, y_train)

        print(rf.predict(X_test))
        print(y_test)
        # print(rf.predict(np.array(testing_data[['home_id', 'away_id']])))
        # print(testing_data[['home_goals', 'away_goals']])
        '''
        return None

    def LSTM_predict(self, round_number=38, league_id=39):
        return None


if __name__ == '__main__':
    ml = MachineLearning()
    ml.RFN_predict(38)
