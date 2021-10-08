# Make Requests

### JSON-RPC Methods

Below is a quick command line example using CURL:

```
$ curl -X POST
-H "Content-Type: application/json"
--data '{"jsonrpc": "2.0", "id": 1, "method": "eth_blockNumber",
"params": []}'
"https://mainnet.backbonecabal.xyz/YOUR-API-KEY"
```

The result should look something like this:

```
$ {"jsonrpc": "2.0","result": "0x3ccb11", "id":1}
```

**NOTE:** "0x3ccb11" will be replaced with the block number of the most
recent block on that network

[Read more about JSON RPC](https://github.com/ethereum/wiki/wiki/JSON-RPC)

Important to note that JSON-RPC is transport agnostic, meaning same
concepts can be used over HTTP, WebSockets or other message passing
environments. All JSON_RPC methods listed in 'Ethereum API' are also
supported over websockets.

### Rest-like Backbone API

```
https://api.backbonecabal.xyz/v1/jsonrpc/mainnet/eth_blockNumber?token=YOUR-API-KEY
```

### Subscriptions and Filters

TODO
