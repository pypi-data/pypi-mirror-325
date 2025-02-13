# WebReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**url_title** | **str** |  | [optional] 
**url_description** | **str** |  | [optional] 

## Example

```python
from bzapi.models.web_reference import WebReference

# TODO update the JSON string below
json = "{}"
# create an instance of WebReference from a JSON string
web_reference_instance = WebReference.from_json(json)
# print the JSON string representation of the object
print(WebReference.to_json())

# convert the object into a dict
web_reference_dict = web_reference_instance.to_dict()
# create an instance of WebReference from a dict
web_reference_from_dict = WebReference.from_dict(web_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


