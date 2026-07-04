---
id: api-users-teams
title: Users & teams
sidebar_position: 5
slug: /api/users-teams
---

# Users & teams

:::note Generated reference
This page is generated from the OpenAPI spec (`scripts/generate_api_docs.py`). Do not edit by hand — regenerate when the API changes.
:::

Manage users, teams, and ownership transfer.

All endpoints require `Authorization: Bearer <accessToken>` — see [Authentication](/api/authentication).

## Users

| Endpoint | Summary |
|---|---|
| [`GET /api/v1/user`](#get-api-v1-user) | List users (paginated) |
| [`POST /api/v1/user`](#post-api-v1-user) | Create user |
| [`GET /api/v1/user/all`](#get-api-v1-user-all) | List all users |
| [`GET /api/v1/user/{id}`](#get-api-v1-user-id) | Get user by id |
| [`PUT /api/v1/user/{id}`](#put-api-v1-user-id) | Update user |
| [`DELETE /api/v1/user/{id}`](#delete-api-v1-user-id) | Delete user |
| [`PUT /api/v1/user/pass/{id}`](#put-api-v1-user-pass-id) | Change user password (admin) |
| [`POST /api/v1/user/changeOwner`](#post-api-v1-user-changeowner) | Transfer alert rules and endpoints between users |

### `GET /api/v1/user` {#get-api-v1-user}

**List users (paginated)**

Requires owner or manager role.

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `page` | query |  | integer |  |
| `perPage` | query |  | integer |  |
| `username` | query |  | string | Filter by username (partial match) |

**Responses:** `200` Paginated users; each item includes `roles` string array · `403` Forbidden

### `POST /api/v1/user` {#post-api-v1-user}

**Create user**

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `username` | string | ✅ |  |
| `name` | string | ✅ |  |
| `password` | string | ✅ |  |
| `confirmPassword` | string | ✅ |  |
| `role` | string (owner \| manager \| member) | ✅ |  |

**Responses:** `200` Created · `403` Forbidden · `422` Validation error

### `GET /api/v1/user/all` {#get-api-v1-user-all}

**List all users**

Unpaginated list for dropdowns and sharing UI.

**Responses:** `200` All users

### `GET /api/v1/user/{id}` {#get-api-v1-user-id}

**Get user by id**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` User · `404` Not Found

### `PUT /api/v1/user/{id}` {#put-api-v1-user-id}

**Update user**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `username` | string | ✅ |  |
| `name` | string | ✅ |  |
| `role` | string (owner \| manager \| member) | ✅ |  |

**Responses:** `200` Updated · `403` Forbidden

### `DELETE /api/v1/user/{id}` {#delete-api-v1-user-id}

**Delete user**

Reassigns owned endpoints and alert rules to the system admin user. Cannot delete `admin`.

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Deleted user record · `403` Forbidden

### `PUT /api/v1/user/pass/{id}` {#put-api-v1-user-pass-id}

**Change user password (admin)**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `password` | string | ✅ |  |
| `confirmPassword` | string | ✅ |  |

**Responses:** `200` Password updated · `403` Forbidden

### `POST /api/v1/user/changeOwner` {#post-api-v1-user-changeowner}

**Transfer alert rules and endpoints between users**

Owner role only. Moves all alert rules and endpoints from `fromUser` to `toUser`.

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `fromUser` | string | ✅ | Source user id |
| `toUser` | string | ✅ | Target user id |

**Responses:** `200` Ownership transferred · `403` Forbidden

## Teams

| Endpoint | Summary |
|---|---|
| [`GET /api/v1/team`](#get-api-v1-team) | Get list of teams |
| [`POST /api/v1/team`](#post-api-v1-team) | Create new team |
| [`GET /api/v1/team/all`](#get-api-v1-team-all) | Get all of teams |
| [`GET /api/v1/team/{id}`](#get-api-v1-team-id) | Get team by ID |
| [`PUT /api/v1/team/{id}`](#put-api-v1-team-id) | Update team |
| [`DELETE /api/v1/team/{id}`](#delete-api-v1-team-id) | Delete team |

### `GET /api/v1/team` {#get-api-v1-team}

**Get list of teams**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `page` | query |  | integer | Page number |
| `perPage` | query |  | integer |  |
| `name` | query |  | string |  |

**Responses:** `200` List of teams

### `POST /api/v1/team` {#post-api-v1-team}

**Create new team**

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | ✅ | Example: `Customer Service` |
| `ownerId` | string | ✅ |  |
| `userIds` | array of string | ✅ |  |
| `description` | string |  |  |

**Responses:** `201` Team created · `422` Validation error

### `GET /api/v1/team/all` {#get-api-v1-team-all}

**Get all of teams**

**Responses:** `200` List of teams

### `GET /api/v1/team/{id}` {#get-api-v1-team-id}

**Get team by ID**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Team details · `404` Not found

### `PUT /api/v1/team/{id}` {#put-api-v1-team-id}

**Update team**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | ✅ |  |
| `ownerId` | string | ✅ |  |
| `userIds` | array of string | ✅ |  |
| `description` | string |  |  |

**Responses:** `200` Team updated · `404` Not found

### `DELETE /api/v1/team/{id}` {#delete-api-v1-team-id}

**Delete team**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Team deleted · `404` Not found

