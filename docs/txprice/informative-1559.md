# How I Think About EIP-1559


[adietrichs, author & source, hackmd](https://hackmd.io/@adietrichs/eip-1559)

*With all the activity this week around the Ethereum London hard fork, I have noticed people having a wide range of ways to think about EIP-1559, the hard fork &#39;s main protocol change. So I thought I would try to outline my own perspective on the EIP here, to ideally help integrate these different lines of thinking. If you strongly disagree with any point made here, come find me over on twitter at [@adietrichs](https://twitter.com/adietrichs) - I would love to hear from you!*

[TOC]

*See Conclusion for a tl;dr.*

## The Status Quo

In order to understand the motivation and implications of EIP-1559, we first have to look at the current-day situation in Ethereum. The parts of the overall blockchain mechanism relevant to us are those of transaction pricing and inclusion, as these are where the main changes of the EIP take place. In the first section we will formalize this as the market for transaction inclusion, and distinguish it from the recently emerged separate market of transaction ordering (à la flashbots).

We will then have a look at this market, developing a simple model for it as a fixed-supply iterated first-price auction.

Finally, we will have a closer look at the kinds of miner revenue identified in that model, and examine in what way those can be considered forms of miner extractable value (MEV).

### Distinction between Markets for Inclusion and Ordering

Like most blockchains Ethereum has a fee payment system directly built into the protocol. First, every transaction specifies a price per gas it is willing to pay. Then, when added into a block, the sending account is charged for the total cost of transaction execution, i.e. `total_fee = gas_price * gas_consumed`. Users send a fee with their transactions to incentivize miners to include those transactions into a block, which thus creates a market for transaction inclusion.

Starting a few years ago, specialized use case patterns emerged that necessitated control not only over general inclusion of transactions, but over their precise position within a block. The most prominent example of this is front-running, where a user targets another user &#39;s in-flight transaction, aiming to have their transaction included right before the target one. By setting up the chain state in a precise and use case specific way (e.g. move an exchange market in a desired direction), the user can then profit off their knowledge of the subsequent transaction &#39;s effect.

Initially, these ordering-specific use cases relied solely on the same built-in transaction fee mechanism, as miner sorting algorithms are generally predictable and thus can be influenced with some success. However, with the space getting progressively more competitive, this soon led to considerable amounts of wasted fees for transactions in the incorrect block position. Flashbots was started as an intermediary service between users and miners to address this problem and create a proper market for transaction ordering. This market is mostly independent of the one for transaction inclusion and is barely touched by the changes introduced in EIP-1559. We will thus in the following limit our focus on the market for transaction inclusion. We will also for simplicity ignore any residual ordering-related activity still being facilitated via the native transaction fee mechanism.

Note also that the term &#34;miner extractable value &#34;(MEV) was coined to refer to value accruing to miners based on their control over secondary aspects of block creation such as transaction ordering. In the following we will explore how the more traditional miner revenue for transaction inclusion can also be considered to be a form of MEV. However, this is not a common use of the terminology and is thus best understood as a thought experiment limited to the context of this writeup.

### Fixed-Supply Iterated First-Price Auction

To understand the nature of the market for transaction inclusion, it is useful to look at a diagram of the relevant supply and demand curves:

![diagram of the supply and demand curves for transaction inclusion on Ethereum before EIP-1559](https://i.imgur.com/xsw69CA.png)
*Diagram of the pre-1559 short-term supply and demand curves of the transaction inclusion market, in the case of full blocks. Note that this diagram includes multiple simplifications as a tradeoff between accuracy and legibility. Note also that if you aren &#39;t used to the concept of supply &amp;demand curves and how to interpret such diagrams, it might be useful to stop for a bit and try to really understand what you are looking at (including the following sections for context), as most of the remaining writeup is directly based on it.*

The somewhat unusual shape of this diagram is my attempt of illustrating the particularities of the blockchain context. The best way to think about the market is as a **fixed-supply iterated first-price** auction. The following sections will go through these three attributes individually and relate them to the diagram above:

#### Fixed-Supply

Like most blockchains, Ethereum has a hard limit for the size of new blocks, set in the form of a block gas limit. Consequently, the &#34;supply for block space &#34;(i.e. the amount of transactions miners are willing to include into a block) is fixed at that limit. This is illustrated by the vertical part of the supply curve in the diagram.

As a nuance, transaction inclusion is not entirely free for miners. In particular, adding transactions makes the overall block bigger and thus slower to propagate through the network, in turn slightly increasing the uncle risk for the miner. For that reasons, miners usually set a minimum gas price (geth defaults to 1 Gwei) and reject transactions below that threshold, even if this leads to non-full blocks. Consequently, the supply curve has a horizontal part at the bottom, slightly above 0.

#### First-Price

The demand side of the market consist of the payment willingness of users as revealed by the gas prices of their transactions and follows a typical demand curve (labeled &#34;revealed demand &#34;in the diagram - for &#34;true demand &#34;see next section). Its intersection with the supply curve indicates the market clearing gas price for transaction inclusion (indicated as the dashed horizontal line).

Under the current system, transactions have to pay the full gas price they specify, even if it is above that market clearing value. This property is comparable to that of a first-price auction (or more generally any situation with perfect price discrimination). Consequently, most users end up over-paying for inclusion of their transactions.

#### Iterated

The last relevant aspect of the market is its iterated nature. Because blocks are created every 15(-ish) seconds, transactions have multiple chances of inclusion. Users also have the chance to bump the gas price if the initial price turns out to have been insufficient. Furthermore, market clearing prices of prior blocks give a rough indication of the required gas price for inclusion.

For these reasons, many users don &#39;t initially set the gas price to their maximum payment willingness. This leads to a gap between the observed (revealed) demand and the theoretical true demand. To illustrate this point, the diagram also includes a &#34;true demand &#34;curve above the revealed one.

### Types of Miner Revenue

One neat aspect of supply / demand diagrams is that the area between the curves naturally represents consumer and producer surplus, with the split dependent on the extent of price discrimination. (*To illustrate that point: The height under the revealed demand curve indicates the gas prices (eth/gas) paid by included transactions, and the width of the supply curve indicates the block gas limit (gas). So the &#34;product &#34;of the two indicates the total eth paid in tx fees to the miner.*)

In our case we have perfect price discrimination, so both areas under the curve (cyan and purple) represent miner surplus. As this is pure miner profit and fits the general definition of &#34;value accruing to miners based on their control over block creation &#34;, it can make sense to call that surplus MEV. The nature of these two areas however turns out to be quite distinct, as outlined in the following sections.

Note that the (orange) bottom area also represents miner revenue. However, as it reflects the &#34;production cost &#34;of filling the block with transactions, it is not part of their profit.

Note also that the topmost (green) area does not represent any money actually paid, but rather the theoretical user surplus resulting from their lower revealed gas price preferences. This area is included only for illustration purposes and not further considered in the following.


#### &#34;Base MEV &#34;(purple)

This portion of the MEV represents the miner profit in a uniform-price auction setting. If every transaction were to only pay the market clearing gas price, this is the profit the miner would still be left with.

This is what people refer to when they point out that EIP-1559 will not make Ethereum transactions cheaper: There is no way of reducing the size of the purple area in the diagram, as it is a natural consequence of any market equilibrium with fixed supply and high demand.

#### &#34;First-Price MEV &#34;(cyan)

This portion of the MEV represents the additional miner profit stemming from their ability to do perfect price discrimination.

This is what people refer to when they point out that the current fee market over-charges many users.


## EIP-1559

Having looked at the current transaction inclusion market in some detail, we are now ready to turn to the changes introduced by EIP-1559. We will first look at the history of the EIP (including both the motivation for it and its design), before then constructing a fee market model for it analogous to the one above. We will contrast the two models and see how EIP-1559 effects the forms of MEV identified above. Finally, we will also look at base fee payments as the first ever form of protocol revenue, one of the EIP &#39;s side effects.

### History

#### Motivation

Equipped with the model of the current fee market, it is now worthwhile to revisit the [original proposal by Vitalik](https://ethresear.ch/t/first-and-second-price-auctions-and-improved-transaction-fee-markets/2410) of what would later become EIP-1559. As laid out by Vitalik, the motivation was to turn the first-price auction system into a uniform-price one (or at least make as much headway as possible to that end). In other words, the goal was to remove or minimize the &#34;first-price MEV &#34;(the cyan area) in our first diagram.

#### Design

To facilitate this goal, some sort of in-protocol oracle for the market clearing inclusion price was necessary. The proposed mechanism was to enshrine a minimum gas price (called base fee) into the protocol. Simultaneously, the maximum block size would be doubled, using a simple [proportional controller](https://en.wikipedia.org/wiki/Proportional_control) for the base fee to target 50% filled blocks. Simply put: Because most blocks would now no longer be completely full (with not enough transactions willing to pay the base fee), the size of a block can be used as an indication for whether (and how much) the current base fee level is too high or too low, relative to the &#34;ideal fee level &#34;that would lead to exactly 50% filled blocks. The base fee could then be adjusted appropriately, and its current level used as the desired price oracle.

Note that this mechanism is only possible due to the fact that the primary bottleneck for the Ethereum block size is the long-term cost imposed by transactions (i.e. mostly state growth). While there are also short-term limiting factors for block size (such as propagation and verification time), those are more forgiving and thus allow for this 2x increase of the maximum block size. This is also the reason for the higher throughput of chains like the Binance Smart Chain that only optimize for short-term throughput, without concern about long-term effects.

With this price oracle, we can now turn the first-price auction system into a uniform-price one, by only charging transactions the base fee. As this makes the base fee a possible target for miner manipulation, it turns out that it is important to no longer have the base fee payment go directly to them, as they could otherwise add extra transactions to their blocks for free, distorting the base fee adjustment signal (see Vitalik &#39;s post for details). As the base fee is legible by the protocol, this can easily be avoided by collecting the base fee from users directly, but not forwarding it to the miner. This effectively turns these payments into direct protocol revenue (the first of its kind for Ethereum!). See the section below for further discussion.

While the mechanism as described almost works, it lacks one important piece: An incentive for miners to include transactions at all. As they don &#39;t receive the base fee payment, they lack the cost offset from our earlier model. So for the final version of EIP-1559, a new fee type (the priority fee) is added to transactions, with a first-price auction reinstated for that fee part only. Given that the minimum priority fee is fairly small and well understood, this small regression back to a first-price system is however of limited significance.

### Fee Market Model

With all the elements of the EIP in place, we can now construct an updated fee market model:

![diagram of the supply and demand curves for transaction inclusion on Ethereum after EIP-1559](https://i.imgur.com/sIov6Yw.png)

*Diagram of the post-1559 short-term supply and demand curves of the transaction inclusion market, for the case of a non-full (but slightly over the 1/2 target) block.*

The main changes in comparison to the original diagram come from the introduction of the base fee, the doubling of the block size limit, and the new effective gas price payment method.

#### Base Fee

The base fee now acts as a price floor, with miner revenue only applied on top. Consequently, the supply curve is raised by that amount.

#### Block Size Limit

With a doubled block size limit, the supply curve is now also drawn out twice as wide. For most blocks, this leads to a demand level insufficient to fill the whole block, as indicated by the new intersection between supply and revealed demand in the horizontal part of the supply curve.

In the situation displayed in the diagram, the miner would be able to fill 2/3 of the block, which would in turn lead to a slight base fee increase for the next block.

#### Effective Gas Price

The last change is the introduction of the effective gas price payment method. Instead of a gas price, transactions specify a max fee and a max priority fee (both per gas). Instead of paying the full max fee, the transaction only pays the base fee and the full max priority fee (though capped by the overall max fee). This leads to a mostly flat effective price curve in the diagram, only slightly curved to reflect the first-price priority fee auction.

### Effect on MEV

As the original intention of the EIP was to reduce one of the two types of MEV, it is useful to now revisit these types and see how they are impacted by the changes:

#### &#34;Base MEV &#34;As observed for the original model, the purple &#34;base MEV &#34;rectangle was not removable or reducible, as it is a fundamental property of the limited-supply market. However, as it turns out, one thing that we can do (and in fact have to do for the EIP to work) is have the protocol capture this MEV and thus effectively turn it into &#34;PEV &#34;(protocol extractable value). While this does not reduce transaction prices for users, it completely gets rid of one form of MEV, redistributing it directly to the protocol itself instead.

#### &#34;First-Price MEV &#34;The motivation behind EIP-1559 was to remove or at least reduce the &#34;first-price MEV &#34;that came from miners effectively over-charging most users. Under the EIP, this form of MEV is indeed greatly reduced and now limited to first-price priority fee extraction. The biggest part of the previous MEV is turned into user surplus, i.e. money that stays in the users &#39;wallets.

Note that for all of our considerations we focused on the &#34;normal &#34;case of non-full blocks. In rare situations of sudden demand spikes, consecutive blocks can be full for a small but sustained period of time. During that time, the priority fee would effectively assume the role of the previous gas price, and the &#34;first-price MEV &#34;would absorb all the extra user surplus that is normally freed by the EIP. It is however expected that these times of extreme demand spikes will only make up an insignificant portion of the overall blockchain activity.

### Base Fee as Protocol Revenue

The last aspect worth discussing on the topic of EIP-1559 is the first-of-its-kind protocol revenue source it creates. For the first time ever will Ethereum the protocol not only have expenses (block / staking rewards via issuance of new ETH) but also actively generate revenue.

It is important to note that this is somewhat unusual behaviour, and that thus no strict social consensus around what to do with that revenue is yet in place. The decision for now is to burn the ETH collected, to counteract the issuance for security payments. This is generally in line with the principle of &#34;minimal issuance &#34;, a principle with high levels of community support. While I personally strongly agree with this choice for the use of funds (for reasons I will expand on in my next writeup), I think it is incorrect to simply subsume it under &#34;minimal issuance &#34;. It is yet to be seen whether it will over time be added to the social consensus as a principle of its own (&#34;burn all protocol revenue &#34;) and reach a similarly strong level of universal community buy-in.

A possible alternative use of the revenue would be R &amp;D spending, although I agree with [Vitalik &#39;s assessment](https://vitalik.ca/general/2021/03/23/legitimacy.html) that for reasons of legitimacy the Ethereum base layer should abstain from discretionary spending like that.

A third alternative worth exploring is that of additional security spending. It would require some sort of fee smoothing mechanism to avoid the problems around miner manipulation outlined above. Crucially, a mechanism like that would mitigate the [incentive instability](https://www.cs.princeton.edu/~arvindn/publications/mining_CCS.pdf) of pure fee-based security funding. In my opinion it would not be a good fit for chains like Ethereum that already target (and pay for) a specific level of security. It could however be interesting for chains like Bitcoin that target zero inflation and are fine with a variable security level as a resulting tradeoff. In that context, an EIP-1559-like mechanism could both fix the incentive instability issues, as well as bring all of the benefits of first-price MEV removal and an in-protocol price oracle. I would not be surprised to see such a mechanism emerge for Bitcoin relatively soon, once Ethereum has conclusively demonstrated the general viability of the EIP.



## Conclusion

The markets for transaction inclusion and ordering are by now two mostly separate and independent markets. While MEV is a term coined in the context of transaction ordering, it can also be applied to the analysis of simple transaction inclusion. Before EIP-1559, transaction inclusion contained two forms of MEV: &#34;base MEV &#34;(fees extractable due to limited block size supply) and &#34;first-price MEV &#34;(fees extractable due to price discrimination).

EIP-1559 achieves its goal of greatly reducing &#34;first-price MEV &#34;, by introducing the base fee and using it to charge only the effective gas price. The residual MEV is a result of the need for a separate priority fee.

As a side effect of the EIP, the &#34;base MEV &#34;is captured by the protocol and turned into protocol revenue. This is the first time the Ethereum protocol ever generates revenue. While burning these extracted fees is a sensible choice for Etheruem, other blockchains may choose alternative uses. In particular, Bitcoin could implement an EIP-1559-like mechanism with revenues paid to miners via fee smoothing.

As a secondary side effect, the protocol now also exposes a price oracle for the minimum inclusion fee level (to be precise, up to the priority fee). This oracle can be accessed both on-chain via the new `BASEFEE` opcode and off-chain via any client. This will enable new use cases and could improve the UX of existing Ethereum-related applications.
