---
id: splunk
title: Splunk
sidebar_position: 6
slug: /integrations/splunk
---

# Splunk

Use a Splunk alert action (webhook):

1. In your saved search / alert: **Trigger actions → Webhook**
2. URL: `https://skylogs.example.com/api/v1/ingest/splunk/<token>`

Useful for SOC workflows: route security alerts to a security team with its own escalation policy, separate from infrastructure alerting.

{/* TODO: document payload mapping and severity translation */}
