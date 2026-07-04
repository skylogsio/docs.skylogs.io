---
id: api-alert-rules
title: Alert rules
sidebar_position: 4
slug: /api/alert-rules
---

# Alert rules

:::note Generated reference
This page is generated from the OpenAPI spec (`scripts/generate_api_docs.py`). Do not edit by hand — regenerate when the API changes.
:::

Alert rules are the core object of the Skylogs API: each rule defines what to match from a source (Prometheus, Zabbix, Grafana, an inbound API alert, …), who owns it, and how to notify. Creation uses a single endpoint with a `type` discriminator selecting the body shape. Behavior rules attach notification, template, or silence behavior to an alert rule.

All endpoints require `Authorization: Bearer <accessToken>` — see [Authentication](/api/authentication).

## AlertRule

| Endpoint | Summary |
|---|---|
| [`GET /api/v1/alert-rule`](#get-api-v1-alert-rule) | List alert rules |
| [`POST /api/v1/alert-rule`](#post-api-v1-alert-rule) | Create alert rule |
| [`GET /api/v1/alert-rule/{id}`](#get-api-v1-alert-rule-id) | Get alert rule by id |
| [`PUT /api/v1/alert-rule/{id}`](#put-api-v1-alert-rule-id) | Update alert rule |
| [`DELETE /api/v1/alert-rule/{id}`](#delete-api-v1-alert-rule-id) | Delete alert rule |
| [`POST /api/v1/alert-rule/pin/{id}`](#post-api-v1-alert-rule-pin-id) | Toggle pin on alert rule |
| [`POST /api/v1/alert-rule/acknowledge/{id}`](#post-api-v1-alert-rule-acknowledge-id) | Acknowledge an alert (current user) |
| [`GET /api/v1/alert-rule/acknowledgeL/{id}`](#get-api-v1-alert-rule-acknowledgel-id) | Acknowledge alert using login link (system user) |
| [`POST /api/v1/alert-rule/resolve/{id}`](#post-api-v1-alert-rule-resolve-id) | Manually resolve alert |
| [`POST /api/v1/alert-rule/silent/{id}`](#post-api-v1-alert-rule-silent-id) | Toggle silence for current user on a single alert rule |
| [`GET /api/v1/alert-rule/filter-endpoints`](#get-api-v1-alert-rule-filter-endpoints) | Get selectable endpoints for alert rules |
| [`GET /api/v1/alert-rule/types`](#get-api-v1-alert-rule-types) | List available alert rule types |
| [`GET /api/v1/alert-rule/status`](#get-api-v1-alert-rule-status) | Get status timelines for a batch of alert rules |
| [`GET /api/v1/alert-rule/history/{id}`](#get-api-v1-alert-rule-history-id) | Get history for an alert rule |
| [`GET /api/v1/alert-rule/triggered/{id}`](#get-api-v1-alert-rule-triggered-id) | Get triggered/fired alerts for an alert rule |
| [`GET /api/v1/alert-rule/create-data`](#get-api-v1-alert-rule-create-data) | Get form data for creating an alert rule |
| [`GET /api/v1/alert-rule/create-data/data-source/{type}`](#get-api-v1-alert-rule-create-data-data-source-type) | Get data sources by type for alert rule creation |
| [`GET /api/v1/alert-rule/create-data/zabbix`](#get-api-v1-alert-rule-create-data-zabbix) | Get Zabbix hosts, actions, and severities |
| [`GET /api/v1/alert-rule/create-data/rules`](#get-api-v1-alert-rule-create-data-rules) | Get external alert rule names (Prometheus/Grafana) |
| [`GET /api/v1/alert-rule/create-data/labels`](#get-api-v1-alert-rule-create-data-labels) | Get Prometheus labels |
| [`GET /api/v1/alert-rule/create-data/label-values/{label}`](#get-api-v1-alert-rule-create-data-label-values-label) | Get Prometheus label values |
| [`POST /api/v1/alert-rule/group-action/silent`](#post-api-v1-alert-rule-group-action-silent) | Silence filtered alert rules for current user |
| [`POST /api/v1/alert-rule/group-action/unsilent`](#post-api-v1-alert-rule-group-action-unsilent) | Remove silence from filtered alert rules for current user |
| [`POST /api/v1/alert-rule/group-action/delete`](#post-api-v1-alert-rule-group-action-delete) | Delete filtered alert rules |
| [`POST /api/v1/alert-rule/group-action/add-user-notify`](#post-api-v1-alert-rule-group-action-add-user-notify) | Add users, teams, or endpoints to filtered alert rules |
| [`GET /api/v1/alert-rule-tag`](#get-api-v1-alert-rule-tag) | List all alert rule tags |
| [`GET /api/v1/alert-rule-tag/{id}`](#get-api-v1-alert-rule-tag-id) | Get tags for an alert rule |
| [`PUT /api/v1/alert-rule-tag/{id}`](#put-api-v1-alert-rule-tag-id) | Update tags for an alert rule |
| [`GET /api/v1/alert-rule-notify/{id}`](#get-api-v1-alert-rule-notify-id) | Get notification endpoints for an alert rule |
| [`PUT /api/v1/alert-rule-notify/{id}`](#put-api-v1-alert-rule-notify-id) | Add notification endpoints to an alert rule |
| [`DELETE /api/v1/alert-rule-notify/{alertId}/{endpointId}`](#delete-api-v1-alert-rule-notify-alertid-endpointid) | Remove a notification endpoint from an alert rule |
| [`POST /api/v1/alert-rule-notify/test/{id}`](#post-api-v1-alert-rule-notify-test-id) | Send a test notification for an alert rule |
| [`GET /api/v1/alert-rule-notify/batchAlert`](#get-api-v1-alert-rule-notify-batchalert) | Get selectable endpoints for batch notification assignment |
| [`PUT /api/v1/alert-rule-notify/batchAlert`](#put-api-v1-alert-rule-notify-batchalert) | Add endpoints to multiple alert rules |
| [`GET /api/v1/alert-rule-user/{id}`](#get-api-v1-alert-rule-user-id) | Get user and team access data for an alert rule |
| [`PUT /api/v1/alert-rule-user/{id}`](#put-api-v1-alert-rule-user-id) | Add users or teams to an alert rule |
| [`DELETE /api/v1/alert-rule-user/{alertId}/{userId}`](#delete-api-v1-alert-rule-user-alertid-userid) | Remove a user or team from an alert rule |

### `GET /api/v1/alert-rule` {#get-api-v1-alert-rule}

**List alert rules**

Returns a paginated list of alert rules visible to the authenticated user. Pinned rules appear first.

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `page` | query |  | integer | Page number |
| `perPage` | query |  | integer |  |
| `alertname` | query |  | string | Filter by alert rule name (case-insensitive partial match) |
| `userId` | query |  | string | Filter by owner or shared user id |
| `types` | query |  | string | Comma-separated alert types |
| `tags` | query |  | string | Comma-separated tags (all must match) |
| `silentStatus` | query |  | string (silent \| active) | Filter by silence state for the current user |
| `endpointId` | query |  | string | Filter by linked endpoint id |
| `status` | query |  | object | Filter by alert `state` field |

**Responses:** `200` Paginated alert rules · `401` Unauthorized

### `POST /api/v1/alert-rule` {#post-api-v1-alert-rule}

**Create alert rule**

Creates an alert rule. All types use this endpoint; set `type` to select the request body shape (see schema oneOf / discriminator). Prometheus, Grafana, and PMM additionally use `queryType` (`dynamic` vs `textQuery`).

**Request body** (`application/json`)

The body is selected by the `type` discriminator:

<details><summary><b>API alert rule</b> — Inbound webhook alert (fire, resolve, status). Server generates `apiToken` after create.</summary>

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Unique alert rule name Example: `High CPU usage` |
| `description` | string |  | Example: `Fires when CPU exceeds threshold` |
| `showAcknowledgeBtn` | boolean |  | Show acknowledge action in notification messages |
| `tags` | array of string |  | Example: `["production", "cpu"]` |
| `userIds` | array of string |  | Additional users granted access (MongoDB user ids) |
| `teamIds` | array of string |  | Teams granted access |
| `endpointIds` | array of string |  | Notification endpoints to attach |
| `type` | string (api) |  |  |
| `enableAutoResolve` | boolean |  | Automatically resolve firing instances after a period Example: `true` |
| `autoResolveMinutes` | integer |  | Minutes until auto-resolve when enableAutoResolve is true Example: `5` |

</details>

<details><summary><b>Notification alert rule</b> — Receives generic notification webhooks. Server generates `apiToken` after create.</summary>

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Unique alert rule name Example: `High CPU usage` |
| `description` | string |  | Example: `Fires when CPU exceeds threshold` |
| `showAcknowledgeBtn` | boolean |  | Show acknowledge action in notification messages |
| `tags` | array of string |  | Example: `["production", "cpu"]` |
| `userIds` | array of string |  | Additional users granted access (MongoDB user ids) |
| `teamIds` | array of string |  | Teams granted access |
| `endpointIds` | array of string |  | Notification endpoints to attach |
| `type` | string (notification) |  |  |

</details>

<details><summary><b>AlertRuleStorePrometheus</b> — Prometheus alert rule — choose dynamic or textQuery variant.</summary>

*Variant `queryType`: **Prometheus (dynamic)***

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Unique alert rule name Example: `High CPU usage` |
| `description` | string |  | Example: `Fires when CPU exceeds threshold` |
| `showAcknowledgeBtn` | boolean |  | Show acknowledge action in notification messages |
| `tags` | array of string |  | Example: `["production", "cpu"]` |
| `userIds` | array of string |  | Additional users granted access (MongoDB user ids) |
| `teamIds` | array of string |  | Teams granted access |
| `endpointIds` | array of string |  | Notification endpoints to attach |
| `type` | string (prometheus) |  |  |
| `queryType` | string (dynamic) |  |  |
| `dataSourceIds` | array of string |  | Prometheus data source ids (may be empty) |
| `dataSourceAlertName` | string |  | Alert name in the external Prometheus/Grafana ruler Example: `HighMemory` |
| `extraField` | array of object |  | Label key/value filters |

*Variant `queryType`: **Prometheus (text query)***

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Unique alert rule name Example: `High CPU usage` |
| `description` | string |  | Example: `Fires when CPU exceeds threshold` |
| `showAcknowledgeBtn` | boolean |  | Show acknowledge action in notification messages |
| `tags` | array of string |  | Example: `["production", "cpu"]` |
| `userIds` | array of string |  | Additional users granted access (MongoDB user ids) |
| `teamIds` | array of string |  | Teams granted access |
| `endpointIds` | array of string |  | Notification endpoints to attach |
| `type` | string (prometheus) |  |  |
| `queryType` | string (textQuery) |  |  |
| `queryText` | string |  | PromQL expression string |
| `queryObject` | object |  | Structured query payload used by the checker |


</details>

<details><summary><b>AlertRuleStoreGrafana</b> — Grafana alert rule — choose dynamic or textQuery variant.</summary>

*Variant `queryType`: **Grafana (dynamic)***

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Unique alert rule name Example: `High CPU usage` |
| `description` | string |  | Example: `Fires when CPU exceeds threshold` |
| `showAcknowledgeBtn` | boolean |  | Show acknowledge action in notification messages |
| `tags` | array of string |  | Example: `["production", "cpu"]` |
| `userIds` | array of string |  | Additional users granted access (MongoDB user ids) |
| `teamIds` | array of string |  | Teams granted access |
| `endpointIds` | array of string |  | Notification endpoints to attach |
| `type` | string (grafana) |  |  |
| `queryType` | string (dynamic) |  |  |
| `dataSourceIds` | array of string |  |  |
| `dataSourceAlertName` | string |  |  |
| `extraField` | array of object |  |  |

*Variant `queryType`: **Grafana (text query)***

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Unique alert rule name Example: `High CPU usage` |
| `description` | string |  | Example: `Fires when CPU exceeds threshold` |
| `showAcknowledgeBtn` | boolean |  | Show acknowledge action in notification messages |
| `tags` | array of string |  | Example: `["production", "cpu"]` |
| `userIds` | array of string |  | Additional users granted access (MongoDB user ids) |
| `teamIds` | array of string |  | Teams granted access |
| `endpointIds` | array of string |  | Notification endpoints to attach |
| `type` | string (grafana) |  |  |
| `queryType` | string (textQuery) |  |  |
| `queryText` | string |  |  |
| `queryObject` | object |  |  |


</details>

<details><summary><b>AlertRuleStorePmm</b> — Percona PMM alert rule — choose dynamic or textQuery variant.</summary>

*Variant `queryType`: **PMM (dynamic)***

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Unique alert rule name Example: `High CPU usage` |
| `description` | string |  | Example: `Fires when CPU exceeds threshold` |
| `showAcknowledgeBtn` | boolean |  | Show acknowledge action in notification messages |
| `tags` | array of string |  | Example: `["production", "cpu"]` |
| `userIds` | array of string |  | Additional users granted access (MongoDB user ids) |
| `teamIds` | array of string |  | Teams granted access |
| `endpointIds` | array of string |  | Notification endpoints to attach |
| `type` | string (pmm) |  |  |
| `queryType` | string (dynamic) |  |  |
| `dataSourceIds` | array of string |  |  |
| `dataSourceAlertName` | string |  |  |
| `extraField` | array of object |  |  |

*Variant `queryType`: **PMM (text query)***

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Unique alert rule name Example: `High CPU usage` |
| `description` | string |  | Example: `Fires when CPU exceeds threshold` |
| `showAcknowledgeBtn` | boolean |  | Show acknowledge action in notification messages |
| `tags` | array of string |  | Example: `["production", "cpu"]` |
| `userIds` | array of string |  | Additional users granted access (MongoDB user ids) |
| `teamIds` | array of string |  | Teams granted access |
| `endpointIds` | array of string |  | Notification endpoints to attach |
| `type` | string (pmm) |  |  |
| `queryType` | string (textQuery) |  |  |
| `queryText` | string |  |  |
| `queryObject` | object |  |  |


</details>

<details><summary><b>Sentry alert rule</b> — Webhook-driven Sentry issue alerts.</summary>

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Unique alert rule name Example: `High CPU usage` |
| `description` | string |  | Example: `Fires when CPU exceeds threshold` |
| `showAcknowledgeBtn` | boolean |  | Show acknowledge action in notification messages |
| `tags` | array of string |  | Example: `["production", "cpu"]` |
| `userIds` | array of string |  | Additional users granted access (MongoDB user ids) |
| `teamIds` | array of string |  | Teams granted access |
| `endpointIds` | array of string |  | Notification endpoints to attach |
| `type` | string (sentry) |  |  |
| `dataSourceIds` | array of string |  |  |
| `dataSourceAlertName` | string |  | Sentry project or alert identifier configured in Skylogs |

</details>

<details><summary><b>Splunk alert rule</b></summary>

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Unique alert rule name Example: `High CPU usage` |
| `description` | string |  | Example: `Fires when CPU exceeds threshold` |
| `showAcknowledgeBtn` | boolean |  | Show acknowledge action in notification messages |
| `tags` | array of string |  | Example: `["production", "cpu"]` |
| `userIds` | array of string |  | Additional users granted access (MongoDB user ids) |
| `teamIds` | array of string |  | Teams granted access |
| `endpointIds` | array of string |  | Notification endpoints to attach |
| `type` | string (splunk) |  |  |
| `dataSourceIds` | array of string |  |  |
| `dataSourceAlertName` | string |  |  |

</details>

<details><summary><b>Metabase alert rule</b></summary>

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Unique alert rule name Example: `High CPU usage` |
| `description` | string |  | Example: `Fires when CPU exceeds threshold` |
| `showAcknowledgeBtn` | boolean |  | Show acknowledge action in notification messages |
| `tags` | array of string |  | Example: `["production", "cpu"]` |
| `userIds` | array of string |  | Additional users granted access (MongoDB user ids) |
| `teamIds` | array of string |  | Teams granted access |
| `endpointIds` | array of string |  | Notification endpoints to attach |
| `type` | string (metabase) |  |  |
| `dataSourceIds` | array of string |  |  |
| `dataSourceAlertName` | string |  |  |

</details>

<details><summary><b>Zabbix alert rule</b> — Filter Zabbix webhooks by hosts, actions, and severities (0–5 as strings, or omit for all).</summary>

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Unique alert rule name Example: `High CPU usage` |
| `description` | string |  | Example: `Fires when CPU exceeds threshold` |
| `showAcknowledgeBtn` | boolean |  | Show acknowledge action in notification messages |
| `tags` | array of string |  | Example: `["production", "cpu"]` |
| `userIds` | array of string |  | Additional users granted access (MongoDB user ids) |
| `teamIds` | array of string |  | Teams granted access |
| `endpointIds` | array of string |  | Notification endpoints to attach |
| `type` | string (zabbix) |  |  |
| `dataSourceIds` | array of string |  |  |
| `hosts` | array of string |  | Example: `["web-01"]` |
| `actions` | array of string |  | Example: `["Action1"]` |
| `severities` | array of string (0 \| 1 \| 2 \| 3 \| 4 \| 5) |  | Zabbix severity codes 0 (not classified) through 5 (disaster) Example: `["5"]` |

</details>

<details><summary><b>Elastic alert rule</b> — Document-count threshold on an Elastic data view.</summary>

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Unique alert rule name Example: `High CPU usage` |
| `description` | string |  | Example: `Fires when CPU exceeds threshold` |
| `showAcknowledgeBtn` | boolean |  | Show acknowledge action in notification messages |
| `tags` | array of string |  | Example: `["production", "cpu"]` |
| `userIds` | array of string |  | Additional users granted access (MongoDB user ids) |
| `teamIds` | array of string |  | Teams granted access |
| `endpointIds` | array of string |  | Notification endpoints to attach |
| `type` | string (elastic) |  |  |
| `dataSourceId` | string |  |  |
| `dataviewName` | string |  | Example: `responses` |
| `dataviewTitle` | string |  | Example: `responses*` |
| `queryString` | string |  | Example: `OriginStatus:>=400` |
| `minutes` | integer |  | Look-back window in minutes Example: `15` |
| `conditionType` | string (greaterOrEqual \| lessOrEqual) |  |  |
| `countDocument` | integer |  | Document count threshold Example: `5` |

</details>

<details><summary><b>VictoriaLogs alert rule</b> — Log line count threshold on a VictoriaLogs data source.</summary>

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Unique alert rule name Example: `High CPU usage` |
| `description` | string |  | Example: `Fires when CPU exceeds threshold` |
| `showAcknowledgeBtn` | boolean |  | Show acknowledge action in notification messages |
| `tags` | array of string |  | Example: `["production", "cpu"]` |
| `userIds` | array of string |  | Additional users granted access (MongoDB user ids) |
| `teamIds` | array of string |  | Teams granted access |
| `endpointIds` | array of string |  | Notification endpoints to attach |
| `type` | string (victoria_logs) |  |  |
| `dataSourceId` | string |  |  |
| `queryString` | string |  |  |
| `minutes` | integer |  | Example: `15` |
| `conditionType` | string (greaterOrEqual \| lessOrEqual) |  |  |
| `countDocument` | integer |  | Example: `5` |

</details>

**Responses:** `200` Created successfully · `422` Validation error

### `GET /api/v1/alert-rule/{id}` {#get-api-v1-alert-rule-id}

**Get alert rule by id**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Alert rule details · `403` Forbidden · `404` Not Found

### `PUT /api/v1/alert-rule/{id}` {#put-api-v1-alert-rule-id}

**Update alert rule**

Updates an alert rule. Send the payload for the rule's existing type (type cannot be changed). Non-admin users can only update rules they own.

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Request body** (`application/json`)

<details><summary><b>Update API alert rule</b></summary>

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  |  |
| `description` | string |  |  |
| `showAcknowledgeBtn` | boolean |  |  |
| `tags` | array of string |  |  |
| `userIds` | array of string |  |  |
| `teamIds` | array of string |  |  |
| `endpointIds` | array of string |  |  |
| `enableAutoResolve` | boolean |  |  |
| `autoResolveMinutes` | integer |  |  |

</details>

<details><summary><b>Update notification alert rule</b></summary>

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  |  |
| `description` | string |  |  |
| `showAcknowledgeBtn` | boolean |  |  |
| `tags` | array of string |  |  |
| `userIds` | array of string |  |  |
| `teamIds` | array of string |  |  |
| `endpointIds` | array of string |  |  |

</details>

<details><summary><b>AlertRuleUpdatePrometheus</b></summary>

*Variant `queryType`: **Update Prometheus (dynamic)***

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  |  |
| `description` | string |  |  |
| `showAcknowledgeBtn` | boolean |  |  |
| `tags` | array of string |  |  |
| `userIds` | array of string |  |  |
| `teamIds` | array of string |  |  |
| `endpointIds` | array of string |  |  |
| `queryType` | string (dynamic) |  |  |
| `dataSourceIds` | array of string |  |  |
| `dataSourceAlertName` | string |  |  |
| `extraField` | array of object |  |  |

*Variant `queryType`: **Update Prometheus (text query)***

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  |  |
| `description` | string |  |  |
| `showAcknowledgeBtn` | boolean |  |  |
| `tags` | array of string |  |  |
| `userIds` | array of string |  |  |
| `teamIds` | array of string |  |  |
| `endpointIds` | array of string |  |  |
| `queryType` | string (textQuery) |  |  |
| `queryText` | string |  |  |
| `queryObject` | object |  |  |


</details>

<details><summary><b>AlertRuleUpdateGrafana</b></summary>

*Variant `queryType`: **Update Grafana (dynamic)***

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  |  |
| `description` | string |  |  |
| `showAcknowledgeBtn` | boolean |  |  |
| `tags` | array of string |  |  |
| `userIds` | array of string |  |  |
| `teamIds` | array of string |  |  |
| `endpointIds` | array of string |  |  |
| `queryType` | string (dynamic) |  |  |
| `dataSourceIds` | array of string |  |  |
| `dataSourceAlertName` | string |  |  |
| `extraField` | array of object |  |  |

*Variant `queryType`: **Update Grafana (text query)***

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  |  |
| `description` | string |  |  |
| `showAcknowledgeBtn` | boolean |  |  |
| `tags` | array of string |  |  |
| `userIds` | array of string |  |  |
| `teamIds` | array of string |  |  |
| `endpointIds` | array of string |  |  |
| `queryType` | string (textQuery) |  |  |
| `queryText` | string |  |  |
| `queryObject` | object |  |  |


</details>

<details><summary><b>AlertRuleUpdatePmm</b></summary>

*Variant `queryType`: **Update PMM (dynamic)***

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  |  |
| `description` | string |  |  |
| `showAcknowledgeBtn` | boolean |  |  |
| `tags` | array of string |  |  |
| `userIds` | array of string |  |  |
| `teamIds` | array of string |  |  |
| `endpointIds` | array of string |  |  |
| `queryType` | string (dynamic) |  |  |
| `dataSourceIds` | array of string |  |  |
| `dataSourceAlertName` | string |  |  |
| `extraField` | array of object |  |  |

*Variant `queryType`: **Update PMM (text query)***

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  |  |
| `description` | string |  |  |
| `showAcknowledgeBtn` | boolean |  |  |
| `tags` | array of string |  |  |
| `userIds` | array of string |  |  |
| `teamIds` | array of string |  |  |
| `endpointIds` | array of string |  |  |
| `queryType` | string (textQuery) |  |  |
| `queryText` | string |  |  |
| `queryObject` | object |  |  |


</details>

<details><summary><b>Update Sentry alert rule</b></summary>

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  |  |
| `description` | string |  |  |
| `showAcknowledgeBtn` | boolean |  |  |
| `tags` | array of string |  |  |
| `userIds` | array of string |  |  |
| `teamIds` | array of string |  |  |
| `endpointIds` | array of string |  |  |
| `dataSourceIds` | array of string |  |  |
| `dataSourceAlertName` | string |  |  |

</details>

<details><summary><b>Update Splunk alert rule</b></summary>

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  |  |
| `description` | string |  |  |
| `showAcknowledgeBtn` | boolean |  |  |
| `tags` | array of string |  |  |
| `userIds` | array of string |  |  |
| `teamIds` | array of string |  |  |
| `endpointIds` | array of string |  |  |
| `dataSourceIds` | array of string |  |  |
| `dataSourceAlertName` | string |  |  |

</details>

<details><summary><b>Update Metabase alert rule</b></summary>

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  |  |
| `description` | string |  |  |
| `showAcknowledgeBtn` | boolean |  |  |
| `tags` | array of string |  |  |
| `userIds` | array of string |  |  |
| `teamIds` | array of string |  |  |
| `endpointIds` | array of string |  |  |
| `dataSourceIds` | array of string |  |  |
| `dataSourceAlertName` | string |  |  |

</details>

<details><summary><b>Update Zabbix alert rule</b></summary>

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  |  |
| `description` | string |  |  |
| `showAcknowledgeBtn` | boolean |  |  |
| `tags` | array of string |  |  |
| `userIds` | array of string |  |  |
| `teamIds` | array of string |  |  |
| `endpointIds` | array of string |  |  |
| `dataSourceIds` | array of string |  |  |
| `hosts` | array of string |  |  |
| `actions` | array of string |  |  |
| `severities` | array of string (0 \| 1 \| 2 \| 3 \| 4 \| 5) |  |  |

</details>

<details><summary><b>Update Elastic alert rule</b></summary>

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  |  |
| `description` | string |  |  |
| `showAcknowledgeBtn` | boolean |  |  |
| `tags` | array of string |  |  |
| `userIds` | array of string |  |  |
| `teamIds` | array of string |  |  |
| `endpointIds` | array of string |  |  |
| `dataSourceId` | string |  |  |
| `dataviewName` | string |  |  |
| `dataviewTitle` | string |  |  |
| `queryString` | string |  |  |
| `minutes` | integer |  |  |
| `conditionType` | string (greaterOrEqual \| lessOrEqual) |  |  |
| `countDocument` | integer |  |  |

</details>

<details><summary><b>Update VictoriaLogs alert rule</b></summary>

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  |  |
| `description` | string |  |  |
| `showAcknowledgeBtn` | boolean |  |  |
| `tags` | array of string |  |  |
| `userIds` | array of string |  |  |
| `teamIds` | array of string |  |  |
| `endpointIds` | array of string |  |  |
| `dataSourceId` | string |  |  |
| `queryString` | string |  |  |
| `minutes` | integer |  |  |
| `conditionType` | string (greaterOrEqual \| lessOrEqual) |  |  |
| `countDocument` | integer |  |  |

</details>

**Responses:** `200` Updated successfully · `403` Forbidden · `404` Not Found

### `DELETE /api/v1/alert-rule/{id}` {#delete-api-v1-alert-rule-id}

**Delete alert rule**

Deletes the alert rule for admins/owners, or removes the current user access and endpoints for shared users.

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Deleted · `404` Not Found

### `POST /api/v1/alert-rule/pin/{id}` {#post-api-v1-alert-rule-pin-id}

**Toggle pin on alert rule**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Pin toggled

### `POST /api/v1/alert-rule/acknowledge/{id}` {#post-api-v1-alert-rule-acknowledge-id}

**Acknowledge an alert (current user)**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Acknowledged · `403` Forbidden

### `GET /api/v1/alert-rule/acknowledgeL/{id}` {#get-api-v1-alert-rule-acknowledgel-id}

**Acknowledge alert using login link (system user)**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Acknowledged or already acknowledged

### `POST /api/v1/alert-rule/resolve/{id}` {#post-api-v1-alert-rule-resolve-id}

**Manually resolve alert**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Resolved · `403` Forbidden

### `POST /api/v1/alert-rule/silent/{id}` {#post-api-v1-alert-rule-silent-id}

**Toggle silence for current user on a single alert rule**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Silence toggled

### `GET /api/v1/alert-rule/filter-endpoints` {#get-api-v1-alert-rule-filter-endpoints}

**Get selectable endpoints for alert rules**

**Responses:** `200` Selectable endpoints

### `GET /api/v1/alert-rule/types` {#get-api-v1-alert-rule-types}

**List available alert rule types**

**Responses:** `200` Alert rule type enum values

### `GET /api/v1/alert-rule/status` {#get-api-v1-alert-rule-status}

**Get status timelines for a batch of alert rules**

Returns a fixed-bucket status timeline per alert rule over `[fromTime, toTime]`. Each bucket is colored by the worst status that occurred inside it (critical > warning > resolved > unknown) and carries every raw underlying status change that overlaps it, for hover/click incident detail. Alert rules the user cannot access are silently omitted from the response.

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `alertRuleIds` | query | ✅ | array of string | Alert rule ids to build timelines for |
| `fromTime` | query | ✅ | integer | Window start (unix timestamp, seconds) |
| `toTime` | query | ✅ | integer | Window end (unix timestamp, seconds), must be after fromTime |
| `bucketCount` | query |  | integer | Number of equal-width buckets to divide the window into |

**Responses:** `200` Status timeline per alert rule · `422` Validation error

### `GET /api/v1/alert-rule/history/{id}` {#get-api-v1-alert-rule-history-id}

**Get history for an alert rule**

Returns paginated state-change history. Shape depends on alert type (API instances, Prometheus/Grafana checks, Elastic/VictoriaLogs checks, etc.).

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |
| `perPage` | query |  | integer | Items per page |
| `from` | query |  | string | Start datetime (Y-m-d H:i) |
| `to` | query |  | string | End datetime (Y-m-d H:i) |

**Responses:** `200` Paginated history records · `403` Forbidden · `404` Not Found

### `GET /api/v1/alert-rule/triggered/{id}` {#get-api-v1-alert-rule-triggered-id}

**Get triggered/fired alerts for an alert rule**

Returns currently firing data: API `AlertInstance` rows, Prometheus/Grafana alert arrays, Zabbix webhook events, or Elastic/VictoriaLogs check documents depending on type.

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Fired instances or active check payload · `404` Not Found

### `GET /api/v1/alert-rule/create-data` {#get-api-v1-alert-rule-create-data}

**Get form data for creating an alert rule**

**Responses:** `200` Endpoints and selectable users

### `GET /api/v1/alert-rule/create-data/data-source/{type}` {#get-api-v1-alert-rule-create-data-data-source-type}

**Get data sources by type for alert rule creation**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `type` | path | ✅ | string (prometheus \| sentry \| grafana \| pmm \| zabbix \| splunk \| elastic \| victoria_logs) |  |

**Responses:** `200` Data sources

### `GET /api/v1/alert-rule/create-data/zabbix` {#get-api-v1-alert-rule-create-data-zabbix}

**Get Zabbix hosts, actions, and severities**

**Responses:** `200` Zabbix metadata

### `GET /api/v1/alert-rule/create-data/rules` {#get-api-v1-alert-rule-create-data-rules}

**Get external alert rule names (Prometheus/Grafana)**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `type` | query | ✅ | string (prometheus \| grafana) |  |
| `dataSourceId` | query | ✅ | string |  |

**Responses:** `200` External rule names

### `GET /api/v1/alert-rule/create-data/labels` {#get-api-v1-alert-rule-create-data-labels}

**Get Prometheus labels**

**Responses:** `200` Prometheus labels

### `GET /api/v1/alert-rule/create-data/label-values/{label}` {#get-api-v1-alert-rule-create-data-label-values-label}

**Get Prometheus label values**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `label` | path | ✅ | string |  |

**Responses:** `200` Label values

### `POST /api/v1/alert-rule/group-action/silent` {#post-api-v1-alert-rule-group-action-silent}

**Silence filtered alert rules for current user**

Uses the same query filters as the alert rule list endpoint.

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `alertname` | query |  | string |  |
| `userId` | query |  | string |  |
| `types` | query |  | string |  |
| `tags` | query |  | string |  |
| `silentStatus` | query |  | string (silent \| active) |  |
| `endpointId` | query |  | string |  |
| `status` | query |  | object | Filter by alert state |

**Responses:** `200` Rules silenced

### `POST /api/v1/alert-rule/group-action/unsilent` {#post-api-v1-alert-rule-group-action-unsilent}

**Remove silence from filtered alert rules for current user**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `alertname` | query |  | string |  |
| `userId` | query |  | string |  |
| `types` | query |  | string |  |
| `tags` | query |  | string |  |
| `silentStatus` | query |  | string (silent \| active) |  |
| `endpointId` | query |  | string |  |
| `status` | query |  | object | Filter by alert state |

**Responses:** `200` Silence removed

### `POST /api/v1/alert-rule/group-action/delete` {#post-api-v1-alert-rule-group-action-delete}

**Delete filtered alert rules**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `alertname` | query |  | string |  |
| `userId` | query |  | string |  |
| `types` | query |  | string |  |
| `tags` | query |  | string |  |
| `endpointId` | query |  | string |  |
| `status` | query |  | object | Filter by alert state |

**Responses:** `200` Rules deleted or access removed

### `POST /api/v1/alert-rule/group-action/add-user-notify` {#post-api-v1-alert-rule-group-action-add-user-notify}

**Add users, teams, or endpoints to filtered alert rules**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `alertname` | query |  | string |  |
| `userId` | query |  | string |  |
| `types` | query |  | string |  |
| `tags` | query |  | string |  |
| `endpointId` | query |  | string |  |
| `status` | query |  | object | Filter by alert state |

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `userIds` | array of string |  |  |
| `teamIds` | array of string |  |  |
| `endpointIds` | array of string |  |  |

**Responses:** `200` Access or notifications updated

### `GET /api/v1/alert-rule-tag` {#get-api-v1-alert-rule-tag}

**List all alert rule tags**

**Responses:** `200` All tags

### `GET /api/v1/alert-rule-tag/{id}` {#get-api-v1-alert-rule-tag-id}

**Get tags for an alert rule**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Alert rule tags · `403` Forbidden

### `PUT /api/v1/alert-rule-tag/{id}` {#put-api-v1-alert-rule-tag-id}

**Update tags for an alert rule**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `tags` | array of string |  |  |

**Responses:** `200` Tags updated · `403` Forbidden

### `GET /api/v1/alert-rule-notify/{id}` {#get-api-v1-alert-rule-notify-id}

**Get notification endpoints for an alert rule**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Current and selectable endpoints

### `PUT /api/v1/alert-rule-notify/{id}` {#put-api-v1-alert-rule-notify-id}

**Add notification endpoints to an alert rule**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `endpointIds` | array of string |  |  |

**Responses:** `200` Endpoints added

### `DELETE /api/v1/alert-rule-notify/{alertId}/{endpointId}` {#delete-api-v1-alert-rule-notify-alertid-endpointid}

**Remove a notification endpoint from an alert rule**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `alertId` | path | ✅ | string |  |
| `endpointId` | path | ✅ | string |  |

**Responses:** `200` Endpoint removed

### `POST /api/v1/alert-rule-notify/test/{id}` {#post-api-v1-alert-rule-notify-test-id}

**Send a test notification for an alert rule**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Test notification queued · `403` Forbidden

### `GET /api/v1/alert-rule-notify/batchAlert` {#get-api-v1-alert-rule-notify-batchalert}

**Get selectable endpoints for batch notification assignment**

**Responses:** `200` Selectable endpoints

### `PUT /api/v1/alert-rule-notify/batchAlert` {#put-api-v1-alert-rule-notify-batchalert}

**Add endpoints to multiple alert rules**

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `alertIds` | array of string |  |  |
| `endpoints` | array of string |  |  |

**Responses:** `200` Batch update completed

### `GET /api/v1/alert-rule-user/{id}` {#get-api-v1-alert-rule-user-id}

**Get user and team access data for an alert rule**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Users and teams · `403` Forbidden

### `PUT /api/v1/alert-rule-user/{id}` {#put-api-v1-alert-rule-user-id}

**Add users or teams to an alert rule**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `userIds` | array of string |  |  |
| `teamIds` | array of string |  |  |

**Responses:** `200` Access updated · `403` Forbidden

### `DELETE /api/v1/alert-rule-user/{alertId}/{userId}` {#delete-api-v1-alert-rule-user-alertid-userid}

**Remove a user or team from an alert rule**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `alertId` | path | ✅ | string |  |
| `userId` | path | ✅ | string |  |

**Responses:** `200` Access removed · `403` Forbidden

## AlertRule Behavior Rules

| Endpoint | Summary |
|---|---|
| [`GET /api/v1/alert-rule-behavior-rule/selectable-alert-rules/{alertRuleId}`](#get-api-v1-alert-rule-behavior-rule-selectable-alert-rules-alertruleid) | List selectable alert rules for silent behavior rules |
| [`GET /api/v1/alert-rule-behavior-rule/{alertRuleId}`](#get-api-v1-alert-rule-behavior-rule-alertruleid) | List behavior rules |
| [`POST /api/v1/alert-rule-behavior-rule/{alertRuleId}`](#post-api-v1-alert-rule-behavior-rule-alertruleid) | Create a behavior rule |
| [`PUT /api/v1/alert-rule-behavior-rule/{alertRuleId}/{ruleId}`](#put-api-v1-alert-rule-behavior-rule-alertruleid-ruleid) | Update a behavior rule |
| [`DELETE /api/v1/alert-rule-behavior-rule/{alertRuleId}/{ruleId}`](#delete-api-v1-alert-rule-behavior-rule-alertruleid-ruleid) | Delete a behavior rule |

### `GET /api/v1/alert-rule-behavior-rule/selectable-alert-rules/{alertRuleId}` {#get-api-v1-alert-rule-behavior-rule-selectable-alert-rules-alertruleid}

**List selectable alert rules for silent behavior rules**

Returns alert rules the user can access whose type supports resolved/critical status. Excludes the current alert rule. Use the returned `id` values in `dependsOnAlertRuleIds` when creating or updating a silent behavior rule.

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `alertRuleId` | path | ✅ | string | Alert rule MongoDB `_id` being configured |

**Responses:** `200` Selectable alert rules · `403` Forbidden · `404` Alert rule not found

### `GET /api/v1/alert-rule-behavior-rule/{alertRuleId}` {#get-api-v1-alert-rule-behavior-rule-alertruleid}

**List behavior rules**

Returns notification, template, and silent rules for the alert rule. Each item shape depends on `type` (see `AlertRuleBehaviorRule` schema).

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `alertRuleId` | path | ✅ | string | Alert rule MongoDB `_id` |

**Responses:** `200` Behavior rules · `403` Forbidden · `404` Alert rule not found

### `POST /api/v1/alert-rule-behavior-rule/{alertRuleId}` {#post-api-v1-alert-rule-behavior-rule-alertruleid}

**Create a behavior rule**

One endpoint for all behavior rule types. Set `type` in the body and use the matching schema (`notification`, `template`, or `silent`). Requires admin access on the alert rule.

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `alertRuleId` | path | ✅ | string | Alert rule MongoDB `_id` |

**Request body** (`application/json`)

Create a behavior rule. Set `type` to pick the payload shape (same URL for all types). Requires alert rule admin access.

**Responses:** `200` Behavior rule created · `403` Forbidden · `422` Validation error

### `PUT /api/v1/alert-rule-behavior-rule/{alertRuleId}/{ruleId}` {#put-api-v1-alert-rule-behavior-rule-alertruleid-ruleid}

**Update a behavior rule**

Send only fields allowed for the existing rule type. The rule `type` cannot be changed. `ruleId` is the UUID returned when the rule was created.

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `alertRuleId` | path | ✅ | string | Alert rule MongoDB `_id` |
| `ruleId` | path | ✅ | string | Behavior rule UUID |

**Request body** (`application/json`)

Update a behavior rule. Send the variant that matches the rule's existing type (identified by `ruleId` in the path).

**Responses:** `200` Behavior rule updated · `403` Forbidden · `404` Not Found · `422` Validation error

### `DELETE /api/v1/alert-rule-behavior-rule/{alertRuleId}/{ruleId}` {#delete-api-v1-alert-rule-behavior-rule-alertruleid-ruleid}

**Delete a behavior rule**

Removes any behavior rule (notification, template, or silent) by its UUID.

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `alertRuleId` | path | ✅ | string | Alert rule MongoDB `_id` |
| `ruleId` | path | ✅ | string | Behavior rule UUID |

**Responses:** `200` Behavior rule deleted · `403` Forbidden · `404` Not Found

