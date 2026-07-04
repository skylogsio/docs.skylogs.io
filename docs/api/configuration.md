---
id: api-configuration
title: Notification provider configs
sidebar_position: 8
slug: /api/configuration
---

# Notification provider configs

:::note Generated reference
This page is generated from the OpenAPI spec (`scripts/generate_api_docs.py`). Do not edit by hand — regenerate when the API changes.
:::

Instance-wide provider configuration for call, email, SMS, and Telegram delivery, plus the Skylogs cluster configuration. Providers support a **default** and a **backup** config — if the default provider fails, delivery falls back to the backup.

All endpoints require `Authorization: Bearer <accessToken>` — see [Authentication](/api/authentication).

## ConfigCall

| Endpoint | Summary |
|---|---|
| [`GET /api/v1/config/call`](#get-api-v1-config-call) | List call configuration |
| [`POST /api/v1/config/call`](#post-api-v1-config-call) | Create call config |
| [`GET /api/v1/config/call/{id}`](#get-api-v1-config-call-id) | Get config by id |
| [`PUT /api/v1/config/call/{id}`](#put-api-v1-config-call-id) | Update call config |
| [`DELETE /api/v1/config/call/{id}`](#delete-api-v1-config-call-id) | Delete call config |
| [`POST /api/v1/config/call/make-default/{id}`](#post-api-v1-config-call-make-default-id) | make default config call |
| [`POST /api/v1/config/call/make-backup/{id}`](#post-api-v1-config-call-make-backup-id) | make backup config call |
| [`GET /api/v1/config/call/providers`](#get-api-v1-config-call-providers) | List available call config providers |

### `GET /api/v1/config/call` {#get-api-v1-config-call}

**List call configuration**

**Responses:** `200` OK

### `POST /api/v1/config/call` {#post-api-v1-config-call}

**Create call config**

**Request body** (`application/json`)

The body is selected by the `provider` discriminator:

#### Kave Negar Call Config

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | ✅ | Example: `Primary Call` |
| `provider` | string (kaveNegar) | ✅ | Example: `kaveNegar` |
| `apiToken` | string | ✅ | Example: `your-api-token-here` |

**Responses:** `201` Created · `422` Validation error

### `GET /api/v1/config/call/{id}` {#get-api-v1-config-call-id}

**Get config by id**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` OK · `404` Not Found

### `PUT /api/v1/config/call/{id}` {#put-api-v1-config-call-id}

**Update call config**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Request body** (`application/json`)

The body is selected by the `provider` discriminator:

#### Kave Negar Call Config

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | ✅ | Example: `Primary Call` |
| `provider` | string (kaveNegar) | ✅ | Example: `kaveNegar` |
| `apiToken` | string | ✅ | Example: `your-api-token-here` |

**Responses:** `200` OK · `404` Not Found

### `DELETE /api/v1/config/call/{id}` {#delete-api-v1-config-call-id}

**Delete call config**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Deleted · `404` Not Found

### `POST /api/v1/config/call/make-default/{id}` {#post-api-v1-config-call-make-default-id}

**make default config call**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` OK

### `POST /api/v1/config/call/make-backup/{id}` {#post-api-v1-config-call-make-backup-id}

**make backup config call**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` OK

### `GET /api/v1/config/call/providers` {#get-api-v1-config-call-providers}

**List available call config providers**

**Responses:** `200` OK

## ConfigEmail

| Endpoint | Summary |
|---|---|
| [`GET /api/v1/config/email`](#get-api-v1-config-email) | List email configuration |
| [`POST /api/v1/config/email`](#post-api-v1-config-email) | Create email config |
| [`GET /api/v1/config/email/{id}`](#get-api-v1-config-email-id) | Get config by id |
| [`PUT /api/v1/config/email/{id}`](#put-api-v1-config-email-id) | Update email config |
| [`DELETE /api/v1/config/email/{id}`](#delete-api-v1-config-email-id) | Delete email config |
| [`POST /api/v1/config/email/make-default/{id}`](#post-api-v1-config-email-make-default-id) | make default config email |
| [`POST /api/v1/config/email/make-backup/{id}`](#post-api-v1-config-email-make-backup-id) | make backup config email |
| [`GET /api/v1/config/email/providers`](#get-api-v1-config-email-providers) | List available email config providers |

### `GET /api/v1/config/email` {#get-api-v1-config-email}

**List email configuration**

**Responses:** `200` OK

### `POST /api/v1/config/email` {#post-api-v1-config-email}

**Create email config**

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Example: `Primary Email` |
| `host` | string |  | Example: `email.skylogs.io` |
| `port` | string |  | Example: `80` |
| `username` | string |  | Example: `admin` |
| `password` | string |  | Example: `123456789` |
| `fromAddress` | string |  | Example: `Info@skylogs.io` |

**Responses:** `201` Created · `422` Validation error

### `GET /api/v1/config/email/{id}` {#get-api-v1-config-email-id}

**Get config by id**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` OK · `404` Not Found

### `PUT /api/v1/config/email/{id}` {#put-api-v1-config-email-id}

**Update email config**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Example: `Primary Email` |
| `host` | string |  | Example: `email.skylogs.io` |
| `port` | string |  | Example: `80` |
| `username` | string |  | Example: `admin` |
| `password` | string |  | Example: `123456789` |
| `fromAddress` | string |  | Example: `Info@skylogs.io` |

**Responses:** `200` OK · `404` Not Found

### `DELETE /api/v1/config/email/{id}` {#delete-api-v1-config-email-id}

**Delete email config**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Deleted · `404` Not Found

### `POST /api/v1/config/email/make-default/{id}` {#post-api-v1-config-email-make-default-id}

**make default config email**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` OK

### `POST /api/v1/config/email/make-backup/{id}` {#post-api-v1-config-email-make-backup-id}

**make backup config email**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` OK

### `GET /api/v1/config/email/providers` {#get-api-v1-config-email-providers}

**List available email config providers**

**Responses:** `200` OK

## ConfigSms

| Endpoint | Summary |
|---|---|
| [`GET /api/v1/config/sms`](#get-api-v1-config-sms) | List sms configuration |
| [`POST /api/v1/config/sms`](#post-api-v1-config-sms) | Create sms config |
| [`GET /api/v1/config/sms/{id}`](#get-api-v1-config-sms-id) | Get config by id |
| [`PUT /api/v1/config/sms/{id}`](#put-api-v1-config-sms-id) | Update sms config |
| [`DELETE /api/v1/config/sms/{id}`](#delete-api-v1-config-sms-id) | Delete sms config |
| [`POST /api/v1/config/sms/make-default/{id}`](#post-api-v1-config-sms-make-default-id) | make default config sms |
| [`POST /api/v1/config/sms/make-backup/{id}`](#post-api-v1-config-sms-make-backup-id) | make backup config sms |
| [`GET /api/v1/config/sms/providers`](#get-api-v1-config-sms-providers) | List available sms config providers |

### `GET /api/v1/config/sms` {#get-api-v1-config-sms}

**List sms configuration**

**Responses:** `200` OK

### `POST /api/v1/config/sms` {#post-api-v1-config-sms}

**Create sms config**

**Request body** (`application/json`)

The body is selected by the `provider` discriminator:

#### Kave Negar SMS Config

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | ✅ | Example: `Primary SMS` |
| `provider` | string (kaveNegar) | ✅ | Example: `kaveNegar` |
| `apiToken` | string | ✅ | Example: `your-api-token-here` |
| `senderNumber` | string | ✅ | Example: `10008000800` |

**Responses:** `201` Created · `422` Validation error

### `GET /api/v1/config/sms/{id}` {#get-api-v1-config-sms-id}

**Get config by id**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` OK · `404` Not Found

### `PUT /api/v1/config/sms/{id}` {#put-api-v1-config-sms-id}

**Update sms config**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Request body** (`application/json`)

The body is selected by the `provider` discriminator:

#### Kave Negar SMS Config

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | ✅ | Example: `Primary SMS` |
| `provider` | string (kaveNegar) | ✅ | Example: `kaveNegar` |
| `apiToken` | string | ✅ | Example: `your-api-token-here` |
| `senderNumber` | string | ✅ | Example: `10008000800` |

**Responses:** `200` OK · `404` Not Found

### `DELETE /api/v1/config/sms/{id}` {#delete-api-v1-config-sms-id}

**Delete sms config**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Deleted · `404` Not Found

### `POST /api/v1/config/sms/make-default/{id}` {#post-api-v1-config-sms-make-default-id}

**make default config sms**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` OK

### `POST /api/v1/config/sms/make-backup/{id}` {#post-api-v1-config-sms-make-backup-id}

**make backup config sms**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` OK

### `GET /api/v1/config/sms/providers` {#get-api-v1-config-sms-providers}

**List available sms config providers**

**Responses:** `200` OK

## ConfigTelegram

| Endpoint | Summary |
|---|---|
| [`GET /api/v1/config/telegram`](#get-api-v1-config-telegram) | List Telegram proxy configs |
| [`POST /api/v1/config/telegram`](#post-api-v1-config-telegram) | Create Telegram proxy config |
| [`GET /api/v1/config/telegram/{id}`](#get-api-v1-config-telegram-id) | Get Telegram config by id |
| [`PUT /api/v1/config/telegram/{id}`](#put-api-v1-config-telegram-id) | Update Telegram proxy config |
| [`DELETE /api/v1/config/telegram/{id}`](#delete-api-v1-config-telegram-id) | Delete Telegram proxy config |
| [`POST /api/v1/config/telegram/activate/{id}`](#post-api-v1-config-telegram-activate-id) | Activate a Telegram config |
| [`POST /api/v1/config/telegram/deactivate`](#post-api-v1-config-telegram-deactivate) | Deactivate current Telegram config |

### `GET /api/v1/config/telegram` {#get-api-v1-config-telegram}

**List Telegram proxy configs**

Ordered with active config first.

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `name` | query |  | string | Filter by name |

**Responses:** `200` Telegram configs

### `POST /api/v1/config/telegram` {#post-api-v1-config-telegram}

**Create Telegram proxy config**

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | ✅ |  |
| `type` | string (http \| socks5) | ✅ |  |
| `host` | string | ✅ |  |
| `port` | string | ✅ |  |
| `username` | string |  |  |
| `password` | string |  |  |

**Responses:** `200` Created (inactive until activated) · `422` Validation error

### `GET /api/v1/config/telegram/{id}` {#get-api-v1-config-telegram-id}

**Get Telegram config by id**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` OK · `404` Not Found

### `PUT /api/v1/config/telegram/{id}` {#put-api-v1-config-telegram-id}

**Update Telegram proxy config**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | ✅ |  |
| `type` | string (http \| socks5) | ✅ |  |
| `host` | string | ✅ |  |
| `port` | string | ✅ |  |
| `username` | string |  |  |
| `password` | string |  |  |

**Responses:** `200` Updated

### `DELETE /api/v1/config/telegram/{id}` {#delete-api-v1-config-telegram-id}

**Delete Telegram proxy config**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Deleted

### `POST /api/v1/config/telegram/activate/{id}` {#post-api-v1-config-telegram-activate-id}

**Activate a Telegram config**

Deactivates any other active config.

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Activated

### `POST /api/v1/config/telegram/deactivate` {#post-api-v1-config-telegram-deactivate}

**Deactivate current Telegram config**

**Responses:** `200` Deactivated

## ConfigSkylogs

| Endpoint | Summary |
|---|---|
| [`GET /api/v1/config/skylogs/cluster`](#get-api-v1-config-skylogs-cluster) | Get cluster configuration |
| [`POST /api/v1/config/skylogs/cluster`](#post-api-v1-config-skylogs-cluster) | Save cluster configuration |

### `GET /api/v1/config/skylogs/cluster` {#get-api-v1-config-skylogs-cluster}

**Get cluster configuration**

Returns saved config or defaults (`type: main`, empty source URL/token).

**Responses:** `200` Cluster config

### `POST /api/v1/config/skylogs/cluster` {#post-api-v1-config-skylogs-cluster}

**Save cluster configuration**

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | string (main \| agent) | ✅ |  |
| `sourceUrl` | string |  | Required when type is agent |
| `sourceToken` | string |  | Required when type is agent |

**Responses:** `200` Saved config · `422` Validation error

