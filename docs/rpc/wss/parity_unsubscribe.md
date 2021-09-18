# parity_unsubscribe

Unsubscribes from a subscription. NOTE: parity_unsubscribe is only
supported on the Kovan network

### REQUEST PARAMS

- `SUBSCRIPTION ID` _[required]_

#### EXAMPLE

```bash
>wscat -c wss://kovan.backbonecabal.xyz/ws

>{"method":"parity_unsubscribe","params":["0x070fa1c4d1b3fd81"],"id":1,"jsonrpc":"2.0"}
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
