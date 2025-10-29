---
layout: post
title: "Chrome DevTools CLI for Claude Code"
date: 2025-10-28T19:49:40-0400
tags: [llm, chrome, meta-quest, claude-code]
---

I've been using Claude Code to build many wondrous (but often half working)
things.  Part of that is getting it to test on it's own in a web browser.
The official [Chrome DevTools
MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) kept freezing up
while I was using it with a Meta Quest 3, and when it did work, asking for
console logs would return massive amounts of data that filled my context
(are there more dreaded words than "Compacting Conversation..."?).

Chrome DevTools Protocol (CDP) is Chrome's way of letting external programs
control the browser - taking screenshots, evaluating JavaScript, monitoring
network traffic.  Most CDP tools are libraries meant to be imported into
code, but Claude Code needs a CLI.

I built `@myerscarpenter/cdp-cli`.  It outputs NDJSON (newline-delimited
JSON) - one complete JSON object per line, making it grep-compatible and
easy to parse.

The key feature is the console command.  By default it outputs bare JSON
strings and shows only the last 10 messages:

```bash
cdp-cli console "GitHub"
"Page loaded"
"API call successful"
```

This saves tokens.  When you need more detail, flags like `--verbose`,
`--tail 50`, or `--all` give you control over how much data comes back.
When truncated, it warns on stderr so Claude Code knows there's more
available.

I'm also liking using cli's over mcp's as you can see exactly what it's
doing.

Chrome needs to be running with remote debugging enabled:

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9222
```

Or you could ask Claude to port forward 9222 from your Quest with
[adb](https://developer.android.com/tools/adb).

Then install and use:

```bash
npm install -g @myerscarpenter/cdp-cli
cdp-cli tabs
cdp-cli console "GitHub" --tail 5
cdp-cli screenshot "GitHub" --output screenshot.jpg
```

Commands cover page management (tabs, new, go, close), debugging (console,
snapshot, eval, screenshot), network inspection, and input automation
(click, fill, key).

See it on [GitHub](https://github.com/myers/cdp-cli) and
[npm](https://www.npmjs.com/package/@myerscarpenter/cdp-cli).
