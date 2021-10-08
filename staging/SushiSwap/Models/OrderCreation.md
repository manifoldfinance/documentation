# OrderCreation

## Properties

| Name                  | Type               | Description                                                                                                                             | Notes                        |
| --------------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| **sellToken**         | [**String**](#)    | Ethereum 40 byte address encoded as a hex with &#x60;0x&#x60; prefix.                                                                   | [optional] [default to null] |
| **buyToken**          | [**String**](#)    | Ethereum 40 byte address encoded as a hex with &#x60;0x&#x60; prefix.                                                                   | [optional] [default to null] |
| **sellAmount**        | [**String**](#)    | Amount of a token. uint256 encoded in decimal.                                                                                          | [optional] [default to null] |
| **buyAmount**         | [**String**](#)    | Amount of a token. uint256 encoded in decimal.                                                                                          | [optional] [default to null] |
| **validTo**           | [**Integer**](#)   | Unix timestamp until the order is valid. uint32.                                                                                        | [optional] [default to null] |
| **appData**           | [**Integer**](#)   | Arbitrary identifier sent along with the order. Could be used to track the interface or other meta-aspects of the order. uint32 encoded | [optional] [default to null] |
| **feeAmount**         | [**String**](#)    | Amount of a token. uint256 encoded in decimal.                                                                                          | [optional] [default to null] |
| **kind**              | [**OrderType**](#) |                                                                                                                                         | [optional] [default to null] |
| **partiallyFillable** | [**Boolean**](#)   | Is this a fill-or-kill order or a partially fillable order?                                                                             | [optional] [default to null] |
| **Signature**         | [**Object**](#)    | 65 bytes encoded as hex with &#x60;0x&#x60; prefix. r + s + v from the spec.                                                            | [optional] [default to null] |
