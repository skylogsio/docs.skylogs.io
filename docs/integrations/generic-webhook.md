---
id: generic-webhook
title: Generic webhook
sidebar_position: 9
slug: /integrations/generic-webhook
---

# Generic webhook

For any tool not covered by a native integration:

```
POST https://skylogs.example.com/api/v1/ingest/webhook/<token>
Content-Type: application/json
```

```json
{
  "summary": "Disk usage above 90% on db-14",
  "severity": "warning",
  "source": "custom-monitor",
  "resource": "db-14",
  "status": "firing",
  "tags": {"team": "database", "env": "production"},
  "dedup_key": "disk-db-14"
}
```

{/* TODO: confirm real payload schema */}

## Deduplication and auto-resolve

Alerts with the same `dedup_key` are collapsed into one. Send the same `dedup_key` with `"status": "resolved"` to auto-resolve.

## Severity values

`critical`, `warning`, `info` {/* TODO: confirm the real severity enum */}
