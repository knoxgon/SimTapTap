# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.hero_turn import HeroTurn  # noqa: F401,E501
from swagger_server.models.pet_turn import PetTurn  # noqa: F401,E501
from swagger_server import util


class Round(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, hero_turns: List[HeroTurn]=None, pet_turns: List[PetTurn]=None):  # noqa: E501
        """Round - a model defined in Swagger

        :param hero_turns: The hero_turns of this Round.  # noqa: E501
        :type hero_turns: List[HeroTurn]
        :param pet_turns: The pet_turns of this Round.  # noqa: E501
        :type pet_turns: List[PetTurn]
        """
        self.swagger_types = {
            'hero_turns': List[HeroTurn],
            'pet_turns': List[PetTurn]
        }

        self.attribute_map = {
            'hero_turns': 'heroTurns',
            'pet_turns': 'petTurns'
        }

        self._hero_turns = hero_turns
        self._pet_turns = pet_turns

    @classmethod
    def from_dict(cls, dikt) -> 'Round':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Round of this Round.  # noqa: E501
        :rtype: Round
        """
        return util.deserialize_model(dikt, cls)

    @property
    def hero_turns(self) -> List[HeroTurn]:
        """Gets the hero_turns of this Round.


        :return: The hero_turns of this Round.
        :rtype: List[HeroTurn]
        """
        return self._hero_turns

    @hero_turns.setter
    def hero_turns(self, hero_turns: List[HeroTurn]):
        """Sets the hero_turns of this Round.


        :param hero_turns: The hero_turns of this Round.
        :type hero_turns: List[HeroTurn]
        """

        self._hero_turns = hero_turns

    @property
    def pet_turns(self) -> List[PetTurn]:
        """Gets the pet_turns of this Round.


        :return: The pet_turns of this Round.
        :rtype: List[PetTurn]
        """
        return self._pet_turns

    @pet_turns.setter
    def pet_turns(self, pet_turns: List[PetTurn]):
        """Sets the pet_turns of this Round.


        :param pet_turns: The pet_turns of this Round.
        :type pet_turns: List[PetTurn]
        """

        self._pet_turns = pet_turns
