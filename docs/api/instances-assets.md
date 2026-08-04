---
id: api-instances-assets
title: Instances & profile assets
sidebar_position: 10
slug: /api/instances-assets
---

# Instances & profile assets

:::note Generated reference
This page is generated from the OpenAPI spec (`scripts/generate_api_docs.py`). Do not edit by hand — regenerate when the API changes.
:::

Skylogs instances represent connected Skylogs deployments (e.g. zones). Profile assets provision alert rules from asset definitions.

All endpoints require `Authorization: Bearer <accessToken>` — see [Authentication](/api/authentication).

## SkylogsInstance

| Endpoint | Summary |
|---|---|
| [`GET /api/v1/skylogs-instance`](#get-api-v1-skylogs-instance) | List Skylogs instances (paginated) |
| [`POST /api/v1/skylogs-instance`](#post-api-v1-skylogs-instance) | Create Skylogs instance |
| [`GET /api/v1/skylogs-instance/all`](#get-api-v1-skylogs-instance-all) | List all Skylogs instances |
| [`GET /api/v1/skylogs-instance/status/{id}`](#get-api-v1-skylogs-instance-status-id) | Check if instance is connected |
| [`GET /api/v1/skylogs-instance/{id}`](#get-api-v1-skylogs-instance-id) | Get Skylogs instance by id |
| [`PUT /api/v1/skylogs-instance/{id}`](#put-api-v1-skylogs-instance-id) | Update Skylogs instance |
| [`DELETE /api/v1/skylogs-instance/{id}`](#delete-api-v1-skylogs-instance-id) | Delete Skylogs instance |

### `GET /api/v1/skylogs-instance` {#get-api-v1-skylogs-instance}

**List Skylogs instances (paginated)**

Owner role only.

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `page` | query |  | integer |  |
| `perPage` | query |  | integer |  |
| `name` | query |  | string | Filter by name (partial match) |

**Responses:** `200` Paginated instances (token hidden)

### `POST /api/v1/skylogs-instance` {#post-api-v1-skylogs-instance}

**Create Skylogs instance**

Generates a unique `token` for agent authentication. Owner role only.

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | ✅ |  |
| `type` | string | ✅ |  |
| `url` | string | ✅ |  |

**Responses:** `200` Created · `422` Validation error

### `GET /api/v1/skylogs-instance/all` {#get-api-v1-skylogs-instance-all}

**List all Skylogs instances**

**Responses:** `200` All instances without pagination

### `GET /api/v1/skylogs-instance/status/{id}` {#get-api-v1-skylogs-instance-status-id}

**Check if instance is connected**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Connection status

### `GET /api/v1/skylogs-instance/{id}` {#get-api-v1-skylogs-instance-id}

**Get Skylogs instance by id**

Owner role only.

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Instance · `404` Not Found

### `PUT /api/v1/skylogs-instance/{id}` {#put-api-v1-skylogs-instance-id}

**Update Skylogs instance**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | ✅ |  |
| `type` | string | ✅ |  |
| `url` | string | ✅ |  |

**Responses:** `200` Updated

### `DELETE /api/v1/skylogs-instance/{id}` {#delete-api-v1-skylogs-instance-id}

**Delete Skylogs instance**

Also removes related health cluster data. Owner role only.

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Deleted instance

## ProfileAsset

| Endpoint | Summary |
|---|---|
| [`GET /api/v1/profile/asset`](#get-api-v1-profile-asset) | List profile assets (paginated) |
| [`POST /api/v1/profile/asset`](#post-api-v1-profile-asset) | Create profile asset and provision alert rules |
| [`GET /api/v1/profile/asset/{id}`](#get-api-v1-profile-asset-id) | Get profile asset by id |
| [`PUT /api/v1/profile/asset/{id}`](#put-api-v1-profile-asset-id) | Update profile asset |
| [`DELETE /api/v1/profile/asset/{id}`](#delete-api-v1-profile-asset-id) | Delete profile asset |

### `GET /api/v1/profile/asset` {#get-api-v1-profile-asset}

**List profile assets (paginated)**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `page` | query |  | integer |  |
| `perPage` | query |  | integer |  |
| `name` | query |  | string |  |

**Responses:** `200` Paginated profile assets with `user` relation

### `POST /api/v1/profile/asset` {#post-api-v1-profile-asset}

**Create profile asset and provision alert rules**

Creates alert rules from `config` via ProfileService and stores their ids in `createdAlertRuleIds`.

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | ✅ |  |
| `ownerId` | string | ✅ |  |
| `config` | object | ✅ |  |

**Responses:** `200` Created

### `GET /api/v1/profile/asset/{id}` {#get-api-v1-profile-asset-id}

**Get profile asset by id**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Profile asset · `404` Not Found

### `PUT /api/v1/profile/asset/{id}` {#put-api-v1-profile-asset-id}

**Update profile asset**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | ✅ |  |
| `ownerId` | string | ✅ |  |
| `config` | object | ✅ |  |

**Responses:** `200` Updated

### `DELETE /api/v1/profile/asset/{id}` {#delete-api-v1-profile-asset-id}

**Delete profile asset**

Deletes linked alert rules via ProfileService.

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Deleted asset

