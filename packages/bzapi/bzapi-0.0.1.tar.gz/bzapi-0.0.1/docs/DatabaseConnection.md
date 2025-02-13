# DatabaseConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postgres_connection_url** | **str** |  | [optional] 

## Example

```python
from bzapi.models.database_connection import DatabaseConnection

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseConnection from a JSON string
database_connection_instance = DatabaseConnection.from_json(json)
# print the JSON string representation of the object
print(DatabaseConnection.to_json())

# convert the object into a dict
database_connection_dict = database_connection_instance.to_dict()
# create an instance of DatabaseConnection from a dict
database_connection_from_dict = DatabaseConnection.from_dict(database_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


