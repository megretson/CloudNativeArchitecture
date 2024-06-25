# StepDifference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipe_field** | **str** |  | 
**recipe_id** | **float** |  | 
**make_id** | **float** |  | 
**difference** | [**StepDifferenceAllOfDifference**](StepDifferenceAllOfDifference.md) |  | 

## Example

```python
from openapi_client.models.step_difference import StepDifference

# TODO update the JSON string below
json = "{}"
# create an instance of StepDifference from a JSON string
step_difference_instance = StepDifference.from_json(json)
# print the JSON string representation of the object
print(StepDifference.to_json())

# convert the object into a dict
step_difference_dict = step_difference_instance.to_dict()
# create an instance of StepDifference from a dict
step_difference_from_dict = StepDifference.from_dict(step_difference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


