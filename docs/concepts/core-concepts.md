---
id: core-concepts
title: Core concepts
sidebar_position: 1
slug: /concepts
---

# Core concepts

Skylogs is built around **shared responsibility**: every team owns its own alerts, escalation paths, and part of the response, instead of funneling everything through a single ops team. These are the objects you'll work with.

## Alert

A single signal from a monitoring source — e.g. *"disk > 90% on db-14"*. Alerts arrive through [integrations](/integrations), are **deduplicated** (repeats of the same problem collapse into one alert via a fingerprint / `dedup_key`) and **correlated** (related alerts, like a host-down and its thirty dependent service alerts, are grouped).

An alert has a lifecycle: **firing → acknowledged → resolved** (or snoozed). Acknowledging stops the escalation clock; resolution can be manual or automatic when the source sends a recovery event.

## Incident

A managed event, usually created from one or more alerts, with an owner, a severity, a timeline, and a lifecycle: **open → mitigating → resolved → postmortem**. Alerts are signals; incidents are the coordinated response to signals that matter.

## Team

The ownership unit. Alerts route to teams; teams have escalation policies, on-call schedules, and members with roles. The shared-responsibility model lives here: routing rules map alert sources and tags to the teams that own them.

## Escalation policy

The ordered steps taken when an alert isn't acknowledged: *notify on-call → wait 5 minutes → notify secondary → wait 10 minutes → notify manager…* A good policy always ends in a step that cannot be missed.

## On-call schedule

Rotations that determine who receives a team's pages right now. Schedules support shift swaps and overrides, and on-call load is tracked per person.

## Endpoint

A way to reach a person: phone call, SMS, email, Slack, Microsoft Teams, Telegram. Endpoints are **verified** — Skylogs confirms deliverability so a critical page is never sent to a dead channel. Users set per-severity preferences (e.g., critical → phone; warning → Slack).

## Zone

A complete Skylogs deployment, typically one per datacenter or region. Zones federate through Sentinel: organizational data (users, teams, endpoints, schedules, policies) is synchronized everywhere, while alert data intentionally stays local to the zone that ingested it. See [Architecture](/architecture) for why.

## RCA report & postmortem

After resolution, the troubleshooting workspace produces an **RCA report** (root cause, propagation chain, supporting alerts) and the incident timeline becomes a **postmortem** (what happened, when, who did what, impact, action items).
