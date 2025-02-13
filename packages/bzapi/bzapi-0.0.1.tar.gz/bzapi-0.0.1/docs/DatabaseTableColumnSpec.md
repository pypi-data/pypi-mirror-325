# DatabaseTableColumnSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_name** | **str** |  | [optional] 
**type** | **str** |  | 
**is_primary** | **bool** |  | [optional] [default to False]
**display_name** | **str** |  | 
**display_group** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**action_type** | **str** |  | [optional] [default to 'extraction']
**categories** | **List[str]** |  | [optional] 
**sub_table_db_name** | **str** |  | [optional] 
**table_columns** | [**List[DatabaseTableColumnSpec]**](DatabaseTableColumnSpec.md) |  | [optional] 

## Example

```python
from bzapi.models.database_table_column_spec import DatabaseTableColumnSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseTableColumnSpec from a JSON string
database_table_column_spec_instance = DatabaseTableColumnSpec.from_json(json)
# print the JSON string representation of the object
print(DatabaseTableColumnSpec.to_json())

# convert the object into a dict
database_table_column_spec_dict = database_table_column_spec_instance.to_dict()
# create an instance of DatabaseTableColumnSpec from a dict
database_table_column_spec_from_dict = DatabaseTableColumnSpec.from_dict(database_table_column_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


