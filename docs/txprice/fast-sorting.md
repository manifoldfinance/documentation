# EIP-1559 Transaction Pool for Fast Sorting

## TL;DL
- The idea of an EIP-1559 transaction pool for fast sorting.
- Computational complexity
    - Add a transaction in $O(\log n)$
    - Sort transactions when basefee changes in $O(k \log n)$
    - Pop the most profitable transaction in $O(\log n)$
    - Produce a block in $O(m \log n)$
    - $n$: The number of transactions in a txpool
    - $k$: The number of transactions where the miner bribe varies with basefee
    - $m$: The number of transactions in a block
- Implementation: https://github.com/minaminao/eip1559txpool

## Background

### Transaction Pool in First-price Auction
In the current fee market, which is a first-price auction mechanism, one strategy to optimize the miner &#39;s fee revenue is to put transactions into a block in a `gas_price` order.

_NOTE: Strictly speaking, although nonce also needs to be considered, it is not be considered in the following sections because it does not affect the computational complexity._

#### Vector Implementation
If a txpool is implemented as a vector, it must be sorted in `gas_price` order before creating a block. The computational complexity of sorting is $O(n \log n)$, that of adding a transaction is $O(1)$, and that of deleting a transaction is $O(n)$. However, transaction deletion can be done to $O(1)$ by lazy evaluation.

#### Heap Implementation
If a txpool is implemented as a heap, there will be no need to sort. Adding a transaction takes $O(\log n)$, and deleting a transaction takes $O(n \log n)$. However, transaction deletion can be done to $O(\log n)$ by lazy evaluation.

#### Self-balancing Binary Search Tree (SBST) Implementation
If a txpool is implemented as an [SBST](https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree), there will be no need to sort as well as a heap implementation. Adding a transaction takes $O(\log n)$, and deleting a transaction takes $O(\log n)$.

#### Summary of Computational Complexity in First-price Auction

|Operation|Vector|Heap|SBST|
|-|-|-|-|
|Add a transaction| $O(1)$|$O(\log n)$|$O(\log n)$|
|Delete a transaction| $O(1)$ by lazy evalutaion|$O(\log n)$ by lazy evalutaion|$O(\log n)$|
|Pop the most profitable transaction| $O(1)$ after sorting|$O(\log n)$|$O(\log n)$|
|Sort transactions| $O(n \log n)$|-|-|

The space complexity is $O(n)$.

### Transaction Pool in EIP-1559
An EIP-1559 transaction has the parameters `base_fee` and `fee_cap`. The `miner_bribe` is `min(fee_cap - base_fee, max_miner_bribe)`, and it is optimal to put transactions into a block in the order of `miner_bribe`.
However, `miner_bribe` depends on `base_fee`. A fast transaction pool is non-trivial.

According to https://hackmd.io/@adietrichs/1559-transaction-sorting , when `base_fee` changes, there are two transaction sets: one in which `miner_bribe` changes and one in which `miner_bribe` does not change. Let us denote these sets as $D$ and $S$, respectively. It is known that the order of transactions belonging to $D$ and that to $S$ does not change before and after the `base_fee` change.

By using this property well, an efficient transaction pool can be constructed.

## Proposed Txpool

### Architecture
The txpool is consists of three SBSTs.

1. Static state transactions SBST (`sbst_static`)
   - Include all $S$ transactions.
   - Include condition: `fee_cap - max_miner_bribe &gt;= base_fee`
   - Key: `(max_miner_bribe, transaction_hash)`
   - Value: `transaction`
2. Dynamic state transactions SBST (`sbst_dynamic`)
   - Include all $D$ transactions.
   - Include condition: `fee_cap - max_miner_bribe &lt;base_fee`
   - Key: `(fee_cap, transaction_hash)`
   - Value: `transaction`
3. State decision SBST (`sbst_decision`)
   - Include all transactions.
   - Key: `fee_cap - max_miner_bribe`
   - Value: `transaction`

_NOTE: I have included the implementations below, but they are implemented in C++ because Python does not have SBST in the standard library. Other language implementations such as Python and Rust are WIP._

### Computational Complexity of Proposed Txpool

|Operation|Vector|SBST (Proposed)|
|-|-|-|-|
|Add a transaction| $O(1)$|$O(\log n)$|
|Delete a transaction| $O(1)$ by lazy evalutaion|$O(\log n)$|
|Pop the most profitable transaction| $O(1)$ after sorting|$O(\log n)$|
|Sort transactions when basefee changes | $O(n \log n)$|$O(k \log n)$|

The space complexity is $O(n)$.

### Pop The Most Profitable Transaction: $O(\log n)$
The most profitable transaction is either of the following two.
1. $tx_{S,\max}$: The most profitable transaction in $S$
2. $tx_{D,\max}$: The most profitable transaction in $D$

$tx_{S,\max}$ is the one with the highest `max_miner_bribe` in $S$. `sbst_static` is sorted in order of `max_miner_bribe` because its key is `(max_miner_bribe, transaction_hash)`. Hence, finding and deleting $tx_{S,\max}$ is possible with $O(\log n)$ due to the property of SBST.

$tx_{D,\max}$ is the one with the highest `fee_cap` in $D$. `sbst_dynamic` is sorted in order of `fee_cap` because its key is `(fee_cap, transaction_hash)`. Hence, finding and deleting $tx_{D,\max}$ is possible with $O(\log n)$ due to the property of SBST.

By comparing the revenue of $tx_{S,\max}$ and $tx_{D,\max}$, we can select the most profitable transaction out of the entire transaction set.

