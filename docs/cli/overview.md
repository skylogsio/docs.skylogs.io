---
id: cli-overview
title: Skylogs CLI
sidebar_position: 1
slug: /cli
---

# Skylogs CLI

**skyctl** is a command-line client for the Skylogs API, written in Go with [Cobra](https://github.com/spf13/cobra). It authenticates against your Skylogs instance and lets you list and delete alerts, endpoints, users, and datasources without leaving the terminal.

Source: [github.com/skylogsio/skyctl](https://github.com/skylogsio/skyctl)

:::caution Early stage
`skyctl` is a very young project (single-commit history, no tagged releases, no published binaries). Its API base URL is currently **hardcoded** to a development endpoint rather than pointing at your own Skylogs instance, so treat the commands below as a preview of the shape of the tool rather than something you can install and run against production today.
:::

## Building from source

No packaged binaries are published yet — build it yourself:

```bash
git clone https://github.com/skylogsio/skyctl.git
cd skyctl
go build -o skyctl .
```

## Authenticating

```bash
./skyctl login --username <username> --password <password>
```

On success, `skyctl` prints an access token and the export command for it — copy that into your shell:

```bash
export SKYCTL_TOKEN=<token>
```

Every other command reads the token from the `SKYCTL_TOKEN` environment variable; there's no credential storage yet, so this is per-session.

## Commands

| Command | Description |
|---|---|
| `skyctl login` | Authenticate and print an access token |
| `skyctl get alerts` | List alerts |
| `skyctl get endpoints` | List notification endpoints |
| `skyctl get users` | List users |
| `skyctl get datasources` | List datasources |
| `skyctl del alert <alertname>` | Delete an alert by name |
| `skyctl del user <username>` | Delete a user by username |

### `skyctl get alerts`

| Flag | Description |
|---|---|
| `--type` | Filter by alert type |
| `--status` | Filter by alert status |
| `--endpoints` | Filter by endpoints |
| `--env` | Filter by environment |
| `--silent` | Suppress output |

```bash
skyctl get alerts --type prometheus --status firing
```

### `skyctl get endpoints`

| Flag | Description |
|---|---|
| `--type` | Filter by endpoint type |

```bash
skyctl get endpoints --type email
```

### `skyctl del alert` / `skyctl del user`

Both take the resource identifier as a positional argument:

```bash
skyctl del alert high-cpu-usage
skyctl del user jdoe
```

## Notes

- This page documents what's implemented in the `main` branch today; expect the command surface, auth flow, and configurability (a real `--server`/config-file option instead of the hardcoded API URL) to change as the project matures.
- For the full HTTP API these commands wrap, see [API reference → Alert rules](/api/alert-rules) and [Authentication](/api/authentication).
