## `Staking`






### `initialize(address _epochClock)` (public)





### `deposit(address tokenAddress, uint256 amount)` (public)





### `withdraw(address tokenAddress, uint256 amount)` (public)





### `_withdraw(address from, address tokenAddress, uint256 amount)` (internal)





### `initEpochForTokens(address[] tokensLP, uint128 epochId)` (public)





### `emergencyWithdraw(address tokenAddress)` (public)





### `getEpochUserBalance(address user, address token, uint128 epochId) → uint256` (public)

VIEWS



### `balanceLocked(address user, address token) → uint256` (public)





### `getCurrentEpoch() → uint128` (public)





### `getEpochPoolSize(address tokenAddress, uint128 epochId) → uint256` (public)





### `currentEpochMultiplier() → uint128` (public)





### `computeNewMultiplier(uint256 prevBalance, uint128 prevMultiplier, uint256 amount, uint128 currentMultiplier) → uint128` (public)





### `epochIsInitialized(address token, uint128 epochId) → bool` (public)





### `getCheckpointBalance(struct Staking.Checkpoint c) → uint256` (internal)





### `getCheckpointEffectiveBalance(struct Staking.Checkpoint c) → uint256` (internal)






### `Deposit(address user, address tokenAddress, uint256 amount)`





### `Withdraw(address user, address tokenAddress, uint256 amount)`





### `InitEpochForTokens(address caller, uint128 epochId, address[] tokens)`





### `EmergencyWithdraw(address user, address tokenAddress, uint256 amount)`





