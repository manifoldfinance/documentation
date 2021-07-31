# FeeInformation

## Properties

| Name               | Type                        | Description                                                                                                                     | Notes                        |
| ------------------ | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| **expirationDate** | [**String**](string.md)     | Expiration date of the offered fee. Order service might not accept the fee after this expiration date. Encoded as ISO 8601 UTC. | [optional] [default to null] |
| **minimalFee**     | [**String**](string.md)     | Amount of a token. uint256 encoded in decimal.                                                                                  | [optional] [default to null] |
| **feeRatio**       | [**BigDecimal**](number.md) | The fee ratio charged on a sellAmount. Denoted in basis points                                                                  | [optional] [default to null] |
