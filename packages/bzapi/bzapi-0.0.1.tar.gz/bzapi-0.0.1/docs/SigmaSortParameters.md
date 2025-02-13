# SigmaSortParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**direction** | **str** |  | [optional] 
**sort_column** | **str** |  | [optional] 
**offset_id** | **int** |  | [optional] 
**offset** | **str** |  | [optional] 

## Example

```python
from bzapi.models.sigma_sort_parameters import SigmaSortParameters

# TODO update the JSON string below
json = "{}"
# create an instance of SigmaSortParameters from a JSON string
sigma_sort_parameters_instance = SigmaSortParameters.from_json(json)
# print the JSON string representation of the object
print(SigmaSortParameters.to_json())

# convert the object into a dict
sigma_sort_parameters_dict = sigma_sort_parameters_instance.to_dict()
# create an instance of SigmaSortParameters from a dict
sigma_sort_parameters_from_dict = SigmaSortParameters.from_dict(sigma_sort_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


