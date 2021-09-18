## `PoolRouter`






### `constructor(address _smartPool, address _wrappingContract, address _treasury, address _foldToken, uint256 _protocolFee)` (public)





### `deposit(address tokenIn, uint256 tokenAmountIn, uint256 minPoolAmountOut, uint256 liquidationFee)` (public)

This methods performs the following actions:
            1. pull token for user
            2. joinswap into balancer pool, recieving lp
            3. stake lp tokens into Wrapping Contrat which mints FOLD to User



### `depositAll(uint256 poolAmountOut, uint256[] maxTokensAmountIn, uint256 liquidationFee)` (public)

This methods performs the following actions:
            1. pull tokens for user
            2. join into balancer pool, recieving lp
            3. stake lp tokens into Wrapping Contrat which mints FOLD to User



### `withdraw(address tokenOut, uint256 poolAmountIn, uint256 minAmountOut)` (public)

This methods performs the following actions:
            1. burn FOLD from user and unstake lp
            2. exitswap lp into one of the underlyings
            3. send the underlying to the User



### `withdrawAll(uint256 poolAmountIn, uint256[] minAmountsOut)` (public)

This methods performs the following actions:
            1. burn FOLD from user and unstake lp
            2. exitswap lp into all of the underlyings
            3. send the underlyings to the User



### `liquidate(address liquidatedUser, address tokenOut, uint256 poolAmountIn, uint256 minAmountOut)` (public)

This methods performs the following actions:
            1. burn FOLD from caller and unstake lp of liquidatedUser
            2. exitswap lp into one of the underlyings
            3. send the underlying to the caller
            4. transfer fee from caller to liquidatedUser



### `collectFeesToDAO(address token)` (public)





### `getPoolTokens() → address[]` (public)

VIEWS



### `getTokenWeights() → uint256[]` (public)





### `getFoldAmountOutSingle(address tokenIn, uint256 tokenAmountIn, uint256 minPoolAmountOut) → uint256 poolAmountOut` (public)





### `getTokensAmountIn(uint256 poolAmountOut, uint256[] maxAmountsIn) → uint256[] actualAmountsIn` (public)





### `getFoldAmountInSingle(address tokenOut, uint256 tokenAmountOut, uint256 maxPoolAmountIn) → uint256 poolAmountIn` (public)





### `getTokenAmountOutSingle(address tokenOut, uint256 poolAmountIn, uint256 minTokenAmountOut) → uint256 tokenAmountOut` (public)





### `getTokensAmountOut(uint256 poolAmountIn, uint256[] minAmountsOut) → uint256[] actualAmountsOut` (public)





### `_getTokensAmountIn(uint256 poolAmountOut, uint256[] maxAmountsIn) → uint256[] actualAmountsIn` (internal)






