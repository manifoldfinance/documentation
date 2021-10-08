## eth_accounts

### v1/jsonrpc/:network/eth_accounts

Returns a list of addresses owned by client.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_accounts`

> HEADERS

`Content-Type: application/json`

!!! example

```bash

curl -sL https://api.sushirelay.com/v1/eth_accounts

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_accounts","params":[],"id":73}
```

> RESPONSE

> RESULT FIELDS

- `ADDRESSES` - arrays of hex codes as strings representing the
  addresses owned by the client

> BODY

```js
{
    jsonrpc: "2.0",
    id: 1,
    result: ["0xc94770007dda54cF92009BFF0dE90c06F603a09f"]
}
```
## eth_blockNumber

### v1/jsonrpc/:network/eth_blockNumber

Returns the number of most recent block.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_blockNumber`

> HEADERS

`Content-Type: application/json`

!!! example

```bash

curl -sL https://api.sushirelay.com/v1/eth_blockNumber

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_blockNumber","params": [],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":73}
```

> RESPONSE

> RESULT FIELDS

- `BLOCK NUMBER` - a hex code of an integer representing the current
  block number the client is on.

> BODY

```js
{
    jsonrpc: "2.0",
    id: 1,
    result: "0x5c174e"
}
```
## eth_gasPrice

### v1/jsonrpc/:network/eth_gasPrice

Returns the number of hashes per second that the node is mining with.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_gasPrice`

> HEADERS

`Content-Type: application/json`

!!! example

```bash

curl -sL https://api.sushirelay.com/v1/eth_gasPrice

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_gasPrice","params": [],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_gasPrice","params":[],"id":73}
```

> RESPONSE

> RESULT FIELDS

- `HASHRATE` - a hex code of an integer representing the current gas
  price in wei.

> BODY

```js
{
    jsonrpc: "2.0",
    id: 1,
    result: "0x3b9acde7"
}
```
## eth_getBalance

### v1/jsonrpc/:network/eth_getBalance

Returns the balance of the account of given address.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_getBalance?params=:paramsJSONArray`

> HEADERS

`Content-Type: application/json`

!!! example
     REQUEST PARAMS

- `ADDRESS` _[required]_ - a string representing the address (20 bytes)
  to check for balance

- `BLOCK PARAMETER` _[required]_ - an integer block number, or the
  string "latest", "earliest" or "pending", see the
  [default block parameter](https://github.com/ethereum/wiki/wiki/JSON-RPC##the-default-block-parameter)

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/eth_getBalance --data-urlencode 'params=["0xc94770007dda54cF92009BFF0dE90c06F603a09f","latest"]'

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_getBalance","params": ["0xc94770007dda54cF92009BFF0dE90c06F603a09f", "latest"],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_getBalance","params":["0xc94770007dda54cF92009BFF0dE90c06F603a09f","latest"],"id":73}
```

> RESPONSE

> RESULT FIELDS

- `BALANCE` - integer of the current balance in wei.

> BODY

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x29a33d8a9314006"
}
```
## eth_getBlockByHash

### v1/jsonrpc/:network/eth_getBlockByHash

Returns information about a block by hash.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_getBlockByHash?params=:paramsJSONArray`

> HEADERS

`Content-Type: application/json`

!!! example
     REQUEST PARAMS

- `BLOCK HASH` _[required]_ - a string representing the hash (32 bytes)
  of a block
- `SHOW TRANSACTION DETAILS FLAG` _[required]_ - if set to true, it
  returns the full transaction objects, if false only the hashes of the
  transactions.

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/eth_getBlockByHash --data-urlencode 'params=["0xb3b20624f8f0f86eb50dd04688409e5cea4bd02d700bf6e79e9384d47d6a5a35",false]'

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_getBlockByHash","params": ["0xb3b20624f8f0f86eb50dd04688409e5cea4bd02d700bf6e79e9384d47d6a5a35",false],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_getBlockByHash","params": ["0xb3b20624f8f0f86eb50dd04688409e5cea4bd02d700bf6e79e9384d47d6a5a35",false],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `BLOCK` - A block object, or null when no block was found
  - `number`: the block number. null when its pending block.
  - `hash`: 32 Bytes - hash of the block. null when its pending block.
  - `parentHash`: 32 Bytes - hash of the parent block.
  - `nonce`: 8 Bytes - hash of the generated proof-of-work. null when
    its pending block.
  - `sha3Uncles`: 32 Bytes - SHA3 of the uncles data in the block.
  - `logsBloom`: 256 Bytes - the bloom filter for the logs of the block.
    null when its pending block.
  - `transactionsRoot`: 32 Bytes - the root of the transaction trie of
    the block.
  - `stateRoot`: 32 Bytes - the root of the final state trie of the
    block.
  - `receiptsRoot`: 32 Bytes - the root of the receipts trie of the
    block.
  - `miner`: 20 Bytes - the address of the beneficiary to whom the
    mining rewards were given.
  - `difficulty`: integer of the difficulty for this block.
  - `totalDifficulty`: integer of the total difficulty of the chain
    until this block.
  - `extraData`: the "extra data" field of this block.
  - `size`: integer the size of this block in bytes.
  - `gasLimit`: the maximum gas allowed in this block.
  - `gasUsed`: the total used gas by all transactions in this block.
  - `timestamp`: the unix timestamp for when the block was collated.
  - `transactions`: Array - Array of transaction objects, or 32 Bytes
    transaction hashes depending on the last given parameter.
  - `uncles`: an Array of uncle hashes.

> BODY

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "difficulty": "0xbfabcdbd93dda",
    "extraData": "0x737061726b706f6f6c2d636e2d6e6f64652d3132",
    "gasLimit": "0x79f39e",
    "gasUsed": "0x79ccd3",
    "hash": "0xb3b20624f8f0f86eb50dd04688409e5cea4bd02d700bf6e79e9384d47d6a5a35",
    "logsBloom": "0x4848112002a2020aaa0812180045840210020005281600c80104264300080008000491220144461026015300100000128005018401002090a824a4150015410020140400d808440106689b29d0280b1005200007480ca950b15b010908814e01911000054202a020b05880b914642a0000300003010044044082075290283516be82504082003008c4d8d14462a8800c2990c88002a030140180036c220205201860402001014040180002006860810ec0a1100a14144148408118608200060461821802c081000042d0810104a8004510020211c088200420822a082040e10104c00d010064004c122692020c408a1aa2348020445403814002c800888208b1",
    "miner": "0x5a0b54d5dc17e0aadc383d2db43b0a0d3e029c4c",
    "mixHash": "0x3d1fdd16f15aeab72e7db1013b9f034ee33641d92f71c0736beab4e67d34c7a7",
    "nonce": "0x4db7a1c01d8a8072",
    "number": "0x5bad55",
    "parentHash": "0x61a8ad530a8a43e3583f8ec163f773ad370329b2375d66433eb82f005e1d6202",
    "receiptsRoot": "0x5eced534b3d84d3d732ddbc714f5fd51d98a941b28182b6efe6df3a0fe90004b",
    "sha3Uncles": "0x8a562e7634774d3e3a36698ac4915e37fc84a2cd0044cb84fa5d80263d2af4f6",
    "size": "0x41c7",
    "stateRoot": "0xf5208fffa2ba5a3f3a2f64ebd5ca3d098978bedd75f335f56b705d8715ee2305",
    "timestamp": "0x5b541449",
    "totalDifficulty": "0x12ac11391a2f3872fcd",
    "transactions": [
      "0x8784d99762bccd03b2086eabccee0d77f14d05463281e121a62abfebcf0d2d5f",
      "0x311be6a9b58748717ac0f70eb801d29973661aaf1365960d159e4ec4f4aa2d7f",
      "0xe42b0256058b7cad8a14b136a0364acda0b4c36f5b02dea7e69bfd82cef252a2",
      "0x4eb05376055c6456ed883fc843bc43df1dcf739c321ba431d518aecd7f98ca11",
      "0x994dd9e72b212b7dc5fd0466ab75adf7d391cf4f206a65b7ad2a1fd032bb06d7",
      "0xf6feecbb9ab0ac58591a4bc287059b1133089c499517e91a274e6a1f5e7dce53",
      "0x7e537d687a5525259480440c6ea2e1a8469cd98906eaff8597f3d2a44422ff97",
      "0xa762220e92bed6d77a2c19ffc60dad77d71bd5028c5230c896ab4b9552a39b50",
      "0xf1fa677edda7e5add8e794732c7554cd5459a5c12781dc71de73c7937dfb2775"
    ],
    "transactionsRoot": "0xf98631e290e88f58a46b7032f025969039aa9b5696498efc76baf436fa69b262",
    "uncles": [
      "0x824cce7c7c2ec6874b9fa9a9a898eb5f27cbaf3991dfa81084c3af60d1db618c"
    ]
  }
}
```
## eth_getBlockByNumber

