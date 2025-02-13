# DatabaseRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**database_id** | **str** |  | [optional] 
**db_table_name** | **str** |  | 
**created_at** | **datetime** |  | 
**created_by** | **str** |  | 
**updated_at** | **datetime** |  | 
**extraction_job_id** | **str** |  | [optional] 
**fields** | [**Dict[str, DatabaseRecordFieldsValue]**](DatabaseRecordFieldsValue.md) |  | 

## Example

```python
from bzapi.models.database_record import DatabaseRecord

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseRecord from a JSON string
database_record_instance = DatabaseRecord.from_json(json)
# print the JSON string representation of the object
print(DatabaseRecord.to_json())

# convert the object into a dict
database_record_dict = database_record_instance.to_dict()
# create an instance of DatabaseRecord from a dict
database_record_from_dict = DatabaseRecord.from_dict(database_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


