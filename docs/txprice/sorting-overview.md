# EIP-1559 Transaction Sorting: Overview

**tl;dr** Transaction comparison and sorting in the mempool is used for two main problems: On the upper end, finding the most attractive transactions during mining; and on the lower end, identifying the least promising transactions for eviction. For legacy transactions, both problems use the `gas_price` as the relevant decision metric and max-/min-heaps as efficient partially sorted data structures. For EIP-1559, these problems require different metrics. For mining, a (somewhat more complex) explicit solution seems feasible. For eviction, heuristics are needed that are both efficiently implementable and robust under many different base fee paradigms.

---

As a proposal for a new transaction pricing model, [EIP-1559](https://eips.ethereum.org/EIPS/eip-1559) will change many aspects of Ethereum clients &#39;behavior. One of the areas most impacted is the mempool, i.e. the part of a client responsible for handling in-flight transactions on their way from users to miners.

Tim Beiko [recently listed 4 open questions](https://hackmd.io/@timbeiko/1559-tx-pool-mgmt) around mempool handling of EIP-1559 transactions, with three of them closely tied to the problem of transaction sorting. Here we aim to give a brief overview of different aspects of mempool transaction sorting and how they are impacted by EIP-1559.

*This document is mainly intended to serve as a basis of discussion for the [upcoming implementers &#39;call](https://github.com/ethereum/pm/issues/226). It will be followed up by a more comprehensive writeup. As the Quilt team has only recently joined the EIP-1559 effort, it is very possible that we made incorrect assumption or overlooked relevant existing work. Feedback in these cases and in general is much appreciated!*

## Mempool Sorting

There are two main distinct sorting problems: Miners, when picking transactions for a new block,  want to get the currently most profitable transactions. And all nodes, when reaching the maximum mempool capacity, want to get the transactions with the lowest inclusion chance, that they can evict to make room for more promising transactions. Both of these problems consist of two sub-problems: The choice of a comparison metric and the choice of an efficient data structure for transactions, based on that metric.

For current (legacy) transactions, both the high-end sorting for mining and the low-end sorting for eviction rely on the `gas_price` transaction field as their comparison metric. This in turn also leads to the same choice of data structure, namely a (partially-sorted) max-heap for mining and a (partially-sorted) min-heap for eviction.

For EIP-1559 transactions, the situation is more complex. For mining, the relevant metric is the current effective transaction tip, i.e. the amount per gas the transaction is willing to pay to the miner for inclusion. For eviction however, this is not the correct metric to use. As the effective transaction tip depends on the current protocol `base_fee`, the relative order of transaction changes over time and is not an accurate heuristic for inclusion chance. Thus, a more elaborate metric, ideally close to &#34;estimated average future effective transaction tip &#34;, is necessary.

The change in metrics also requires different data structures for EIP-1559 transaction sorting. For mining, a solution based on a slightly more complex heap-approach [is in the process of being prototyped](https://github.com/adietrichs/1559Simulations). For eviction, the choice of data structure depends on the choice of metric. In particular, this imposes an additional constraint on the choice of metric: Find a metric that is accurate enough under a vast variety of `base_fee` regimes, while also being efficiently implementable.

The third sorting-related problem mentioned by Tim is that of transaction replacement (for transactions with the same sender and nonce). It is similar to that of eviction, with an added focus on DOS protection and predicatability. For EIP-1559 transactions, a decision rule similar to the `min_price_bump` for legacy transactions can be devised.

## Current Situation

### Transaction Format

|Name       |Description|
|-----------|-----------|
|`gas_price`|The fee the transaction is willing to pay (per gas used)|

While there are additional transaction fields relevant for mempool handling, this is the one relevant for sorting and also the one that sets legacy transactions apart from their EIP-1559 counterparts.

It is important to note that the payment willingness as indicated by `gas_price` for any given transaction is a static value, i.e. cannot depend on the overall current gas price level. Thus, the relative order of transaction always remains the same, as illustrated in this plot:

![](https://i.imgur.com/NXsCoOq.png)

A mempool holding all of these transactions can be certain that C &gt;E &gt;A &gt;B &gt;D will always  correctly describe the relative payment willingness of the transactions. It is thus possible to create and maintain efficient (partially) sorted views of the transactions in mempool.

### Mining

When assembling a new block, miners need a way to find the most profitable transactions to include. They can do so by querying the mempool for the upper end of (currently executable) pending transactions. For this purpose, the mempool maintains a (partially sorted) max-heap of its transactions, allowing efficient queries for the highest paying transactions.

*Note: As these heaps are only needed for mining (see below for those used by all nodes), they are usually created and maintained by the mining module directly and not technically part of the mempool. For simplicity we subsume these parts under &#34;mempool &#34;.*

### All Nodes

As nodes only have a limited amount of memory to work with, they cannot keep an unlimited amount of transactions in their mempools. That means that once that limit is reached, they need a way to decide whether to keep additional incoming transactions and if so, which transactions to drop in their favor.

Nodes ideally want to prioritize transactions by chance of future on-chain inclusion, dropping those with the least chances of ever being included by a miner. As the relative attractiveness of transactions for miners only depends on their `gas_price`, it remains constant over time. Thus, the transactions currently least attractive will also have the lowest chances of eventual inclusion.

When choosing which transactions to drop, the mempool thus need to be able to find the transactions with the lowest `gas_price`. It does so by maintaining a (partially sorted) min-heap of its transactions.

Decisions on transaction replacement (i.e. when the mempool already holds a transaction from the same sender with the same nonce) are done with the same `gas_price` metric. An additional minimum price bump is enforecd to ensure DOS protection.

## Changes Under EIP-1559

### Transaction Format

|Name     |Description|
|---------|-----------|
|`fee_cap`|The total fee the transaction is willing to pay (per gas used)|
|`tip`    |The maximum share of the total fee the transaction is willing to pay to the miner (per gas used)|

Under EIP-1559, transaction fees are no longer fully paid to the miner. Instead, there is a protocol-wide and dynamically adjusted `base_fee` (per gas used) that each transaction is required to burn. In addition, transactions can tip the miner to increase their chance of timely inclusion. Instead of specifying a `gas_price`, transactions now set a `tip` amount and a `fee_cap`. If `base_fee + tip` exceeds `fee_cap`, the tip is reduced to `fee_cap - base_fee`.

As the effective payment to the miner can thus be lower than the tip specified in the transaction, miner expectations for any given transation is no longer static. As an important consequence, the relative order of transaction is also no longer static, as illustrated by this plot:

![](https://i.imgur.com/aV22Drb.png)


This example mirrors the total payment willingness of the legacy example above, but sets varying values for `tip`. The plot shows the effective tip for each transaction as a function of the current `base_fee`. As one can see, the lines now intersect, indicating `base_fee` levels at which the relative order of the specific two transactions flips. This behavior has been [noted in the past](https://github.com/ethereum/rig/blob/master/eip1559/notes-call3.md#important-client-strategies) when analysing the properties of EIP-1559 transactions.

Each transaction can be in one of two states for any given `base_fee`:
While `base_fee &lt;= fee_cap - tip`, the transaction is willing to pay a constant `tip` to the miner (*static state*). Transactions that set `tip == fee_cap` (Tx D in the plot) are never in this state.
Once `base_fee &gt;fee_cap - tip`, the miner payment ability of a transaction is in a *dynamic range*, decreasing further with increasing `base_fee`.

### Mining

As before, miners need a way to find the most profitable transactions to include into a new block and thus want to be able to query the mempool for the current upper end of pending transactions. Given the current `base_fee`, a transaction &#39;s profitability for the miner is given by its effective tip. Thus, the sorting in this context is not a problem of the right metric, but only of efficient implementation.

As the relative order of transactions can change over time, the simple single-heap approach for legacy transactions is no longer sufficient. However, the order does stay constant for transactions within both the static and dynamic state respectively, changing only for those that leave either of these states due to a change in the `base_fee` (that crosses `fee_cap - tip`). Thus, it seems plausible that a fairly simple new sorting mechanism can be devised relying on this observation and adjusting the sorting on `base_fee` changes. Work on the prototyping of such an mechanism has been started and can be found [here](https://github.com/adietrichs/1559Simulations).

### All Nodes

For eviction, nodes still want to prioritize transactions by chance of future on-chain inclusion. Under EIP-1559 however, the relative attraciveness of transactions as given by their effective tip depends on the `base_fee`. As the `base_fee` is adjusted over time, its future behavior is unknown. Thus, a precise ordering by chance of future inclusion is impossible. Instead, the goal has to be to find a heuristic for estimation of this chance that is both efficiently computable and robust (i.e. reasonably precise) under many different `base fee` paradigms.

In addition to the current `base_fee`, the heuristic could also take into account empirical data from recent history, e.g. `base_fee` volatility over the last 24h. However, this area still needs further work. Importantly, it is unclear what the practical limits for per-block (i.e. every time the `base_fee` changes) are and how severely those restrict the choice of heuristic.

For transaction replacement, in principle the same heuristic could be used. However, to make replacement predictable for users (as a replacement is usually a conscious effort by a user), a simple rule that enforces improved mining attractiveness and incorporates DOS protection is preferable. A simple example would be
```
new_tx.fee_cap &gt;= old_tx.fee_cap + min_bump &amp;&amp;new_tx.tip &gt;= old_tx.tip + min_bump
where min_bump = 0.1 * old_tx.tip
```
but alternative approaches are possible.
