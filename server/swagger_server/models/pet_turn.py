# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.battle_effect import BattleEffect  # noqa: F401,E501
from swagger_server.models.battle_pet_ref import BattlePetRef  # noqa: F401,E501
from swagger_server import util


class PetTurn(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, pet: BattlePetRef=None, effects: BattleEffect=None):  # noqa: E501
        """PetTurn - a model defined in Swagger

        :param pet: The pet of this PetTurn.  # noqa: E501
        :type pet: BattlePetRef
        :param effects: The effects of this PetTurn.  # noqa: E501
        :type effects: BattleEffect
        """
        self.swagger_types = {
            'pet': BattlePetRef,
            'effects': BattleEffect
        }

        self.attribute_map = {
            'pet': 'pet',
            'effects': 'effects'
        }

        self._pet = pet
        self._effects = effects

    @classmethod
    def from_dict(cls, dikt) -> 'PetTurn':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PetTurn of this PetTurn.  # noqa: E501
        :rtype: PetTurn
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pet(self) -> BattlePetRef:
        """Gets the pet of this PetTurn.


        :return: The pet of this PetTurn.
        :rtype: BattlePetRef
        """
        return self._pet

    @pet.setter
    def pet(self, pet: BattlePetRef):
        """Sets the pet of this PetTurn.


        :param pet: The pet of this PetTurn.
        :type pet: BattlePetRef
        """

        self._pet = pet

    @property
    def effects(self) -> BattleEffect:
        """Gets the effects of this PetTurn.


        :return: The effects of this PetTurn.
        :rtype: BattleEffect
        """
        return self._effects

    @effects.setter
    def effects(self, effects: BattleEffect):
        """Sets the effects of this PetTurn.


        :param effects: The effects of this PetTurn.
        :type effects: BattleEffect
        """

        self._effects = effects