### v1/jsonrpc/:network/eth_getBlockByNumber

Returns information about a block by hash.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_getBlockByNumber?params=:paramsJSONArray`

> HEADERS

`Content-Type: application/json`

!!! example
     REQUEST PARAMS

- `BLOCK PARAMETER` _[required]_ - an integer block number, or the
  string "latest", "earliest" or "pending", see the
  [default block parameter](https://github.com/ethereum/wiki/wiki/JSON-RPC##the-default-block-parameter)
- `SHOW TRANSACTION DETAILS FLAG` _[required]_ - if set to true, it
  returns the full transaction objects, if false only the hashes of the
  transactions.

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/eth_getBlockByNumber --data-urlencode 'params=["0x5BAD55",false]'

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params": ["0x5BAD55",false],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params": ["0x5BAD55",false],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `BLOCK` - A block object, or null when no block was found
  - `number`: the block number. null when its pending block.
  - `hash`: 32 Bytes - hash of the block. null when its pending block.
  - `parentHash`: 32 Bytes - hash of the parent block.
  - `nonce`: 8 Bytes - hash of the generated proof-of-work. null when
    its pending block.
  - `sha3Uncles`: 32 Bytes - SHA3 of the uncles data in the block.
  - `logsBloom`: 256 Bytes - the bloom filter for the logs of the block.
    null when its pending block.
  - `transactionsRoot`: 32 Bytes - the root of the transaction trie of
    the block.
  - `stateRoot`: 32 Bytes - the root of the final state trie of the
    block.
  - `receiptsRoot`: 32 Bytes - the root of the receipts trie of the
    block.
  - `miner`: 20 Bytes - the address of the beneficiary to whom the
    mining rewards were given.
  - `difficulty`: integer of the difficulty for this block.
  - `totalDifficulty`: integer of the total difficulty of the chain
    until this block.
  - `extraData`: the "extra data" field of this block.
  - `size`: integer the size of this block in bytes.
  - `gasLimit`: the maximum gas allowed in this block.
  - `gasUsed`: the total used gas by all transactions in this block.
  - `timestamp`: the unix timestamp for when the block was collated.
  - `transactions`: Array - Array of transaction objects, or 32 Bytes
    transaction hashes depending on the last given parameter.
  - `uncles`: an Array of uncle hashes.

> BODY

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "difficulty": "0xbfabcdbd93dda",
    "extraData": "0x737061726b706f6f6c2d636e2d6e6f64652d3132",
    "gasLimit": "0x79f39e",
    "gasUsed": "0x79ccd3",
    "hash": "0xb3b20624f8f0f86eb50dd04688409e5cea4bd02d700bf6e79e9384d47d6a5a35",
    "logsBloom": "0x4848112002a2020aaa0812180045840210020005281600c80104264300080008000491220144461026015300100000128005018401002090a824a4150015410020140400d808440106689b29d0280b1005200007480ca950b15b010908814e01911000054202a020b05880b914642a0000300003010044044082075290283516be82504082003008c4d8d14462a8800c2990c88002a030140180036c220205201860402001014040180002006860810ec0a1100a14144148408118608200060461821802c081000042d0810104a8004510020211c088200420822a082040e10104c00d010064004c122692020c408a1aa2348020445403814002c800888208b1",
    "miner": "0x5a0b54d5dc17e0aadc383d2db43b0a0d3e029c4c",
    "mixHash": "0x3d1fdd16f15aeab72e7db1013b9f034ee33641d92f71c0736beab4e67d34c7a7",
    "nonce": "0x4db7a1c01d8a8072",
    "number": "0x5bad55",
    "parentHash": "0x61a8ad530a8a43e3583f8ec163f773ad370329b2375d66433eb82f005e1d6202",
    "receiptsRoot": "0x5eced534b3d84d3d732ddbc714f5fd51d98a941b28182b6efe6df3a0fe90004b",
    "sha3Uncles": "0x8a562e7634774d3e3a36698ac4915e37fc84a2cd0044cb84fa5d80263d2af4f6",
    "size": "0x41c7",
    "stateRoot": "0xf5208fffa2ba5a3f3a2f64ebd5ca3d098978bedd75f335f56b705d8715ee2305",
    "timestamp": "0x5b541449",
    "totalDifficulty": "0x12ac11391a2f3872fcd",
    "transactions": [
      "0x8784d99762bccd03b2086eabccee0d77f14d05463281e121a62abfebcf0d2d5f",
      "0x311be6a9b58748717ac0f70eb801d29973661aaf1365960d159e4ec4f4aa2d7f",
      "0xe42b0256058b7cad8a14b136a0364acda0b4c36f5b02dea7e69bfd82cef252a2",
      "0x4eb05376055c6456ed883fc843bc43df1dcf739c321ba431d518aecd7f98ca11",
      "0x994dd9e72b212b7dc5fd0466ab75adf7d391cf4f206a65b7ad2a1fd032bb06d7",
      "0xf6feecbb9ab0ac58591a4bc287059b1133089c499517e91a274e6a1f5e7dce53",
      "0x7e537d687a5525259480440c6ea2e1a8469cd98906eaff8597f3d2a44422ff97",
      "0xa762220e92bed6d77a2c19ffc60dad77d71bd5028c5230c896ab4b9552a39b50",
      "0xf1fa677edda7e5add8e794732c7554cd5459a5c12781dc71de73c7937dfb2775"
    ],
    "transactionsRoot": "0xf98631e290e88f58a46b7032f025969039aa9b5696498efc76baf436fa69b262",
    "uncles": [
      "0x824cce7c7c2ec6874b9fa9a9a898eb5f27cbaf3991dfa81084c3af60d1db618c"
    ]
  }
}
```
## eth_getBlockTransactionCountByHash

### v1/jsonrpc/:network/eth_getBlockTransactionCountByHash

Returns the number of transactions in a block from a block matching the
given block hash.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_getBlockTransactionCountByHash?params=:paramsJSONArray`

> HEADERS

`Content-Type: application/json`

!!! example
     REQUEST PARAMS

- `BLOCK HASH` _[required]_ - a string representing the hash (32 bytes)
  of a block

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/eth_getBlockTransactionCountByHash --data-urlencode 'params=["0xb3b20624f8f0f86eb50dd04688409e5cea4bd02d700bf6e79e9384d47d6a5a35"]'

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByHash","params": ["0xb3b20624f8f0f86eb50dd04688409e5cea4bd02d700bf6e79e9384d47d6a5a35"],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByHash","params": ["0xb3b20624f8f0f86eb50dd04688409e5cea4bd02d700bf6e79e9384d47d6a5a35"],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `BLOCK TRANSACTION COUNT` - a hex code of the integer representing the
  number of transactions in the provided block

> BODY

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x50"
}
```
## eth_getBlockTransactionCountByNumber

### v1/jsonrpc/:network/eth_getBlockTransactionCountByNumber

Returns the number of transactions in a block matching the given block
number.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_getBlockTransactionCountByNumber?params=:paramsJSONArray`

> HEADERS

`Content-Type: application/json`

!!! example
     REQUEST PARAMS

- `BLOCK PARAMETER` _[required]_ - an integer block number, or the
  string "latest", "earliest" or "pending", see the
  [default block parameter](https://github.com/ethereum/wiki/wiki/JSON-RPC##the-default-block-parameter)

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/eth_getBlockTransactionCountByNumber --data-urlencode 'params=["latest"]'

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByNumber","params": ["latest"],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByNumber","params": ["latest"],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `BLOCK TRANSACTION COUNT` - a hex code of the integer representing the
  number of transactions in the provided block

> BODY

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x57"
}
```
## eth_getCode

### v1/jsonrpc/:network/eth_getCode

