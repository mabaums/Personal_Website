# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.fixture import Fixture  # noqa: E501
from swagger_server.models.player import Player  # noqa: E501
from swagger_server.models.predicted_game import PredictedGame  # noqa: E501
from swagger_server.models.team import Team  # noqa: E501
from swagger_server.models.team_standing import TeamStanding  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClientController(BaseTestCase):
    """ClientController integration test stubs"""

    def test_get_fixture(self):
        """Test case for get_fixture

        Get basic info about a fixture
        """
        query_string = [('fixture_id', 56)]
        response = self.client.open(
            '/mabaums/Personal_Website/1.2.0/fixture',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_player(self):
        """Test case for get_player

        get basic info about a player
        """
        query_string = [('player_id', 56)]
        response = self.client.open(
            '/mabaums/Personal_Website/1.2.0/player',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_squad(self):
        """Test case for get_squad

        get list of players from a team
        """
        query_string = [('team_id', 56)]
        response = self.client.open(
            '/mabaums/Personal_Website/1.2.0/squad',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_standing(self):
        """Test case for get_standing

        Get standings from the selected league
        """
        query_string = [('league_id', 56),
                        ('season', 56)]
        response = self.client.open(
            '/mabaums/Personal_Website/1.2.0/standings',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_team(self):
        """Test case for get_team

        get team of specified id
        """
        query_string = [('team_id', 56)]
        response = self.client.open(
            '/mabaums/Personal_Website/1.2.0/team',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_predict_game(self):
        """Test case for predict_game

        Predict the outcome of two teams playing
        """
        query_string = [('home_id', 56),
                        ('away_id', 56),
                        ('algo_id', 56)]
        response = self.client.open(
            '/mabaums/Personal_Website/1.2.0/predictGame',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_predict_round(self):
        """Test case for predict_round

        Predict a certain round based on the previous weeks.
        """
        query_string = [('round_number', 56),
                        ('algo_id', 56)]
        response = self.client.open(
            '/mabaums/Personal_Website/1.2.0/predictRound',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
