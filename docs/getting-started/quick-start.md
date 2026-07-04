---
id: quick-start
title: Quick start — your first alert
sidebar_position: 2
slug: /quick-start
---

# Quick start — your first alert

You've [installed Skylogs](/installation). In the next ten minutes you'll verify the entire pipeline — ingestion, routing, escalation, and notification — with one test alert.

## 1. Add and verify your notification endpoint

1. Go to **Profile → Endpoints** and add a channel (email is the fastest to test).
2. Complete verification — Skylogs sends a confirmation you must acknowledge. Verification is what guarantees a critical page is never sent to a dead channel.

## 2. Create a team and a minimal escalation policy

1. **Teams → New team** — e.g. `demo`.
2. Add yourself as a member and set yourself on call.
3. Create an escalation policy: *notify on-call immediately*. That's enough for the test.

## 3. Create an API token

**Settings → API tokens → New token.** Copy it. {/* TODO: confirm menu path */}

## 4. Fire the test alert

```bash
curl -X POST http://localhost:PORT/api/v1/alerts \
  -H "Authorization: Bearer <YOUR_API_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "source": "quick-start",
    "severity": "critical",
    "summary": "Quick start test alert",
    "service": "demo"
  }'
```

{/* TODO: replace with the real ingestion endpoint and minimal payload */}

Within seconds you should see the alert on the dashboard **and** receive a notification on your verified endpoint. That's the full pipeline working end to end.

## 5. Acknowledge and resolve

Acknowledge the alert (from the notification or the dashboard) — note that the escalation clock stops. Then resolve it.

## Next steps

- Connect a real datasource: [Prometheus / Alertmanager](/integrations/prometheus-alertmanager) is the most common starting point; [Zabbix](/integrations/zabbix) if you're a network/datacenter shop.
- Set up real [schedules and escalation policies](/user-guide).
- Planning production? Read [Deployment](/deployment) before you rely on a single node.
