# DataExtraction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**progress** | **int** |  | 
**status** | **str** |  | 
**sources** | [**List[Source]**](Source.md) |  | 
**command** | **str** |  | [optional] 
**answer** | **str** |  | 
**references** | [**List[ChatBlockReference]**](ChatBlockReference.md) |  | 

## Example

```python
from bzapi.models.data_extraction import DataExtraction

# TODO update the JSON string below
json = "{}"
# create an instance of DataExtraction from a JSON string
data_extraction_instance = DataExtraction.from_json(json)
# print the JSON string representation of the object
print(DataExtraction.to_json())

# convert the object into a dict
data_extraction_dict = data_extraction_instance.to_dict()
# create an instance of DataExtraction from a dict
data_extraction_from_dict = DataExtraction.from_dict(data_extraction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


