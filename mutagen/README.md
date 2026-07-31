
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

Sync

```bash
mutagen sync create \
  --name <session-name> \
  --mode two-way-safe \
  --ignore-vcs \
  <local_folder_path> \
  <remote_machine>:<remote_path>
```

Monitor

```bash
mutagen sync monitor <session-name>
```

Flush

```bash
mutagen sync flush <session-name>
```

Show sync

```bash
mutagen sync list
```

Terminate sync

```bash
mutagen sync terminate <session-name>
```