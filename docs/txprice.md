# TXPrice.com

[toc]


## Overview

> api.txprice.com

An overview of the new typed transaction envelope system


## API


Type0 and Type2 Transactions
Type0 transactions (Pre EIP-1559) should utilize the Price number under each confidence level.

Type2 transactions (EIP-1559) should utilize the values for maxPriorityFeePerGas (also known as the "tip") and maxFeePerGas .


### Glossary 

**maxPrice**
Highest priced transaction in the mempool

**currentBlockNumber**
Block number at the time of prediction

**msSinceLastBlock**
Milliseconds since the last block was mined relative to when data was computed

**blockNumber**
Block this prediction is for

**baseFeePerGas**
Base fee per gas for current block in gwei. (Only type2 transactions Post EIP-1559 have this value and it's burned by the network upon transaction success).
estimatedTransactionCount
Number of items we estimate will be included in next block based on mempool snapshot

**confidence**
0-99 likelihood the next block will contain a transaction with a gas price >= to the listed price

**Price**
Price in Gwei (used for type0 transactions: Pre EIP-1559)

**maxPriorityFeePerGas**
Max priority fee per gas in gwei also known as the "tip" (used for type2 transactions: EIP-1559)

**maxFeePerGas**
Max fee per gas in gwei (used for type2 transactions: EIP-1559). Our current max fee heuristic is Base Fee * 2 + Priority Fee. This is to protect against a 'rapid' rise in the base fee while your transaction fee is pending. In most cases, the actual transaction fee will approximate Base Fee + Priority Fee.


## Client Implementation Details

London Hardfork implementation details

### Go-Ethereum (Geth)

> Edit: Geth's gas price oracle retrieves the cheapest 3 transactions from the past X blocks, and uses the 60th percentile as the suggestion for the price. The 60th percentile ensures we're aiming for inclusion in 2-3 blocks, whereas looking at the minimums ensures we're trying to push prices downward instead of up.
> [reference]: https://github.com/ethereum/pm/issues/328#issuecomment-853234014


The Gas Price Oracle ('GPO') tracks the 60th percentile of the minimum tip paid over the last 20 blocks, looking at the 3 transactions with the smallest tip for each block. 

`eth_maxPriorityFeePerGas` returns GPO while

`eth_gasPrice` returns GPO + current basefee

The gas price oracle internally calculates the priority fees actually paid by the transactions. For the eth_gasPrice call, we will return the estimated priority fee + 1 basefee (which will essentially be the "current" full gasPrice that we estimate pre-London). For eth_maxPriorityFeePerGas, we return the estimated priority fee. The user needs to set the maxFeePerGas either manually based on the tip, or Geth defaults to the priority fee + 2x baseFee.





Gas price recommendations now modeled as Priority Fees
optional field #1: suggestBaseFee
optional field #2: gasUsedRatio

`suggestBaseFee` may be added to the returned safe/proposed/fast priority fee recommendations to derive a suggested MaxFeePerGas.

`gasUsedRatio` can be used to evaluate how busy the network is, allowing you to adjust your parameters accordingly.



### EIP-1559 JSON RPC Changes

The [eth1.0-apis repository](https://github.com/ethereum/eth1.0-apis) is not versioned (yet!) and hence it can be hard to track the various changes introduced by EIP-1559. Here is a list to make this easier. 

### 1559 Summary

EIP-1559 introduces a new transaction type (`0x02`) and adds a field to the block header (`baseFeePerGas`). At a high level, anything which either returns a transaction or a block will be affected post-1559. 

### API Changes

The following APIs calls are changed with the introduction of EIP-1559:

* `eth_call` 
    * This API has the most substantial behavior modifications. They are described [here](https://github.com/ethereum/go-ethereum/pull/23027). 
* `eth_getBlockBy*` endpoints
    * A new field `baseFeePerGas` is added on post-London blocks
* `eth_getRawTransaction*` endpoints 
    * RLP encoded EIP-1559 transactions may be returned post-London
* `eth_getTransactionBy*` endpoints
    * `gasPrice` now interpreted as `maxFeePerGas` before the tx is mined and `effectiveGasPrice` after it's mined (for EIP-1559 txs). This field is deprecated (no EOL set yet) for EIP-1559 transactions.
    * EIP-1559 transactions will have two new fields, `maxPriorityFeePerGas` and `maxFeePerGas`
* `eth_getTransactionReceipt`
    * A new field `effectiveGasPrice` is added to the receipt. Pre-London, it is equal to the transaction's `gasPrice`. Post-London, it is equal to the actual gas price paid for inclusion. This calculation differs depending if the transaction is an EIP-1559 transaction or not.
* `eth_getUncleBy*` endpoints
    * A new field `baseFeePerGas` is added on post-London blocks
* `eth_sendTransaction`
    * EIP-1559 transaction fields `maxPriorityFeePergas` and `maxFeePerGas` are now supported. Clients will calculate reasonable values for these fields if they're omitted. Legacy transactions can still be sent by specifying a `gasPrice`
* `eth_estimateGas`
    * Either `gasPrice` or `maxFeePerGas` and `maxPriorityFeePerGas` are now required. Before, it was okay to omit `gasPrice` because it could be filled with `0`. Now the `baseFeePerGas` must be taken into account, and the fee payment must be large enough to cover the base fee.
* `eth_sendRawTransaction`
    * This method now supports RLP encoded EIP-1559 transactions

Note:`*` at the end of a name refers to all variations of this API call. 

Additionally, the following JSON RPC endpoint was introduced:

* `eth_feeHistory`, which returns historical data about transaction fees. More information on it can be found [here](https://github.com/zsfelfoldi/feehistory).
    * Maybe mention that geth will have a breaking change for this endpoint to support hex-encoded values vs. integers? (https://github.com/ethereum/go-ethereum/pull/23239)