Returns code at a given address.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_getCode?params=:paramsJSONArray`

> HEADERS

`Content-Type: application/json`

!!! example
     REQUEST PARAMS

- `ADDRESS` _[required]_ - a string representing the address (20 bytes)
  of the code
- `BLOCK PARAMETER` _[required]_ - an integer block number, or the
  string "latest", "earliest" or "pending", see the
  [default block parameter](https://github.com/ethereum/wiki/wiki/JSON-RPC##the-default-block-parameter)

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/eth_getCode --data-urlencode 'params=["0x06012c8cf97bead5deae237070f9587f8e7a266d","latest"]'

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_getCode","params": ["0x06012c8cf97bead5deae237070f9587f8e7a266d"],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_getCode","params": ["0x06012c8cf97bead5deae237070f9587f8e7a266d"],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `CODE` - a hex of the code at the given address

> BODY

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x606060............"
}
```
## eth_getLogs

### v1/jsonrpc/:network/eth_getLogs

Returns an array of all logs matching a given filter object.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_getLogs?params=:paramsJSONArray`

> HEADERS

`Content-Type: application/json`

!!! example
     REQUEST PARAMS

- `FILTER OBJECT`
  - `address` _[optional]_ - a string representing the address (20
    bytes) to check for balance
  - `fromBlock` _[optional, default is "latest"]_ - an integer block
    number, or the string "latest", "earliest" or "pending"
  - `toBlock` _[optional, default is "latest"]_ - an integer block
    number, or the string "latest", "earliest" or "pending"
  - `topics`_[optional]_ - Array of 32 Bytes DATA topics. Topics are
    order-dependent.
  - `blockhash`:_[optional, \*\*\_future_\*\*]\_ With the addition of
    EIP-234, `blockHash` will be a new filter option which restricts the
    logs returned to the single block with the 32-byte hash `blockHash`.
    Using `blockHash` is equivalent to `fromBlock` = `toBlock` = the
    block number with hash `blockHash`. If `blockHash` is present in in
    the filter criteria, then neither `fromBlock` nor `toBlock` are
    allowed.

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/eth_getLogs --data-urlencode 'params=[{"topics":["0x241ea03ca20251805084d27d4440371c34a0b85ff108f6bb5611248f73818b80"]}]'

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_getLogs","params":[{"topics":["0x241ea03ca20251805084d27d4440371c34a0b85ff108f6bb5611248f73818b80"]}],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_getLogs","params": ["0x241ea03ca20251805084d27d4440371c34a0b85ff108f6bb5611248f73818b80"],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `LOG OBJECTS` - An array of log objects, or an empty array if nothing
  has changed since last poll.

  - For filters created with `eth_newBlockFilter` the return are block
    hashes of 32 Bytes), e.g. ["0x3454645634534..."]
  - For filters created with `eth_newPendingTransactionFilter` the
    return are transaction hashes of 32 Bytes), e.g.
    ["0x6345343454645..."].
  - For filters created with `eth_newFilter` logs are objects with
    following params:
    - `removed`: true when the log was removed, due to a chain
      reorganization. false if its a valid log.
    - `logIndex`: integer of the log index position in the block. null
      when its pending log.
    - `transactionIndex`: integer of the transactions index position log
      was created from. null when its pending log.
    - `transactionHash`: 32 Bytes - hash of the transactions this log
      was created from. null when its pending log.
    - `blockHash`: 32 Bytes - hash of the block where this log was in.
      null when its pending. null when its pending log.
    - `blockNumber`: the block number where this log was in. null when
      its pending. null when its pending log.
    - `address`: 20 Bytes - address from which this log originated.
    - `data`: contains one or more 32 Bytes non-indexed arguments of the
      log.
    - `topics`: Array of 0 to 4 32 Bytes of indexed log arguments. (In
      solidity: The first topic is the hash of the signature of the
      event (e.g. Deposit(address,bytes32,uint256)), except you declared
      the event with the anonymous specifier.)

> BODY

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "address": "0x1a94fce7ef36bc90959e206ba569a12afbc91ca1",
      "topics": [
        "0x241ea03ca20251805084d27d4440371c34a0b85ff108f6bb5611248f73818b80"
      ],
      "data": "0x0000000000000000000000003e3310720058c51f0de456e273c626cdd35065700000000000000000000000000000000000000000000000000000000000003185000000000000000000000000000000000000000000000000000000000000318200000000000000000000000000000000000000000000000000000000005c2a23",
      "blockNumber": "0x5c29fb",
      "transactionHash": "0x3dc91b98249fa9f2c5c37486a2427a3a7825be240c1c84961dfb3063d9c04d50",
      "transactionIndex": "0x1d",
      "blockHash": "0x7c5a35e9cb3e8ae0e221ab470abae9d446c3a5626ce6689fc777dcffcab52c70",
      "logIndex": "0x1d",
      "removed": false
    },
    {
      "address": "0x06012c8cf97bead5deae237070f9587f8e7a266d",
      "topics": [
        "0x241ea03ca20251805084d27d4440371c34a0b85ff108f6bb5611248f73818b80"
      ],
      "data": "0x00000000000000000000000077ea137625739598666ded665953d26b3d8e374400000000000000000000000000000000000000000000000000000000000749ff00000000000000000000000000000000000000000000000000000000000a749d00000000000000000000000000000000000000000000000000000000005c2a0f",
      "blockNumber": "0x5c29fb",
      "transactionHash": "0x788b1442414cb9c9a36dba2abe250763161a6f6395788a2e808f1b34e92beec1",
      "transactionIndex": "0x54",
      "blockHash": "0x7c5a35e9cb3e8ae0e221ab470abae9d446c3a5626ce6689fc777dcffcab52c70",
      "logIndex": "0x57",
      "removed": false
    }
  ]
}
```
## eth_getStorageAt

### v1/jsonrpc/:network/eth_getStorageAt

Returns the value from a storage position at a given address.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_getStorageAt?params=:paramsJSONArray`

> HEADERS

`Content-Type: application/json`

!!! example
     REQUEST PARAMS

- `ADDRESS` _[required]_ - a string representing the address (20 bytes)
  of the storage
- `STORAGE POSITION` _[required]_ - a hex code of the position in the
  storage
- `BLOCK PARAMETER` _[required]_ - an integer block number, or the
  string "latest", "earliest" or "pending", see the
  [default block parameter](https://github.com/ethereum/wiki/wiki/JSON-RPC##the-default-block-parameter)

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/eth_getStorageAt --data-urlencode 'params=["0x295a70b2de5e3953354a6a8344e616ed314d7251", "0x6661e9d6d8b923d5bbaab1b96e1dd51ff6ea2a93520fdc9eb75d059238b8c5e9", "latest"]'

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_getStorageAt","params": ["0x295a70b2de5e3953354a6a8344e616ed314d7251", "0x6661e9d6d8b923d5bbaab1b96e1dd51ff6ea2a93520fdc9eb75d059238b8c5e9", "latest"],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_getStorageAt","params": ["0x295a70b2de5e3953354a6a8344e616ed314d7251", "0x6661e9d6d8b923d5bbaab1b96e1dd51ff6ea2a93520fdc9eb75d059238b8c5e9", "latest"],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `STORAGE VALUE` - a hex code of the integer indicating the value of
  the storage position at the provided address

> BODY

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x000000000000000000000000000000000000000000000000000000000000162e"
}
```

Calculating the correct position depends on the storage to retrieve.
Consider the following contract deployed at
`0x295a70b2de5e3953354a6a8344e616ed314d7251` by address
`0x391694e7e0b0cce554cb130d723a9d27458f9298`,

```
contract Storage {
    uint pos0;
    mapping(address => uint) pos1;

    function Storage() {
        pos0 = 1234;
        pos1[msg.sender] = 5678;
    }
}
```

Retrieving the value of pos0 is straight forward:

