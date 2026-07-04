---
id: intro
title: What is Skylogs?
sidebar_position: 1
slug: /
---

# What is Skylogs?

Skylogs is an **open-source incident response platform** — an alternative to tools like incident.io, PagerDuty, and Opsgenie that you run on your own infrastructure.

It consolidates alerts from your observability stack (Prometheus, Grafana, Zabbix, Datadog, Splunk, ELK, and anything with a webhook), routes them to the right people through escalation policies and on-call schedules, and manages the full incident lifecycle — from first alert to root cause analysis and postmortem.

Skylogs is built on one core belief:

> **Incident response is an organizational responsibility, not just an infrastructure concern.**

Instead of concentrating incident response in a single ops team, Skylogs implements a **shared responsibility model**: every team owns its alerts, its escalation paths, and its part of the response — with RBAC and clear ownership boundaries keeping it safe.

## Why Skylogs?

- **🔓 Truly open source** — MIT-licensed, self-hosted, no feature-gated core. Your alert and incident data never leaves your infrastructure.
- **🤝 Shared responsibility by design** — team-scoped alert ownership, per-user notification preferences, and role-based access control make cross-team incident response practical.
- **🔍 Root cause, not just paging** — a built-in troubleshooting workspace helps responders find root cause during the incident, then export RCA reports and postmortems.
- **🌍 Built to survive disasters — including its own** — multi-zone federation (Sentinel) plus Raft-based high availability. See [Architecture](/architecture).

## Where to start

| I want to… | Go to |
|---|---|
| Install Skylogs and fire a test alert | [Installation](/installation) → [Quick start](/quick-start) |
| Understand the moving parts | [Core concepts](/concepts) and [Architecture](/architecture) |
| Connect Prometheus, Zabbix, Grafana, … | [Integrations](/integrations) |
| Run it in production with HA / multi-zone | [Deployment](/deployment) |
| Use it as a responder or on-call engineer | [User guide](/user-guide) |
| Administer users, teams, and channels | [Admin guide](/admin-guide) |
| Automate with the REST API | [API reference](/api) |

## Get involved

Skylogs is developed in the open at [github.com/skylogsio/skylogs](https://github.com/skylogsio/skylogs). Bug reports, feature requests, integrations, and documentation improvements are all welcome — see [Contributing](/contributing).
