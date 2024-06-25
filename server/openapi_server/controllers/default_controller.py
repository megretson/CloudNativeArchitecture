import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.difference_object import DifferenceObject  # noqa: E501
from openapi_server.models.recipe import Recipe  # noqa: E501
from openapi_server import util
from openapi_server.helpers.database_helper import DatabaseHelper

db_helper = DatabaseHelper()

def add_recipe(recipe=None):  # noqa: E501
    """add a new recipe

     # noqa: E501

    :param recipe: 
    :type recipe: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        recipe = Recipe.from_dict(connexion.request.get_json())  # noqa: E501
    return db_helper.create_recipe(recipe)


def add_recipe_make(recipe_id, recipe=None):  # noqa: E501
    """say that you made a recipe

     # noqa: E501

    :param recipe_id: ID of recipe to return
    :type recipe_id: int
    :param recipe: 
    :type recipe: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        recipe = Recipe.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_recipe(recipe_id):  # noqa: E501
    """Recieve information on a recipe

     # noqa: E501

    :param recipe_id: ID of recipe to return
    :type recipe_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return db_helper.read_recipe(recipe_id)


def get_recipe_make(recipe_id, make_id):  # noqa: E501
    """Recieve information on a given make of a recipe

     # noqa: E501

    :param recipe_id: ID of recipe to return
    :type recipe_id: int
    :param make_id: ID of make to return
    :type make_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_recipe_make_differences(recipe_id, make_id):  # noqa: E501
    """Recieve information on a given make of a recipe, including any variations between the make and the actual recipe

     # noqa: E501

    :param recipe_id: ID of recipe to return
    :type recipe_id: int
    :param make_id: ID of make to return
    :type make_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def update_recipe(recipe=None):  # noqa: E501
    """update a recipe

     # noqa: E501

    :param recipe: 
    :type recipe: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        recipe = Recipe.from_dict(connexion.request.get_json())  # noqa: E501
    return db_helper.update_recipe(recipe)
