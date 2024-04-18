SSH Tunneling

```bash
ssh -L 9998:localhost:15672 -p 2223 user@remote.mq.internal -N
# -L : 啟用轉送功能
# -p : remote host 開啟 2223 port
# -N : 不會登入 remote host 的 shell 進行轉送

curl http://localhost:9998
```

下圖僅為推測

```mermaid
flowchart LR

    host["host (9998)"] --> remote["(2223) SSH Tunnel (??)"];
    remote --> internal["(15672) RabbitMQ"];
```
