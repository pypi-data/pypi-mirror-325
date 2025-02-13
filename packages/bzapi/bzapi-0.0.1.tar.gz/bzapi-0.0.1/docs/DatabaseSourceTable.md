# DatabaseSourceTable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_archived** | **bool** |  | [optional] [default to False]
**db_table_name** | **str** |  | [optional] 
**display_name** | **str** |  | 
**columns** | [**List[DatabaseTableColumnSpec]**](DatabaseTableColumnSpec.md) |  | 

## Example

```python
from bzapi.models.database_source_table import DatabaseSourceTable

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseSourceTable from a JSON string
database_source_table_instance = DatabaseSourceTable.from_json(json)
# print the JSON string representation of the object
print(DatabaseSourceTable.to_json())

# convert the object into a dict
database_source_table_dict = database_source_table_instance.to_dict()
# create an instance of DatabaseSourceTable from a dict
database_source_table_from_dict = DatabaseSourceTable.from_dict(database_source_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


