---
id: ingestion
title: Alert ingestion (webhooks)
sidebar_position: 3
slug: /api/ingestion
---

# Alert ingestion (webhooks)

Inbound alerts do **not** use JWT auth. Each alert rule of an inbound type carries its own token, so monitoring systems can deliver without holding user credentials.

There are two ingestion styles:

## 1. API alerts — fire / resolve / stop

Create an alert rule with `type: "api"` ([Alert rules](/api/alert-rules)); the server generates an `apiToken` for it. Your systems then drive the alert's state:

```
POST /api/v1/fire-alert       # start firing
POST /api/v1/resolve-alert    # resolve
POST /api/v1/stop-alert       # alias of resolve
POST /api/v1/status-alert     # post a status update
POST /api/v1/notification-alert  # notification-type payload
```

Authentication uses the alert rule's **API alert token** (the `ApiAlertAuth` middleware), not a bearer JWT. {/* TODO: document exactly where the token goes — header name or body field — and the full request payload with an example */}

Responses: `200` accepted · `401` invalid token · `429` rate limited.

API alert rules support **auto-resolve**: set `enableAutoResolve: true` and `autoResolveMinutes` on the rule to resolve firing instances automatically if no resolve call arrives — useful for sources that can fire but never confirm recovery.

## 2. Per-source webhooks — token in the URL

For supported monitoring systems, create an alert rule of the matching type and point the tool at its dedicated webhook URL. The token is embedded in the path:

```
POST /api/v1/grafana-alert/{token}
POST /api/v1/zabbix-alert/{token}
POST /api/v1/splunk-alert/{token}
POST /api/v1/sentry-alert/{token}
POST /api/v1/pmm-alert/{token}
```

Skylogs parses each tool's native payload — no reshaping needed. Setup instructions per tool are in [Integrations](/integrations). {/* TODO: document where the {token} is obtained in the UI/API for each rule type, and add one example payload per source */}

Prometheus-family sources (`prometheus`, `victoria_logs`, and PMM's Alertmanager-compatible mode) are matched through data sources and alert rule filters rather than a per-rule webhook — see [Data sources](/api/data-sources) and the Prometheus rule schemas in [Alert rules](/api/alert-rules).

## Security notes

- Treat webhook tokens as secrets: they authorize firing alerts (and paging humans). Rotate a token by recreating the rule if leaked. {/* TODO: confirm rotation mechanism */}
- Always deliver over HTTPS.
- Rate limiting applies to ingestion (`429`) — see [Rate limits](/api/rate-limits).