```bash
curl -sL -X POST --data '{"jsonrpc":"2.0", "method": "eth_getStorageAt", "params": ["0x295a70b2de5e3953354a6a8344e616ed314d7251", "0x0", "latest"], "id": 1}' localhost:8545
```

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x00000000000000000000000000000000000000000000000000000000000004d2"
}
```

Retrieving an element of the map is harder. The position of an element
in the map is calculated with:

```js
keccak(LeftPad32(key, 0), LeftPad32(map position, 0))
```

This means to retrieve the storage on
`pos1["0x391694e7e0b0cce554cb130d723a9d27458f9298"]` we need to
calculate the position with:

```js
keccak(
  decodeHex(
    '000000000000000000000000391694e7e0b0cce554cb130d723a9d27458f9298' +
      '0000000000000000000000000000000000000000000000000000000000000001'
  )
);
```

The geth console which comes with the web3 library can be used to make
the calculation:

```js
> var key = "000000000000000000000000391694e7e0b0cce554cb130d723a9d27458f9298" + "0000000000000000000000000000000000000000000000000000000000000001"
undefined
> web3.sha3(key, {"encoding": "hex"})
"0x6661e9d6d8b923d5bbaab1b96e1dd51ff6ea2a93520fdc9eb75d059238b8c5e9"
```

Now to fetch the storage:

```bash
curl -sL -X POST --data '{"jsonrpc":"2.0", "method": "eth_getStorageAt", "params": ["0x295a70b2de5e3953354a6a8344e616ed314d7251", "0x6661e9d6d8b923d5bbaab1b96e1dd51ff6ea2a93520fdc9eb75d059238b8c5e9", "latest"], "id": 1}' localhost:8545
```

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x000000000000000000000000000000000000000000000000000000000000162e"
}
```
## eth_getTransactionByBlockHashAndIndex

## /v1/jsonrpc/:network/eth_getTransactionByBlockHashAndIndex

Returns information about a transaction by block hash and transaction
index position.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_getTransactionByBlockHashAndIndex?params=:paramsJSONArray`

> HEADERS

`Content-Type: application/json`

!!! example
     REQUEST PARAMS

- `BLOCK HASH` _[required]_ - a string representing the hash (32 bytes)
  of a block
- `TRANSACTION INDEX POSITION` _[required]_ - a hex of the integer
  representing the position in the block

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/eth_getTransactionByBlockHashAndIndex --data-urlencode 'params=["0xb3b20624f8f0f86eb50dd04688409e5cea4bd02d700bf6e79e9384d47d6a5a35","0x0"]'

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockHashAndIndex","params": ["0xb3b20624f8f0f86eb50dd04688409e5cea4bd02d700bf6e79e9384d47d6a5a35","0x0"],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_getTransactionByBlockHashAndIndex","params": ["0xb3b20624f8f0f86eb50dd04688409e5cea4bd02d700bf6e79e9384d47d6a5a35","0x0"],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `TRANSACTION` - A transaction object, or null when no transaction was
  found
  - `hash`: 32 Bytes - hash of the transaction.
  - `nonce`: the number of transactions made by the sender prior to this
    one.
  - `blockHash`: 32 Bytes - hash of the block where this transaction was
    in. null when its pending.
  - `blockNumber`: block number where this transaction was in. null when
    its pending.
  - `transactionIndex`: integer of the transactions index position in
    the block. null when its pending.
  - `from`: 20 Bytes - address of the sender.
  - `to`: 20 Bytes - address of the receiver. null when its a contract
    creation transaction.
  - `value`: value transferred in Wei.
  - `gasPrice`: gas price provided by the sender in Wei.
  - `gas`: gas provided by the sender.
  - `input`: the data send along with the transaction.

> BODY

```js
{
    jsonrpc: "2.0",
    id: 1,
    result: {
        blockHash: "0xb3b20624f8f0f86eb50dd04688409e5cea4bd02d700bf6e79e9384d47d6a5a35",
        blockNumber: "0x5bad55",
        from: "0x398137383b3d25c92898c656696e41950e47316b",
        gas: "0x1d45e",
        gasPrice: "0xfa56ea00",
        hash: "0xbb3a336e3f823ec18197f1e13ee875700f08f03e2cab75f0d0b118dabb44cba0",
        input: "0xf7d8c88300000000000000000000000000000000000000000000000000000000000cee6100000000000000000000000000000000000000000000000000000000000ac3e1",
        nonce: "0x18",
        to: "0x06012c8cf97bead5deae237070f9587f8e7a266d",
        transactionIndex: "0x11",
        value: "0x1c6bf526340000",
        v: "0x25",
        r: "0x2a378831cf81d99a3f06a18ae1b6ca366817ab4d88a70053c41d7a8f0368e031",
        s: "0x450d831a05b6e418724436c05c155e0a1b7b921015d0fbc2f667aed709ac4fb5"
    }
}
```
## eth_getTransactionByBlockNumberAndIndex

### v1/jsonrpc/:network/eth_getTransactionByBlockNumberAndIndex

Returns information about a transaction by block number and transaction
index position.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_getTransactionByBlockNumberAndIndex?params=:paramsJSONArray`

> HEADERS

`Content-Type: application/json`

!!! example
     REQUEST PARAMS

