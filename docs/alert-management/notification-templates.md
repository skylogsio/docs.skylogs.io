---
id: notification-templates
title: Custom Notification Templates
sidebar_position: 10
slug: /alert-management/notification-templates
---

# Custom Notification Templates

A **template behavior rule** replaces the default notification text for selected endpoints on one alert rule. Endpoints that are not listed on a template rule keep the default message.

Custom templates are available for these alert types:

- [Prometheus](/alert-management/prometheus-alert)
- [Grafana](/alert-management/grafana-alert) and [PMM](/alert-management/pmm-alert) (same placeholders)
- [API](/alert-management/api-alert) and [Notification](/alert-management/notification-alert) (same placeholders)

Every other alert type still sends Skylogs' default message. That includes Sentry, Zabbix, Splunk, Elasticsearch, VictoriaLogs, Metabase, and Health Check. Placeholder syntax for those types is not available yet, so leave them on the default message.

## How a template rule is applied

The steps in this section apply to the alert types listed above. The sample uses Prometheus placeholders. Use the placeholders for your alert type from the sections below.

Create a behavior rule with `type` set to `template`, a display `name`, the `endpointIds` that should use the custom text, and the `template` string.

```json
{
  "name": "Disk alert template",
  "type": "template",
  "endpointIds": ["<endpoint-id>"],
  "template": "{{name}}\n\n{{state_line}}\n{{alert_items labels=\"pod,namespace\" annotations=\"summary\"}}\n{{date}}"
}
```

