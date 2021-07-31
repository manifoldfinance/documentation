<!-- order:290 -->

### 37. eth_sendRawTransaction

Sends a [signed transaction](https://besu.hyperledger.org/en/stable/HowTo/Send-Transactions/Transactions). A transaction
can send ether, deploy a contract, or interact with a contract. Set the maximum transaction fee for transactions using
the [`--rpc-tx-feecap`](https://besu.hyperledger.org/en/stable/CLI/CLI-Syntax#rpc-tx-feecap) CLI option.

You can interact with contracts using [`eth_sendRawTransaction` or `eth_call`].

To avoid exposing your private key, create signed transactions offline and send the signed transaction data using
`eth_sendRawTransaction`.

> **important**
>
> Besu does not implement
> [`eth_sendTransaction`](https://besu.hyperledger.org/en/stable/HowTo/Send-Transactions/Account-Management).
>
> [EthSigner](https://docs.ethsigner.consensys.net/) provides transaction signing and implements
> [`eth_sendTransaction`](https://docs.ethsigner.consensys.net/Using-EthSigner/Using-EthSigner/#eth_sendtransaction).
<!-- order:291 -->

#### Parameters

`data` - Signed transaction serialized to hexadecimal format. For example:

`params: ["0xf869018203e882520894f17f52151ebef6c7334fad080c5704d77216b732881bc16d674ec80000801ba02da1c48b670996dcb1f447ef9ef00b33033c48a4fe938f420bec3e56bfd24071a062e0aa78a81bf0290afbc3a9d8e9a068e6d74caa66c5e0fa8a46deaae96b0833"]`

> **note**
>
> [Creating and Sending Transactions](https://besu.hyperledger.org/en/stable/HowTo/Send-Transactions/Transactions)
> includes examples of creating signed transactions using the [web3.js](https://github.com/ethereum/web3.js/) library.
<!-- order:292 -->

#### Returns

`result` : `data` - 32-byte transaction hash.

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
    "method": "eth_sendRawTransaction",
    "params": [
        "0xf86a018203e882520894f17f52151ebef6c7334fad080c5704d77216b732896c6b935b8bbd400000801ba093129415f03b4794fd1512e79ee7f097e4271f66721020f8407aac92179893a5a0451b875d89721ec98be55201092980b0a87bb1c48507fccb86da713596b2a09e"
    ],
    "id": 1
}
```

**_More example Requests/Responses:_**
<!-- order:293 -->

##### I. Example Request: eth_sendRawTransaction

**_Body:_**

```js
{"jsonrpc":"2.0","method":"eth_sendRawTransaction","params" :["0xf85f808203e8832dc6c08080914f785b6f626a656374204f626a6563745d1ba004193142058b4fe6802677a939e76f93e7fa30e91835a911e206f9855330929ca055ce11a262c804a168c8a801e55a68b3d578a4b52b9dfbed98c4aa47f88a0adf"], "id":1}
```
<!-- order:294 -->

##### I. Example Response: eth_sendRawTransaction

```js
{
  "jsonrpc" : "2.0",
  "id" : 1,
  "result" : "0xac182cc23bb94696217aa17ca15bd466106af9ba7ea7420aae24ff37338d6e3b"
}
```

**_Status Code:_** 200

<br>
