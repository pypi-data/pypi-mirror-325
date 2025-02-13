# bzapi.DefaultApi

All URIs are relative to *https://flow.boltzbit.com/bz-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_chat_query_post**](DefaultApi.md#v2_chat_query_post) | **POST** /v2/chat-query | Chat query
[**v2_chat_query_streamed_post**](DefaultApi.md#v2_chat_query_streamed_post) | **POST** /v2/chat-query-streamed | Streamed chat query
[**v2_data_extraction_post**](DefaultApi.md#v2_data_extraction_post) | **POST** /v2/data-extraction | Data extraction
[**v2_databases_database_id_delete**](DefaultApi.md#v2_databases_database_id_delete) | **DELETE** /v2/databases/{databaseId} | Delete a database
[**v2_databases_database_id_get**](DefaultApi.md#v2_databases_database_id_get) | **GET** /v2/databases/{databaseId} | Get a database
[**v2_databases_database_id_put**](DefaultApi.md#v2_databases_database_id_put) | **PUT** /v2/databases/{databaseId} | Update a database
[**v2_databases_database_id_records_list_post**](DefaultApi.md#v2_databases_database_id_records_list_post) | **POST** /v2/databases/{databaseId}/records/list | List database records
[**v2_databases_database_id_records_post**](DefaultApi.md#v2_databases_database_id_records_post) | **POST** /v2/databases/{databaseId}/records | Create a database record
[**v2_databases_database_id_records_record_id_delete**](DefaultApi.md#v2_databases_database_id_records_record_id_delete) | **DELETE** /v2/databases/{databaseId}/records/{recordId} | delete the database record
[**v2_databases_database_id_records_record_id_get**](DefaultApi.md#v2_databases_database_id_records_record_id_get) | **GET** /v2/databases/{databaseId}/records/{recordId} | get the database record
[**v2_databases_database_id_records_record_id_put**](DefaultApi.md#v2_databases_database_id_records_record_id_put) | **PUT** /v2/databases/{databaseId}/records/{recordId} | Update a datatbase record
[**v2_databases_database_id_run_analytics_post**](DefaultApi.md#v2_databases_database_id_run_analytics_post) | **POST** /v2/databases/{databaseId}/run-analytics | Execute natural language command on a database
[**v2_databases_post**](DefaultApi.md#v2_databases_post) | **POST** /v2/databases | Create databases
[**v2_documents_bulk_upload_post**](DefaultApi.md#v2_documents_bulk_upload_post) | **POST** /v2/documents/bulk-upload | Bulk upload documents
[**v2_documents_document_id_delete**](DefaultApi.md#v2_documents_document_id_delete) | **DELETE** /v2/documents/{documentId} | Delete a document
[**v2_documents_document_id_get**](DefaultApi.md#v2_documents_document_id_get) | **GET** /v2/documents/{documentId} | Get a document
[**v2_documents_list_get**](DefaultApi.md#v2_documents_list_get) | **GET** /v2/documents/list | List all documents


# **v2_chat_query_post**
> ChatConversationBlock v2_chat_query_post(chat)

Chat query

Given a chat conversation, returns the LLM's response. 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import bzapi
from bzapi.models.chat import Chat
from bzapi.models.chat_conversation_block import ChatConversationBlock
from bzapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flow.boltzbit.com/bz-api
# See configuration.py for a list of all supported configuration parameters.
configuration = bzapi.Configuration(
    host = "https://flow.boltzbit.com/bz-api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = bzapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bzapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bzapi.DefaultApi(api_client)
    chat = bzapi.Chat() # Chat | 

    try:
        # Chat query
        api_response = api_instance.v2_chat_query_post(chat)
        print("The response of DefaultApi->v2_chat_query_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_chat_query_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat** | [**Chat**](Chat.md)|  | 

### Return type

[**ChatConversationBlock**](ChatConversationBlock.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_chat_query_streamed_post**
> str v2_chat_query_streamed_post(chat)

Streamed chat query

This endpoint is the same as /chay-query except the result is streamed as server sent events as it is generated. The final result is simply the content of the last server sent event received. 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import bzapi
from bzapi.models.chat import Chat
from bzapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flow.boltzbit.com/bz-api
# See configuration.py for a list of all supported configuration parameters.
configuration = bzapi.Configuration(
    host = "https://flow.boltzbit.com/bz-api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = bzapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bzapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bzapi.DefaultApi(api_client)
    chat = bzapi.Chat() # Chat | 

    try:
        # Streamed chat query
        api_response = api_instance.v2_chat_query_streamed_post(chat)
        print("The response of DefaultApi->v2_chat_query_streamed_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_chat_query_streamed_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chat** | [**Chat**](Chat.md)|  | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/event-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A stream of server-sent events with the chat query response. |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_data_extraction_post**
> DataExtraction v2_data_extraction_post(data_extraction_request)

Data extraction

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import bzapi
from bzapi.models.data_extraction import DataExtraction
from bzapi.models.data_extraction_request import DataExtractionRequest
from bzapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flow.boltzbit.com/bz-api
# See configuration.py for a list of all supported configuration parameters.
configuration = bzapi.Configuration(
    host = "https://flow.boltzbit.com/bz-api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = bzapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bzapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bzapi.DefaultApi(api_client)
    data_extraction_request = bzapi.DataExtractionRequest() # DataExtractionRequest | 

    try:
        # Data extraction
        api_response = api_instance.v2_data_extraction_post(data_extraction_request)
        print("The response of DefaultApi->v2_data_extraction_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_data_extraction_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_extraction_request** | [**DataExtractionRequest**](DataExtractionRequest.md)|  | 

### Return type

[**DataExtraction**](DataExtraction.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_databases_database_id_delete**
> Database v2_databases_database_id_delete(database_id)

Delete a database

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import bzapi
from bzapi.models.database import Database
from bzapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flow.boltzbit.com/bz-api
# See configuration.py for a list of all supported configuration parameters.
configuration = bzapi.Configuration(
    host = "https://flow.boltzbit.com/bz-api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = bzapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bzapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bzapi.DefaultApi(api_client)
    database_id = 'database_id_example' # str | The database ID

    try:
        # Delete a database
        api_response = api_instance.v2_databases_database_id_delete(database_id)
        print("The response of DefaultApi->v2_databases_database_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_databases_database_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| The database ID | 

### Return type

[**Database**](Database.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |
**404** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_databases_database_id_get**
> Database v2_databases_database_id_get(database_id)

Get a database

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import bzapi
from bzapi.models.database import Database
from bzapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flow.boltzbit.com/bz-api
# See configuration.py for a list of all supported configuration parameters.
configuration = bzapi.Configuration(
    host = "https://flow.boltzbit.com/bz-api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = bzapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bzapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bzapi.DefaultApi(api_client)
    database_id = 'database_id_example' # str | The database ID

    try:
        # Get a database
        api_response = api_instance.v2_databases_database_id_get(database_id)
        print("The response of DefaultApi->v2_databases_database_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_databases_database_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| The database ID | 

### Return type

[**Database**](Database.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |
**404** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_databases_database_id_put**
> Database v2_databases_database_id_put(database_id, database)

Update a database

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import bzapi
from bzapi.models.database import Database
from bzapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flow.boltzbit.com/bz-api
# See configuration.py for a list of all supported configuration parameters.
configuration = bzapi.Configuration(
    host = "https://flow.boltzbit.com/bz-api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = bzapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bzapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bzapi.DefaultApi(api_client)
    database_id = 'database_id_example' # str | The database ID
    database = bzapi.Database() # Database | 

    try:
        # Update a database
        api_response = api_instance.v2_databases_database_id_put(database_id, database)
        print("The response of DefaultApi->v2_databases_database_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_databases_database_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| The database ID | 
 **database** | [**Database**](Database.md)|  | 

### Return type

[**Database**](Database.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |
**404** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_databases_database_id_records_list_post**
> V2DatabasesDatabaseIdRecordsListPost200Response v2_databases_database_id_records_list_post(database_id, list_database_records_request)

List database records

List database records

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import bzapi
from bzapi.models.list_database_records_request import ListDatabaseRecordsRequest
from bzapi.models.v2_databases_database_id_records_list_post200_response import V2DatabasesDatabaseIdRecordsListPost200Response
from bzapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flow.boltzbit.com/bz-api
# See configuration.py for a list of all supported configuration parameters.
configuration = bzapi.Configuration(
    host = "https://flow.boltzbit.com/bz-api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = bzapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bzapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bzapi.DefaultApi(api_client)
    database_id = 'database_id_example' # str | The database ID
    list_database_records_request = bzapi.ListDatabaseRecordsRequest() # ListDatabaseRecordsRequest | 

    try:
        # List database records
        api_response = api_instance.v2_databases_database_id_records_list_post(database_id, list_database_records_request)
        print("The response of DefaultApi->v2_databases_database_id_records_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_databases_database_id_records_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| The database ID | 
 **list_database_records_request** | [**ListDatabaseRecordsRequest**](ListDatabaseRecordsRequest.md)|  | 

### Return type

[**V2DatabasesDatabaseIdRecordsListPost200Response**](V2DatabasesDatabaseIdRecordsListPost200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_databases_database_id_records_post**
> DatabaseRecord v2_databases_database_id_records_post(database_id, database_record)

Create a database record

Create a database record

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import bzapi
from bzapi.models.database_record import DatabaseRecord
from bzapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flow.boltzbit.com/bz-api
# See configuration.py for a list of all supported configuration parameters.
configuration = bzapi.Configuration(
    host = "https://flow.boltzbit.com/bz-api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = bzapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bzapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bzapi.DefaultApi(api_client)
    database_id = 'database_id_example' # str | 
    database_record = bzapi.DatabaseRecord() # DatabaseRecord | 

    try:
        # Create a database record
        api_response = api_instance.v2_databases_database_id_records_post(database_id, database_record)
        print("The response of DefaultApi->v2_databases_database_id_records_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_databases_database_id_records_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**|  | 
 **database_record** | [**DatabaseRecord**](DatabaseRecord.md)|  | 

### Return type

[**DatabaseRecord**](DatabaseRecord.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_databases_database_id_records_record_id_delete**
> DatabaseRecord v2_databases_database_id_records_record_id_delete(database_id, record_id, db_table_name)

delete the database record

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import bzapi
from bzapi.models.database_record import DatabaseRecord
from bzapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flow.boltzbit.com/bz-api
# See configuration.py for a list of all supported configuration parameters.
configuration = bzapi.Configuration(
    host = "https://flow.boltzbit.com/bz-api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = bzapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bzapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bzapi.DefaultApi(api_client)
    database_id = 'database_id_example' # str | The database ID
    record_id = 56 # int | The database record ID
    db_table_name = 'db_table_name_example' # str | The table name

    try:
        # delete the database record
        api_response = api_instance.v2_databases_database_id_records_record_id_delete(database_id, record_id, db_table_name)
        print("The response of DefaultApi->v2_databases_database_id_records_record_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_databases_database_id_records_record_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| The database ID | 
 **record_id** | **int**| The database record ID | 
 **db_table_name** | **str**| The table name | 

### Return type

[**DatabaseRecord**](DatabaseRecord.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful delete database record |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_databases_database_id_records_record_id_get**
> DatabaseRecord v2_databases_database_id_records_record_id_get(database_id, record_id, db_table_name)

get the database record

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import bzapi
from bzapi.models.database_record import DatabaseRecord
from bzapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flow.boltzbit.com/bz-api
# See configuration.py for a list of all supported configuration parameters.
configuration = bzapi.Configuration(
    host = "https://flow.boltzbit.com/bz-api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = bzapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bzapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bzapi.DefaultApi(api_client)
    database_id = 'database_id_example' # str | The database ID
    record_id = 56 # int | The database record ID
    db_table_name = 'db_table_name_example' # str | The table name

    try:
        # get the database record
        api_response = api_instance.v2_databases_database_id_records_record_id_get(database_id, record_id, db_table_name)
        print("The response of DefaultApi->v2_databases_database_id_records_record_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_databases_database_id_records_record_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| The database ID | 
 **record_id** | **int**| The database record ID | 
 **db_table_name** | **str**| The table name | 

### Return type

[**DatabaseRecord**](DatabaseRecord.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieve the database record |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_databases_database_id_records_record_id_put**
> DatabaseRecord v2_databases_database_id_records_record_id_put(database_id, record_id, db_table_name, database_record)

Update a datatbase record

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import bzapi
from bzapi.models.database_record import DatabaseRecord
from bzapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flow.boltzbit.com/bz-api
# See configuration.py for a list of all supported configuration parameters.
configuration = bzapi.Configuration(
    host = "https://flow.boltzbit.com/bz-api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = bzapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bzapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bzapi.DefaultApi(api_client)
    database_id = 'database_id_example' # str | The database ID
    record_id = 56 # int | The database record ID
    db_table_name = 'db_table_name_example' # str | The table name
    database_record = bzapi.DatabaseRecord() # DatabaseRecord | 

    try:
        # Update a datatbase record
        api_response = api_instance.v2_databases_database_id_records_record_id_put(database_id, record_id, db_table_name, database_record)
        print("The response of DefaultApi->v2_databases_database_id_records_record_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_databases_database_id_records_record_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| The database ID | 
 **record_id** | **int**| The database record ID | 
 **db_table_name** | **str**| The table name | 
 **database_record** | [**DatabaseRecord**](DatabaseRecord.md)|  | 

### Return type

[**DatabaseRecord**](DatabaseRecord.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_databases_database_id_run_analytics_post**
> DatabaseAnalyticsResponse v2_databases_database_id_run_analytics_post(database_id, database_analytics_request)

Execute natural language command on a database

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import bzapi
from bzapi.models.database_analytics_request import DatabaseAnalyticsRequest
from bzapi.models.database_analytics_response import DatabaseAnalyticsResponse
from bzapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flow.boltzbit.com/bz-api
# See configuration.py for a list of all supported configuration parameters.
configuration = bzapi.Configuration(
    host = "https://flow.boltzbit.com/bz-api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = bzapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bzapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bzapi.DefaultApi(api_client)
    database_id = 'database_id_example' # str | The database ID
    database_analytics_request = bzapi.DatabaseAnalyticsRequest() # DatabaseAnalyticsRequest | 

    try:
        # Execute natural language command on a database
        api_response = api_instance.v2_databases_database_id_run_analytics_post(database_id, database_analytics_request)
        print("The response of DefaultApi->v2_databases_database_id_run_analytics_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_databases_database_id_run_analytics_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| The database ID | 
 **database_analytics_request** | [**DatabaseAnalyticsRequest**](DatabaseAnalyticsRequest.md)|  | 

### Return type

[**DatabaseAnalyticsResponse**](DatabaseAnalyticsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_databases_post**
> Database v2_databases_post(database)

Create databases

Create database

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import bzapi
from bzapi.models.database import Database
from bzapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flow.boltzbit.com/bz-api
# See configuration.py for a list of all supported configuration parameters.
configuration = bzapi.Configuration(
    host = "https://flow.boltzbit.com/bz-api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = bzapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bzapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bzapi.DefaultApi(api_client)
    database = bzapi.Database() # Database | 

    try:
        # Create databases
        api_response = api_instance.v2_databases_post(database)
        print("The response of DefaultApi->v2_databases_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_databases_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database** | [**Database**](Database.md)|  | 

### Return type

[**Database**](Database.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_documents_bulk_upload_post**
> List[Document] v2_documents_bulk_upload_post(documents, directory_path=directory_path)

Bulk upload documents

Upload one or more documents to be ingested into the flow system for querying 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import bzapi
from bzapi.models.document import Document
from bzapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flow.boltzbit.com/bz-api
# See configuration.py for a list of all supported configuration parameters.
configuration = bzapi.Configuration(
    host = "https://flow.boltzbit.com/bz-api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = bzapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bzapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bzapi.DefaultApi(api_client)
    documents = None # List[bytearray] | 
    directory_path = 'directory_path_example' # str | The directory path to upload the documents to (optional)

    try:
        # Bulk upload documents
        api_response = api_instance.v2_documents_bulk_upload_post(documents, directory_path=directory_path)
        print("The response of DefaultApi->v2_documents_bulk_upload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_documents_bulk_upload_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents** | **List[bytearray]**|  | 
 **directory_path** | **str**| The directory path to upload the documents to | [optional] 

### Return type

[**List[Document]**](Document.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_documents_document_id_delete**
> str v2_documents_document_id_delete(document_id)

Delete a document

Permanently deletes a document. 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import bzapi
from bzapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flow.boltzbit.com/bz-api
# See configuration.py for a list of all supported configuration parameters.
configuration = bzapi.Configuration(
    host = "https://flow.boltzbit.com/bz-api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = bzapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bzapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bzapi.DefaultApi(api_client)
    document_id = 'document_id_example' # str | The document ID

    try:
        # Delete a document
        api_response = api_instance.v2_documents_document_id_delete(document_id)
        print("The response of DefaultApi->v2_documents_document_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_documents_document_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| The document ID | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |
**404** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_documents_document_id_get**
> Document v2_documents_document_id_get(document_id)

Get a document

Get a document to check its content or current status 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import bzapi
from bzapi.models.document import Document
from bzapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flow.boltzbit.com/bz-api
# See configuration.py for a list of all supported configuration parameters.
configuration = bzapi.Configuration(
    host = "https://flow.boltzbit.com/bz-api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = bzapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bzapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bzapi.DefaultApi(api_client)
    document_id = 'document_id_example' # str | The document ID

    try:
        # Get a document
        api_response = api_instance.v2_documents_document_id_get(document_id)
        print("The response of DefaultApi->v2_documents_document_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_documents_document_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| The document ID | 

### Return type

[**Document**](Document.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |
**404** | Error response |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_documents_list_get**
> List[Document] v2_documents_list_get(ids=ids)

List all documents

Retrieve a list of all document resources.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import bzapi
from bzapi.models.document import Document
from bzapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://flow.boltzbit.com/bz-api
# See configuration.py for a list of all supported configuration parameters.
configuration = bzapi.Configuration(
    host = "https://flow.boltzbit.com/bz-api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = bzapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with bzapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bzapi.DefaultApi(api_client)
    ids = ['ids_example'] # List[str] | A list of ids to filter the results (optional)

    try:
        # List all documents
        api_response = api_instance.v2_documents_list_get(ids=ids)
        print("The response of DefaultApi->v2_documents_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v2_documents_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[str]**](str.md)| A list of ids to filter the results | [optional] 

### Return type

[**List[Document]**](Document.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

