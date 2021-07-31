<!-- order:182 -->

#### Returns

`array` - [Log objects](https://besu.hyperledger.org/en/stable/Reference/API-Objects#log-object).

**_Endpoint:_**

```bash
Method: POST
Type: RAW
URL: http://{{rpc-http-host}}:{{rpc-http-port}}
```

**_Body:_**

```js
{
    "jsonrpc": "2.0",
    "method": "eth_getFilterLogs",
    "params": [
        "0x5ace5de3985749b6a1b2b0d3f3e1fb69"
    ],
    "id": 1
}
```

**_More example Requests/Responses:_**
