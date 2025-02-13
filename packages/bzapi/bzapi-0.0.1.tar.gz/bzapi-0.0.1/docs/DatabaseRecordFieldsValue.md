# DatabaseRecordFieldsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** |  | 
**reference** | **object** |  | 
**raw_value** | **str** |  | [optional] 

## Example

```python
from bzapi.models.database_record_fields_value import DatabaseRecordFieldsValue

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseRecordFieldsValue from a JSON string
database_record_fields_value_instance = DatabaseRecordFieldsValue.from_json(json)
# print the JSON string representation of the object
print(DatabaseRecordFieldsValue.to_json())

# convert the object into a dict
database_record_fields_value_dict = database_record_fields_value_instance.to_dict()
# create an instance of DatabaseRecordFieldsValue from a dict
database_record_fields_value_from_dict = DatabaseRecordFieldsValue.from_dict(database_record_fields_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


