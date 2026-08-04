---
id: pmm
title: PMM (Percona)
sidebar_position: 8
slug: /integrations/pmm
---

# PMM (Percona Monitoring and Management)

PMM's alerting is Alertmanager-compatible — configure the Skylogs [Alertmanager receiver URL](/integrations/prometheus-alertmanager) in PMM's alert settings.

Database-specific labels (service, node, cluster) are preserved as tags for routing — useful for giving each database team ownership of its own alerts.

{/* TODO: add PMM-specific screenshots and label examples */}
