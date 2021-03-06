# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.artifact import Artifact  # noqa: F401,E501
from swagger_server.models.equipment_level import EquipmentLevel  # noqa: F401,E501
from swagger_server.models.rune import Rune  # noqa: F401,E501
from swagger_server import util


class HeroEquipment(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, helmet: EquipmentLevel=None, chest: EquipmentLevel=None, weapon: EquipmentLevel=None, pendant: EquipmentLevel=None, rune: Rune=None, artifact: Artifact=None):  # noqa: E501
        """HeroEquipment - a model defined in Swagger

        :param helmet: The helmet of this HeroEquipment.  # noqa: E501
        :type helmet: EquipmentLevel
        :param chest: The chest of this HeroEquipment.  # noqa: E501
        :type chest: EquipmentLevel
        :param weapon: The weapon of this HeroEquipment.  # noqa: E501
        :type weapon: EquipmentLevel
        :param pendant: The pendant of this HeroEquipment.  # noqa: E501
        :type pendant: EquipmentLevel
        :param rune: The rune of this HeroEquipment.  # noqa: E501
        :type rune: Rune
        :param artifact: The artifact of this HeroEquipment.  # noqa: E501
        :type artifact: Artifact
        """
        self.swagger_types = {
            'helmet': EquipmentLevel,
            'chest': EquipmentLevel,
            'weapon': EquipmentLevel,
            'pendant': EquipmentLevel,
            'rune': Rune,
            'artifact': Artifact
        }

        self.attribute_map = {
            'helmet': 'helmet',
            'chest': 'chest',
            'weapon': 'weapon',
            'pendant': 'pendant',
            'rune': 'rune',
            'artifact': 'artifact'
        }

        self._helmet = helmet
        self._chest = chest
        self._weapon = weapon
        self._pendant = pendant
        self._rune = rune
        self._artifact = artifact

    @classmethod
    def from_dict(cls, dikt) -> 'HeroEquipment':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Hero_equipment of this HeroEquipment.  # noqa: E501
        :rtype: HeroEquipment
        """
        return util.deserialize_model(dikt, cls)

    @property
    def helmet(self) -> EquipmentLevel:
        """Gets the helmet of this HeroEquipment.


        :return: The helmet of this HeroEquipment.
        :rtype: EquipmentLevel
        """
        return self._helmet

    @helmet.setter
    def helmet(self, helmet: EquipmentLevel):
        """Sets the helmet of this HeroEquipment.


        :param helmet: The helmet of this HeroEquipment.
        :type helmet: EquipmentLevel
        """

        self._helmet = helmet

    @property
    def chest(self) -> EquipmentLevel:
        """Gets the chest of this HeroEquipment.


        :return: The chest of this HeroEquipment.
        :rtype: EquipmentLevel
        """
        return self._chest

    @chest.setter
    def chest(self, chest: EquipmentLevel):
        """Sets the chest of this HeroEquipment.


        :param chest: The chest of this HeroEquipment.
        :type chest: EquipmentLevel
        """

        self._chest = chest

    @property
    def weapon(self) -> EquipmentLevel:
        """Gets the weapon of this HeroEquipment.


        :return: The weapon of this HeroEquipment.
        :rtype: EquipmentLevel
        """
        return self._weapon

    @weapon.setter
    def weapon(self, weapon: EquipmentLevel):
        """Sets the weapon of this HeroEquipment.


        :param weapon: The weapon of this HeroEquipment.
        :type weapon: EquipmentLevel
        """

        self._weapon = weapon

    @property
    def pendant(self) -> EquipmentLevel:
        """Gets the pendant of this HeroEquipment.


        :return: The pendant of this HeroEquipment.
        :rtype: EquipmentLevel
        """
        return self._pendant

    @pendant.setter
    def pendant(self, pendant: EquipmentLevel):
        """Sets the pendant of this HeroEquipment.


        :param pendant: The pendant of this HeroEquipment.
        :type pendant: EquipmentLevel
        """

        self._pendant = pendant

    @property
    def rune(self) -> Rune:
        """Gets the rune of this HeroEquipment.


        :return: The rune of this HeroEquipment.
        :rtype: Rune
        """
        return self._rune

    @rune.setter
    def rune(self, rune: Rune):
        """Sets the rune of this HeroEquipment.


        :param rune: The rune of this HeroEquipment.
        :type rune: Rune
        """
        if rune is None:
            raise ValueError("Invalid value for `rune`, must not be `None`")  # noqa: E501

        self._rune = rune

    @property
    def artifact(self) -> Artifact:
        """Gets the artifact of this HeroEquipment.


        :return: The artifact of this HeroEquipment.
        :rtype: Artifact
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact: Artifact):
        """Sets the artifact of this HeroEquipment.


        :param artifact: The artifact of this HeroEquipment.
        :type artifact: Artifact
        """
        if artifact is None:
            raise ValueError("Invalid value for `artifact`, must not be `None`")  # noqa: E501

        self._artifact = artifact
