from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.difference import Difference
from openapi_server import util

from openapi_server.models.difference import Difference  # noqa: E501

class IngredientDifference(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, recipe_field=None, recipe_id=None, make_id=None, difference=None, ingredient_id=None, ingredient_field=None):  # noqa: E501
        """IngredientDifference - a model defined in OpenAPI

        :param recipe_field: The recipe_field of this IngredientDifference.  # noqa: E501
        :type recipe_field: str
        :param recipe_id: The recipe_id of this IngredientDifference.  # noqa: E501
        :type recipe_id: float
        :param make_id: The make_id of this IngredientDifference.  # noqa: E501
        :type make_id: float
        :param difference: The difference of this IngredientDifference.  # noqa: E501
        :type difference: Difference
        :param ingredient_id: The ingredient_id of this IngredientDifference.  # noqa: E501
        :type ingredient_id: float
        :param ingredient_field: The ingredient_field of this IngredientDifference.  # noqa: E501
        :type ingredient_field: str
        """
        self.openapi_types = {
            'recipe_field': str,
            'recipe_id': float,
            'make_id': float,
            'difference': Difference,
            'ingredient_id': float,
            'ingredient_field': str
        }

        self.attribute_map = {
            'recipe_field': 'recipeField',
            'recipe_id': 'recipeId',
            'make_id': 'makeId',
            'difference': 'difference',
            'ingredient_id': 'ingredientId',
            'ingredient_field': 'ingredientField'
        }

        self._recipe_field = recipe_field
        self._recipe_id = recipe_id
        self._make_id = make_id
        self._difference = difference
        self._ingredient_id = ingredient_id
        self._ingredient_field = ingredient_field

    @classmethod
    def from_dict(cls, dikt) -> 'IngredientDifference':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ingredientDifference of this IngredientDifference.  # noqa: E501
        :rtype: IngredientDifference
        """
        return util.deserialize_model(dikt, cls)

    @property
    def recipe_field(self) -> str:
        """Gets the recipe_field of this IngredientDifference.


        :return: The recipe_field of this IngredientDifference.
        :rtype: str
        """
        return self._recipe_field

    @recipe_field.setter
    def recipe_field(self, recipe_field: str):
        """Sets the recipe_field of this IngredientDifference.


        :param recipe_field: The recipe_field of this IngredientDifference.
        :type recipe_field: str
        """
        allowed_values = ["rating", "ingredient", "instruction"]  # noqa: E501
        if recipe_field not in allowed_values:
            raise ValueError(
                "Invalid value for `recipe_field` ({0}), must be one of {1}"
                .format(recipe_field, allowed_values)
            )

        self._recipe_field = recipe_field

    @property
    def recipe_id(self) -> float:
        """Gets the recipe_id of this IngredientDifference.


        :return: The recipe_id of this IngredientDifference.
        :rtype: float
        """
        return self._recipe_id

    @recipe_id.setter
    def recipe_id(self, recipe_id: float):
        """Sets the recipe_id of this IngredientDifference.


        :param recipe_id: The recipe_id of this IngredientDifference.
        :type recipe_id: float
        """
        if recipe_id is None:
            raise ValueError("Invalid value for `recipe_id`, must not be `None`")  # noqa: E501

        self._recipe_id = recipe_id

    @property
    def make_id(self) -> float:
        """Gets the make_id of this IngredientDifference.


        :return: The make_id of this IngredientDifference.
        :rtype: float
        """
        return self._make_id

    @make_id.setter
    def make_id(self, make_id: float):
        """Sets the make_id of this IngredientDifference.


        :param make_id: The make_id of this IngredientDifference.
        :type make_id: float
        """
        if make_id is None:
            raise ValueError("Invalid value for `make_id`, must not be `None`")  # noqa: E501

        self._make_id = make_id

    @property
    def difference(self) -> Difference:
        """Gets the difference of this IngredientDifference.


        :return: The difference of this IngredientDifference.
        :rtype: Difference
        """
        return self._difference

    @difference.setter
    def difference(self, difference: Difference):
        """Sets the difference of this IngredientDifference.


        :param difference: The difference of this IngredientDifference.
        :type difference: Difference
        """
        if difference is None:
            raise ValueError("Invalid value for `difference`, must not be `None`")  # noqa: E501

        self._difference = difference

    @property
    def ingredient_id(self) -> float:
        """Gets the ingredient_id of this IngredientDifference.


        :return: The ingredient_id of this IngredientDifference.
        :rtype: float
        """
        return self._ingredient_id

    @ingredient_id.setter
    def ingredient_id(self, ingredient_id: float):
        """Sets the ingredient_id of this IngredientDifference.


        :param ingredient_id: The ingredient_id of this IngredientDifference.
        :type ingredient_id: float
        """
        if ingredient_id is None:
            raise ValueError("Invalid value for `ingredient_id`, must not be `None`")  # noqa: E501

        self._ingredient_id = ingredient_id

    @property
    def ingredient_field(self) -> str:
        """Gets the ingredient_field of this IngredientDifference.


        :return: The ingredient_field of this IngredientDifference.
        :rtype: str
        """
        return self._ingredient_field

    @ingredient_field.setter
    def ingredient_field(self, ingredient_field: str):
        """Sets the ingredient_field of this IngredientDifference.


        :param ingredient_field: The ingredient_field of this IngredientDifference.
        :type ingredient_field: str
        """
        allowed_values = ["quantity", "measurement", "ingredientName"]  # noqa: E501
        if ingredient_field not in allowed_values:
            raise ValueError(
                "Invalid value for `ingredient_field` ({0}), must be one of {1}"
                .format(ingredient_field, allowed_values)
            )

        self._ingredient_field = ingredient_field
