---
id: integrations-overview
title: Overview
sidebar_position: 1
slug: /integrations
---

# Integrations overview

Skylogs ingests alerts from your existing monitoring stack. Every integration feeds the same pipeline: **parsing → deduplication → correlation → routing → escalation → notification.**

If your tool isn't listed, use the [generic webhook](/integrations/generic-webhook) or the [REST API](/api) — anything that can send an HTTP POST can page through Skylogs.

## How ingestion works

Each integration you create in Skylogs gets a unique ingestion URL with an embedded token:

```
https://skylogs.example.com/api/v1/ingest/<integration-type>/<token>
```

{/* TODO: confirm real URL scheme */}

Point your monitoring tool at that URL. Skylogs parses the tool's native payload format — you do not need to reshape the data.

## Available integrations

| Source | Guide |
|---|---|
| Prometheus / Alertmanager / vmalert | [Prometheus & Alertmanager](/integrations/prometheus-alertmanager) |
| Grafana Alerting | [Grafana](/integrations/grafana) |
| Zabbix | [Zabbix](/integrations/zabbix) |
| Datadog | [Datadog](/integrations/datadog) |
| Splunk | [Splunk](/integrations/splunk) |
| Elastic / ELK | [Elastic](/integrations/elastic) |
| PMM (Percona) | [PMM](/integrations/pmm) |
| Anything else | [Generic webhook](/integrations/generic-webhook) |

## Outbound notification channels

Skylogs delivers notifications through **phone call, SMS, email, Slack, Microsoft Teams, and Telegram**. Channel setup is in the [Admin guide](/admin-guide); personal endpoint preferences are in the [User guide](/user-guide). Every endpoint can be **verified**, so a critical page is never sent to a dead channel.

## Requesting an integration

Open a [feature request](https://github.com/skylogsio/skylogs/issues) with the tool name and a sample of its webhook payload. Integrations are one of the easiest ways to [contribute](/contributing).
