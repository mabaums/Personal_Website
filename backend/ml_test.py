import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Embedding, Dropout, Dense
from sklearn.preprocessing import RobustScaler
import seaborn as sns
from pylab import rcParams
import numpy as np
import tensorflow as tf
import random as python_random
import os
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc
from  matplotlib.ticker import FuncFormatter

sns.set(style='whitegrid', palette='muted', font_scale=1.5)

rcParams['figure.figsize'] = 22, 10

def main():
    data_set = "prem.csv"
    data = pd.read_csv(data_set)
    data = data[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']]
    print(data.head())
    data['Score'] = data['FTHG'] - data['FTAG']
    print(data['Score'])
    data['Round'] = np.zeros((len(data), 1))

    current_round = 1
    for row in range(1, len(data) + 1):
        data['Round'][row - 1] = current_round
        if (row % 10) == 0:
            current_round += 1
    teams = list(set(data['HomeTeam'].values))  # creating a list containing every team
    n_teams = len(teams)  # number of teams
    teamToIdx = {t: i for i, t in enumerate(teams)}  # our team vocabulary

    # assigning the games' home teams their corresponding team id
    homeId = [teamToIdx[id] for id in list(data['HomeTeam'].values)]
    data['Home_Id'] = homeId  # creating a new column for the home team id

    # assigning the games' away teams their corresponding team id
    awayId = [teamToIdx[id] for id in list(data['AwayTeam'].values)]
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

    train_set = data[data['Round'] < 10]
    X_train, y_train = create_dataset(train_set[['Home_Id', 'Away_Id']], train_set.Score)

    model = Sequential()
    model.add(Embedding(n_teams + 1, 9, input_length=2))
    model.add(LSTM(units=128, recurrent_dropout=0.2))
    model.add(Dropout(rate=0.2))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    history = model.fit(X_train, y_train,
                        epochs=25,
                        batch_size=9,
                        validation_split=0.1,
                        shuffle=False)


    def create_train_test_data(data, round):
        train_set = data[data['Round'] < round]
        test_set = data[data['Round'] == round]
        X_train, y_train = create_dataset(train_set[['Home_Id', 'Away_Id']], train_set.Score)
        X_test, y_test = create_dataset(test_set[['Home_Id', 'Away_Id']], test_set.Score)
        return {'train_set': train_set, 'test_set': test_set, 'X_train': X_train, 'y_train': y_train, 'X_test': X_test,
                'y_test': y_test}

    def retransform_y_data(y_test, y_pred):
        y_actual = score_transformer.inverse_transform(y_test.reshape(1, -1)).reshape(-1, 1)
        y_pred = score_transformer.inverse_transform(y_pred).reshape(-1, 1)
        return {'y_actual': y_actual, 'y_pred': y_pred}


    current_data = create_train_test_data(data, 10)
    y_pred = model.predict(current_data['X_test'])
    print(y_pred)
    retransformed_y_data = retransform_y_data(current_data['y_test'], y_pred)
    print(retransformed_y_data)

if __name__ == '__main__':
    main()