---
id: prometheus-alertmanager
title: Prometheus & Alertmanager
sidebar_position: 2
slug: /integrations/prometheus-alertmanager
---

# Prometheus & Alertmanager

The most common setup. Add Skylogs as an Alertmanager receiver:

```yaml
# alertmanager.yml
receivers:
  - name: skylogs
    webhook_configs:
      - url: https://skylogs.example.com/api/v1/ingest/alertmanager/<token>
        send_resolved: true

route:
  receiver: skylogs
```

Skylogs maps Alertmanager fields automatically: `labels.severity` → severity, `labels.alertname` → alert name, `annotations.summary` / `description` → details, `status: resolved` → auto-resolve. Grouped notifications are unpacked into individual alerts and deduplicated by fingerprint.

{/* TODO: verify mapping details */}

## vmalert (VictoriaMetrics)

vmalert speaks the Alertmanager format — point its `-notifier.url` at the same Skylogs receiver URL.

## Blackbox / uptime probes

Service-down alerts from Prometheus Blackbox exporter flow in through this same integration. The probed target is carried as the affected resource, which Skylogs uses in correlation and root cause analysis.

## Tips

- Keep `send_resolved: true` so Skylogs auto-resolves recovered alerts.
- Put routing information in labels (`team`, `service`, `env`) — Skylogs routing rules match on them.
