---
slug: /
title: OpenMEV Documentation
description: SushiSwap Overview
keywords:
  - mev
  - docs
---


# OpenMEV & Sushiswap

OpenMEV and Sushiswap work together to recapture lost MEV profits so that Sushi
traders can trade for free (up to 95%) on the exchange.

These are not `gasless` transactions, these are `paid rebate` transactions! You
get paid to trade more using OpenMEV.

## Support and Help

- [Support Page](https://openmev.page.link/support)
- [Discord Chat](https://openmev.page.link/support-chat)

## Trading for Free on Sushi.com

1. `baseFee` amount is subject to transaction cost rebates

2. Transactions with a slippage tolerance of 1% or higher are eligible for gas
   refunds

3. Refunds are paid out in ETH/WETH/xSUSHI

4. It will take at least 35 blocks to receive a refund, no more than 50.

### Getting Gas Pricing information

Our API Endpoint is here

```bash
curl -s -L api.txprice.com | jq .blockPrices[0].estimatedPrices[3]
```

```json
{
  "confidence": 80,
  "price": 112,
  "maxPriorityFeePerGas": 1.76,
  "maxFeePerGas": 222.52
}
```

## Engine

OpenMEV Engine uses a batch auction-based matching engine to execute orders.
Batch auctions were chosen to reduce the impact of frontrunning on the exchange.

1. All orders for the given market are collected.

2. Orders beyond their time-in-force are canceled.

3. Orders are placed into separate lists by market side, and aggregate supply
   and demand curves are calculated.

4. The matching engine discovers the price at which the aggregate supply and
   demand curves cross, which yields the clearing price. If there is a
   horizontal cross - i.e., two prices for which aggregate supply and demand are
   equal - then the clearing price is the midpoint between the two prices.

5. If both sides of the market have equal volume, then all orders are completely
   filled. If one side has more volume than the other, then the side with higher
   volume is rationed pro-rata based on how much its volume exceeds the other
   side. For example, if aggregate demand is 100 and aggregate supply is 90,
   then every order on the demand side of the market will be matched by 90%.

Orders are sorted based on their price, and order ID. Order IDs are generated at
post time and is the only part of the matching engine that is time-dependent.
However, the oldest order IDs are matched first so there is no incentive to post
an order ahead of someone else’s.
