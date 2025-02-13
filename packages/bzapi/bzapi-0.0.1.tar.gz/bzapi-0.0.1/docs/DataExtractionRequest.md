# DataExtractionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sources** | [**List[Source]**](Source.md) |  | 
**command** | **str** |  | [optional] 

## Example

```python
from bzapi.models.data_extraction_request import DataExtractionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DataExtractionRequest from a JSON string
data_extraction_request_instance = DataExtractionRequest.from_json(json)
# print the JSON string representation of the object
print(DataExtractionRequest.to_json())

# convert the object into a dict
data_extraction_request_dict = data_extraction_request_instance.to_dict()
# create an instance of DataExtractionRequest from a dict
data_extraction_request_from_dict = DataExtractionRequest.from_dict(data_extraction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


