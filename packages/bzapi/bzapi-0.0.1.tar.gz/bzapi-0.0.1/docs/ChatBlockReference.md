# ChatBlockReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**span** | [**Span**](Span.md) |  | [optional] 
**file_reference** | [**FileReference**](FileReference.md) |  | [optional] 
**web_reference** | [**WebReference**](WebReference.md) |  | [optional] 

## Example

```python
from bzapi.models.chat_block_reference import ChatBlockReference

# TODO update the JSON string below
json = "{}"
# create an instance of ChatBlockReference from a JSON string
chat_block_reference_instance = ChatBlockReference.from_json(json)
# print the JSON string representation of the object
print(ChatBlockReference.to_json())

# convert the object into a dict
chat_block_reference_dict = chat_block_reference_instance.to_dict()
# create an instance of ChatBlockReference from a dict
chat_block_reference_from_dict = ChatBlockReference.from_dict(chat_block_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


