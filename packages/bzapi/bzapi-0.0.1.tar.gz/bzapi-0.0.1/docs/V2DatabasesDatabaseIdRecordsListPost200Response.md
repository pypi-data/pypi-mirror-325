# V2DatabasesDatabaseIdRecordsListPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_more** | **bool** |  | 
**offset** | **str** |  | 
**offset_id** | **int** |  | 
**count** | **int** |  | 
**items** | [**List[DatabaseRecord]**](DatabaseRecord.md) |  | 

## Example

```python
from bzapi.models.v2_databases_database_id_records_list_post200_response import V2DatabasesDatabaseIdRecordsListPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of V2DatabasesDatabaseIdRecordsListPost200Response from a JSON string
v2_databases_database_id_records_list_post200_response_instance = V2DatabasesDatabaseIdRecordsListPost200Response.from_json(json)
# print the JSON string representation of the object
print(V2DatabasesDatabaseIdRecordsListPost200Response.to_json())

# convert the object into a dict
v2_databases_database_id_records_list_post200_response_dict = v2_databases_database_id_records_list_post200_response_instance.to_dict()
# create an instance of V2DatabasesDatabaseIdRecordsListPost200Response from a dict
v2_databases_database_id_records_list_post200_response_from_dict = V2DatabasesDatabaseIdRecordsListPost200Response.from_dict(v2_databases_database_id_records_list_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


