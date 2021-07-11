<!-- order:197 -->

#### Returns

`result`: `object` - [Miner data](https://besu.hyperledger.org/en/stable/Reference/API-Objects#miner-data-object).

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
    "method": "eth_getMinerDataByBlockNumber",
    "params": [
        "0x7689D2"
    ],
    "id": 1
}
```

**_More example Requests/Responses:_**
