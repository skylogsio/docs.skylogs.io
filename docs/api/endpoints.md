---
id: api-endpoints
title: Notification endpoints
sidebar_position: 6
slug: /api/endpoints
---

# Notification endpoints

:::note Generated reference
This page is generated from the OpenAPI spec (`scripts/generate_api_docs.py`). Do not edit by hand — regenerate when the API changes.
:::

Endpoints are the channels through which a user or flow is notified (SMS, call, email, Telegram, …). Endpoints are verified with an OTP before they can carry alerts.

All endpoints require `Authorization: Bearer <accessToken>` — see [Authentication](/api/authentication).

| Endpoint | Summary |
|---|---|
| [`GET /api/v1/endpoint`](#get-api-v1-endpoint) | Get list of endpoints |
| [`POST /api/v1/endpoint`](#post-api-v1-endpoint) | Create new endpoint |
| [`GET /api/v1/endpoint/indexFlow`](#get-api-v1-endpoint-indexflow) | Get list of flow endpoints |
| [`GET /api/v1/endpoint/createFlowEndpoints`](#get-api-v1-endpoint-createflowendpoints) | Get endpoints available for flow creation |
| [`GET /api/v1/endpoint/{id}`](#get-api-v1-endpoint-id) | Get endpoint by ID |
| [`PUT /api/v1/endpoint/{id}`](#put-api-v1-endpoint-id) | Update endpoint |
| [`DELETE /api/v1/endpoint/{id}`](#delete-api-v1-endpoint-id) | Delete endpoint |
| [`POST /api/v1/endpoint/sendOTP`](#post-api-v1-endpoint-sendotp) | send OTP code |
| [`POST /api/v1/endpoint/changeOwner/{id}`](#post-api-v1-endpoint-changeowner-id) | Change endpoint owner |

### `GET /api/v1/endpoint` {#get-api-v1-endpoint}

**Get list of endpoints**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `page` | query |  | integer | Page number |
| `perPage` | query |  | integer | Items per page |
| `name` | query |  | string | Filter by name |

**Responses:** `200` List of endpoints · `401` Unauthorized

### `POST /api/v1/endpoint` {#post-api-v1-endpoint}

**Create new endpoint**

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | ✅ | Example: `My SMS Endpoint` |
| `type` | string (sms \| call \| email \| telegram \| bale \| teams \| matter-most \| flow) | ✅ | Example: `sms` |
| `value` | string | ✅ | Example: `09000000000` |
| `accessUserIds` | array of string |  |  |
| `accessTeamIds` | array of string |  |  |
| `otpCode` | string |  | For sms, call, email type the otp verification is required Example: `12345` |
| `chatId` | string |  | For Telegram type |
| `threadId` | string |  | For Telegram type |
| `botToken` | string |  | For Telegram type |
| `steps` | array of object |  | For flow type - array of steps with wait and endpoint types |

**Responses:** `201` Endpoint created successfully. Response structure varies based on endpoint type. · `422` Validation error

### `GET /api/v1/endpoint/indexFlow` {#get-api-v1-endpoint-indexflow}

**Get list of flow endpoints**

**Responses:** `200` List of flow endpoints · `401` Unauthorized

### `GET /api/v1/endpoint/createFlowEndpoints` {#get-api-v1-endpoint-createflowendpoints}

**Get endpoints available for flow creation**

**Responses:** `200` List of available endpoints · `401` Unauthorized

### `GET /api/v1/endpoint/{id}` {#get-api-v1-endpoint-id}

**Get endpoint by ID**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Endpoint details. Response structure varies based on endpoint type (sms, email, telegram, flow, etc.) · `404` Not found

### `PUT /api/v1/endpoint/{id}` {#put-api-v1-endpoint-id}

**Update endpoint**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | ✅ | Example: `Updated Endpoint Name` |
| `type` | string (sms \| call \| email \| telegram \| bale \| teams \| matter-most \| flow) | ✅ | Example: `telegram` |
| `value` | string | ✅ | Example: `09000000000` |
| `accessUserIds` | array of string |  |  |
| `accessTeamIds` | array of string |  |  |
| `otpCode` | string |  | For sms, call, email type the otp verification is required if the value updated in process Example: `12345` |
| `chatId` | string |  | For Telegram type |
| `threadId` | string |  | For Telegram type |
| `botToken` | string |  | For Telegram type |
| `steps` | array of object |  | For flow type - array of steps with wait and endpoint types |

**Responses:** `200` Endpoint updated successfully. Response structure varies based on endpoint type. · `404` Not found

### `DELETE /api/v1/endpoint/{id}` {#delete-api-v1-endpoint-id}

**Delete endpoint**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Endpoint deleted successfully · `404` Not found

### `POST /api/v1/endpoint/sendOTP` {#post-api-v1-endpoint-sendotp}

**send OTP code**

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | string (sms \| call \| email) | ✅ | Example: `sms` |
| `value` | string | ✅ | Example: `09000000000` |

**Responses:** `201` OTP code has been sent successfully. · `422` Validation error

### `POST /api/v1/endpoint/changeOwner/{id}` {#post-api-v1-endpoint-changeowner-id}

**Change endpoint owner**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `userId` | string | ✅ | Example: `user123` |

**Responses:** `200` Owner changed successfully · `404` Not found

