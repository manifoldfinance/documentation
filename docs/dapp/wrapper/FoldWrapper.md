## `FoldWrapper`





### `onlyRouter()`






### `initialize(address _epochClock, address _dysonDao, address _balancerLP, address _poolRouter)` (public)





### `deposit(address lpOwner, uint256 amount, uint256 liquidationPremium)` (public)

Stores `amount`  tokens for the `lpOwner` into the vault
      If deposit is made with 0 amount it just updates the liquidation fee



### `liquidate(address liquidator, address lpOwner, uint256 amount)` (public)





### `withdraw(address lpOwner, uint256 amount)` (public)





### `_withdraw(address lpOwner, uint256 amount)` (internal)





### `initEpoch(uint128 epochId)` (public)





### `emergencyWithdraw()` (public)

Allows anyone to take out the LP tokens if there have been no withdraws for 1o0 epochs
        This does not burn FOLD as it is an emergency action



### `setMaxLiquidationFee(uint256 newFee)` (public)

Allows DAO to update max liquidation fee, does not affect existing positions



### `setLiquidationFee(uint256 value)` (public)

Allows users to update their liquidation fee



### `getEpochUserBalance(address user, uint128 epochId) → uint256` (public)

VIEWS



### `balanceLocked(address user) → uint256` (public)





### `getCurrentEpoch() → uint128` (public)





### `getEpochPoolSize(uint128 epochId) → uint256` (public)





### `currentEpochMultiplier() → uint128` (public)





### `computeNewMultiplier(uint256 prevBalance, uint128 prevMultiplier, uint256 amount, uint128 currentMultiplier) → uint128` (public)





### `epochIsInitialized(uint128 epochId) → bool` (public)





### `getCheckpointBalance(struct FoldWrapper.Checkpoint c) → uint256` (internal)





### `getCheckpointEffectiveBalance(struct FoldWrapper.Checkpoint c) → uint256` (internal)






### `Deposit(address user, uint256 amount)`





### `Withdraw(address user, uint256 amount)`





### `Liquidate(address liquidator, address user, uint256 feeAmount, uint256 amount)`





### `InitEpoch(address caller, uint128 epochId)`





### `EmergencyWithdraw(address user, uint256 amount)`





