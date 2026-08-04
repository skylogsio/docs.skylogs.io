---
id: rate-limits
title: Rate limits & errors
sidebar_position: 13
slug: /api/rate-limits
draft: true
---

# Rate limits & errors

:::info Under construction
This page is planned but not yet written. Remove `draft: true` from the frontmatter when it's ready to publish. Want to help? See [Contributing](/contributing).
:::

*Purpose: limits, error code catalog, retry guidance.*

## Confirmed so far

- Ingestion endpoints (`/fire-alert`) return `429` when rate limited.

## Planned outline

- Rate limit values and headers
- Error code catalog
- Retry/backoff guidance
- Idempotency on ingestion
