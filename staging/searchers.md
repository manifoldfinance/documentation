# Searchers

> Searcher Information

## SDK

[See @openmev/sdk](https://github.com/manifoldfinance/openmev-sdk)

### transaction.proto

`transaction.proto`

```protobufs
message FrontierTransaction {

  string value = 1;     // hex encoded big integer
  string input = 2;     // hex bytes
  int64 nonce = 3;      //
  string gasPrice = 4;  // hex encoded big integer
  int64 gasLimit = 5;

  optional string v = 6;    // hex encoded big integer
  optional string r = 7;    // hex encoded big integer
  optional string s = 8;    // hex encoded big integer

  optional string to = 9;  //
  optional string chain_id = 10;   // hex encoded big integer
  optional string sender = 11;
}

message AccessListEntry {
  string address = 1;
  repeated string storageKeys = 2;
}

message EIP2930Transaction {

  string chain_id = 1;  // hex encoded big integer
  string value = 2;     // hex encoded big integer
  string input = 3;     // hex bytes
  int64 nonce = 4;      //
  string gasPrice = 5;  // hex encoded big integer
  int64 gasLimit = 6;

  repeated AccessListEntry accessList = 7;

  optional int32 v = 8;     // byte value
  optional string r = 9;    // hex encoded big integer
  optional string s = 10;    // hex encoded big integer

  optional string to = 11;
  optional string sender = 12;
}

message EIP1559Transaction {

  string chain_id = 1;  // hex encoded big integer
  string value = 2;     // hex encoded big integer
  string input = 3;     // hex bytes
  int64 nonce = 4;      //
  string maxPriorityFeePerGas = 5;  // hex encoded big integer
  string maxFeePerGas = 6;          // hex encoded big integer
  int64 gasLimit = 7;

  repeated AccessListEntry accessList = 8;

  optional int32 v = 9;       // byte value
  optional string r = 10;    // hex encoded big integer
  optional string s = 11;    // hex encoded big integer

  optional string to = 12;
  optional string sender = 13;
}

enum TransactionType {
  FRONTIER = 0;
  EIP2930 = 1;
  EIP1559 = 2;
}

message Transaction {

  TransactionType type = 1;
  optional string signed = 2;
  optional int64 deadline_at = 3;

  optional string transaction_hash = 16;
  optional int32 transaction_index = 17;

  optional string block_hash = 18;
  optional string block_number = 19;

  optional string gas_price = 20;

  optional TransactionReceipt receipt = 21;

  oneof payload {
    FrontierTransaction transaction_frontier = 22;
    EIP2930Transaction transaction_eip2930 = 23;
    EIP1559Transaction transaction_eip1559 = 24;
  }

  oneof action {
    org.openmev.protobuf.action.SwapExactTokensForTokens swap_exact_tokens_for_tokens = 33;
    org.openmev.protobuf.action.SwapTokensForExactTokens swap_tokens_for_exact_tokens = 34;
    org.openmev.protobuf.action.SwapExactETHForTokens swap_exact_eth_for_tokens = 35;
    org.openmev.protobuf.action.SwapTokensForExactETH swap_tokens_for_exact_ETH = 36;
    org.openmev.protobuf.action.SwapExactTokensForETH swap_exact_tokens_for_ETH = 37;
    org.openmev.protobuf.action.SwapETHForExactTokens swap_eth_for_exact_tokens = 38;
    org.openmev.protobuf.action.SwapExactTokensForTokensSupportingFeeOnTransferTokens swap_exact_tokens_for_tokens_supporting_fee_on_transfer_tokens = 39;
    org.openmev.protobuf.action.SwapExactETHForTokensSupportingFeeOnTransferTokens swap_exact_eth_for_tokens_supporting_fee_on_transfer_tokens = 40;
    org.openmev.protobuf.action.SwapExactTokensForETHSupportingFeeOnTransferTokens swap_exact_tokens_for_eth_supporting_fee_on_transfer_tokens = 41;
  }
}
```
