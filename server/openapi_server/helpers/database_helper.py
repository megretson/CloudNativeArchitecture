from openapi_server.models.recipe import Recipe
import boto3
from openapi_server.models.recipe import Recipe  # noqa: E501
from openapi_server.models.recipe import Ingredient  # noqa: E501
from openapi_server.models.recipe import Step  # noqa: E501

class DatabaseHelper:

    def __init__(self) -> None:
        self.client = boto3.client('dynamodb', region_name='us-east-2')
        self.recipeTable = 'Recipes'
        self.differenceTable = 'MakeDifferences'

    def create_recipe(self, recipe):
        resp = self.client.put_item(
            TableName = self.recipeTable,
            Item = DatabaseHelper.recipe_to_item(recipe)
        )
        return recipe

    def read_recipe(self, recipe_id):
        resp = self.client.get_item(
            TableName = self.recipeTable,
            Key={
                'recipeId': { 'S': str(recipe_id) }
            }
        )
        item = resp.get('Item')
        if not item:
            return None
        return DatabaseHelper.recipe_from_item(item)

    def update_recipe(self, recipe):
        self.create_recipe(recipe)

    def create_recipe_difference(recipe):
        pass

    def ingredient_to_item(ingredient):
        item_dict = {
            'ingredientId': {'N': str(ingredient.ingredient_id)},
            'ingredientName': {'S': ingredient.ingredient_name},
            'measurement' : {'S' : ingredient.measurement},
            'quantity': {'N': str(ingredient.quantity)}
        }
        return item_dict

    def ingredient_from_item(item):
        ingredient = Ingredient()
        ingredient.ingredient_id = item["ingredientId"]["N"]
        ingredient.ingredient_name = item["ingredientName"]["S"]
        ingredient.measurement = item["measurement"]['S']
        ingredient.quantity = item["quantity"]["N"]
        return ingredient

    def recipe_from_item(item):
        ingredients = [DatabaseHelper.ingredient_from_item(
            i.get('M')) for i in item.get('ingredients').get('L')]
        steps = [DatabaseHelper.step_from_item(i.get('M'))
                 for i in item.get('steps').get('L')]
        recipe_id = item.get('recipeId').get('S')
        rating = item.get('rating').get('N')
        name = item.get('recipeName').get('S')
        return Recipe(recipe_name=name, recipe_id=recipe_id, rating=rating, ingredients=ingredients, steps=steps)

    def recipe_to_item(recipe):
        ingredients = [{'M': DatabaseHelper.ingredient_to_item(i)} for i in recipe.ingredients]
        steps = [{'M': DatabaseHelper.step_to_item(s)} for s in recipe.steps]
        item_dict = {
            'recipeId': {'S': str(int(recipe.recipe_id))},
            'rating': {'N': str(recipe.rating)},
            'ingredients': {'L': ingredients},
            'steps': {'L': steps},
            "recipeName": {'S': str(recipe.recipe_name)}
        }
        return item_dict

    def step_to_item(step):
        step_dict = {
            'stepId': {'N': str(step.step_id)},
            'stepText': {'S': step.step_text}
        }
        return step_dict

    def step_from_item(item):
        step = Step()
        step.step_id = item["stepId"]["N"]
        step.step_text = item["stepText"]["S"]
        return step