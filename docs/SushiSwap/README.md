---
sort: 3
---

# SushiSwap User API

> Documentation for Order Book API

## Documentation for API Endpoints

All URIs are relative to *https://api.sushirelay.com*

| Class        | Method                              | HTTP request                           | Description                                                                                                                                                                                             |
| ------------ | ----------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| _DefaultApi_ | [**apiV1OrdersGet**](#)             | **GET** /api/v1/orders                 | Get existing orders.                                                                                                                                                                                    |
| _DefaultApi_ | [**apiV1OrdersPost**](#)            | **POST** /api/v1/orders                | Create a new order.                                                                                                                                                                                     |
| _DefaultApi_ | [**apiV1OrdersUIDDelete**](#)       | **DELETE** /api/v1/orders/{UID}        | Cancels order by marking it invalid with a timestamp.                                                                                                                                                   |
| _DefaultApi_ | [**apiV1OrdersUIDGet**](#)          | **GET** /api/v1/orders/{UID}           | Get existing order from UID.                                                                                                                                                                            |
| _DefaultApi_ | [**apiV1SolvableOrdersGet**](#t)    | **GET** /api/v1/solvable_orders        | Get solvable orders.                                                                                                                                                                                    |
| _DefaultApi_ | [**apiV1TokensSellTokenFeeGet**](#) | **GET** /api/v1/tokens/{sellToken}/fee | The fee that is charged for placing an order. The fee is described by a minimum fee - in order to cover the gas costs for onchain settling - and a feeRatio charged to the users for using the service. |
| _DefaultApi_ | [**apiV1TradesGet**](#)             | **GET** /api/v1/trades                 | Get existing Trades.                                                                                                                                                                                    |

### Documentation for Models

- [FeeInformation](#)
- [Order](#)
- [OrderCancellation](#)
- [OrderCancellationError](#)
- [OrderCreation](#)
- [OrderMetaData](#)
- [OrderPostError](#)
- [OrderType](#)
- [Trade](#)

### Documentation for Authorization

All endpoints do not require authorization.
