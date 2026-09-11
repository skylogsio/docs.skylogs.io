---
id: cli-overview
title: Skylogs CLI
sidebar_position: 1
slug: /cli
---

# Skylogs CLI

The **Skylogs CLI** (binary `skylogs`) is a terminal client for Skylogs, written in Go. It has two interaction styles: one-shot direct commands (built with [Cobra](https://github.com/spf13/cobra)) and a persistent interactive shell — closer to the MySQL CLI than a full-screen TUI — aimed at incident response from the terminal.

Source: [github.com/skylogsio/skylogs-cli](https://github.com/skylogsio/skylogs-cli)

:::caution Early stage
This is a single-commit, unreleased project — no tagged versions or published binaries yet. The command surface documented here reflects the `main` branch today and will grow (the project's own design notes call out a `services`/incident-management command family as the natural next step).
:::

## Building from source

```bash
git clone https://github.com/skylogsio/skylogs-cli.git
cd skylogs-cli
go build -o skylogs ./cmd/skylogs
```

Requires Go 1.26+.

## Two ways to use it

**Interactive shell** — run `skylogs` with no arguments:

```text
$ skylogs

Skylogs Interactive Shell  • incident response from your terminal

› User   mobin
› Roles  owner

skylogs>
```

**Direct commands**:

```bash
skylogs version
skylogs status
skylogs alert-rules
```

## Authentication

- The interactive shell prompts for username and password (password input hidden) if no valid session exists yet.
- Access and refresh tokens are stored in the OS keyring (macOS Keychain, Windows Credential Manager, or the Linux Secret Service) under the service name `skylogs-cli` — never in a plaintext file.
- On startup, the stored session is validated against `POST /api/v1/auth/me`. A `401` triggers an automatic token refresh (`POST /api/v1/auth/refresh`); if the refresh token itself is rejected, you're prompted to log in again. Non-auth failures (server errors, no network) are reported as-is rather than treated as an expired session.
- **Direct commands don't prompt for a password themselves** — they reuse whatever session is already in the keyring. Run the interactive shell at least once first to authenticate.
- Log out from inside the shell with `logout`: this invalidates the session on the server (`POST /api/v1/auth/logout`) and deletes the local tokens.

## Configuration

The CLI talks to `https://skylogs-api.qcluster.org/api/` by default. Point it at your own instance with an environment variable:

```bash
export SKYLOGS_API_URL="https://your-skylogs-instance/api/"
```

## Direct commands

| Command | Description |
|---|---|
| `skylogs version` | Print the CLI version |
| `skylogs zone list` | List available zones |
| `skylogs status` | List Skylogs statuses |
| `skylogs alert-rules` | List alert rules |
| `skylogs alert-rules get --id <id>` | Get one alert rule's full detail |
| `skylogs alert-rules fire --id <id>` | Show an alert rule's currently-firing data |
| `skylogs alert-rules history --id <id>` | Show an alert rule's history |
| `skylogs alert-rules access --id <id>` | Show users/teams with access to an alert rule |

Data-producing commands accept a common set of flags:

| Flag | Description |
|---|---|
| `-o, --output` | `table` (default), `json`, or `yaml` |
| `--file <path>` | Write output to a file instead of stdout |
| `--zone <name>` | Run the command against a specific zone instead of `main` (persistent flag; only valid with a direct command, not the interactive shell) |

### `skylogs status`

| Flag | Description |
|---|---|
| `--search <text>` | Search by name or tag |
| `--tag <tag>` | Filter by tag (repeatable) |
| `--fired` | Only statuses with active critical or warning alerts |
| `--page`, `--per-page` | Pagination (`--per-page` max 100) |

### `skylogs alert-rules`

| Flag | Description |
|---|---|
| `--search <text>` | Search by alert rule name |
| `--type <type>` | Filter by alert type (repeatable) |
| `--tag <tag>` | Filter by tag (repeatable) |
| `--state <state>` | `unknown`, `warning`, `critical`, `triggered`, or `resolved` |
| `--silent <status>` | `silent` or `active` |
| `--fired` | Shorthand for `--state triggered` (cannot combine with a different `--state`) |
| `--page`, `--per-page` | Pagination (`--per-page` max 100) |

### `skylogs alert-rules fire` / `skylogs alert-rules history`

Both require `--id <id>` and support `--page`/`--per-page` plus `--detail <row>` — pass the row number shown in the table to drill into that item's full detail instead of the summary table. Which columns are available depends on the alert rule's type.

```bash
skylogs alert-rules fire --id <alert-rule-id> --detail 2 -o json
```

## Interactive shell

Running `skylogs` with no arguments opens a REPL at a `skylogs>` prompt.

| Command | Description |
|---|---|
| `help [command]` | List commands, or show usage for one |
| `status` | Open the interactive status view |
| `alert-rules` | Open the interactive alert-rules view |
| `zone [name\|list]` | Show, switch, or list the active zone |
| `logout` | Log out and remove the current session |
| `exit` | Exit the shell |

`status` and `alert-rules` drop you into their own sub-prompt (`status>` / `alert-rules>`) with: `search`, `filter`, `sort` (status only), `next` / `prev`, `per-page <n>`, `select <row>` (open a row's detail view), `refresh`, `help`, and `back` to return to `skylogs>`.

The shell uses readline-style line editing: ↑/↓ for command history, Ctrl+A/E for line movement, Ctrl+C to cancel the current input, Ctrl+D to exit, and Tab completion for command names. History persists across sessions under your OS config directory, e.g. `~/.config/skylogs/history` on Linux.

## Notes

- The interactive shell and the direct Cobra commands are two separate frontends over the same underlying service layer — they don't call each other.
- Local roles/permissions shown in the shell banner are informational only; the Skylogs server is always the authority for what an authenticated user can actually do.
- For the underlying HTTP API these commands wrap, see [API reference → Alert rules](/api/alert-rules) and [Authentication](/api/authentication).
