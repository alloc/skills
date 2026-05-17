# Example: WebSocket Handler

Use this example only when the task needs a concrete WebSocket handler shape. For lifecycle concepts, read [runtime-primitives.md](./runtime-primitives.md) first.

## Config

Enable WebSocket support before adding handlers:

```ts
import { defineConfig } from "nitro";

export default defineConfig({
  features: {
    websocket: true,
  },
});
```

## Handler

```ts
import { defineWebSocketHandler } from "nitro";

export default defineWebSocketHandler({
  open(peer) {
    peer.subscribe("chat");
    peer.send({ user: "server", message: "connected" });
  },
  message(peer, message) {
    const text = message.text();
    peer.publish("chat", {
      user: peer.toString(),
      message: text,
    });
  },
  close(peer) {
    peer.unsubscribe("chat");
  },
});
```

## Checks

- Validate and sanitize message payloads before broadcasting.
- Use namespaces or topics to separate unrelated channels.
- Confirm the deployment target supports WebSockets.
- Test reconnect behavior from the client if the app exposes a persistent UI.
