# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.game import Game  # noqa: E501
from swagger_server.models.team import Team  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClientController(BaseTestCase):
    """ClientController integration test stubs"""

    def test_get_standing(self):
        """Test case for get_standing

        Get standings of premier league
        """
        response = self.client.open(
            '/mabaums/Personal_Website/1.1.0/standings',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_teams(self):
        """Test case for get_teams

        returns Teams
        """
        response = self.client.open(
            '/mabaums/Personal_Website/1.1.0/teams',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_predict_game(self):
        """Test case for predict_game

        Predict the outcome of two teams playing
        """
        query_string = [('home_id', 56),
                        ('away_id', 56)]
        response = self.client.open(
            '/mabaums/Personal_Website/1.1.0/predict',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_predict_round(self):
        """Test case for predict_round

        predict every game of a certain round
        """
        query_string = [('round_number', 56)]
        response = self.client.open(
            '/mabaums/Personal_Website/1.1.0/predictRound',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
