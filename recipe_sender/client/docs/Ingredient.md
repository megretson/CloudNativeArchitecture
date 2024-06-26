# Ingredient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingredient_id** | **float** |  | [optional] 
**quantity** | **float** |  | [optional] 
**measurement** | **str** |  | [optional] 
**ingredient_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ingredient import Ingredient

# TODO update the JSON string below
json = "{}"
# create an instance of Ingredient from a JSON string
ingredient_instance = Ingredient.from_json(json)
# print the JSON string representation of the object
print(Ingredient.to_json())

# convert the object into a dict
ingredient_dict = ingredient_instance.to_dict()
# create an instance of Ingredient from a dict
ingredient_from_dict = Ingredient.from_dict(ingredient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