Send that body to `POST /api/v1/alert-rule-behavior-rule/{alertRuleId}`. See [Alert rules → Behavior rules](/api/alert-rules#alertrule-behavior-rules) for create, update, and delete.

Rules:

- The template is rendered when the notification is sent, using the alert payload at that moment.
- One template rule can target several endpoints. Each listed endpoint receives that text.
- If two template rules list the same endpoint, the later rule in the alert rule's behavior-rule list wins.
- An empty template is ignored. That endpoint falls back to the default message.
- Placeholder names are case-sensitive. `{{Name}}` is not the same as `{{name}}`.
- Spaces inside the braces are ignored: `{{ name }}` and `{{name}}` are the same.
- Text outside `{{...}}` is copied as written, including line breaks.
- A placeholder Skylogs does not recognize for that alert type is replaced with an empty string.

## Prometheus

### Default template

```
{{name}}

{{state_line}}
{{alert_items labels="*" annotations="*"}}
{{date}}
```

### Placeholders

| Placeholder | Result |
|---|---|
| `{{name}}` | Alert rule name |
| `{{state}}` | `critical` while firing, `resolved` when resolved. Otherwise the rule's stored state. |
| `{{state_line}}` | `State: Fire 🔥` or `State: Resolved ✅`, followed by a blank line. Empty when the payload state is neither. |
| `{{fireCount}}` | Current firing count on the alert rule |
| `{{date}}` | Jalali (Solar Hijri) date at send time, as `date: YYYY/MM/DD`. The prefix is lowercase and there is no time. |
| `{{dataSourceName}}` | Data source name on the payload, or on the first firing alert |
| `{{label.KEY}}` | One label from the first firing alert. `{{label.pod}}` prints that pod name. Missing or empty labels print nothing. |
| `{{annotation.KEY}}` | One annotation from the first firing alert, such as `{{annotation.summary}}` |
| `{{severity_line}}` | Severity of the first firing alert. See [Severity line](#severity-line). |
| `{{labels:alertname,pod}}` | Selected labels from the first firing alert, one `key : value` line each, in the order you list |
| `{{labels:*}}` | Every non-empty label on the first firing alert |
| `{{labels:* exclude=job,namespace}}` | Every non-empty label except the keys after `exclude=` |
| `{{annotations:summary,description}}` | Selected annotations, same rules as `{{labels:...}}` |
| `{{annotations:* exclude=runbook_url}}` | Every non-empty annotation except the listed keys |
| `{{alert_items ...}}` | One section per alert in the payload. See [Per-alert sections](#per-alert-sections). |

`{{label.*}}`, `{{annotation.*}}`, `{{labels:...}}`, `{{annotations:...}}`, and `{{severity_line}}` read the **first firing alert**. If every alert in the payload is resolved, they use the first alert in the list.

Empty label and annotation values are left out of blocks. A key you name that is missing is skipped, so the line does not appear.

### Per-alert sections

`{{alert_items}}` prints every alert, firing and resolved. Each section ends with a blank line, a `************` separator, and another blank line.

```
{{alert_items labels="pod,namespace" annotations="summary,description" show_data_source="false"}}
```

| Attribute | Meaning |
|---|---|
| `labels="pod,namespace"` | Only these labels, in this order. Omit the attribute to include every non-empty label. `labels="*"` does the same. |
| `exclude_labels="job,alertname"` | Every non-empty label except these keys. This replaces `labels=`. Use it when you want "all except", not together with an include list. |
| `annotations="summary"` | Only these annotations. `annotations="*"` or omitting the attribute includes every non-empty annotation. |
| `exclude_annotations="runbook_url"` | Every non-empty annotation except these keys. This replaces `annotations=`. |
| `show_data_source="true"` | Prometheus only. Default is `true`. When the alert has a data source name, the section includes `Data Source: ...`. Set `"false"` to hide that line. |

A firing critical alert renders like this:

```
Fire 🔥
Data Source: Prom DS
pod : api-1
namespace : prod
summary : CPU is high
description : Pod api-1 CPU above 90%

************

```

### Severity line

Used by `{{severity_line}}` and as the first line of each `{{alert_items}}` section.

| Alert | Line |
|---|---|
| Resolved | `Resolved ✅` |
| Firing, `severity=warning` | `Warning ⚠️` |
| Firing, `severity=info` | `Info ℹ️` |
| Firing, any other severity (including `critical` or missing) | `Fire 🔥` |

### Example

```
{{name}} — {{state}}
{{severity_line}}
Pod: {{label.pod}}
{{annotation.summary}}

{{alert_items labels="*" exclude_labels="job" annotations="summary,description" show_data_source="false"}}
{{date}}
```

## Grafana and PMM

Grafana and PMM share this syntax. PMM does not have a separate placeholder set.

### Default template

```
{{name}}

{{state_line}}
Data Source: {{dataSourceName}}

{{alert_items labels="*" annotations="*"}}
{{date}}
```

The Prometheus placeholders above work here, with these differences:

| Placeholder | Grafana / PMM behavior |
|---|---|
| `{{state}}` | Still `critical` or `resolved` |
| `{{state_line}}` | `State: Firing 🔥` or `State: Resolved ✅`, followed by a blank line |
| `{{date}}` | Jalali date as `Date: YYYY/MM/DD`. The prefix is capitalized. No time. |
| `{{dataSourceName}}` | Name on the webhook payload, or on the first firing alert |
| `{{alert_items}}` | Same label, annotation, and severity rules. `show_data_source` is ignored. Put `Data Source: {{dataSourceName}}` in the template when you want the data source on its own line. |

### Example

```
{{name}}
{{state_line}}
Host: {{label.instance}}
{{annotations:summary,description}}
{{date}}
```

## API and Notification

API alerts and Notification alerts share this syntax. They do not support `{{label.*}}`, `{{labels:...}}`, `{{annotations:...}}`, or `{{alert_items}}`.

### Default template

```
{{name}}
{{state_line}}
{{instance_line}}{{description_line}}{{date}}
```

`{{instance_line}}` and `{{description_line}}` already end with a newline when they have a value, so they sit on their own lines without an extra break in the template. When the value is empty, the placeholder disappears and the next line moves up.

### Placeholders

| Placeholder | Result |
|---|---|
| `{{name}}` | Alert rule name. `{{alertRuleName}}` is the same value. |
| `{{state}}` | `critical`, `resolved`, or `notification` |
| `{{state_line}}` | `State: Fire 🔥`, `State: Resolve ✅`, `State: Notification 📢`, or `state: Unknown`. No extra blank line. |
| `{{instance}}` | Instance value. `{{alert.instance}}` is the same value. |
| `{{instance_line}}` | `Instance: ...` plus a newline, or nothing when instance is empty |
| `{{description}}` | Description. `{{alert.description}}` is the same value. |
| `{{description_line}}` | `Description: ...` plus a newline, or nothing when empty |
| `{{summary}}` | Summary. `{{alert.summary}}` is the same value. |
| `{{summary_line}}` | `Summary: ...` plus a newline, or nothing when empty |
| `{{fireCount}}` | Current firing count on the alert rule |
| `{{date}}` | Jalali datetime as `Date: YYYY/MM/DD HH:mm:ss` |

A firing API alert with the default template looks like this:

```
API Alert
State: Fire 🔥
Instance: host-1
Description: disk full
Date: 1405/06/28 20:00:00
```

### Example

```
{{name}}
{{state_line}}
{{instance_line}}{{summary_line}}{{description_line}}Job: {{job}}
{{date}}
```