- `BLOCK PARAMETER` _[required]_ - an integer block number, or the
  string "latest", "earliest" or "pending", see the
  [default block parameter](https://github.com/ethereum/wiki/wiki/JSON-RPC##the-default-block-parameter)
- `TRANSACTION INDEX POSITION` _[required]_ - a hex of the integer
  representing the position in the block

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/eth_getTransactionByBlockNumberAndIndex --data-urlencode 'params=["0x5BAD55","0x0"]'

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_getTransactionByBlockNumberAndIndex","params": ["0x5BAD55","0x0"],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_getTransactionByBlockNumberAndIndex","params": ["0x5BAD55","0x0"],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `TRANSACTION` - A transaction object, or null when no transaction was
  found
  - `hash`: 32 Bytes - hash of the transaction.
  - `nonce`: the number of transactions made by the sender prior to this
    one.
  - `blockHash`: 32 Bytes - hash of the block where this transaction was
    in. null when its pending.
  - `blockNumber`: block number where this transaction was in. null when
    its pending.
  - `transactionIndex`: integer of the transactions index position in
    the block. null when its pending.
  - `from`: 20 Bytes - address of the sender.
  - `to`: 20 Bytes - address of the receiver. null when its a contract
    creation transaction.
  - `value`: value transferred in Wei.
  - `gasPrice`: gas price provided by the sender in Wei.
  - `gas`: gas provided by the sender.
  - `input`: the data send along with the transaction.

> BODY

```js
{
    jsonrpc: "2.0",
    id: 1,
    result: {
        blockHash: "0xb3b20624f8f0f86eb50dd04688409e5cea4bd02d700bf6e79e9384d47d6a5a35",
        blockNumber: "0x5bad55",
        from: "0x398137383b3d25c92898c656696e41950e47316b",
        gas: "0x1d45e",
        gasPrice: "0xfa56ea00",
        hash: "0xbb3a336e3f823ec18197f1e13ee875700f08f03e2cab75f0d0b118dabb44cba0",
        input: "0xf7d8c88300000000000000000000000000000000000000000000000000000000000cee6100000000000000000000000000000000000000000000000000000000000ac3e1",
        nonce: "0x18",
        to: "0x06012c8cf97bead5deae237070f9587f8e7a266d",
        transactionIndex: "0x11",
        value: "0x1c6bf526340000",
        v: "0x25",
        r: "0x2a378831cf81d99a3f06a18ae1b6ca366817ab4d88a70053c41d7a8f0368e031",
        s: "0x450d831a05b6e418724436c05c155e0a1b7b921015d0fbc2f667aed709ac4fb5"
    }
}
```
## eth_getTransactionByHash

### v1/jsonrpc/:network/eth_getTransactionByHash

Returns information about a transaction for a given hash.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_getTransactionByHash?params=:paramsJSONArray`

> HEADERS

`Content-Type: application/json`

!!! example
     REQUEST PARAMS

- `TRANSACTION HASH` _[required]_ - a string representing the hash (32
  bytes) of a transaction

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/eth_getTransactionByHash --data-urlencode 'params=["0xbb3a336e3f823ec18197f1e13ee875700f08f03e2cab75f0d0b118dabb44cba0"]'

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params": ["0xbb3a336e3f823ec18197f1e13ee875700f08f03e2cab75f0d0b118dabb44cba0"],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_getTransactionByHash","params": ["0xbb3a336e3f823ec18197f1e13ee875700f08f03e2cab75f0d0b118dabb44cba0"],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `TRANSACTION` - A transaction object, or null when no transaction was
  found
  - `hash`: 32 Bytes - hash of the transaction.
  - `nonce`: the number of transactions made by the sender prior to this
    one.
  - `blockHash`: 32 Bytes - hash of the block where this transaction was
    in. null when its pending.
  - `blockNumber`: block number where this transaction was in. null when
    its pending.
  - `transactionIndex`: integer of the transactions index position in
    the block. null when its pending.
  - `from`: 20 Bytes - address of the sender.
  - `to`: 20 Bytes - address of the receiver. null when its a contract
    creation transaction.
  - `value`: value transferred in Wei.
  - `gasPrice`: gas price provided by the sender in Wei.
  - `gas`: gas provided by the sender.
  - `input`: the data send along with the transaction.

> BODY

```js
{
    jsonrpc: "2.0",
    id: 1,
    result: {
        blockHash: "0xb3b20624f8f0f86eb50dd04688409e5cea4bd02d700bf6e79e9384d47d6a5a35",
        blockNumber: "0x5bad55",
        from: "0x398137383b3d25c92898c656696e41950e47316b",
        gas: "0x1d45e",
        gasPrice: "0xfa56ea00",
        hash: "0xbb3a336e3f823ec18197f1e13ee875700f08f03e2cab75f0d0b118dabb44cba0",
        input: "0xf7d8c88300000000000000000000000000000000000000000000000000000000000cee6100000000000000000000000000000000000000000000000000000000000ac3e1",
        nonce: "0x18",
        to: "0x06012c8cf97bead5deae237070f9587f8e7a266d",
        transactionIndex: "0x11",
        value: "0x1c6bf526340000",
        v: "0x25",
        r: "0x2a378831cf81d99a3f06a18ae1b6ca366817ab4d88a70053c41d7a8f0368e031",
        s: "0x450d831a05b6e418724436c05c155e0a1b7b921015d0fbc2f667aed709ac4fb5"
    }
}
```
## eth_getTransactionCount

### v1/jsonrpc/:network/eth_getTransactionCount

Returns the number of transactions sent from an address.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_getTransactionCount?params=:paramsJSONArray`

> HEADERS

`Content-Type: application/json`

!!! example
     REQUEST PARAMS

- `ADDRESS` _[required]_ - a string representing the address (20 bytes)
  to check for transaction count for
- `BLOCK PARAMETER` _[required]_ - an integer block number, or the
  string "latest", "earliest" or "pending", see the
  [default block parameter](https://github.com/ethereum/wiki/wiki/JSON-RPC##the-default-block-parameter)

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/eth_getTransactionCount --data-urlencode 'params=["0xc94770007dda54cF92009BFF0dE90c06F603a09f","latest"]'

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_getTransactionCount","params": ["0xc94770007dda54cF92009BFF0dE90c06F603a09f","latest"],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_getTransactionCount","params": ["0xc94770007dda54cF92009BFF0dE90c06F603a09f","latest"],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `TRANSACTION COUNT` - a hex code of the integer representing the
  number of transactions sent from this address.

> BODY

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x1a"
}
```
## eth_getTransactionReceipt

### v1/jsonrpc/:network/eth_getTransactionReceipt

Returns the receipt of a transaction by transaction hash. **Note** that
the receipt is not available for pending transactions.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_getTransactionReceipt?params=:paramsJSONArray`

> HEADERS

`Content-Type: application/json`

!!! example
     REQUEST PARAMS

- `TRANSACTION HASH` _[required]_ - a string representing the hash (32
  bytes) of a transaction

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/eth_getTransactionReceipt --data-urlencode 'params=["0xbb3a336e3f823ec18197f1e13ee875700f08f03e2cab75f0d0b118dabb44cba0"]'

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_getTransactionReceipt","params": ["0xbb3a336e3f823ec18197f1e13ee875700f08f03e2cab75f0d0b118dabb44cba0"],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_getTransactionReceipt","params": ["0xbb3a336e3f823ec18197f1e13ee875700f08f03e2cab75f0d0b118dabb44cba0"],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `TRANSACTION RECEIPT` - A transaction receipt object, or null when no
  receipt was found:
  - `transactionHash`: 32 Bytes - hash of the transaction.
  - `transactionIndex`: integer of the transactions index position in
    the block.
  - `blockHash`: 32 Bytes - hash of the block where this transaction was
    in.
  - `blockNumber`: block number where this transaction was in.
  - `from`: 20 Bytes - address of the sender.
  - `to`: 20 Bytes - address of the receiver. null when its a contract
    creation transaction.
  - `cumulativeGasUsed`: the total amount of gas used when this
    transaction was executed in the block.
  - `gasUsed`: the amount of gas used by this specific transaction
    alone.
  - `contractAddress`: 20 Bytes - the contract address created, if the
    transaction was a contract creation, otherwise - null.
  - `logs`: Array - Array of log objects, which this transaction
    generated.
  - `logsBloom`: 256 Bytes - Bloom filter for light clients to quickly
    retrieve related logs.

It also returns _either_: - `root` : 32 bytes of post-transaction
stateroot (pre Byzantium) - `status`: either 1 (success) or 0 (failure)

> BODY

```js
{
"id":1,
"jsonrpc":"2.0",
"result": {
     transactionHash: '0xb903239f8543d04b5dc1ba6579132b143087c68db1b2168786408fcbce568238',
     transactionIndex:  '0x1', // 1
     blockNumber: '0xb', // 11
     blockHash: '0xc6ef2fc5426d6ad6fd9e2a26abeab0aa2411b7ab17f30a99d3cb96aed1d1055b',
     cumulativeGasUsed: '0x33bc', // 13244
     gasUsed: '0x4dc', // 1244
     contractAddress: '0xb60e8dd61c5d32be8058bb8eb970870f07233155', // or null, if none was created
     logs: [{
         // logs as returned by getFilterLogs, etc.
     }, ...],
     logsBloom: "0x00...0", // 256 byte bloom filter
     status: '0x1'
  }
}
```
## eth_getUncleByBlockHashAndIndex

### v1/jsonrpc/:network/eth_getUncleByBlockHashAndIndex

Returns information about the 'Uncle' of a block by hash and the Uncle
index position.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_getUncleByBlockHashAndIndex?params=:paramsJSONArray`

> HEADERS

`Content-Type: application/json`

!!! example
     REQUEST PARAMS

- `BLOCK HASH` _[required]_ - a string representing the hash (32 bytes)
  of a block
- `UNCLE INDEX POSITION` _[required]_ - a hex of the integer indicating
  the uncle's index position.

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/eth_getUncleByBlockHashAndIndex --data-urlencode 'params=["0xb3b20624f8f0f86eb50dd04688409e5cea4bd02d700bf6e79e9384d47d6a5a35","0x0"]'

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_getUncleByBlockHashAndIndex","params": ["0xb3b20624f8f0f86eb50dd04688409e5cea4bd02d700bf6e79e9384d47d6a5a35","0x0"],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_getTransactionCount","params": ["0xc94770007dda54cF92009BFF0dE90c06F603a09f","latest"],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `BLOCK` - A block object, or null when no block was found
  - `number`: the block number. null when its pending block.
  - `hash`: 32 Bytes - hash of the block. null when its pending block.
  - `parentHash`: 32 Bytes - hash of the parent block.
  - `nonce`: 8 Bytes - hash of the generated proof-of-work. null when
    its pending block.
  - `sha3Uncles`: 32 Bytes - SHA3 of the uncles data in the block.
  - `logsBloom`: 256 Bytes - the bloom filter for the logs of the block.
    null when its pending block.
  - `transactionsRoot`: 32 Bytes - the root of the transaction trie of
    the block.
  - `stateRoot`: 32 Bytes - the root of the final state trie of the
    block.
  - `receiptsRoot`: 32 Bytes - the root of the receipts trie of the
    block.
  - `miner`: 20 Bytes - the address of the beneficiary to whom the
    mining rewards were given.
  - `difficulty`: integer of the difficulty for this block.
  - `totalDifficulty`: integer of the total difficulty of the chain
    until this block.
  - `extraData`: the "extra data" field of this block.
  - `size`: integer the size of this block in bytes.
  - `gasLimit`: the maximum gas allowed in this block.
  - `gasUsed`: the total used gas by all transactions in this block.
  - `timestamp`: the unix timestamp for when the block was collated.
  - `uncles`: an Array of uncle hashes.

Note: An uncle doesn't contain individual transactions.

> BODY

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "difficulty": "0xbfabcdbd93dda",
    "extraData": "0x737061726b706f6f6c2d636e2d6e6f64652d3132",
    "gasLimit": "0x79f39e",
    "gasUsed": "0x79ccd3",
    "hash": "0xb3b20624f8f0f86eb50dd04688409e5cea4bd02d700bf6e79e9384d47d6a5a35",
    "logsBloom": "0x4848112002a2020aaa0812180045840210020005281600c80104264300080008000491220144461026015300100000128005018401002090a824a4150015410020140400d808440106689b29d0280b1005200007480ca950b15b010908814e01911000054202a020b05880b914642a0000300003010044044082075290283516be82504082003008c4d8d14462a8800c2990c88002a030140180036c220205201860402001014040180002006860810ec0a1100a14144148408118608200060461821802c081000042d0810104a8004510020211c088200420822a082040e10104c00d010064004c122692020c408a1aa2348020445403814002c800888208b1",
    "miner": "0x5a0b54d5dc17e0aadc383d2db43b0a0d3e029c4c",
    "mixHash": "0x3d1fdd16f15aeab72e7db1013b9f034ee33641d92f71c0736beab4e67d34c7a7",
    "nonce": "0x4db7a1c01d8a8072",
    "number": "0x5bad55",
    "parentHash": "0x61a8ad530a8a43e3583f8ec163f773ad370329b2375d66433eb82f005e1d6202",
    "receiptsRoot": "0x5eced534b3d84d3d732ddbc714f5fd51d98a941b28182b6efe6df3a0fe90004b",
    "sha3Uncles": "0x8a562e7634774d3e3a36698ac4915e37fc84a2cd0044cb84fa5d80263d2af4f6",
    "size": "0x41c7",
    "stateRoot": "0xf5208fffa2ba5a3f3a2f64ebd5ca3d098978bedd75f335f56b705d8715ee2305",
    "timestamp": "0x5b541449",
    "totalDifficulty": "0x12ac11391a2f3872fcd",
    "transactionsRoot": "0xf98631e290e88f58a46b7032f025969039aa9b5696498efc76baf436fa69b262",
    "uncles": []
  }
}
```
## eth_getUncleByBlockNumberAndIndex

### v1/jsonrpc/:network/eth_getUncleByBlockNumberAndIndex

Returns information about the 'Uncle' of a block by hash and the Uncle
index position.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_getUncleByBlockNumberAndIndex?params=:paramsJSONArray`

> HEADERS

`Content-Type: application/json`

!!! example
     REQUEST PARAMS

- `BLOCK PARAMETER` _[required]_ - an integer block number, or the
  string "latest", "earliest" or "pending", see the
  [default block parameter](https://github.com/ethereum/wiki/wiki/JSON-RPC##the-default-block-parameter)
- `UNCLE INDEX POSITION` _[required]_ - a hex of the integer indicating
  the uncle's index position.

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/eth_getUncleByBlockNumberAndIndex --data-urlencode 'params=["0x29c","0x0"]'

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_getUncleByBlockNumberAndIndex","params": ["0x29c","0x0"],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_getUncleByBlockNumberAndIndex","params": ["0x29c","0x0"],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `BLOCK` - A block object, or null when no block was found
  - `number`: the block number. null when its pending block.
  - `hash`: 32 Bytes - hash of the block. null when its pending block.
  - `parentHash`: 32 Bytes - hash of the parent block.
  - `nonce`: 8 Bytes - hash of the generated proof-of-work. null when
    its pending block.
  - `sha3Uncles`: 32 Bytes - SHA3 of the uncles data in the block.
  - `logsBloom`: 256 Bytes - the bloom filter for the logs of the block.
    null when its pending block.
  - `transactionsRoot`: 32 Bytes - the root of the transaction trie of
    the block.
  - `stateRoot`: 32 Bytes - the root of the final state trie of the
    block.
  - `receiptsRoot`: 32 Bytes - the root of the receipts trie of the
    block.
  - `miner`: 20 Bytes - the address of the beneficiary to whom the
    mining rewards were given.
  - `difficulty`: integer of the difficulty for this block.
  - `totalDifficulty`: integer of the total difficulty of the chain
    until this block.
  - `extraData`: the "extra data" field of this block.
  - `size`: integer the size of this block in bytes.
  - `gasLimit`: the maximum gas allowed in this block.
  - `gasUsed`: the total used gas by all transactions in this block.
  - `timestamp`: the unix timestamp for when the block was collated.
  - `uncles`: an Array of uncle hashes.

Note: An uncle doesn't contain individual transactions.

> BODY

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "difficulty": "0xbfabcdbd93dda",
    "extraData": "0x737061726b706f6f6c2d636e2d6e6f64652d3132",
    "gasLimit": "0x79f39e",
    "gasUsed": "0x79ccd3",
    "hash": "0xb3b20624f8f0f86eb50dd04688409e5cea4bd02d700bf6e79e9384d47d6a5a35",
    "logsBloom": "0x4848112002a2020aaa0812180045840210020005281600c80104264300080008000491220144461026015300100000128005018401002090a824a4150015410020140400d808440106689b29d0280b1005200007480ca950b15b010908814e01911000054202a020b05880b914642a0000300003010044044082075290283516be82504082003008c4d8d14462a8800c2990c88002a030140180036c220205201860402001014040180002006860810ec0a1100a14144148408118608200060461821802c081000042d0810104a8004510020211c088200420822a082040e10104c00d010064004c122692020c408a1aa2348020445403814002c800888208b1",
    "miner": "0x5a0b54d5dc17e0aadc383d2db43b0a0d3e029c4c",
    "mixHash": "0x3d1fdd16f15aeab72e7db1013b9f034ee33641d92f71c0736beab4e67d34c7a7",
    "nonce": "0x4db7a1c01d8a8072",
    "number": "0x5bad55",
    "parentHash": "0x61a8ad530a8a43e3583f8ec163f773ad370329b2375d66433eb82f005e1d6202",
    "receiptsRoot": "0x5eced534b3d84d3d732ddbc714f5fd51d98a941b28182b6efe6df3a0fe90004b",
    "sha3Uncles": "0x8a562e7634774d3e3a36698ac4915e37fc84a2cd0044cb84fa5d80263d2af4f6",
    "size": "0x41c7",
    "stateRoot": "0xf5208fffa2ba5a3f3a2f64ebd5ca3d098978bedd75f335f56b705d8715ee2305",
    "timestamp": "0x5b541449",
    "totalDifficulty": "0x12ac11391a2f3872fcd",
    "transactionsRoot": "0xf98631e290e88f58a46b7032f025969039aa9b5696498efc76baf436fa69b262",
    "uncles": []
  }
}
```
## eth_getUncleCountByBlockHash

### v1/jsonrpc/:network/eth_getUncleCountByBlockHash

Returns the number of uncles in a block from a block matching the given
block hash.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_getUncleCountByBlockHash?params=:paramsJSONArray`

> HEADERS

`Content-Type: application/json`

!!! example
     REQUEST PARAMS

- `BLOCK HASH` _[required]_ - a string representing the hash (32 bytes)
  of a block

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/eth_getUncleCountByBlockHash --data-urlencode 'params=["0xb3b20624f8f0f86eb50dd04688409e5cea4bd02d700bf6e79e9384d47d6a5a35"]'

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_getUncleCountByBlockHash","params": ["0xb3b20624f8f0f86eb50dd04688409e5cea4bd02d700bf6e79e9384d47d6a5a35"],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_getUncleCountByBlockHash","params": ["0xb3b20624f8f0f86eb50dd04688409e5cea4bd02d700bf6e79e9384d47d6a5a35"],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `BLOCK TRANSACTION COUNT` - a hex code of the integer representing the
  number of uncles in the provided block

> BODY

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x1"
}
```
## eth_getUncleCountByBlockNumber

### v1/jsonrpc/:network/eth_getUncleCountByBlockNumber

Returns the number of uncles in a block from a block matching the given
block number.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_getUncleCountByBlockNumber?params=:paramsJSONArray`

> HEADERS

`Content-Type: application/json`

!!! example
     REQUEST PARAMS

- `BLOCK PARAMETER` _[required]_ - an integer block number, or the
  string "latest", "earliest" or "pending", see the
  [default block parameter](https://github.com/ethereum/wiki/wiki/JSON-RPC##the-default-block-parameter)

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/eth_getUncleCountByBlockNumber --data-urlencode 'params=["latest"]'

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_getUncleCountByBlockNumber","params": ["latest"],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_getUncleCountByBlockNumber","params": ["latest"],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `BLOCK TRANSACTION COUNT` - a hex code of the integer representing the
  number of uncles in the provided block

> BODY

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x57"
}
```
## eth_getWork

### v1/jsonrpc/:network/eth_getWork

Returns the hash of the current block, the seedHash, and the boundary
condition to be met ("target").

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_getWork`

> HEADERS

`Content-Type: application/json`

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/eth_getWork

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_getWork","params": [],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_getWork","params": [],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `WORK ARRAY`
  - 32 Bytes - current block header pow-hash
  - 32 Bytes - the seed hash used for the DAG.
  - 32 Bytes - the boundary condition ("target"), 2^256 / difficulty.

> BODY

```js
{
  "id":1,
  "jsonrpc":"2.0",
  "result": [
      "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
      "0x5EED00000000000000000000000000005EED0000000000000000000000000000",
      "0xd1ff1c01710000000000000000000000d1ff1c01710000000000000000000000"
    ]
}
```
## eth_hashrate

### v1/jsonrpc/:network/eth_hashrate

Returns the number of hashes per second that the node is mining with.
Only applicable when the node is mining.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_hashrate`

> HEADERS

`Content-Type: application/json`

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/eth_hashrate

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_hashrate","params": [],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_hashrate","params": [],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `HASHRATE` - a hex code of an integer representing the number of
  hashes per second.

> BODY

```js
{
    jsonrpc: "2.0",
    id: 1,
    result: "0x38a"
}
```
## eth_mining

### v1/jsonrpc/:network/eth_mining

Returns true if client is actively mining new blocks.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_mining`

> HEADERS

`Content-Type: application/json`

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/eth_mining

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_mining","params": [],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_mining","params": [],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `IS MINING FLAG` - a boolean indicating if the client is mining

> BODY

```js
{
    jsonrpc: "2.0",
    id: 1,
    result: true
}
```
## eth_protocolVersion

### v1/jsonrpc/:network/eth_protocolVersion

Returns the current ethereum protocol version.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_protocolVersion`

> HEADERS

`Content-Type: application/json`

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/eth_protocolVersion

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_protocolVersion","params": [],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_protocolVersion","params": [],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `PROTOCOL VERSION` - a string indicating the current ethereum protocol
  version

> BODY

```js
{
    jsonrpc: "2.0",
    id: 1,
    result: "54""
}
```
## eth_syncing

### v1/jsonrpc/:network/eth_syncing

Returns an object with data about the sync status or false.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/eth_syncing`

> HEADERS

`Content-Type: application/json`

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/eth_syncing

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"eth_syncing","params": [],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"eth_syncing","params": [],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `SYNC STATUS` - a boolean as false **only** when not syncing
- `SYNC BLOCKS` i. `startingBlock` - a hexcode of the integer indicating
  the block at which the import started (will only be reset, after the
  sync reached his head) ii. `currentBlock` - a hexcode of the integer
  indicating the current block, same as eth_blockNumber iii.
  `highestBlock` - a hexcode of the integer indicating the highest block

> BODY

```js
\\ When not syncing
{
    jsonrpc: "2.0",
    id: 1,
    result: "1"
}

\\ When syncing
{
    "id":1,
    "jsonrpc": "2.0",
    "result": {
        startingBlock: '0x384',
        currentBlock: '0x386',
        highestBlock: '0x454'
    }
}
```
## net_listening

### v1/jsonrpc/:network/net_listening

Returns true if client is actively listening for network connections.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/net_listening`

> HEADERS

`Content-Type: application/json`

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/net_listening

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"net_listening","params": [],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"net_listening","params": [],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `LISTENING FLAG` - a boolean indicating whether the client is actively
  listening for network connections

> BODY

```js
{
    jsonrpc: "2.0",
    id: 1,
    result: true
}
```
## net_peerCount

### v1/jsonrpc/:network/net_peerCount

Returns the number of peers currently connected to the client.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/net_peerCount`

> HEADERS

`Content-Type: application/json`

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/net_peerCount

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"net_peerCount","params": [],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"net_peerCount","params": [],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `PEER COUNT` - integer of the number of connected peers.

> BODY

```js
{
    jsonrpc: "2.0",
    id: 1,
    result: "0x64"
}
```
## net_version

### v1/jsonrpc/:network/net_version

Returns the current network id.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/net_version`

> HEADERS

`Content-Type: application/json`

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/net_version

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"net_version","params": [],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"net_version","params": [],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `NETWORK ID` - a string representing the current network id.

> BODY

```js
{
    jsonrpc: "2.0",
    id: 1,
    result: "1"
}
```
## method

### v1/jsonrpc/network/method

A request using an "HTTP GET-compatible" (non-state-changing) JSON-RPC
method. Most Ethereum JSON-RPC methods can be described in this way,
since they query the blockchain for various pieces of information. Use
the `/v1/jsonrpc/{network}/methods` endpoint to get the list of
permitted methods.

###### GET

`GET https://api.sushirelay.com/v1/jsonrpc/network/method?params=`

| Parameters |                                                                                                                                                                |        |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| network    | Ethereum network in lowercase. Possible values: `api.staging., `ropsten`, `kovan`, `rinkeby`                                                                       | Enum   |
| method     | JSON-RPC method. Use the `/v1/jsonrpc/{network}/methods` endpoint to get the list of permitted methods.                                                        | String |
| params     | This is the params field that would normally be part of the JSON-RPC POST body. Use the exact same format. If it's omitted, it will default to an empty array. | Array  |

###### Request

```
curl -sL --include \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
  'https://api.sushirelay.com/v1/jsonrpc/{network}/{method}?params='
```

###### Response

| Attributes                              |          |        |
| --------------------------------------- | -------- | ------ |
| `jsonrpc`                               | required | enum   |
| JSON-RPC version                        | `2.0`    | string |
| `id`                                    | required | number |
| JSON-RPC request ID                     |          |        |
| `result`                                |          | string |
| JSON-RPC result (can also be an object) |          |        |

######## JSON-RPC Response

`200`

> HEADERS

`Content-Type:application/json`

> BODY

```
{
  "jsonrpc": "2.0",
  "id": -5294191,
  "result": "sed dolor eu ullamco"
}
```

**JSON Schema**

```
{
  "type": "object",
  "properties": {
    "jsonrpc": {
      "type": "string",
      "description": "JSON-RPC version",
      "enum": [
        "2.0"
      ]
    },
    "id": {
      "type": "integer",
      "description": "JSON-RPC request ID"
    },
    "result": {
      "type": "string",
      "description": "JSON-RPC result (can also be an object)"
    }
  },
  "required": [
    "jsonrpc",
    "id"
  ]
}
```

###### Response

Bad JSON in `params` query parameter

`400`

> HEADERS

`Content-Type:application/json`

###### Response

JSON-RPC method is not a valid GET method

`404`

> HEADERS

`Content-Type:application/json`

###### Response

Server error

`500`

> HEADERS

`Content-Type:application/json`

###### Response

Ethereum client error

`502`

> HEADERS

`Content-Type:application/json`
## methods

### v1/jsonrpc/network/methods

The JSON-RPC methods supported by the `/v1/jsonrpc/{network}/{method}`
(GET) and `/v1/jsonrpc/{network}` (POST) endpoints.

###### GET

`GET https://api.sushirelay.com/v1/jsonrpc/network/methods`

###### Parameters

| Attributes |                                                                                          |      |
| ---------- | ---------------------------------------------------------------------------------------- | ---- |
| network    | Ethereum network in lowercase. Possible values: `api.staging., `ropsten`, `kovan`, `rinkeby` | enum |

###### Request

```
curl -sL --include \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
  'https://api.sushirelay.com/v1/jsonrpc/{network}/methods'
```

###### Response

| Attributes                                                                       |          |       |
| -------------------------------------------------------------------------------- | -------- | ----- |
| `get`                                                                            | required | array |
| List of methods supported by the `/v1/jsonrpc/{network}/{method}` endpoint (GET) | `string` | 0     |
| `post`                                                                           | required | array |
| List of methods supported by the `/v1/jsonrpc/{network}` endpoint (POST)         | `string` | 0     |

######## Methods Response

`200`

> HEADERS

`Content-Type:application/json`

> BODY

```
{
  "get": [
    "culpa ipsum sunt dolor",
    "labore in",
    "sunt pariatur eiusmod",
    "nostrud mollit"
  ],
  "post": [
    "aute aliqua elit",
    "eu tempor nulla Excepteur eiusmod",
    "ipsum et officia laborum"
  ]
}
```

**JSON Schema**

```
{
  "type": "object",
  "properties": {
    "get": {
      "type": "array",
      "description": "List of methods supported by the /v1/jsonrpc/{network}/{method} endpoint (GET)",
      "items": {
        "type": "string"
      }
    },
    "post": {
      "type": "array",
      "description": "List of methods supported by the /v1/jsonrpc/{network} endpoint (POST)",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "get",
    "post"
  ]
}
```

###### Response

Server error

`500`

> HEADERS

`Content-Type:application/json`
## symbol

### v1/jsonrpc/symbol

Get pricing (ticker) data for various currency pairs (fiat, crypto, and
tokens) using data from several exchanges. This endpoint shows the price
at the exchange with the most volume for the symbol. Use the
`/v1/ticker/symbols` endpoint for the full list of supported symbols.

###### GET

`GET https://api.sushirelay.com/v1/ticker/symbol`

| Parameters |                               |        |
| ---------- | ----------------------------- | ------ |
| `symbol`   | Ticker symbol (currency pair) | String |

###### Request

```
curl -sL --include \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
  'https://api.sushirelay.com/v1/ticker/{symbol}'
```

###### Response

| Attributes      |                                             |
| --------------- | ------------------------------------------- |
| `base`          | string                                      |
|                 | Currency pair base                          |
| `quote`         | string                                      |
|                 | Currency pair quote                         |
| `bid`           | number                                      |
|                 | Bid at the exchange with the most volume    |
| `ask`           | number                                      |
|                 | Ask at the exchange with most volume        |
| `exchange`      | string                                      |
|                 | The exchange with the most volume           |
| `volume`        | number                                      |
|                 | Volume at the exchange with the most volume |
| `num_exchanges` | number                                      |
|                 | Number of exchanges queried                 |
| `total_volume`  | number                                      |
|                 | Total volume across all exchanges queried   |
| `timestamp`     | number                                      |
|                 | Unix timestamp                              |

######## Ticker Response

`200`

> HEADERS

`Content-Type:application/json`
## full

### v1/ticker/symbol/full

Get pricing (ticker) data for various currency pairs (fiat, crypto, and
tokens) using data from several exchanges. This endpoint shows the price
at various exchanges where the symbol is traded. Use the
`/v1/ticker/symbols` endpoint for the full list of supported symbols.

###### GET

`GET https://api.sushirelay.com/v1/ticker/symbol/full`

| Parameters |                              |        |
| ---------- | ---------------------------- | ------ |
| Symbol     | Ticker symbol (currency pair | string |

###### Request

```
curl -sL --include \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
  'https://api.sushirelay.com/v1/ticker/{symbol}/full'
```

###### Response

| Attributes                           |                     |
| ------------------------------------ | ------------------- |
| `base`                               | string              |
|                                      | Currency pair base  |
| `quote`                              | string              |
|                                      | Currency pair quote |
| `tickers`                            | array               |
| List of tickers at various exchanges |                     |
| `object`                             | 0                   |
| `bid`                                | number              |
| `ask`                                | number              |
| `exchange`                           | string              |
| `volume`                             | number              |
| `timestamp | number                  |

######## Full ticker Response

`200`

> HEADERS

`Content-Type:application/json`
## symbols

### v1/ticker/symbols

Get a list of supported symbols (currency pairs), including fiat,
crypto, and tokens

###### GET

`GET https://api.sushirelay.com/v1/ticker/symbols`

###### Request

```
curl -sL --include \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
  'https://api.sushirelay.com/v1/ticker/symbols'
```

###### Response

| Attributes                                 |          |       |
| ------------------------------------------ | -------- | ----- |
| `symbols`                                  |          | array |
| List of supported symbols (currency pairs) | `string` | 0     |

######## Symbols Response

`200`

> HEADERS

`Content-Type:application/json`
## v1 Blacklist

### v1/blacklist

Return a blacklist of phishing sites. This list is maintained by GitHub
user 409H at
[https://github.com/409H/EtherAddressLookup/blob/master/blacklists/domains.json](https://github.com/409H/EtherAddressLookup/blob/master/blacklists/domains.json).

###### GET

`GET https://api.sushirelay.com/v1/blacklist`

###### Request

```
curl -sL --include \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
  'https://api.sushirelay.com/v1/blacklist'
```

###### Response

| Attributes |     |
| ---------- | --- |
| string     | 0   |

######## List of blacklisted phishing domains

`200`

> HEADERS

`Content-Type:application/json`

> BODY

```
[
  "quis esse ut",
  "dolor quis",
  "dolore culpa et",
  "laboris Ut ut nisi commodo",
  "l"
]
```

**JSON Schema**

```
{
  "type": "array",
  "items": {
    "type": "string"
  }
}
```

######## Response

Github is having issues

`502`

> HEADERS

`Content-Type:application/json`
## v2 Blacklist

### v2/blacklist

Return a blacklist of phishing sites, as well as a whitelist and a
fuzzylist. This list is maintained by the MetaMask project at
[https://github.com/MetaMask/eth-phishing-detect/blob/master/src/config.json](https://github.com/MetaMask/eth-phishing-detect/blob/master/src/config.json).

###### GET

`GET https://api.sushirelay.com/v2/blacklist`

###### Request

```
curl -sL --include \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
  'https://api.sushirelay.com/v2/blacklist'
```

###### Response

| Attributes  |          |           |
| ----------- | -------- | --------- |
| `version`   | required | number    |
|             |          | Version   |
| `tolerance` | required | number    |
|             |          | Tolerance |
| `fuzzylist` | required | array     |
| Fuzzylist   | string   | 0         |
| `whitelist` | required | array     |
| Whitelist   | string   | 0         |
| `blacklist` | required | array     |
| Blacklist   | string   | 0         |

######## Phishing blacklist, whitelist, and fuzzylist

`200`

> HEADERS

`Content-Type:application/json`

> BODY

```
{
  "version": 38611173,
  "tolerance": 49572925,
  "fuzzylist": [
    "eiusmod anim mollit Ut",
    "minim et ea ex"
  ],
  "whitelist": [
    "irure Duis",
    "officia minim voluptate cillum ullamco",
    "nostrud aliquip",
    "ex in sint velit",
    "Excepteur veniam fugi"
  ],
  "blacklist": [
    "do in tempor consectet"
  ]
}
```

**JSON Schema**

```
{
  "type": "object",
  "properties": {
    "version": {
      "type": "integer",
      "description": "Version"
    },
    "tolerance": {
      "type": "integer",
      "description": "Tolerance"
    },
    "fuzzylist": {
      "description": "Fuzzylist",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "whitelist": {
      "description": "Whitelist",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "blacklist": {
      "description": "Blacklist",
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "version",
    "tolerance",
    "fuzzylist",
    "whitelist",
    "blacklist"
  ]
}
```

######## Response

Github is having issues

`502`

> HEADERS

`Content-Type:application/json`
## web3_clientVersion

### v1/jsonrpc/:network/web3_clientVersion

Returns the current client version.

> REQUEST

`GET https://api.sushirelay.com/v1/jsonrpc/:network/web3_clientVersion`

> HEADERS

`Content-Type: application/json`

!!! example

```bash

curl -sL -G https://api.sushirelay.com/v1/web3_clientVersion

// HTTP POST
curl -sL https://api.staging.sushirelay.com/ \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"jsonrpc":"2.0","method":"web3_clientVersion","params": [],"id":1}'

// WEBSOCKETS
>wscat -c wss://api.staging.sushirelay.com/ws
>{"jsonrpc":"2.0","method":"web3_clientVersion","params": [],"id":1}
```

> RESPONSE

> RESULT FIELDS

- `STRING` - The current client version

> BODY

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "Geth/v1.8.6-patched-leveldb-8818ab0b/linux-amd64/go1.9.2"
}
```
