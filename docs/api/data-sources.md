---
id: api-data-sources
title: Data sources & Prometheus
sidebar_position: 7
slug: /api/data-sources
---

# Data sources & Prometheus

:::note Generated reference
This page is generated from the OpenAPI spec (`scripts/generate_api_docs.py`). Do not edit by hand — regenerate when the API changes.
:::

Data sources connect Skylogs to monitoring systems. The Prometheus endpoints let clients browse labels, rules, and currently firing alerts of a connected Prometheus.

All endpoints require `Authorization: Bearer <accessToken>` — see [Authentication](/api/authentication).

## Data Sources

| Endpoint | Summary |
|---|---|
| [`GET /api/v1/data-source`](#get-api-v1-data-source) | Get list of data sources |
| [`POST /api/v1/data-source`](#post-api-v1-data-source) | Create new data source |
| [`GET /api/v1/data-source/types`](#get-api-v1-data-source-types) | Get available data source types |
| [`GET /api/v1/data-source/{id}`](#get-api-v1-data-source-id) | Get data source by ID |
| [`PUT /api/v1/data-source/{id}`](#put-api-v1-data-source-id) | Update data source |
| [`DELETE /api/v1/data-source/{id}`](#delete-api-v1-data-source-id) | Delete data source |
| [`GET /api/v1/data-source/status/{id}`](#get-api-v1-data-source-status-id) | Check if data source is connected |

### `GET /api/v1/data-source` {#get-api-v1-data-source}

**Get list of data sources**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `page` | query |  | integer | Page number |
| `perPage` | query |  | integer |  |
| `name` | query |  | string |  |

**Responses:** `200` List of data sources

### `POST /api/v1/data-source` {#post-api-v1-data-source}

**Create new data source**

**Request body** (`application/json`)

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | ✅ | Example: `Production Prometheus` |
| `type` | string (prometheus \| sentry \| grafana \| pmm \| zabbix \| splunk \| elastic) | ✅ | Example: `prometheus` |
| `url` | string | ✅ | Example: `https://prometheus.example.com` |
| `api_token` | string |  |  |
| `username` | string |  |  |
| `password` | string |  |  |

**Responses:** `201` Data source created · `422` Validation error

### `GET /api/v1/data-source/types` {#get-api-v1-data-source-types}

**Get available data source types**

**Responses:** `200` List of data source types

### `GET /api/v1/data-source/{id}` {#get-api-v1-data-source-id}

**Get data source by ID**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Data source details · `404` Not found

### `PUT /api/v1/data-source/{id}` {#put-api-v1-data-source-id}

**Update data source**

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
| `api_token` | string |  |  |
| `username` | string |  |  |
| `password` | string |  |  |

**Responses:** `200` Data source updated · `404` Not found

### `DELETE /api/v1/data-source/{id}` {#delete-api-v1-data-source-id}

**Delete data source**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Data source deleted · `404` Not found

### `GET /api/v1/data-source/status/{id}` {#get-api-v1-data-source-status-id}

**Check if data source is connected**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `id` | path | ✅ | string |  |

**Responses:** `200` Connection status

## Prometheus

| Endpoint | Summary |
|---|---|
| [`GET /api/v1/prometheus/rules`](#get-api-v1-prometheus-rules) | Get Prometheus alert rule names |
| [`GET /api/v1/prometheus/labels`](#get-api-v1-prometheus-labels) | Get Prometheus label names |
| [`GET /api/v1/prometheus/label-values/{label}`](#get-api-v1-prometheus-label-values-label) | Get values for a Prometheus label |
| [`GET /api/v1/prometheus/triggered`](#get-api-v1-prometheus-triggered) | Get currently firing Prometheus alerts |

### `GET /api/v1/prometheus/rules` {#get-api-v1-prometheus-rules}

**Get Prometheus alert rule names**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `data_source_id` | query | ✅ | string | Prometheus data source id |

**Responses:** `200` External rule names (cached)

### `GET /api/v1/prometheus/labels` {#get-api-v1-prometheus-labels}

**Get Prometheus label names**

**Responses:** `200` Label names

### `GET /api/v1/prometheus/label-values/{label}` {#get-api-v1-prometheus-label-values-label}

**Get values for a Prometheus label**

**Parameters**

| Name | In | Required | Type | Description |
|---|---|---|---|---|
| `label` | path | ✅ | string |  |

**Responses:** `200` Label values

### `GET /api/v1/prometheus/triggered` {#get-api-v1-prometheus-triggered}

**Get currently firing Prometheus alerts**

**Responses:** `200` Triggered alerts from Prometheus (cached ~5s)

