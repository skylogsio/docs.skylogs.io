---
id: migrating
title: Migrating from Opsgenie / PagerDuty
sidebar_position: 4
slug: /migrating
draft: true
---

# Migrating from Opsgenie / PagerDuty

:::info Under construction
This page is planned but not yet written. Remove `draft: true` from the frontmatter when it's ready to publish. Want to help? See [Contributing](/contributing).
:::

*Purpose: help teams leaving Opsgenie (sunset) or PagerDuty move to Skylogs with minimal risk.*

## Planned outline

- What maps to what: services→teams, escalation policies, schedules, users
- Export from Opsgenie / PagerDuty (API scripts)
- Import into Skylogs (API scripts / import tool)
- Running both systems in parallel during cutover
- Redirecting integrations (Alertmanager receivers, webhooks)
- Decommission checklist
