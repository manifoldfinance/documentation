# **unstable**TokenVault

>

```
__unstable__TokenVault
```

### 🔎 Details

Similar to an Escrow for tokens, this contract allows its primary account to spend its tokens as it sees fit. This contract is an internal helper for PostDeliveryCrowdsale, and should not be used outside of this context.

### 🎟 Events

#### PrimaryTransferred

|   Name    | Indexed |   Type    |
| :-------: | :-----: | :-------: |
| recipient | `false` | `address` |

## `transferPrimary`

> 👀 `nonpayable`

### 🔎 Details

Transfers contract to a new primary.

### ⚙️ Parameters

| Name |   Type    | Description                 |
| :--: | :-------: | --------------------------- |
|  0   | `address` | The address of new primary. |

## `primary`

> 👀 `view`

### → Returns

the address of the primary.

|     Name      |   Type    |
| :-----------: | :-------: |
| Not specified | `address` |

## `transfer`

> 👀 `nonpayable`
