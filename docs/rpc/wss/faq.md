# FAQ / FYI

**What is the Backbone endpoint for WebSockets?**

`wss://<network>.backbonecabal.xyz/ws`

**What are the supported networks?**

Mainnet, Ropsten, Rinkeby, Kovan

**Is batch support available?**

Yes

**Is compression enabled?**

Yes

**Max payload size?**

128MB

**Why does my websocket connection disconnect after a while?**

Idle connections that exceed beyond an hour will get disconnected.
Adding 'pings' to your websocket connection will prevent the connection
from going idle. Any unrecognized requests will trigger the server to
close the connection with an error message.

**Non-empty 'Sec-WebSocket-Protocol' header error?**

web3.js 1.0.0-beta.34 has an open issue with request headers
https://github.com/ethereum/web3.js/issues/1559. Please revert/downgrade
to 1.0.0-beta.33.

**Why is includeTransactions option not working for eth_subscribe?**

Though the includeTransactions option is included in the Ethereum
Pub/Sub API documentation, currently it is not returning the expected
results. For more information:
https://github.com/ethereum/go-ethereum/issues/15804.
