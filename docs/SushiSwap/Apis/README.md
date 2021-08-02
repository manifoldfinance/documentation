# API Overview

{% include list.liquid all=true %}

All URIs are relative to *https://api.sushirelay.com*

| Method                              | HTTP request                           | Description                                           |
| ----------------------------------- | -------------------------------------- | ----------------------------------------------------- |
| [**apiV1OrdersGet**](#)             | **GET** /api/v1/orders                 | Get existing orders.                                  |
| [**apiV1OrdersPost**](#)            | **POST** /api/v1/orders                | Create a new order.                                   |
| [**apiV1OrdersUIDDelete**](#)       | **DELETE** /api/v1/orders/{UID}        | Cancels order by marking it invalid with a timestamp. |
| [**apiV1OrdersUIDGet**](#)          | **GET** /api/v1/orders/{UID}           | Get existing order from UID.                          |
| [**apiV1SolvableOrdersGet**](#)     | **GET** /api/v1/solvable_orders        | Get solvable orders.                                  |
| [**apiV1TokensSellTokenFeeGet**](#) | **GET** /api/v1/tokens/{sellToken}/fee |
| [**apiV1TradesGet**](#)             | **GET** /api/v1/trades                 | Get existing Trades.                                  |

<a name="apiV1OrdersGet"></a>

# **apiV1OrdersGet**

> List apiV1OrdersGet(owner, sellToken, buyToken, includeFullyExecuted,
> includeInvalidated, includeInsufficientBalance, minValidTo)

Get existing orders.

    By default all currently valid orders are returned. The set of returned orders can be reduced by setting owner, sell token, buy token filters. It can be increased by disabling different order validity exclusion criteria.

### Parameters

| Name                           | Type        | Description                                                                      | Notes                         |
| ------------------------------ | ----------- | -------------------------------------------------------------------------------- | ----------------------------- |
| **owner**                      | **String**  | Ethereum 40 byte address encoded as a hex with &#x60;0x&#x60; prefix.            | [optional] [default to null]  |
| **sellToken**                  | **String**  | Ethereum 40 byte address encoded as a hex with &#x60;0x&#x60; prefix.            | [optional] [default to null]  |
| **buyToken**                   | **String**  | Ethereum 40 byte address encoded as a hex with &#x60;0x&#x60; prefix.            | [optional] [default to null]  |
| **includeFullyExecuted**       | **Boolean** | Should fully executed orders be returned?                                        | [optional] [default to false] |
| **includeInvalidated**         | **Boolean** | Should orders that have been invalidated in the smart contract be returned?      | [optional] [default to false] |
| **includeInsufficientBalance** | **Boolean** | Should fill or kill orders that are not sufficiently funded be included?         | [optional] [default to false] |
| **minValidTo**                 | **Integer** | Minimum valid_to timestamp for included orders. The default is the current time. | [optional] [default to null]  |

### Return type

[**List**](#)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="apiV1OrdersPost"></a>

# **apiV1OrdersPost**

> String apiV1OrdersPost(body)

Create a new order.

### Parameters

| Name     | Type                   | Description          | Notes |
| -------- | ---------------------- | -------------------- | ----- |
| **body** | [**OrderCreation**](#) | The order to create. |

### Return type

[**String**](#)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="apiV1OrdersUIDDelete"></a>

# **apiV1OrdersUIDDelete**

> apiV1OrdersUIDDelete(uID, body)

Cancels order by marking it invalid with a timestamp.

    The successful deletion might not prevent solvers from settling the order Authentication must be provided by signing the following message:

### Parameters

| Name     | Type                       | Description                                                                                                                                                                          | Notes             |
| -------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| **uID**  | **String**                 | Unique identifier for the order: 56 bytes encoded as hex with &#x60;0x&#x60; prefix. Bytes 0 to 32 are the order digest, bytes 30 to 52 the owner address and bytes 52..56 valid to, | [default to null] |
| **body** | [**OrderCancellation**](#) | Signed OrderCancellation                                                                                                                                                             |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

<a name="apiV1OrdersUIDGet"></a>

# **apiV1OrdersUIDGet**

> List apiV1OrdersUIDGet(uID)

Get existing order from UID.

### Parameters

| Name    | Type       | Description                                                                                                                                                                          | Notes             |
| ------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| **uID** | **String** | Unique identifier for the order: 56 bytes encoded as hex with &#x60;0x&#x60; prefix. Bytes 0 to 32 are the order digest, bytes 30 to 52 the owner address and bytes 52..56 valid to, | [default to null] |

### Return type

[**List**](#)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="apiV1SolvableOrdersGet"></a>

# **apiV1SolvableOrdersGet**

> List apiV1SolvableOrdersGet()

Get solvable orders.

    The set of orders that solvers should be solving right now. These orders are determined to be valid at the time of the request.

### Parameters

This endpoint does not need any parameter.

### Return type

[**List**](#)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="apiV1TokensSellTokenFeeGet"></a>

# **apiV1TokensSellTokenFeeGet**

> FeeInformation apiV1TokensSellTokenFeeGet(sellToken)

    The fee that is charged for placing an order. The fee is described by a minimum fee - in order to cover the gas costs for onchain settling - and a feeRatio charged to the users for using the service.

### Parameters

| Name          | Type       | Description                                                           | Notes             |
| ------------- | ---------- | --------------------------------------------------------------------- | ----------------- |
| **sellToken** | **String** | Ethereum 40 byte address encoded as a hex with &#x60;0x&#x60; prefix. | [default to null] |

### Return type

[**FeeInformation**](#)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="apiV1TradesGet"></a>

# **apiV1TradesGet**

> List apiV1TradesGet(owner, orderUid)

Get existing Trades.

    By default all trades are returned. Queries can be refined by specifiying owner or order_uid.

### Parameters

| Name         | Type       | Description                                                                                                                                                                          | Notes                        |
| ------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- |
| **owner**    | **String** | Ethereum 40 byte address encoded as a hex with &#x60;0x&#x60; prefix.                                                                                                                | [optional] [default to null] |
| **orderUid** | **String** | Unique identifier for the order: 56 bytes encoded as hex with &#x60;0x&#x60; prefix. Bytes 0 to 32 are the order digest, bytes 30 to 52 the owner address and bytes 52..56 valid to, | [optional] [default to null] |

### Return type

[**List**](#)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json
