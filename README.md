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
litellm --config config.yaml --port 4000
```

## Applications

### Use with Claude Code

#### Install

```bash
npm install -g @anthropic-ai/claude-code
```

#### Configure

Copy [settings.json](settings.json) from this repo to `~/.claude/settings.json`:

```bash
cp settings.json ~/.claude/settings.json
```


#### Run

```bash
claude
```
