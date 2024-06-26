# IngredientDifference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipe_field** | **str** |  | 
**recipe_id** | **float** |  | 
**make_id** | **float** |  | 
**difference** | [**Difference**](Difference.md) |  | 
**ingredient_id** | **float** |  | 
**ingredient_field** | **str** |  | 

## Example

```python
from openapi_client.models.ingredient_difference import IngredientDifference

# TODO update the JSON string below
json = "{}"
# create an instance of IngredientDifference from a JSON string
ingredient_difference_instance = IngredientDifference.from_json(json)
# print the JSON string representation of the object
print(IngredientDifference.to_json())

# convert the object into a dict
ingredient_difference_dict = ingredient_difference_instance.to_dict()
# create an instance of IngredientDifference from a dict
ingredient_difference_from_dict = IngredientDifference.from_dict(ingredient_difference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


