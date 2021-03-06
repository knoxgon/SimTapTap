# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Pet(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, level: int=None, tier: int=None, skill1level: int=None, skill2level: int=None, skill3level: int=None, skill4level: int=None):  # noqa: E501
        """Pet - a model defined in Swagger

        :param id: The id of this Pet.  # noqa: E501
        :type id: str
        :param level: The level of this Pet.  # noqa: E501
        :type level: int
        :param tier: The tier of this Pet.  # noqa: E501
        :type tier: int
        :param skill1level: The skill1level of this Pet.  # noqa: E501
        :type skill1level: int
        :param skill2level: The skill2level of this Pet.  # noqa: E501
        :type skill2level: int
        :param skill3level: The skill3level of this Pet.  # noqa: E501
        :type skill3level: int
        :param skill4level: The skill4level of this Pet.  # noqa: E501
        :type skill4level: int
        """
        self.swagger_types = {
            'id': str,
            'level': int,
            'tier': int,
            'skill1level': int,
            'skill2level': int,
            'skill3level': int,
            'skill4level': int
        }

        self.attribute_map = {
            'id': 'id',
            'level': 'level',
            'tier': 'tier',
            'skill1level': 'skill1level',
            'skill2level': 'skill2level',
            'skill3level': 'skill3level',
            'skill4level': 'skill4level'
        }

        self._id = id
        self._level = level
        self._tier = tier
        self._skill1level = skill1level
        self._skill2level = skill2level
        self._skill3level = skill3level
        self._skill4level = skill4level

    @classmethod
    def from_dict(cls, dikt) -> 'Pet':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Pet of this Pet.  # noqa: E501
        :rtype: Pet
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Pet.

        Which pet is described  # noqa: E501

        :return: The id of this Pet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Pet.

        Which pet is described  # noqa: E501

        :param id: The id of this Pet.
        :type id: str
        """
        allowed_values = ["EDISON", "VINCI", "RAPHAEL"]  # noqa: E501
        if id not in allowed_values:
            raise ValueError(
                "Invalid value for `id` ({0}), must be one of {1}"
                .format(id, allowed_values)
            )

        self._id = id

    @property
    def level(self) -> int:
        """Gets the level of this Pet.

        The level of the pet itself  # noqa: E501

        :return: The level of this Pet.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level: int):
        """Sets the level of this Pet.

        The level of the pet itself  # noqa: E501

        :param level: The level of this Pet.
        :type level: int
        """
        if level is not None and level > 200:  # noqa: E501
            raise ValueError("Invalid value for `level`, must be a value less than or equal to `200`")  # noqa: E501
        if level is not None and level < 0:  # noqa: E501
            raise ValueError("Invalid value for `level`, must be a value greater than or equal to `0`")  # noqa: E501

        self._level = level

    @property
    def tier(self) -> int:
        """Gets the tier of this Pet.

        The tier of the pet  # noqa: E501

        :return: The tier of this Pet.
        :rtype: int
        """
        return self._tier

    @tier.setter
    def tier(self, tier: int):
        """Sets the tier of this Pet.

        The tier of the pet  # noqa: E501

        :param tier: The tier of this Pet.
        :type tier: int
        """
        if tier is not None and tier > 4:  # noqa: E501
            raise ValueError("Invalid value for `tier`, must be a value less than or equal to `4`")  # noqa: E501
        if tier is not None and tier < 0:  # noqa: E501
            raise ValueError("Invalid value for `tier`, must be a value greater than or equal to `0`")  # noqa: E501

        self._tier = tier

    @property
    def skill1level(self) -> int:
        """Gets the skill1level of this Pet.

        The level of the pet's first skill (active)  # noqa: E501

        :return: The skill1level of this Pet.
        :rtype: int
        """
        return self._skill1level

    @skill1level.setter
    def skill1level(self, skill1level: int):
        """Sets the skill1level of this Pet.

        The level of the pet's first skill (active)  # noqa: E501

        :param skill1level: The skill1level of this Pet.
        :type skill1level: int
        """
        if skill1level is not None and skill1level > 120:  # noqa: E501
            raise ValueError("Invalid value for `skill1level`, must be a value less than or equal to `120`")  # noqa: E501
        if skill1level is not None and skill1level < 0:  # noqa: E501
            raise ValueError("Invalid value for `skill1level`, must be a value greater than or equal to `0`")  # noqa: E501

        self._skill1level = skill1level

    @property
    def skill2level(self) -> int:
        """Gets the skill2level of this Pet.

        The level of the pet's second skill (passive)  # noqa: E501

        :return: The skill2level of this Pet.
        :rtype: int
        """
        return self._skill2level

    @skill2level.setter
    def skill2level(self, skill2level: int):
        """Sets the skill2level of this Pet.

        The level of the pet's second skill (passive)  # noqa: E501

        :param skill2level: The skill2level of this Pet.
        :type skill2level: int
        """
        if skill2level is not None and skill2level > 20:  # noqa: E501
            raise ValueError("Invalid value for `skill2level`, must be a value less than or equal to `20`")  # noqa: E501
        if skill2level is not None and skill2level < 0:  # noqa: E501
            raise ValueError("Invalid value for `skill2level`, must be a value greater than or equal to `0`")  # noqa: E501

        self._skill2level = skill2level

    @property
    def skill3level(self) -> int:
        """Gets the skill3level of this Pet.

        The level of the pet's third skill (passive)  # noqa: E501

        :return: The skill3level of this Pet.
        :rtype: int
        """
        return self._skill3level

    @skill3level.setter
    def skill3level(self, skill3level: int):
        """Sets the skill3level of this Pet.

        The level of the pet's third skill (passive)  # noqa: E501

        :param skill3level: The skill3level of this Pet.
        :type skill3level: int
        """
        if skill3level is not None and skill3level > 20:  # noqa: E501
            raise ValueError("Invalid value for `skill3level`, must be a value less than or equal to `20`")  # noqa: E501
        if skill3level is not None and skill3level < 0:  # noqa: E501
            raise ValueError("Invalid value for `skill3level`, must be a value greater than or equal to `0`")  # noqa: E501

        self._skill3level = skill3level

    @property
    def skill4level(self) -> int:
        """Gets the skill4level of this Pet.

        The level of the pet's fourth skill (passive)  # noqa: E501

        :return: The skill4level of this Pet.
        :rtype: int
        """
        return self._skill4level

    @skill4level.setter
    def skill4level(self, skill4level: int):
        """Sets the skill4level of this Pet.

        The level of the pet's fourth skill (passive)  # noqa: E501

        :param skill4level: The skill4level of this Pet.
        :type skill4level: int
        """
        if skill4level is not None and skill4level > 20:  # noqa: E501
            raise ValueError("Invalid value for `skill4level`, must be a value less than or equal to `20`")  # noqa: E501
        if skill4level is not None and skill4level < 0:  # noqa: E501
            raise ValueError("Invalid value for `skill4level`, must be a value greater than or equal to `0`")  # noqa: E501

        self._skill4level = skill4level
