---
id: grafana
title: Grafana
sidebar_position: 3
slug: /integrations/grafana
---

# Grafana

Grafana Alerting supports webhook contact points:

1. In Grafana: **Alerting → Contact points → New contact point → Webhook**
2. URL: `https://skylogs.example.com/api/v1/ingest/grafana/<token>`
3. Select the contact point in your notification policies.

Resolved notifications from Grafana auto-resolve the corresponding Skylogs alert.

{/* TODO: verify payload mapping and add a screenshot of the contact point form */}
