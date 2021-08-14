# Manifold Finance

This documentation is compromised of:

- OpenMEV
- Manifold Stratagies
- Associated Libraries

## OpenMEV

Maximal (formerly Miner) Extractable Value (MEV) is the value that can be extracted from a blockchain by any agent without special permissions.  Considering this permissionless nature, any agent with transaction ordering rights will be in a privileged position to perform the extraction.  In Proof of Work blockchains, it is miners who determine transaction ordering within a block, hence the former “miner” term. 
In practice, bot operators seek to extract MEV.

OpenMEV provides infrastructure and implementations of 'bot operators' for the purposes of capturing MEV.


## Total Addressable Market

> The first important point to make is that MEV
> is a theoretical quantity that we can only approach asymptotically. 
> Unforseen extraction methods can and will be devised (every new DeFi hack is an MEV extraction event). 
> Hence, we will here focus instead on the Realized Extractable Value, notated REV, where REV≤MEV.
> In other words, REV is the actual value extracted from the blockchain from MEV
>
> Alejo Salles – Flashbots.net

