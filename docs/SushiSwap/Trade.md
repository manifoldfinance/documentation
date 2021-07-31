# Trade

## Properties

| Name                     | Type                      | Description                                                                                                                                                                          | Notes                        |
| ------------------------ | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- |
| **blockNumber**          | [**Integer**](integer.md) | Block in which trade occurred.                                                                                                                                                       | [optional] [default to null] |
| **logIndex**             | [**Integer**](integer.md) | Index in which transaction was included in block.                                                                                                                                    | [optional] [default to null] |
| **orderUid**             | [**String**](string.md)   | Unique identifier for the order: 56 bytes encoded as hex with &#x60;0x&#x60; prefix. Bytes 0 to 32 are the order digest, bytes 30 to 52 the owner address and bytes 52..56 valid to, | [optional] [default to null] |
| **owner**                | [**String**](string.md)   | Ethereum 40 byte address encoded as a hex with &#x60;0x&#x60; prefix.                                                                                                                | [optional] [default to null] |
| **sellToken**            | [**String**](string.md)   | Ethereum 40 byte address encoded as a hex with &#x60;0x&#x60; prefix.                                                                                                                | [optional] [default to null] |
| **buyToken**             | [**String**](string.md)   | Ethereum 40 byte address encoded as a hex with &#x60;0x&#x60; prefix.                                                                                                                | [optional] [default to null] |
| **sellAmount**           | [**String**](string.md)   | Amount of a token. uint256 encoded in decimal.                                                                                                                                       | [optional] [default to null] |
| **sellAmountBeforeFees** | [**String**](string.md)   | A big unsigned integer encoded in decimal.                                                                                                                                           | [optional] [default to null] |
| **buyAmount**            | [**String**](string.md)   | Amount of a token. uint256 encoded in decimal.                                                                                                                                       | [optional] [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
