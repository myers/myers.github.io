---
layout: post
title: "Starship Prompt in Claude Code's Status Line"
date: 2026-02-27T13:49:48-0500
tags: [claude-code, llm]
---

Claude Code has a status line at the bottom of the terminal that shows you
the current model and context usage.  It's useful, but it doesn't show you
where you are in the filesystem or what git branch you're on.  I already
have [Starship](https://starship.rs/) configured with all that information
for my shell prompt, so I figured: why not reuse it?

Claude Code lets you set a custom status line command in
`~/.claude/settings.json`.  The command receives a JSON blob on stdin with
the model name, working directory, and context window usage, and whatever
you print to stdout becomes the status line.

The trick is getting starship to output something Claude Code can actually
render.  Starship detects which shell it's running in and wraps ANSI color
codes with shell-specific escape sequences - `%{...%}` for zsh, `\[...\]`
for bash.  Claude Code isn't a shell, so those sequences show up as
literal garbage:

{% raw %}
```
[Opus 4.6] | ctx:18% | %{%}~/p/dot-files%{%} on %{%} %{%}main%{%} %{%}❯%{%}
```
{% endraw %}

The fix: set `STARSHIP_SHELL=plain`.  There's no actual "plain" shell type
in starship's code (I checked - it has bash, fish, zsh, etc.), but
unrecognized values fall through to an "unknown" handler that outputs raw
ANSI codes without any shell wrapping.

I also didn't want the `❯` prompt character in a status line, so I point
starship at a separate config that disables the `character` and
`line_break` modules:

```toml
# claude-starship.toml
[character]
disabled = true

[line_break]
disabled = true
```

Here's the script:

```bash
#!/bin/bash
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

if [ "$1" = "install" ]; then
    SETTINGS="$HOME/.claude/settings.json"
    COMMAND="$SCRIPT_DIR/claude-statusline.sh"
    mkdir -p "$HOME/.claude"
    if [ -f "$SETTINGS" ]; then
        jq --arg cmd "$COMMAND" \
          '.statusLine = {"type": "command", "command": $cmd}' \
          "$SETTINGS" > "$SETTINGS.tmp" \
            && mv "$SETTINGS.tmp" "$SETTINGS"
    else
        jq -n --arg cmd "$COMMAND" \
          '{"statusLine": {"type": "command", "command": $cmd}}' \
          > "$SETTINGS"
    fi
    echo "Installed. Restart Claude Code to apply."
    exit 0
fi

input=$(cat)
MODEL=$(echo "$input" | jq -r '.model.display_name')
CURRENT_DIR=$(echo "$input" | jq -r '.workspace.current_dir')
CONTEXT_PERCENT=$(echo "$input" | jq -r \
  '.context_window.used_percentage // 0' | cut -d. -f1)

YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

STARSHIP_PROMPT=""
if command -v starship &>/dev/null; then
    STARSHIP_PROMPT=$(cd "$CURRENT_DIR" 2>/dev/null \
      && STARSHIP_SHELL=plain \
         STARSHIP_CONFIG="$SCRIPT_DIR/claude-starship.toml" \
         starship prompt --terminal-width=80 2>/dev/null \
      | tr -d '\n')
fi

printf "${BLUE}[%s]${NC} | ${YELLOW}ctx:%s%%${NC} | %s\n" \
  "$MODEL" "$CONTEXT_PERCENT" "$STARSHIP_PROMPT"
```

Drop the script and `claude-starship.toml` in your dotfiles, then run
`claude-statusline.sh install`.  It uses `jq` to merge the statusLine
config into your existing `~/.claude/settings.json` without clobbering
anything else.

Now my status line shows the model, context usage, current directory, and
git branch - all rendered by my existing starship config.  And because
it's in my private dotfiles repo, `install` works on any machine.
