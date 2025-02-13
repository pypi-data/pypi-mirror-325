# ChatConversationBlock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 
**text** | **str** |  | 
**references** | [**List[ChatBlockReference]**](ChatBlockReference.md) |  | [optional] 

## Example

```python
from bzapi.models.chat_conversation_block import ChatConversationBlock

# TODO update the JSON string below
json = "{}"
# create an instance of ChatConversationBlock from a JSON string
chat_conversation_block_instance = ChatConversationBlock.from_json(json)
# print the JSON string representation of the object
print(ChatConversationBlock.to_json())

# convert the object into a dict
chat_conversation_block_dict = chat_conversation_block_instance.to_dict()
# create an instance of ChatConversationBlock from a dict
chat_conversation_block_from_dict = ChatConversationBlock.from_dict(chat_conversation_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


