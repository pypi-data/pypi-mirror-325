# ListDatabaseRecordsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_name** | **str** |  | [optional] 
**sort** | [**SigmaSortParameters**](SigmaSortParameters.md) |  | [optional] 
**filters** | [**List[SigmaFilterParameters]**](SigmaFilterParameters.md) |  | [optional] 

## Example

```python
from bzapi.models.list_database_records_request import ListDatabaseRecordsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListDatabaseRecordsRequest from a JSON string
list_database_records_request_instance = ListDatabaseRecordsRequest.from_json(json)
# print the JSON string representation of the object
print(ListDatabaseRecordsRequest.to_json())

# convert the object into a dict
list_database_records_request_dict = list_database_records_request_instance.to_dict()
# create an instance of ListDatabaseRecordsRequest from a dict
list_database_records_request_from_dict = ListDatabaseRecordsRequest.from_dict(list_database_records_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


