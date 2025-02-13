# Chat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation** | [**List[ChatConversationBlock]**](ChatConversationBlock.md) |  | 
**model** | **str** |  | [default to 'boltzbit-llm:latest']
**sources** | [**List[Source]**](Source.md) |  | [optional] 

## Example

```python
from bzapi.models.chat import Chat

# TODO update the JSON string below
json = "{}"
# create an instance of Chat from a JSON string
chat_instance = Chat.from_json(json)
# print the JSON string representation of the object
print(Chat.to_json())

# convert the object into a dict
chat_dict = chat_instance.to_dict()
# create an instance of Chat from a dict
chat_from_dict = Chat.from_dict(chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


