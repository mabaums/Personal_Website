import json
from swagger_server.models.game import Game  # noqa: E501
from swagger_server.models.team import Team  # noqa: E501
from machine_learning import MachineLearning
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Embedding, Dropout, Dense
from sklearn.preprocessing import RobustScaler
import numpy as np
from data.datastore import DataStore

datastore = DataStore()
ml = MachineLearning(datastore)

def get_squad(team_id=44):
    return datastore.get_squad(team_id)

def get_player(player_id=0):
    return datastore.get_player(player_id)

def get_fixture(fixture_id=71056):
    return datastore.get_fixture(fixture_id)

def get_team(team_id=65):
    return datastore.get_team(team_id)


def get_standing(league_id, season):
    return datastore.get_standing(league_id, season)

def get_teams():
    return datastore.get_standings()


def predict_game(team_id=10, away_id=9):
    game = Game(1, 100, "Manchester City", "Chelsea ")
    return game


def predict_round(round_number=38):
    return ml.RFN_predict(round_number)
