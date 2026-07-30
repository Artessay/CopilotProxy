# Copilot Proxy

A thin proxy that exposes GitHub Copilot's frontier models behind standard endpoints.


## QuickStart

### Install LiteLLM

```bash
pip install uv
uv tool update-shell
uv tool install 'litellm[proxy]'
```

### Start the proxy

```bash
litellm --config proxy/config.yaml --host 0.0.0.0 --port 4000
```

## Applications

### Use with Claude Code

#### Install

```bash
npm install -g @anthropic-ai/claude-code
```

#### Configure

Copy [claude-code.settings.json](proxy/claude-code.settings.json) from this repo to `~/.claude/settings.json`:

```bash
cp proxy/claude-code.settings.json ~/.claude/settings.json
```


#### Run

```bash
claude
```

### Use with Codex

#### Install

```bash
npm install -g @openai/codex
```

#### Configure

Copy [codex.config.toml](proxy/codex.config.toml) from this repo to `~/.codex/config.toml`:

```bash
cp proxy/codex.config.toml ~/.codex/config.toml
```

#### Run

```bash
codex
```

