---
id: health-check-alert
title: Create a Health Check Alert
sidebar_position: 9
slug: /alert-management/health-check-alert
---

# Create a Health Check Alert

A **health check alert** (also called a dead-man's-switch or heartbeat alert) flips the usual model: instead of firing when something goes wrong, it fires when an expected check-in *stops arriving*. It's the recommended way to monitor Skylogs itself — see [Admin guide → Monitoring Skylogs itself](/admin-guide#operational-maintenance) — and works just as well for any external job or service that should "phone home" on a schedule (cron jobs, backups, sync tasks).

There is no separate `healthcheck` rule type in the API — this pattern is built on the [API alert rule](/alert-management/api-alert) with auto-resolve enabled, so a missed check-in is what triggers the notification.

## How it works

1. You create an **API alert rule** with `enableAutoResolve` turned **off** at the alert level, but drive the state from an external scheduler:
   - Your checker (an external uptime service, cron job, or the monitored system itself) calls the fire endpoint on a fixed interval to say "I'm alive."
   - If Skylogs stops receiving that call within the expected interval, the alert is treated as stale and should be escalated.
2. In practice this is implemented as a **reverse heartbeat**: point an external, independent monitor (outside Skylogs) at Skylogs' own health endpoint, and have *that* monitor fire into Skylogs if Skylogs stops responding. This keeps the check honest — Skylogs must not be its own only observer.

## Steps

1. **Create an API alert rule** (see [Create an API alert](/alert-management/api-alert)) named something like `skylogs-heartbeat`.
2. **Assign endpoints** that should page someone immediately — a missed heartbeat is always urgent.
3. Configure your **external checker** (outside Skylogs) to:
   - Poll Skylogs' health endpoint on an interval, and
   - Call the alert rule's `fire-alert` endpoint if Skylogs is unreachable or unhealthy, and `stop-alert` once it recovers.

```
POST https://mydomain.com/api/v1/fire-alert
Authorization: Bearer <API_TOKEN>
Content-Type: application/json

{
  "instance": "skylogs-heartbeat",
  "description": "External checker could not reach Skylogs"
}
```

```
POST https://mydomain.com/api/v1/stop-alert
Authorization: Bearer <API_TOKEN>
Content-Type: application/json

{
  "instance": "skylogs-heartbeat",
  "description": "Skylogs is reachable again"
}
```

## Notes

- Use a separate, independently-hosted checker — if it runs on the same infrastructure as Skylogs, a full outage can take down both at once and you'll never see the alert.
- The same pattern works for any external job: have the job call `fire-alert` on failure/missed run and `stop-alert` on success, using a stable `instance` id per job.
- {/* TODO: confirm whether Skylogs ships a built-in heartbeat/dead-man's-switch feature, or whether this external-checker pattern is the only supported approach */}
