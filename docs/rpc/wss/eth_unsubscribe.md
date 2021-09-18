# eth_unsubscribe

Subscriptions are cancelled with a regular RPC call with eth_unsubscribe
as method and the subscription id as first parameter. It returns a bool
indicating if the subscription was cancelled successful.

### REQUEST PARAMS

- `SUBSCRIPTION ID` _[required]_

#### EXAMPLE

```bash
>wscat -c wss://mainnet.backbonecabal.xyz/ws

>{"id": 1, "method": "eth_unsubscribe", "params": ["0x9cef478923ff08bf67fde6c64013158d"]}
```

### RESPONSE

#### RESULT FIELDS

- `UNSUBSCRIBED FLAG` - true if the subscription was cancelled
  successful.

#### BODY

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": true
}
```
