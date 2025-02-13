# SigmaFilterParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_name** | **str** |  | 
**like_values** | **List[object]** |  | 
**equal_to_values** | **List[object]** |  | 
**greater_than_value** | **object** |  | 
**less_than_value** | **object** |  | 

## Example

```python
from bzapi.models.sigma_filter_parameters import SigmaFilterParameters

# TODO update the JSON string below
json = "{}"
# create an instance of SigmaFilterParameters from a JSON string
sigma_filter_parameters_instance = SigmaFilterParameters.from_json(json)
# print the JSON string representation of the object
print(SigmaFilterParameters.to_json())

# convert the object into a dict
sigma_filter_parameters_dict = sigma_filter_parameters_instance.to_dict()
# create an instance of SigmaFilterParameters from a dict
sigma_filter_parameters_from_dict = SigmaFilterParameters.from_dict(sigma_filter_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


