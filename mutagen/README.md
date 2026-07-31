
### Forward

Forward port

```bash
mutagen forward create \
  --name <session-name> \
  <remote-host>:tcp:<remote-bind-addr>:<remote-port> \
  tcp:<local-bind-addr>:<local-port>
```

For example

```bash
mutagen forward create \
  --name litellm-port \
  192.168.1.1:tcp:localhost:4000 \
  tcp:localhost:4000
```

Show forward ports

```bash
mutagen forward list
```

Terminate forward port

```bash
mutagen forward terminate <session-name>
```

### Sync

