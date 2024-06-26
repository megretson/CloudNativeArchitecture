# openapi_client.DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/MargaretAnderson/RecipeComparer/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_recipe**](DefaultApi.md#add_recipe) | **POST** /recipes | add a new recipe
[**add_recipe_make**](DefaultApi.md#add_recipe_make) | **POST** /recipes/{recipeId}/makes | say that you made a recipe
[**get_recipe_make**](DefaultApi.md#get_recipe_make) | **GET** /recipes/{recipeId}/makes/{makeId} | Recieve information on a given make of a recipe
[**get_recipe_make_differences**](DefaultApi.md#get_recipe_make_differences) | **GET** /recipes/{recipeId}/makes/{makeId}/differences | Recieve information on a given make of a recipe, including any variations between the make and the actual recipe
[**update_recipe**](DefaultApi.md#update_recipe) | **PUT** /recipes | update a recipe


# **add_recipe**
> add_recipe(recipe=recipe)

add a new recipe

### Example


```python
import openapi_client
from openapi_client.models.recipe import Recipe
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/MargaretAnderson/RecipeComparer/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://virtserver.swaggerhub.com/MargaretAnderson/RecipeComparer/1.0.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    recipe = openapi_client.Recipe() # Recipe |  (optional)

    try:
        # add a new recipe
        api_instance.add_recipe(recipe=recipe)
    except Exception as e:
        print("Exception when calling DefaultApi->add_recipe: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipe** | [**Recipe**](Recipe.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Invalid ID supplied |  -  |
**404** | Pet not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_recipe_make**
> add_recipe_make(recipe_id, recipe=recipe)

say that you made a recipe

### Example


```python
import openapi_client
from openapi_client.models.recipe import Recipe
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/MargaretAnderson/RecipeComparer/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://virtserver.swaggerhub.com/MargaretAnderson/RecipeComparer/1.0.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    recipe_id = 56 # int | ID of recipe to return
    recipe = openapi_client.Recipe() # Recipe |  (optional)

    try:
        # say that you made a recipe
        api_instance.add_recipe_make(recipe_id, recipe=recipe)
    except Exception as e:
        print("Exception when calling DefaultApi->add_recipe_make: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipe_id** | **int**| ID of recipe to return | 
 **recipe** | [**Recipe**](Recipe.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Invalid ID supplied |  -  |
**404** | Pet not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recipe_make**
> get_recipe_make(recipe_id, make_id)

Recieve information on a given make of a recipe

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/MargaretAnderson/RecipeComparer/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://virtserver.swaggerhub.com/MargaretAnderson/RecipeComparer/1.0.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    recipe_id = 56 # int | ID of recipe to return
    make_id = 56 # int | ID of make to return

    try:
        # Recieve information on a given make of a recipe
        api_instance.get_recipe_make(recipe_id, make_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_recipe_make: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipe_id** | **int**| ID of recipe to return | 
 **make_id** | **int**| ID of make to return | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Valid request |  -  |
**404** | Pet not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recipe_make_differences**
> get_recipe_make_differences(recipe_id, make_id)

Recieve information on a given make of a recipe, including any variations between the make and the actual recipe

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/MargaretAnderson/RecipeComparer/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://virtserver.swaggerhub.com/MargaretAnderson/RecipeComparer/1.0.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    recipe_id = 56 # int | ID of recipe to return
    make_id = 56 # int | ID of make to return

    try:
        # Recieve information on a given make of a recipe, including any variations between the make and the actual recipe
        api_instance.get_recipe_make_differences(recipe_id, make_id)
    except Exception as e:
        print("Exception when calling DefaultApi->get_recipe_make_differences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipe_id** | **int**| ID of recipe to return | 
 **make_id** | **int**| ID of make to return | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Valid differences |  -  |
**404** | Pet not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recipe**
> update_recipe(recipe=recipe)

update a recipe

### Example


```python
import openapi_client
from openapi_client.models.recipe import Recipe
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://virtserver.swaggerhub.com/MargaretAnderson/RecipeComparer/1.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://virtserver.swaggerhub.com/MargaretAnderson/RecipeComparer/1.0.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    recipe = openapi_client.Recipe() # Recipe |  (optional)

    try:
        # update a recipe
        api_instance.update_recipe(recipe=recipe)
    except Exception as e:
        print("Exception when calling DefaultApi->update_recipe: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recipe** | [**Recipe**](Recipe.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Invalid ID supplied |  -  |
**404** | Pet not found |  -  |
**405** | Validation exception |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