Also, we have to delete the transaction from `sbst_decision` (explained later) in $O(\log n)$.

Therefore, the overall computational complexity is $O(\log n)$.

**Implementation**
I left it out of the explanation, but I inserted a `-fee_cap` between the first and second elements of the key. The reason is that when there are transactions with the same `max_miner_bribe`, it is better to take the one with the smaller `fee_cap`. When the next `base_fee` is high, transactions with a small `fee_cap` may have a smaller revenue.

```cpp
Tx pop_most_profitable_tx() {
    Tx tx;
    assert(sbst_decision.size() &gt;0);
    if(sbst_static.size() == 0) {
        tx = sbst_dynamic.rbegin()-&gt;second;
        sbst_dynamic.erase(prev(sbst_dynamic.end()));
    } else if(sbst_dynamic.size() == 0) {
        tx = sbst_static.rbegin()-&gt;second;
        sbst_static.erase(prev(sbst_static.end()));
    } else {
        Tx tx_static = sbst_static.rbegin()-&gt;second;
        Tx tx_dynamic = sbst_dynamic.rbegin()-&gt;second;

        if(tx_static.miner_bribe(base_fee) &gt;tx_dynamic.miner_bribe(base_fee)) {
            tx = tx_static;
            sbst_static.erase(prev(sbst_static.end()));
        } else {
            tx = tx_dynamic;
            sbst_dynamic.erase(prev(sbst_dynamic.end()));
        }
    }

    sbst_decision.erase(sbst_decision.find(
        Key(tx.fee_cap - tx.max_miner_bribe, -tx.fee_cap, tx.hash)));
    return tx;
}
```

### Produce Block: $O(m \log n)$
Suppose we select the $m$ most profitable transactions to create a block. Since selecting the most profitable transaction runs in $O(\log n)$, the block production runs in $O(m \log n)$.

### Add Transaction: $O(\log n)$

If `fee_cap - base_fee &gt;= max_miner_bribe`, we add the transaction to `sbst_static` in $O(\log n)$.
If `fee_cap - base_fee &lt;max_miner_bribe`, we add the transaction to `sbst_dynamic` in $O(\log n)$.

It is also added to `sbst_decision` (explained later) in $O(\log n)$.

Therefore, the overall computational complexity is $O(\log n)$.

**Implementation**
```cpp
void add_tx(Tx tx) {
    if(tx.fee_cap - base_fee &gt;= tx.max_miner_bribe) {
        sbst_static.emplace(Key(tx.max_miner_bribe, -tx.fee_cap, tx.hash),
                            tx);
    } else {
        sbst_dynamic.emplace(Key(tx.fee_cap, -tx.fee_cap, tx.hash), tx);
    }
    sbst_decision.emplace(
        Key(tx.fee_cap - tx.max_miner_bribe, -tx.fee_cap, tx.hash), tx);
}
```

### Sort Transactions When Basefee Changes: $O(k \log n)$

When the base_fee changes, do the following.
Let us denote the previous basefee by `prev_base_fee`.

#### If `prev_base_fee` &lt;`base_fee`
We need to move the transaction that moves from $S$ to $D$ from `sbst_static` to `sbst_dynamic`.

The conditions of the transactions are as follows.
- `fee_cap - max_miner_bribe &gt;= prev_base_fee`
- `fee_cap - max_miner_bribe &lt;base_fee`

To check the conditions, `sbst_decision` is used. The key of `sbst_decision` is `fee_cap - max_miner_bribe`. Thus, by performing a binary search by `prev_base_fee` and then by `base_fee`, the transaction set to be moved can be determined in $O(\log n)$.

The move takes $O(\log n)$ to delete a transaction from `sbst_static` and add the transaction to `sbst_dynamic`.

If the number of its moving transactions is $k$, then the total complexity is $O(k \log n)$. `k` is small if the change of basefee is small.


**Implementation**
```cpp
auto left_tx =
    sbst_decision.lower_bound(Key(prev_base_fee, -INT32_MAX, 0));
auto right_tx =
    sbst_decision.lower_bound(Key(base_fee, -INT32_MAX, 0));
for(auto pointer = left_tx; pointer != right_tx; pointer++) {
    Tx tx = pointer-&gt;second;
    if(tx.fee_cap - tx.max_miner_bribe &gt;= prev_base_fee) {
        sbst_static.erase(sbst_static.find(
            Key(tx.max_miner_bribe, -tx.fee_cap, tx.hash)));
        add_tx(tx);
    }
}
```

#### If `base_fee` &lt;`prev_base_fee`
We need to move the transaction that moves from $D$ to $S$ from `sbst_dynamic` to `sbst_static`. The computational complexity is $O(k \log n)$ as above.

**Implementation**
```cpp
auto left_tx =
    sbst_decision.lower_bound(Key(base_fee, -INT32_MAX, 0));
auto right_tx =
    sbst_decision.lower_bound(Key(prev_base_fee, -INT32_MAX, 0));
for(auto pointer = left_tx; pointer != right_tx; pointer++) {
    Tx tx = pointer-&gt;second;
    if(tx.fee_cap - tx.max_miner_bribe &lt;prev_base_fee) {
        sbst_dynamic.erase(sbst_dynamic.find(
            Key(tx.fee_cap, -tx.fee_cap, tx.hash)));
        add_tx(tx);
    }
}
```

## References
- https://hackmd.io/@timbeiko/1559-tx-pool-mgmt
