---
id: backup-restore
title: Backup & restore
sidebar_position: 7
slug: /guides/backup-restore
draft: true
---

# Backup & restore

:::info Under construction
This page is planned but not yet written. Remove `draft: true` from the frontmatter when it's ready to publish. Want to help? See [Contributing](/contributing).
:::

*Purpose: concrete procedures per topology, and how to test restores.*

## Planned outline

- What to back up: MongoDB data, configuration, secrets
- Single-node procedure
- HA cluster: backing up consistent state
- Multi-zone: per-zone backups (alert data is zone-local)
- Restore procedure and verification
- Scheduling and retention of backups
