---
id: sdk-overview
title: Skylogs SDK
sidebar_position: 1
slug: /sdk
draft: true
---

# Skylogs SDK

:::info Under construction
This page is planned but not yet written. Remove `draft: true` from the frontmatter when it's ready to publish. Want to help? See [Contributing](/contributing).
:::

*Purpose: document the official Skylogs SDK(s) for calling the API from application code.*

## What exists today

A repository is reserved at [github.com/skylogsio/skylogs-python-sdk](https://github.com/skylogsio/skylogs-python-sdk) for an official Python SDK, but it currently contains no code — there's nothing installable yet.

In the meantime, integrate directly against the REST API — see [API reference](/api/rest-api) and [Authentication](/api/authentication) — or use [Skylogs CLI](/cli) for ad-hoc/scripted access.

## Planned outline

- Installation (`pip install ...`)
- Client initialization and authentication
- Alerts: create, list, resolve, acknowledge
- Endpoints, users, datasources
- Error handling and retries
- Versioning / compatibility with the REST API
