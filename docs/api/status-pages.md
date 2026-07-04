---
id: api-status-pages
title: Status pages
sidebar_position: 9
slug: /api/status-pages
---

# Status pages

:::note Generated reference
This page is generated from the OpenAPI spec (`scripts/generate_api_docs.py`). Do not edit by hand — regenerate when the API changes.
:::

Create and manage status pages.

All endpoints require `Authorization: Bearer <accessToken>` — see [Authentication](/api/authentication).

| Endpoint | Summary |
|---|---|
| [`GET /api/v1/status/all`](#get-api-v1-status-all) | List all status pages (public) |
| [`GET /api/v1/status`](#get-api-v1-status) | List status pages (paginated) |
| [`POST /api/v1/status`](#post-api-v1-status) | Create status page |
| [`GET /api/v1/status/{id}`](#get-api-v1-status-id) | Get status page by id |
| [`PUT /api/v1/status/{id}`](#put-api-v1-status-id) | Update status page |
| [`DELETE /api/v1/status/{id}`](#delete-api-v1-status-id) | Delete status page |

### `GET /api/v1/status/all` {#get-api-v1-status-all}

**List all status pages (public)**

No JWT required. Used by public status dashboards.

**Responses:** `200` All status records

### `GET /api/v1/status` {#get-api-v1-status}

**List status pages (paginated)**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `page` | query |  | integer |  |
| `perPage` | query |  | integer |  |
| `name` | query |  | string |  |

**Responses:** `200` Paginated status pages

### `POST /api/v1/status` {#post-api-v1-status}

**Create status page**

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | ✅ |  |
| `tags` | array of string | ✅ | Non-empty array of tag names to aggregate alerts |

**Responses:** `200` Created · `422` Validation error

### `GET /api/v1/status/{id}` {#get-api-v1-status-id}

**Get status page by id**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Status page · `404` Not Found

### `PUT /api/v1/status/{id}` {#put-api-v1-status-id}

**Update status page**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | ✅ |  |
| `tags` | array of string | ✅ | Non-empty array of tag names to aggregate alerts |

**Responses:** `200` Updated

### `DELETE /api/v1/status/{id}` {#delete-api-v1-status-id}

**Delete status page**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Deleted

