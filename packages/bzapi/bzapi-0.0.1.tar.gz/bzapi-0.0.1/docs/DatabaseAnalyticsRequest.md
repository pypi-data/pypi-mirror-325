# DatabaseAnalyticsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** |  | [optional] 
**sql_query** | **str** | an explicit sql query to execute directly instead | [optional] 

## Example

```python
from bzapi.models.database_analytics_request import DatabaseAnalyticsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseAnalyticsRequest from a JSON string
database_analytics_request_instance = DatabaseAnalyticsRequest.from_json(json)
# print the JSON string representation of the object
print(DatabaseAnalyticsRequest.to_json())

# convert the object into a dict
database_analytics_request_dict = database_analytics_request_instance.to_dict()
# create an instance of DatabaseAnalyticsRequest from a dict
database_analytics_request_from_dict = DatabaseAnalyticsRequest.from_dict(database_analytics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


