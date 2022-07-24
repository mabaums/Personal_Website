# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Team(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, team_id: int=None, team_name: str=None, team_logo: str=None, form: str=None, description: str=None):  # noqa: E501
        """Team - a model defined in Swagger

        :param team_id: The team_id of this Team.  # noqa: E501
        :type team_id: int
        :param team_name: The team_name of this Team.  # noqa: E501
        :type team_name: str
        :param team_logo: The team_logo of this Team.  # noqa: E501
        :type team_logo: str
        :param form: The form of this Team.  # noqa: E501
        :type form: str
        :param description: The description of this Team.  # noqa: E501
        :type description: str
        """
        self.swagger_types = {
            'team_id': int,
            'team_name': str,
            'team_logo': str,
            'form': str,
            'description': str
        }

        self.attribute_map = {
            'team_id': 'team_id',
            'team_name': 'team_name',
            'team_logo': 'team_logo',
            'form': 'form',
            'description': 'description'
        }
        self._team_id = team_id
        self._team_name = team_name
        self._team_logo = team_logo
        self._form = form
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'Team':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The team of this Team.  # noqa: E501
        :rtype: Team
        """
        return util.deserialize_model(dikt, cls)

    @property
    def team_id(self) -> int:
        """Gets the team_id of this Team.


        :return: The team_id of this Team.
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id: int):
        """Sets the team_id of this Team.


        :param team_id: The team_id of this Team.
        :type team_id: int
        """

        self._team_id = team_id

    @property
    def team_name(self) -> str:
        """Gets the team_name of this Team.


        :return: The team_name of this Team.
        :rtype: str
        """
        return self._team_name

    @team_name.setter
    def team_name(self, team_name: str):
        """Sets the team_name of this Team.


        :param team_name: The team_name of this Team.
        :type team_name: str
        """

        self._team_name = team_name

    @property
    def team_logo(self) -> str:
        """Gets the team_logo of this Team.


        :return: The team_logo of this Team.
        :rtype: str
        """
        return self._team_logo

    @team_logo.setter
    def team_logo(self, team_logo: str):
        """Sets the team_logo of this Team.


        :param team_logo: The team_logo of this Team.
        :type team_logo: str
        """

        self._team_logo = team_logo

    @property
    def form(self) -> str:
        """Gets the form of this Team.


        :return: The form of this Team.
        :rtype: str
        """
        return self._form

    @form.setter
    def form(self, form: str):
        """Sets the form of this Team.


        :param form: The form of this Team.
        :type form: str
        """

        self._form = form

    @property
    def description(self) -> str:
        """Gets the description of this Team.


        :return: The description of this Team.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Team.


        :param description: The description of this Team.
        :type description: str
        """

        self._description = description
