# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class PredictedGame(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, goals_home: int=None, goals_away: int=None, name_home: str=None, name_away: str=None):  # noqa: E501
        """PredictedGame - a model defined in Swagger

        :param goals_home: The goals_home of this PredictedGame.  # noqa: E501
        :type goals_home: int
        :param goals_away: The goals_away of this PredictedGame.  # noqa: E501
        :type goals_away: int
        :param name_home: The name_home of this PredictedGame.  # noqa: E501
        :type name_home: str
        :param name_away: The name_away of this PredictedGame.  # noqa: E501
        :type name_away: str
        """
        self.swagger_types = {
            'goals_home': int,
            'goals_away': int,
            'name_home': str,
            'name_away': str
        }

        self.attribute_map = {
            'goals_home': 'goals_home',
            'goals_away': 'goals_away',
            'name_home': 'name_home',
            'name_away': 'name_away'
        }
        self._goals_home = goals_home
        self._goals_away = goals_away
        self._name_home = name_home
        self._name_away = name_away

    @classmethod
    def from_dict(cls, dikt) -> 'PredictedGame':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The predicted_game of this PredictedGame.  # noqa: E501
        :rtype: PredictedGame
        """
        return util.deserialize_model(dikt, cls)

    @property
    def goals_home(self) -> int:
        """Gets the goals_home of this PredictedGame.


        :return: The goals_home of this PredictedGame.
        :rtype: int
        """
        return self._goals_home

    @goals_home.setter
    def goals_home(self, goals_home: int):
        """Sets the goals_home of this PredictedGame.


        :param goals_home: The goals_home of this PredictedGame.
        :type goals_home: int
        """

        self._goals_home = goals_home

    @property
    def goals_away(self) -> int:
        """Gets the goals_away of this PredictedGame.


        :return: The goals_away of this PredictedGame.
        :rtype: int
        """
        return self._goals_away

    @goals_away.setter
    def goals_away(self, goals_away: int):
        """Sets the goals_away of this PredictedGame.


        :param goals_away: The goals_away of this PredictedGame.
        :type goals_away: int
        """

        self._goals_away = goals_away

    @property
    def name_home(self) -> str:
        """Gets the name_home of this PredictedGame.


        :return: The name_home of this PredictedGame.
        :rtype: str
        """
        return self._name_home

    @name_home.setter
    def name_home(self, name_home: str):
        """Sets the name_home of this PredictedGame.


        :param name_home: The name_home of this PredictedGame.
        :type name_home: str
        """

        self._name_home = name_home

    @property
    def name_away(self) -> str:
        """Gets the name_away of this PredictedGame.


        :return: The name_away of this PredictedGame.
        :rtype: str
        """
        return self._name_away

    @name_away.setter
    def name_away(self, name_away: str):
        """Sets the name_away of this PredictedGame.


        :param name_away: The name_away of this PredictedGame.
        :type name_away: str
        """

        self._name_away = name_away
