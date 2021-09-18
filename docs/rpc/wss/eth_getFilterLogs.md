# eth_getFilterLogs

Returns an array of all logs matching filter with given id.

### REQUEST PARAMS

- `FILTER OBJECT`
  - `fromBlock`_[optional, default: "latest"]_ Integer block number, or
    "latest" for the last mined block or "pending", "earliest" for not
    yet mined transactions.
  - `toBlock`_[optional, default: "latest"]_ Integer block number, or
    "latest" for the last mined block or "pending", "earliest" for not
    yet mined transactions.
  - `address`: _[optional]_ (20 Bytes) Contract address or a list of
    addresses from which logs should originate.
  - `topics`: _[optional]_ Array of 32 Bytes DATA topics. Topics are
    order-dependent. Each topic can also be an array of DATA with "or"
    options.
  - blockhash: _[optional, future]_ With the addition of EIP-234,
    blockHash will be a new filter option which restricts the logs
    returned to the single block with the 32-byte hash blockHash. Using
    blockHash is equivalent to fromBlock = toBlock = the block number
    with hash blockHash. If blockHash is present in in the filter
    criteria, then neither fromBlock nor toBlock are allowed.

#### EXAMPLE

```bash
>wscat -c wss://mainnet.backbonecabal.xyz/ws

>{"jsonrpc":"2.0","method":"eth_getFilterLogs","params":["0xfe704947a3cd3ca12541458a4321c869"],"id":73}
```

### RESPONSE

#### RESULT FIELDS

- `LOG OBJECT ARRAY` - Array of log objects, or an empty array if
  nothing has changed since last poll.
  - For filters created with eth_newBlockFilter the return are block
    hashes (32 Bytes), e.g. ["0x3454645634534..."].
  - For filters created with eth_newPendingTransactionFilter the return
    are transaction hashes (32 Bytes), e.g. ["0x6345343454645..."].
  - For filters created with eth_newFilter logs are objects with
    following params:
- `removed`: true when the log was removed, due to a chain
  reorganization. false if its a valid log.
- `logIndex`: integer of the log index position in the block. null when
  its pending log.
- `transactionIndex`: integer of the transactions index position log was
  created from. null when its pending log.
- `transactionHash`: 32 Bytes - hash of the transactions this log was
  created from. null when its pending log.
- `blockHash`: 32 Bytes - hash of the block where this log was in. null
  when its pending. null when its pending log.
- `blockNumber`: the block number where this log was in. null when its
  pending. null when its pending log.
- `address`: 20 Bytes - address from which this log originated.
- `data`: DATA - contains the non-indexed arguments of the log.
- `topics`: Array of DATA - Array of 0 to 4 32 Bytes DATA of indexed log
  arguments. (In solidity: The first topic is the hash of the signature
  of the event (e.g. Deposit(address,bytes32,uint256)), except you
  declared the event with the anonymous specifier.)

#### BODY

```json
{
    "jsonrpc": "2.0",
    "id": 73,
    "result": [{
        "address": "0xb5a5f22694352c15b00323844ad545abb2b11028",
        "blockHash": "0x99e8663c7b6d8bba3c7627a17d774238eae3e793dee30008debb2699666657de",
        "blockNumber": "0x5d12ab",
        "data": "0x0000000000000000000000000000000000000000000000a247d7a2955b61d000",
        "logIndex": "0x0",
        "removed": false,
        "topics": ["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef", "0x000000000000000000000000bdc0afe57b8e9468aa95396da2ab2063e595f37e", "0x0000000000000000000000007503e090dc2b64a88f034fb45e247cbd82b8741e"],
        "transactionHash": "0xa74c2432c9cf7dbb875a385a2411fd8f13ca9ec12216864b1a1ead3c99de99cd",
        "transactionIndex": "0x3"
    }, {
        "address": "0xe38165c9f6deb144afc9c32c206b024817e1496d",
        "blockHash": "0x99e8663c7b6d8bba3c7627a17d774238eae3e793dee30008debb2699666657de",
        "blockNumber": "0x5d12ab",
        "data": "0x0000000000000000000000000000000000000000000000000000000025c6b720",
        "logIndex": "0x3",
        "removed": false,
        "topics": ["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef", "0x00000000000000000000000080e73e47173b2d00b531bf83bc39e710157125c3", "0x0000000000000000000000008f6cc93795969e5bbbf07c66dfee7d41ad24f1ef"],
        "transactionHash": "0x9e8f1cb1facb9a11a1cf947634053a0b2d557399f926b12127aa10497a2f0153",
        "transactionIndex": "0x5"
    }
}
```
