---
id: api
title: API reference
sidebar_position: 7
slug: /api
---

# API reference

Everything in the Skylogs UI is available through the REST API. Use it to ingest alerts programmatically, automate incident workflows, manage on-call schedules, and pull reporting data.

:::caution Draft
Endpoint paths and schemas below are a documentation skeleton pending the published OpenAPI spec.
:::

{/* TODO: replace every endpoint/field with the real API surface — ideally generate this page from an openapi.yaml committed to the main repo. */}

## Basics

- **Base URL:** `https://<your-skylogs-host>/api/v1`
- **Format:** JSON request and response bodies
- **Authentication:** Bearer token

```
Authorization: Bearer <token>
```

Create API tokens in **Settings → API tokens**. Tokens inherit the RBAC permissions of the user or service account that owns them. {/* TODO: confirm token model */}

**Errors** use standard HTTP status codes with a JSON body:

```json
{ "error": { "code": "not_found", "message": "Alert 8f3a… does not exist" } }
```

## Alerts

```
POST   /alerts                # ingest an alert
GET    /alerts                # list; filters: status, severity, team, page
GET    /alerts/{id}
POST   /alerts/{id}/ack       # acknowledge (stops escalation)
POST   /alerts/{id}/resolve
POST   /alerts/{id}/snooze    # body: { "until": "2026-07-02T15:00:00Z" }
POST   /alerts/{id}/assign    # body: { "user_id": "…" }
```

Ingestion payload — see [Generic webhook](/integrations/generic-webhook) for the schema and `dedup_key` semantics.

## Incidents

```
GET    /incidents
POST   /incidents                     # create (manually or from alerts: { "alert_ids": [...] })
GET    /incidents/{id}
PATCH  /incidents/{id}                # status, severity, commander, …
POST   /incidents/{id}/timeline       # append a timeline entry
GET    /incidents/{id}/rca            # export RCA report
GET    /incidents/{id}/postmortem     # export postmortem
```

## On-call & schedules

```
GET    /schedules
GET    /schedules/{id}/oncall         # who is on call right now
POST   /schedules/{id}/overrides      # shift swap / coverage
GET    /escalation-policies
POST   /escalation-policies
```

The `oncall` endpoint is the one you'll script against most — e.g., posting the current on-call engineer into a Slack channel topic every morning.

## Teams & users

```
GET    /teams
POST   /teams
GET    /users
POST   /users
GET    /users/{id}/endpoints
POST   /users/{id}/endpoints/{id}/verify
```

## Status pages

```
GET    /status-pages
POST   /status-pages/{id}/updates     # publish an update to subscribers
```

## Reporting

```
GET /reports/sla?service=payments&from=2026-01-01&to=2026-06-30
GET /reports/mtta-mttr?team=database&period=90d
GET /reports/oncall-load?team=platform&period=30d
```

## Outbound webhooks

Subscribe external systems to Skylogs events:

```
POST /webhooks
{
  "url": "https://example.com/hooks/skylogs",
  "events": ["alert.firing", "alert.resolved", "incident.created", "incident.resolved"],
  "secret": "…"
}
```

Deliveries are signed with an HMAC header so receivers can verify authenticity. {/* TODO: document header name and signature scheme */}

## Pagination

```json
{ "data": [ … ], "meta": { "page": 1, "per_page": 50, "total": 1204 } }
```

## Versioning & stability

The API is versioned in the URL (`/api/v1`). Backwards-incompatible changes ship as a new version; `v1` fields are only added, never removed or repurposed.
