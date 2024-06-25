# DifferenceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipe_field** | **str** |  | 
**recipe_id** | **float** |  | 
**make_id** | **float** |  | 
**difference** | [**Difference**](Difference.md) |  | 

## Example

```python
from openapi_client.models.difference_object import DifferenceObject

# TODO update the JSON string below
json = "{}"
# create an instance of DifferenceObject from a JSON string
difference_object_instance = DifferenceObject.from_json(json)
# print the JSON string representation of the object
print(DifferenceObject.to_json())

# convert the object into a dict
difference_object_dict = difference_object_instance.to_dict()
# create an instance of DifferenceObject from a dict
difference_object_from_dict = DifferenceObject.from_dict(difference_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


