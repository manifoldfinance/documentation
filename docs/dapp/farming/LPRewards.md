## `LPRewards`






### `constructor(address dysonTokenAddress, address depositLP, address stakeContract, address rewardsVault, uint256 totalDistribution)` (public)





### `initialize()` (public)





### `massHarvest() → uint256` (external)





### `harvest(uint128 epochId) → uint256` (external)





### `_initEpoch(uint128 epochId)` (internal)





### `_harvest(uint128 epochId) → uint256` (internal)





### `getCurrentEpoch() → uint128 epochId` (public)

VIEWS



### `getUserRewardsForEpoch(uint128 epochId) → uint256` (public)





### `depositLP() → address` (public)





### `getPoolSize(uint128 epochId) → uint256` (external)





### `getEpochStake(address userAddress, uint128 epochId) → uint256` (external)





### `userLastEpochIdHarvested() → uint256` (external)





### `_getPoolSize(uint128 epochId) → uint256` (internal)





### `_getUserBalancePerEpoch(address userAddress, uint128 epochId) → uint256` (internal)





### `_stakingEpochId(uint128 epochId) → uint128` (internal)






### `MassHarvest(address user, uint256 sizeAtEpochHarvested, uint256 totalValue)`





### `Harvest(address user, uint128 epochId, uint256 amount)`





### `InitEpoch(address caller, uint128 epochId)`





