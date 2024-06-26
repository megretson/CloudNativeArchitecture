# coding: utf-8

"""
    Recipe Comparison

    This is a recipe comparer tool       

    The version of the OpenAPI document: 1.0.0
    Contact: megretson@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.recipe import Recipe

class TestRecipe(unittest.TestCase):
    """Recipe unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Recipe:
        """Test Recipe
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Recipe`
        """
        model = Recipe()
        if include_optional:
            return Recipe(
                recipe_name = '',
                recipe_id = 1.337,
                rating = 1.337,
                ingredients = [
                    openapi_client.models.ingredient.ingredient(
                        ingredient_id = 1.337, 
                        quantity = 1.337, 
                        measurement = '', 
                        ingredient_name = '', )
                    ],
                steps = [
                    openapi_client.models.step.step(
                        step_id = 1.337, 
                        step_text = '', )
                    ]
            )
        else:
            return Recipe(
        )
        """

    def testRecipe(self):
        """Test Recipe"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
