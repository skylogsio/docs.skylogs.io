---
id: zabbix
title: Zabbix
sidebar_position: 4
slug: /integrations/zabbix
---

# Zabbix

Skylogs treats Zabbix as a first-class citizen — including for network and datacenter teams where Zabbix is the primary monitoring system.

## Setup

1. In Zabbix: **Alerts → Media types → Create media type** (type: Webhook)
2. Import the Skylogs media type template {/* TODO: link the actual template file */}
3. Set the endpoint URL to `https://skylogs.example.com/api/v1/ingest/zabbix/<token>`
4. Create an **action** that sends problems (and recovery events) through this media type.

## Field mapping

Problem severity, host, trigger, and recovery events map to Skylogs severity, resource, alert name, and auto-resolution.

{/* TODO: verify mapping table against the real parser */}

## Tips

- Send **recovery events** too, so alerts auto-resolve.
- Use Zabbix host groups / tags to drive Skylogs routing rules per team.
