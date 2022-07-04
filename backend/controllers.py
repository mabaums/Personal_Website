import json
from swagger_server.models.game import Game  # noqa: E501
from swagger_server.models.team import Team  # noqa: E501

import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Embedding, Dropout, Dense
from sklearn.preprocessing import RobustScaler
import numpy as np
from data.datastore import DataStore

datastore = DataStore()


def get_team(team_id=10):
    return datastore.get_team(team_id)


def get_standing():
    return datastore.get_standings()


def get_teams():
    return datastore.get_standings()


def predict_game(team_id=10, away_id=9):
    game = Game(1, 100, "Manchester City", "Chelsea ")
    return game


def predict_round(round_number=38):
    data = datastore.get_data()
    data = data[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']]  # This will be data used in the LSTM, with the last
    # 3 used as the score
    data['Score'] = data['FTHG'] - data['FTAG']
    data['Round'] = np.zeros((len(data), 1))  # This is sort of chronological, although in reality there are days
    # were some teams won't play or get rescheduled so the LSTM may be less accurate as they will not actually be in
    # order for now
    curr_round = 1

    '''
    This following loop sets the round numbers to each fixture
    '''

    for row in range(1, len(data) + 1):
        data['Round'][row - 1] = curr_round
        if (row % 10) == 0:
            curr_round += 1
    teams = list(set(data['HomeTeam'].values))  # creating a list containing every team
    n_teams = len(teams)  # number of teams
    teamToIdx = {t: i for i, t in enumerate(teams)}  # our team vocabulary
    homeId = [teamToIdx[id] for id in
              list(data['HomeTeam'].values)]  # assigning the games' home teams their corresponding team id
    data['Home_Id'] = homeId  # creating a new column for the home team id
    awayId = [teamToIdx[id] for id in
              list(data['AwayTeam'].values)]  # assigning the games' away teams their corresponding team id
    data['Away_Id'] = awayId  # creating a new row for the away team id

    score_transformer = RobustScaler()
    score_transformer = score_transformer.fit(data[['Score']])
    data['Score'] = score_transformer.transform(data[['Score']])

    def create_dataset(X, y):
        Xs, ys = [], []
        for i in range(len(X)):
            v = X.iloc[i].values
            Xs.append(v)
            ys.append(y.iloc[i])
        return np.array(Xs), np.array(ys)

    def create_train_test_data(data, round):
        train_set = data[data['Round'] < round]
        test_set = data[data['Round'] == round]
        X_train, y_train = create_dataset(train_set[['Home_Id', 'Away_Id']], train_set.Score)
        X_test, y_test = create_dataset(test_set[['Home_Id', 'Away_Id']], test_set.Score)
        return {'train_set': train_set, 'test_set': test_set, 'X_train': X_train, 'y_train': y_train, 'X_test': X_test,
                'y_test': y_test}

    def create_model(n_teams, lstm_units=128, optimizer='adam', loss='mean_squared_error', dropout_rate=0.2,
                     input_length=2, batchsize=10):
        model = Sequential()
        model.add(Embedding(n_teams + 1, batchsize, input_length=input_length))
        model.add(LSTM(units=lstm_units, recurrent_dropout=dropout_rate))
        model.add(Dropout(rate=dropout_rate))
        model.add(Dense(units=1))
        model.compile(optimizer=optimizer, loss=loss)
        return model

    def train_model(model, X, y, epochs=25, batch_size=10):
        history = model.fit(X, y,
                            epochs=epochs,
                            batch_size=batch_size,
                            shuffle=False)
        return history

    def predict_results(model, X):
        y_pred = model.predict(X)
        return y_pred

    def retransform_y_data(y_test, y_pred):
        y_actual = score_transformer.inverse_transform(y_test.reshape(1, -1)).reshape(-1, 1)
        y_pred = score_transformer.inverse_transform(y_pred).reshape(-1, 1)
        return {'y_actual': y_actual, 'y_pred': y_pred}

    current_data = create_train_test_data(data, round_number)
    print(current_data["X_test"])
    model = create_model(n_teams)
    history = train_model(model, X=current_data['X_train'], y=current_data['y_train'])
    y_pred = predict_results(model, current_data['X_test'])
    retransformed_y_data = retransform_y_data(current_data['y_test'], y_pred)

    predicted_games = [
        {"Fixture": i, "Home Team": data['HomeTeam'][(round_number - 1) * 10 + i],
         "Away Team": data['AwayTeam'][(round_number - 1) * 10 + i],
         "Predicted GD": str(retransformed_y_data['y_pred'][i][0]),
         "Predicted Result": str(
             "H" if retransformed_y_data['y_pred'][i][0] > .5 else "A" if retransformed_y_data['y_pred'][i][
                                                                              0] < -.5 else "D"),
         "Actual GD": str(retransformed_y_data['y_actual'][i][0]),
         "Full Time Result": data['FTR'][(round_number - 1) * 10 + i]
         }
        for i in range(len(retransformed_y_data['y_pred']))]
    return predicted_games
