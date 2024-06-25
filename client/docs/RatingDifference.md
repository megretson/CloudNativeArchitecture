# RatingDifference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipe_field** | **str** |  | 
**recipe_id** | **float** |  | 
**make_id** | **float** |  | 
**difference** | [**Difference**](Difference.md) |  | 

## Example

```python
from openapi_client.models.rating_difference import RatingDifference

# TODO update the JSON string below
json = "{}"
# create an instance of RatingDifference from a JSON string
rating_difference_instance = RatingDifference.from_json(json)
# print the JSON string representation of the object
print(RatingDifference.to_json())

# convert the object into a dict
rating_difference_dict = rating_difference_instance.to_dict()
# create an instance of RatingDifference from a dict
rating_difference_from_dict = RatingDifference.from_dict(rating_difference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


