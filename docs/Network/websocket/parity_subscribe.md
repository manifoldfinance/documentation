# parity_subscribe

Starts a subscription (on WebSockets / IPC / TCP transports) to results
of calling some other RPC method. For every change in returned value of
that RPC call a JSON-RPC notification with result and subscription ID
will be sent to a client. NOTE: parity_subscribe is only supported on
the Kovan network

### REQUEST PARAMS

- `RPC method name` _[required]_
  - RPC method name (string type)
- `OPTIONAL ARGUMENTS`
  - `Params` - Parameters passed to RPC method

#### EXAMPLE

```bash
>wscat -c wss://kovan.backbonecabal.xyz/ws

// subscribe to eth_getBalance
>{"method":"parity_subscribe","params":["eth_getBalance",["0x004702bdcC3C7dbFfd943136107E70B827028600","latest"]],"id":1,"jsonrpc":"2.0"}
```

### RESPONSE

#### RESULT FIELDS

- `RESULT` - ID of the newly created subscription on the node

#### BODY

```json
// New Subscription response
{
    "jsonrpc": "2.0",
    "result": "0x070fa1c4d1b3fd81",
    "id": 1
}

// eth_getBalance subscription notification
{
    "jsonrpc":"2.0",
    "method":"parity_subscription",
    "params": {
        "result":"0x36464dbbdd98953718",
        "subscription":"0x49a3a64111acb418"
    }
}
```
