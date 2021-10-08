# Trade

## Properties

| Name                     | Type             | Description                                                                                                                                                                          | Notes                        |
| ------------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- |
| **blockNumber**          | [**Integer**](#) | Block in which trade occurred.                                                                                                                                                       | [optional] [default to null] |
| **logIndex**             | [**Integer**](#) | Index in which transaction was included in block.                                                                                                                                    | [optional] [default to null] |
| **orderUid**             | [**String**](#)  | Unique identifier for the order: 56 bytes encoded as hex with &#x60;0x&#x60; prefix. Bytes 0 to 32 are the order digest, bytes 30 to 52 the owner address and bytes 52..56 valid to, | [optional] [default to null] |
| **owner**                | [**String**](#)  | Ethereum 40 byte address encoded as a hex with &#x60;0x&#x60; prefix.                                                                                                                | [optional] [default to null] |
| **sellToken**            | [**String**](#)  | Ethereum 40 byte address encoded as a hex with &#x60;0x&#x60; prefix.                                                                                                                | [optional] [default to null] |
| **buyToken**             | [**String**](#)  | Ethereum 40 byte address encoded as a hex with &#x60;0x&#x60; prefix.                                                                                                                | [optional] [default to null] |
| **sellAmount**           | [**String**](#)  | Amount of a token. uint256 encoded in decimal.                                                                                                                                       | [optional] [default to null] |
| **sellAmountBeforeFees** | [**String**](#)  | A big unsigned integer encoded in decimal.                                                                                                                                           | [optional] [default to null] |
| **buyAmount**            | [**String**](#)  | Amount of a token. uint256 encoded in decimal.                                                                                                                                       | [optional] [default to null] |
