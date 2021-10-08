# Introduction

Backbone's websocket endpoint provides support for Pub/Sub API as well
as JSON-RPC filter support. The regular Ethereum API is also supported
and documented in the 'examples' portion of 'Ethereum API'

All examples in this reference section uses WSCAT, but will work with
any tool that supports websockets.

Some tools you can use for making these requests

- [WSCAT](https://github.com/websockets/wscat)
- [Advanced Rest Client](https://install.advancedrestclient.com/)

#### EXAMPLE

The following is an example showing a connection to the WebSockets
endpoint and using subscriptions through web3.js 1.0

NOTE: web3.js 1.0.0-beta.34 has an open issue with request headers.
(https://github.com/ethereum/web3.js/issues/1559) Users will have to
revert to version 1.0.0-beta.33 to avoid the issue.

```js
const Web3 = require("web3");

let web3 = new Web3(
  new Web3.providers.WebsocketProvider("wss://mainnet.backbonecabal.xyz/ws")
);

const instance = new web3.eth.Contract(<abi>, <address>);

instance.getPastEvents(
    "SomeEvent",
    { fromBlock: 0, toBlock: "latest" },
    (errors, events) => {
        if (!errors) {
            // process events
        }
    }
);
```
