# Recipe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipe_name** | **str** |  | [optional] 
**recipe_id** | **float** |  | [optional] 
**rating** | **float** |  | [optional] 
**ingredients** | [**List[Ingredient]**](Ingredient.md) |  | [optional] 
**steps** | [**List[Step]**](Step.md) |  | [optional] 

## Example

```python
from openapi_client.models.recipe import Recipe

# TODO update the JSON string below
json = "{}"
# create an instance of Recipe from a JSON string
recipe_instance = Recipe.from_json(json)
# print the JSON string representation of the object
print(Recipe.to_json())

# convert the object into a dict
recipe_dict = recipe_instance.to_dict()
# create an instance of Recipe from a dict
recipe_from_dict = Recipe.from_dict(recipe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


