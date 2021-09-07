## `WrappingRewards`






### `constructor(address _dysonTokenAddress, address _basketBalancer, address _wrappingContract, address _rewardsVault, address _treasury)` (public)





### `massHarvest() → uint256` (external)





### `harvest(uint128 epochId) → uint256` (external)





### `collectFeesToDAO()` (public)





### `getCurrentEpoch() → uint256` (external)





### `getRewardsForEpoch() → uint256` (public)





### `getEpochStake(address userAddress, uint128 epochId) → uint256` (external)





### `userLastEpochIdHarvested() → uint256` (external)





### `getPoolSize(uint128 epochId) → uint256` (external)





### `isBoosted(address user, uint128 epoch) → bool` (public)





### `getUserRewardsForEpoch(uint128 epochId) → uint256` (public)





### `_harvest(uint128 epochId) → uint256` (internal)

INTERNAL



### `_initEpoch(uint128 epochId)` (internal)





### `_getPoolSize(uint128 epochId) → uint256` (internal)





### `_getUserBalancePerEpoch(address userAddress, uint128 epochId) → uint256` (internal)





### `_getEpochId() → uint128 epochId` (internal)





### `_wrapperEpochId(uint128 epochId) → uint128` (internal)






### `MassHarvest(address user, uint256 epochsHarvested, uint256 totalValue)`





### `Harvest(address user, uint128 epochId, uint256 amount)`





### `InitEpoch(address caller, uint128 epochId)`





