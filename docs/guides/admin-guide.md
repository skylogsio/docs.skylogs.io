---
id: admin-guide
title: Admin guide
sidebar_position: 2
slug: /admin-guide
---

# Admin guide

This guide is for Skylogs administrators: users and RBAC, teams, notification channels, routing, status pages, and operational maintenance. For installation see [Installation](/quick-start); for HA and multi-zone topology see [Deployment](/deployment).

## First steps after installation

1. Change the default admin password and create your own admin account.
2. Configure at least one notification channel (below) and verify it works.
3. Create teams and invite users.
4. Create an integration ([Integrations](/integrations)) and fire a test alert end to end.

## Users, roles, and RBAC

Skylogs implements role-based access control aligned with the shared-responsibility model: teams own their alerts and policies; global admin rights stay rare.

| Role | Scope | Typical use |
|---|---|---|
| **Admin** | Instance-wide | Platform owners: channels, integrations, global settings |
| **Team manager** | One or more teams | Owns schedules, escalation policies, team membership |
| **Responder** | Team | Handles alerts and incidents, edits own endpoints |
| **Viewer** | Team or instance | Read-only: dashboards, reports, status |

{/* TODO: replace with the real role model */}

Principles worth enforcing:

- Give teams **manager** rights over their own space instead of adding admins.
- Use **service accounts** with scoped tokens for API integrations — never a human's token in automation.
- Review the **audit log** periodically for permission changes.

## Teams

Teams are the routing and ownership unit. For each team, configure **members** and roles, **on-call schedules** (rotations, shift lengths, timezone, override approval {/* TODO: confirm approval flow */}), and **escalation policies**. Every policy should end in a step that cannot be missed.

## Notification channels

Configure instance-wide channels; users then attach personal endpoints on each.

- **Email** — SMTP settings {/* TODO: env var names */}
- **SMS / Voice call** — gateway configuration {/* TODO: supported providers */}
- **Slack** — bot token, per-team channels; supports acknowledge-from-Slack {/* TODO: confirm */}
- **Microsoft Teams** — connector/webhook configuration
- **Telegram** — bot token

### Endpoint verification

- On creation, the user must confirm a verification message.
- Periodic re-verification can be enabled per channel type. {/* TODO: confirm */}
- Unverified or failing endpoints are flagged on the user profile and in the team readiness view; escalation policies can skip unverified endpoints and alert the team manager.

## Alert routing, deduplication, and noise control

- **Routing rules** map incoming alerts to teams by source, tags, severity, and resource.
- **Deduplication** collapses repeats by fingerprint / `dedup_key`.
- **Correlation** groups related alerts to keep responders out of alert storms.
- **Maintenance windows** suppress expected noise during planned work — scope them to tags/resources, never instance-wide.

Review the **unrouted alerts** view regularly: anything landing there has no owning team — a gap in your shared-responsibility map. {/* TODO: confirm feature name */}

## Status pages

Create public or private status pages per product/service: components, current state, incident updates, subscriber notifications. Branding (logo, domain) is configurable. {/* TODO: confirm custom domain support */}

## Reporting & SLA configuration

Define **services** and their SLA targets; Skylogs computes availability, MTTA, and MTTR per service over long periods. Schedule recurring reports to stakeholders. {/* TODO: confirm scheduled report delivery */}

## Audit log

All administrative and response actions are recorded: who changed a policy, who acknowledged what, which notifications were sent where. Use it for compliance evidence and post-incident review.

## Operational maintenance

- **Backups** — back up MongoDB data and configuration per zone; test restores. In multi-zone deployments alert data is zone-local: back up each zone. {/* TODO: link concrete backup/restore procedure */}
- **Upgrades** — follow release notes; in HA clusters upgrade nodes one at a time. A brief Raft leader election during a rolling upgrade is normal and loses no alerts.
- **Monitoring Skylogs itself** — expose health endpoints to an *external* checker and configure a dead-man's-switch (a heartbeat alert that fires when Skylogs stops reporting). The incident platform must not be its own only observer. {/* TODO: document health endpoints/metrics */}
- **Retention** — configure alert and incident retention to match compliance requirements. {/* TODO: confirm retention settings */}

## Security checklist

- [ ] Default credentials changed; admin accounts minimal
- [ ] TLS on the UI/API and between zones
- [ ] API tokens scoped and rotated; service accounts for automation
- [ ] RBAC reviewed; team managers own team config
- [ ] Audit log retention configured
- [ ] Backups encrypted and restore-tested
