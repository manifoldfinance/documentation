<!-- order:282 -->

#### Returns

`data` - Filter ID.

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
    "method": "eth_newPendingTransactionFilter",
    "params": [],
    "id": 1
}
```

**_More example Requests/Responses:_**
