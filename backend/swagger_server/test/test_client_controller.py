# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.predicted_game import PredictedGame  # noqa: E501
from swagger_server.models.team import Team  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClientController(BaseTestCase):
    """ClientController integration test stubs"""

    def test_get_standing(self):
        """Test case for get_standing

        Get standings from the selected league
        """
        query_string = [('league_id', 56)]
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
