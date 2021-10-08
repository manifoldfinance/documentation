# eth_newFilter

Creates a filter object, based on filter options, to notify when the
state changes (logs). To check if the state has changed, call
eth_getFilterChanges

#### REQUEST PAYLOAD

- `FILTER OBJECT`
  - `address` _[optional]_ - a string representing the address (20
    bytes) to check for balance
  - `fromBlock` _[optional, default is "latest"]_ - an integer block
    number, or the string "latest", "earliest" or "pending"
  - `toBlock` _[optional, default is "latest"]_ - an integer block
    number, or the string "latest", "earliest" or "pending"
  - `topics`_[optional]_ - Array of 32 Bytes DATA topics. Topics are
    order-dependent.

**A note on specifying topic filters:** Topics are order-dependent. A
transaction with a log with topics [A, B] will be matched by the
following topic filters:

- [] - anything"
- [A] - A in first position (and anything after)
- [null, B] - anything in first position AND B in second position (and
  anything after)
- [A, B] - A in first position AND B in second position (and anything
  after)"
- \[[A, B], [A, B]] - (A OR B) in first position AND (A OR B) in second
  position (and anything after)

#### EXAMPLE

```bash
>wscat -c wss://mainnet.backbonecabal.xyz/ws

>{"jsonrpc":"2.0","method":"eth_newFilter","params":[{"topics": ["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"]}],"id":73}
```

### RESPONSE

#### RESULT FIELDS

- `FILTER ID` - A string denoting the newly created filter id

#### BODY

```json
{
  "jsonrpc": "2.0",
  "id": 73,
  "result": "0x7db09f66a25e197d995d3895278b731"
}
```
