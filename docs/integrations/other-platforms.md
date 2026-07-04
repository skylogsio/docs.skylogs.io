---
id: other-platforms
title: Datadog, Splunk, Elastic, PMM
sidebar_position: 5
slug: /integrations/other-platforms
---

# Datadog, Splunk, Elastic, PMM

## Datadog

Use a Datadog webhook integration:

1. **Integrations → Webhooks → New**
2. URL: `https://skylogs.example.com/api/v1/ingest/datadog/<token>`
3. Add `@webhook-skylogs` to your monitor notification messages.

## Splunk

Use a Splunk alert action (webhook):

1. In your saved search / alert: **Trigger actions → Webhook**
2. URL: `https://skylogs.example.com/api/v1/ingest/splunk/<token>`

Useful for SOC workflows: route security alerts to a security team with its own escalation policy, separate from infrastructure alerting.

## Elastic / ELK

Kibana alerting rules support a webhook connector — point it at `https://skylogs.example.com/api/v1/ingest/elastic/<token>`. {/* TODO: document expected payload/template */}

## PMM (Percona Monitoring and Management)

PMM's alerting is Alertmanager-compatible — configure the Skylogs [Alertmanager receiver URL](/integrations/prometheus-alertmanager) in PMM's alert settings. Database-specific labels (service, node, cluster) are preserved as tags for routing.
