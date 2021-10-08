---
title: Manifold FInance Omnibus Documentation
summary: Manifold Finance and OpenMEV Documentation
date: 2021-10-06
---

# Omnibus

!!! attention 
    This aggregated documentation is under active development, some page may be incomplete. 
    Please visit our forums or discord for specific questions!


## OpenMEV Platform Documentation

- Strategy and Implementation details
- End User information
- Help Desk and Troubleshooting
- Searcher Integration
- Formulas and Proofs
- Technical: Technical overview on specific category

### SushiSwap

The SushiSwap integration provides a service that realizes profit by transaction
batching for the purposes of arbitrage by controlling transaction ordering.

Right now every user sends a transaction directly to the network mempool and
thus give away the arbitrage, front-running, back-running opportunities to
miners(or random bots).

OpenMEV provides a credibly neutral platform that enables aggregation of
transactions (batching) for the purposes of extracting MEV profits and returning
them back to the traders.

### What is `credible neutrality`?

> "...that it is not just neutrality that is required here, it is credible
> neutrality. That is, it is not just enough for a mechanism to not be designed
> to favor specific people or outcomes over others; it’s also crucially
> important for a mechanism to be able to convince a large and diverse group of
> people that the mechanism at least makes that basic effort to be fair."
>
> - Vitalik Buterin,
>   [credible neutrality as a guiding principle](https://nakamoto.com/credible-neutrality/)

This ethos is at the heart of OpenMEV. Part of establishing credible neutrality
is having a clear and comprehensive rule book that regulates off-chain behavior
and activities. Our assumption concerning governance is that methods and
processes that work in legacy markets may not be applicable in adversarial
environments such as permissionless blockchains. With that understanding it is
important not to rely solely on such systems and mechanics long term.

Discuss this and more on our
[discourse forums](https://forums.manifoldfinance.com)
