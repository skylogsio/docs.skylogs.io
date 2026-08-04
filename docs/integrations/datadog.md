---
id: datadog
title: Datadog
sidebar_position: 5
slug: /integrations/datadog
---

# Datadog

Use a Datadog webhook integration:

1. **Integrations → Webhooks → New**
2. URL: `https://skylogs.example.com/api/v1/ingest/datadog/<token>`
3. Add `@webhook-skylogs` to your monitor notification messages.

{/* TODO: document field mapping (monitor status, priority, tags) and recovery handling */}
