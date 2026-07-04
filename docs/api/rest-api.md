---
id: rest-api
title: Overview
sidebar_position: 1
slug: /api
---

# Skylogs REST API

Everything in the Skylogs UI is available through the REST API. This section is generated from the [OpenAPI spec](/api/openapi) plus hand-written pages for the concepts the spec can't express.

- **Base URL:** `https://<your-skylogs-host>/api/v1`
- **Interactive explorer:** [api.skylogs.io/api/doc](https://api.skylogs.io/api/doc) (Swagger UI)
- **Format:** JSON request and response bodies
- **Auth:** JWT bearer tokens — see [Authentication](/api/authentication). Inbound alert webhooks use per-rule tokens instead — see [Alert ingestion](/api/ingestion).

## API map

| Area | What it covers |
|---|---|
| [Authentication](/api/authentication) | Login, refresh, logout, password change |
| [Alert ingestion (webhooks)](/api/ingestion) | Firing/resolving alerts from your systems: API alerts and per-source webhooks |
| [Alert rules](/api/alert-rules) | The core object: CRUD, ack/resolve/silence, tags, notification endpoints, access, behavior rules |
| [Users & teams](/api/users-teams) | User and team management, ownership transfer |
| [Notification endpoints](/api/endpoints) | Channels that receive notifications, with OTP verification |
| [Data sources & Prometheus](/api/data-sources) | Connecting monitoring systems; browsing Prometheus labels/rules |
| [Provider configs](/api/configuration) | Call/SMS/email/Telegram provider settings with default + backup, cluster config |
| [Status pages](/api/status-pages) | Status page management |
| [Instances & assets](/api/instances-assets) | Connected Skylogs instances (zones) and profile assets |

## Conventions

**Success envelope.** Mutating endpoints commonly return:

```json
{ "status": true, "message": null }
```

**Validation errors** return `422` with:

```json
{ "status": false, "message": "The name field is required." }
```

**Auth errors** return `401`. Ingestion endpoints may return `429` when rate limited — see [Rate limits](/api/rate-limits).

**Pagination.** List endpoints that paginate accept `page` (and related) query parameters and return paginated envelopes; endpoints suffixed `/all` return the full unpaginated collection (e.g. `GET /api/v1/team` vs `GET /api/v1/team/all`).

**Alert rule types.** Alert rule creation is a single endpoint with a `type` discriminator. Supported types: `api`, `notification`, `prometheus`, `grafana`, `pmm`, `sentry`, `splunk`, `metabase`, `zabbix`, `elastic`, `victoria_logs`. Prometheus, Grafana, and PMM additionally use a `queryType` discriminator (`dynamic` | `textQuery`). Full schemas: [Alert rules](/api/alert-rules).

## Versioning

The API is versioned in the URL (`/api/v1`). {/* TODO: state the compatibility policy: are v1 fields ever removed or repurposed? */}
