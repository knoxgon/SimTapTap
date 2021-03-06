# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Artifact(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, stars: int=None):  # noqa: E501
        """Artifact - a model defined in Swagger

        :param id: The id of this Artifact.  # noqa: E501
        :type id: str
        :param stars: The stars of this Artifact.  # noqa: E501
        :type stars: int
        """
        self.swagger_types = {
            'id': str,
            'stars': int
        }

        self.attribute_map = {
            'id': 'id',
            'stars': 'stars'
        }

        self._id = id
        self._stars = stars

    @classmethod
    def from_dict(cls, dikt) -> 'Artifact':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Artifact of this Artifact.  # noqa: E501
        :rtype: Artifact
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Artifact.

        What artifact this refers to  # noqa: E501

        :return: The id of this Artifact.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Artifact.

        What artifact this refers to  # noqa: E501

        :param id: The id of this Artifact.
        :type id: str
        """
        allowed_values = ["SATANS_POWER", "YAKSHA", "DARK_DESTROYER", "SUNS_HYMN", "BURNING_SOUL", "EYE_OF_HEAVEN", "WIND_WALKER", "SCORCHING_SUN", "DRAGONBLOOD", "SOUND_STEP", "KNIGHTS_VOW", "PRIMEVAL_SOUL", "QUEENS_CROWN", "SOUL_TORRENT", "GIFT_OF_CREATION", "ETERNAL_CURSE"]  # noqa: E501
        if id not in allowed_values:
            raise ValueError(
                "Invalid value for `id` ({0}), must be one of {1}"
                .format(id, allowed_values)
            )

        self._id = id

    @property
    def stars(self) -> int:
        """Gets the stars of this Artifact.

        Number of stars the artifact is leveled up to  # noqa: E501

        :return: The stars of this Artifact.
        :rtype: int
        """
        return self._stars

    @stars.setter
    def stars(self, stars: int):
        """Sets the stars of this Artifact.

        Number of stars the artifact is leveled up to  # noqa: E501

        :param stars: The stars of this Artifact.
        :type stars: int
        """
        if stars is not None and stars > 6:  # noqa: E501
            raise ValueError("Invalid value for `stars`, must be a value less than or equal to `6`")  # noqa: E501
        if stars is not None and stars < 1:  # noqa: E501
            raise ValueError("Invalid value for `stars`, must be a value greater than or equal to `1`")  # noqa: E501

        self._stars = stars
