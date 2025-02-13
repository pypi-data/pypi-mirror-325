# Box


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** |  | 
**y** | **float** |  | 
**w** | **float** |  | 
**h** | **float** |  | 

## Example

```python
from bzapi.models.box import Box

# TODO update the JSON string below
json = "{}"
# create an instance of Box from a JSON string
box_instance = Box.from_json(json)
# print the JSON string representation of the object
print(Box.to_json())

# convert the object into a dict
box_dict = box_instance.to_dict()
# create an instance of Box from a dict
box_from_dict = Box.from_dict(box_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


