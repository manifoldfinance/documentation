# Formulas and Calculations

<!--
@version: v0.1.0
@date: 08/11/2021
@license: CC-ND-NC-2.5
@note: naive implementation, expect changes
-->

[TOC]

## Rebate Calculations

_Note_: naive implementation, expect changes

bundleCost = mev bribe + bundleTxs[1,2,...]

gasAllowance = mev bribe - bundleTxs[1,2,...]

BundleTransactionGas[1,2,...] = Individual Gas Cost

BundleId = The Block Number (or hash?) in which the bundle was included

max_gasRebate = (BundleId(BundleTransactionGas[1,2,...]))

## Transaction Parameters

`targetBlockNumber`: block number at which this bundle is valid

`minTimestamp`: minimum timestamp at which this bundle is valid (inclusive)

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

This formula derives the effective gas price of the bundle by summing up all
payments to coinbase as well as gas fees _except_ for the gas fees of
transactions that have been seen in the mempool.

The gas fees of mempool transactions are deducted to prevent "stuffing" bundles
with high gas price transactions from the mempool to inflate the effective gas
price.

## Appendix

**Expected Execution Price** $(( E [P])$ When a liquidity taker issues a trade
on \(X / Y,\) the taker wishes to execute the trade with the expected execution
price \(E [P]\) (based on the AMM algorithm and \(X / Y\) state), given the
expected slippage.

**Execution Price** \((P):\) During the time difference between a liquidity
taker issuing a transaction, and the transaction being executed (e.g. mined in a
block), the state of the AMM market \(X / Y\) may change. This state change may
induce unexpected slippage resulting in an execution price \(P \neq E [P]\).

**Atomic arbitrage profit (aarb)**: is defined as the gain of two atomically
executed arbitrage trades $TA$ and $TB$ on exchange $A$ and $B$.

**Non-atomic arbitrage profit (naarb)**: is defined as the arbitrage gain, if
$TA$ executes first, and $TB$’s execution follows after $i$ intermediary
transactions.

**Holding value ($Hv$)**: is defined as the change in the averaged price of the
given asset pair on the two exchanges, which represents the asset value change
during the non-atomic execution period.

**Borrowing Capacity ($Bc$)**: Refers to the total value that a borrower is
allowed to request from a lending pool, given its collateral amount. For each
collateral asset 𝑖 of a borrower, its borrowing capacity is defined in
Equation 3.

$$ Bc =∑︁ 𝑉 𝑎𝑙𝑢𝑒 𝑜𝑓 𝐶𝑜𝑙𝑙𝑎𝑡𝑒𝑟al × LT𝑖 $$

**Health Factor ($Hhf$)**: The health factor measures the collateralization
status of a position, defined as the ratio of the borrowing capacity over the
outstanding debts (cf. Equation 4).

$$ Hhf = BC / ∑︁ 𝑉𝑎𝑙𝑢𝑒 𝑜𝑓 𝐷𝑒𝑏𝑡t $$

**MVI**: Mininumal Profitable Viable Input

**Unexpected Price Slippage **\((P- E [P]):\) is the difference between \(P\)
and \(E [P]\).

**Unexpected Slippage Rate** \(\left(\frac{P- E [P]}{ E [P]}\right):\) is
\(\quad\) the unexpected slippage over the expected price.

**Expected Execution Price**: $E [P]$ When a liquidity taker issues a trade on
$X / Y,$ the taker wishes to execute the trade with the expected execution price
$E [P]$ (based on the AMM algorithm and $X / Y$ state), given the expected
slippage.

**Execution Price**: $P$ During the time difference between a liquidity taker
issuing a transaction, and the transaction being executed (e.g. mined in a
block), the state of the AMM market $X / Y$ may change. This state change may
induce unexpected slippage resulting in an execution price $P \neq E [P]$.

**Unexpected Price Slippage**: $P- E [P]$ is the difference between $P$ and
$E [P]$. Unexpected Slippage Rate $\left(\frac{P- E [P]}{ E [P]}\right)$ is
$\quad$ the unexpected slippage over the expected price.
