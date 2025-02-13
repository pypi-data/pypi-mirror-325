# DatabaseAnalyticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sql** | **str** | the executed sql | [optional] 
**records** | [**List[DatabaseRecord]**](DatabaseRecord.md) |  | [optional] 
**column_types** | **Dict[str, str]** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from bzapi.models.database_analytics_response import DatabaseAnalyticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseAnalyticsResponse from a JSON string
database_analytics_response_instance = DatabaseAnalyticsResponse.from_json(json)
# print the JSON string representation of the object
print(DatabaseAnalyticsResponse.to_json())

# convert the object into a dict
database_analytics_response_dict = database_analytics_response_instance.to_dict()
# create an instance of DatabaseAnalyticsResponse from a dict
database_analytics_response_from_dict = DatabaseAnalyticsResponse.from_dict(database_analytics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


