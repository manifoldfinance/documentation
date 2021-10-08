# eth_uninstallFilter

Uninstalls a filter with given id. Should always be called when watch is
no longer needed. Additonally Filters timeout when they aren't requested
with eth_getFilterChanges for a period of time.

#### EXAMPLE

```bash
>wscat -c wss://mainnet.backbonecabal.xyz/ws

>{"jsonrpc":"2.0","method":"eth_uninstallFilter","params":["0xfe704947a3cd3ca12541458a4321c869"],"id":73}
```

### RESPONSE

#### RESULT FIELDS

- `UNINSTALLED FLAG` - true if the filter was successfully uninstalled,
  otherwise false.

#### BODY

```json
{
  "jsonrpc": "2.0",
  "id": 73,
  "result": true
}
```
