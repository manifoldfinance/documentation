# eth_newBlockFilter

Creates a filter in the node, to notify when a new block arrives. To
check if the state has changed, call eth_getFilterChanges.

#### EXAMPLE

```bash
>wscat -c wss://mainnet.backbonecabal.xyz/ws

>{"jsonrpc":"2.0","method":"eth_newBlockFilter","params":[],"id":73}
```

### RESPONSE

#### RESULT FIELDS

- `FILTER ID` - A string denoting the newly created filter id

#### BODY

```json
{
  "jsonrpc": "2.0",
  "id": 73,
  "result": "0xfe704947a3cd3ca12541458a4321c869"
}
```
