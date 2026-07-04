---
id: user-guide
title: User guide
sidebar_position: 1
slug: /user-guide
---

# User guide

This guide is for responders and team members using Skylogs day to day: handling alerts, being on call, responding to incidents, and producing RCA and postmortem reports. If any term is unfamiliar, see [Core concepts](/concepts).

## Setting up your profile

1. **Add your notification endpoints** (Profile → Endpoints) and complete verification for each — Skylogs sends a confirmation you must acknowledge. Unverified endpoints are flagged and should not carry critical alerts.
2. **Set your notification rules** — which channel for which severity. A common pattern: critical → phone call + SMS; warning → Slack; info → email digest. {/* TODO: confirm feature naming */}
3. **Check your on-call schedule** (Schedules → your team) so you know your shifts.

## Handling an alert

When you're paged:

1. **Acknowledge** — this stops the escalation clock and tells your team someone owns it. Acknowledge from the notification itself or the dashboard. {/* TODO: confirm ack-from-channel support */}
2. **Investigate** — the alert view shows the source payload, correlated alerts, the affected resource, and recent history for the same `dedup_key`.
3. **Resolve** when fixed, or **escalate to an incident** if the impact is real and needs coordination.

If you can't take it: **reassign** to a teammate or **snooze** with a reason. Never let an unacknowledged critical alert sit — the escalation policy will move past you, and that's by design.

## Being on call

- Your schedule shows upcoming shifts; you receive a handoff notification at shift start. {/* TODO: confirm */}
- **Overrides / shift swaps:** request an override on the schedule page; the covering person confirms. No config files, no asking an admin.
- **On-call load** is tracked — paging volume per person supports fair rotation and burnout prevention.

## Responding to an incident

1. **Create the incident** from one or more alerts (or manually). Set severity and, for larger events, an incident commander.
2. **Coordinate in the timeline** — acks, status changes, and notifications are recorded automatically; add manual entries for decisions and observations. The timeline becomes the raw material of your postmortem.
3. **Use the troubleshooting workspace** to work toward root cause: correlated alerts are grouped, and the dependency view helps distinguish cause from symptom (one host-down alert explaining thirty service alerts). {/* TODO: align with actual troubleshooting page features */}
4. **Update the status page** if the incident is customer-facing — publish updates to subscribers directly from the incident.
5. **Resolve** when mitigated. The incident moves to the postmortem stage.

## RCA reports and postmortems

- **RCA report** — generated from the troubleshooting workspace: identified root cause, propagation chain, supporting alerts. Export to share with stakeholders. {/* TODO: confirm export formats */}
- **Postmortem** — built from the incident timeline: what happened, when, who did what, impact duration, action items. Edit collaboratively before publishing.

Good habit: hold the postmortem review within a few days of resolution, while context is fresh — and keep it blameless. The report documents systems and processes, not fault.

## Dashboards and reports

- **My alerts / team alerts** — live views filtered to what you own.
- **SLA reports** — per-service availability over long periods.
- **MTTA / MTTR** — how fast your team acknowledges and resolves, trended over time.

## Tips

- Keep `dedup_key` discipline in your monitoring rules — good keys mean one alert per problem instead of a storm.
- Route by tags (team, env, service) rather than one catch-all policy — that's the shared-responsibility model working for you.
- Re-verify endpoints after changing phone numbers or leaving chat workspaces.
