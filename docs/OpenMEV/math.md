# OpenMEV Mechanics and Formulas

> Overview of OpenMEV Applications

## SushiSwap 

Rebating Transaction Costs

Rebating a transaction is determined by:

- Is the function that is called in the transaction eligible?

  - By tracking contract function calls we are better able to provide
    observability in the rebating process, we can also coordinate with teams
    wishing to provide more incentives for specific actions and behaviors

- If yes, what is the percentage that can be rebated?

  - This percentage value is a protocol value that can be adjusted

- What is the transaction cost for the eligible transaction?

  - Thi s the value that the end user utilized in submitting their transaction.

- Calculate the Gas Reporting Index value

  - This uses the gas pricing information from api.txprice.com to calculate the
    gas pricing information to be used in calculating the rebate amount for your
    transaction

- Calculate the rebate amount from the bundle profit surplus
  - We take how much profit the arbitrage made and split it among all eligible
    trades within that bundle

## Rebate Mechanism

1. Eligible transactions are rebated based on the 80th confidence interval for
   gas estimation pricing.

2. This is proportionally distributed based on transactional weight. _Note: a
   naive formula would consider pairings, then slippage tolerance and finally
   transactional amount_

3. The amount of compensation is the fees less to miners and network
   operational transactional costs.

4. Compensation payouts occur no later than a half hour

### Contract Function Eligibility

|                    **$function_calls**                    | **%eligible** |
| :-------------------------------------------------------: | :-----------: |
|                 swapExactTokensForTokens                  |      100      |
|                   swapExactTokensForETH                   |      100      |
|                   swapExactETHForTokens                   |      100      |
|                   swapETHForExactTokens                   |      100      |
|                       getAmountsOut                       |     null      |
|                      addLiquidityETH                      |      50       |
|                       addLiquidity                        |      50       |
|                 swapTokensForExactTokens                  |      100      |
|                       getAmountOut                        |     null      |
|               removeLiquidityETHWithPermit                |      100      |
|                   swapTokensForExactETH                   |      100      |
|                 removeLiquidityWithPermit                 |      25       |
|                    removeLiquidityETH                     |      25       |
|                      removeLiquidity                      |      25       |
|                          factory                          |     null      |
|    swapExactTokensForETHSupportingFeeOnTransferTokens     |       #       |
|   swapExactTokensForTokensSupportingFeeOnTransferTokens   |       #       |
|                       getAmountsIn                        |     null      |
|                           WETH                            |     null      |
|    swapExactETHForTokensSupportingFeeOnTransferTokens     |       #       |
|                        getAmountIn                        |     null      |
| removeLiquidityETHWithPermitSupportingFeeOnTransferTokens |       #       |
|      removeLiquidityETHSupportingFeeOnTransferTokens      |       #       |


### Rebate Calculations

*Note*: naive implementation, expect changes

bundleCost = mev bribe + bundleTxs[1,2,...]

gasAllowance =  mev bribe - bundleTxs[1,2,...]

BundleTransactionGas[1,2,...] = Individual Gas Cost

BundleId = The Block Number (or hash?) in which the bundle was included

max_gasRebate = (BundleId(BundleTransactionGas[1,2,...]))

### Transaction Parameters

`targetBlockNumber`: block number at which this bundle is valid

`minTimestamp`:  minimum timestamp at which this bundle is valid (inclusive)

 `maxTimestamp`: maximum timestamp at which this bundle is valid (inclusive)


### MEV Bundle pricing formula

Our costs for bundling transactions for MEV are as follows:

Formula for calculating the pricing of a bundle (flashbots):

$$s_{v0.2} = \frac{\Delta_{coinbase} + \sum_{T\in U}g_Tp_T - \sum_{T\in M \cap U}g_Tp_T}{\sum_{T\in U}g_T}$$

$s$: bundle $U$ _score_ used to sort bundles.
$U$: ordered list of transactions $T$ in a bundle.
$M$: set of transactions $T$ in the mempool.
$g_{T}$: _gas used_ by transaction $T$.
$p_{T}$: _gas price_ of transaction $T$.
$\Delta_{coinbase}$: coinbase difference from direct payment.

### Explanation

This formula derives the effective gas price of the bundle by summing up all payments to coinbase as well as gas fees *except* for the gas fees of transactions that have been seen in the mempool.

The gas fees of mempool transactions are deducted to prevent "stuffing" bundles with high gas price transactions from the mempool to inflate the effective gas price.


## Transactions Status Coding

| Status        | Description                                                                                                                                                                                                                                                                                                                       |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QUEUED        | The default state when initially creating a transaction during the initial API call. This indicates that this transaction is waiting to be picked up by a background worker.                                                                                                                                                      |
| PROCESSING    | A background worker has started to process this transaction.                                                                                                                                                                                                                                                                      |
| FUNDING       | An auxiliary funding transaction is being initiated (this only applies to non-Ether transactions).                                                                                                                                                                                                                                |
| FUNDED        | An auxiliary funding transaction was successful (this only applies to non-Ether transactions).                                                                                                                                                                                                                                    |
| BROADCASTING  | The transaction is being announced to the blockchain network nodes.                                                                                                                                                                                                                                                               |
| BROADCASTED   | The transaction was successfully announced to the blockchain network nodes.                                                                                                                                                                                                                                                       |
| PENDING       | The transaction is "pending" / "in the mempool", i.e. known to (some) blockchain network nodes, and awaiting inclusion/mining into a block.                                                                                                                                                                                       |
| CONFIRMING    | The transaction was mined into a block, but not enough subsequent blocks have yet been mined to consider that transaction "safe" / confirmed.                                                                                                                                                                                     |
| CONFIRMED     | The transaction was mined into a block and enough subsequent blocks have been mined to consider that transaction "safe" / confirmed.                                                                                                                                                                                              |
| FAILED        | The transaction was mined into a block, but the execution of its smart contract code failed. Several reasons are possible, most notably "out of gas". The transaction is still included in a block because its gas is still awarded to the miner who attempted to execute it.                                                     |
| REJECTED      | The transaction was mined into a block but was rejected during the execution of its smart contract code. Several reasons are possible, most notably Solidity's require() assertions not being satisfied. The transaction is still included in a block because it's gas is still awarded to the miner who attempted to execute it. |
| UNPROCESSABLE | An unrecoverable error occurred which prevents us from getting this transaction onto the blockchain. We have given up (or the customer requested us not to retry).                                                                                                                                                                |
| RETRYING      | A temporary/recoverable error occurred, and this transaction was re-queued as to try getting this transaction onto the blockchain at a later time. This state is more or less equivalent to QUEUED, but its name is more telling.                                                                                                 |
