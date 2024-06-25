import unittest

from flask import json

from openapi_server.models.recipe import Recipe  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_add_recipe(self):
        """Test case for add_recipe

        add a new recipe
        """
        recipe = openapi_server.Recipe()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/MargaretAnderson/RecipeComparer/1.0.0/recipes',
            method='POST',
            headers=headers,
            data=json.dumps(recipe),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_recipe_make(self):
        """Test case for add_recipe_make

        say that you made a recipe
        """
        recipe = openapi_server.Recipe()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/MargaretAnderson/RecipeComparer/1.0.0/recipes/{recipe_id}/makes'.format(recipe_id=56),
            method='POST',
            headers=headers,
            data=json.dumps(recipe),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_recipe(self):
        """Test case for get_recipe

        Recieve information on a recipe
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/MargaretAnderson/RecipeComparer/1.0.0/recipes/{recipe_id}'.format(recipe_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_recipe_make(self):
        """Test case for get_recipe_make

        Recieve information on a given make of a recipe
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/MargaretAnderson/RecipeComparer/1.0.0/recipes/{recipe_id}/makes/{make_id}'.format(recipe_id=56, make_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_recipe_make_differences(self):
        """Test case for get_recipe_make_differences

        Recieve information on a given make of a recipe, including any variations between the make and the actual recipe
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/MargaretAnderson/RecipeComparer/1.0.0/recipes/{recipe_id}/makes/{make_id}/differences'.format(recipe_id=56, make_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_recipe(self):
        """Test case for update_recipe

        update a recipe
        """
        recipe = openapi_server.Recipe()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/MargaretAnderson/RecipeComparer/1.0.0/recipes',
            method='PUT',
            headers=headers,
            data=json.dumps(recipe),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
