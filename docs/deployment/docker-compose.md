---
id: docker-compose
title: Docker Compose (production)
sidebar_position: 1
slug: /deployment/docker-compose
---

# Docker Compose (production)

The [Quick Start](/quick-start) gets Skylogs running in five minutes with defaults. This page covers running the **same Docker Compose deployment in production**: pinned versions, persistent data, TLS, and safe upgrades. For multi-server resilience, continue to [Multi-zone & HA](/deployment/multi-zone-ha).

## Use the stable release

Always pin production to a released version rather than building from source:

```bash
git clone https://github.com/skylogsio/skylogs.git
cd skylogs
git checkout <release-tag>        # pin a version — see the releases page
docker compose up -d
```

`docker-compose-build.yml` (build-from-source) is for development and testing only.

## Configuration

Production settings live in the environment file. At minimum, review: {/* TODO: confirm variable names against .env.example */}

```env
APP_URL=https://skylogs.example.com   # public URL behind your proxy
# strong, unique credentials for MongoDB / Redis
# notification provider settings (SMTP, SMS/call gateway, Telegram, …)
```

:::warning Change the default login
Fresh installs ship with `admin` / `SkylogsAdmin`. Change it immediately — before exposing the instance to your network.
:::

## Persistence

Alert history, incidents, and configuration live in the MongoDB volume. Verify volumes are on durable storage and included in your [backup procedure](/guides/backup-restore):

```bash
docker volume ls | grep skylogs   # confirm volumes exist
```

{/* TODO: list the exact volume names created by the compose file */}

## TLS and reverse proxy

Run Skylogs behind a reverse proxy (nginx, Traefik, Caddy) that terminates TLS. Point the proxy at the Skylogs web port (`8080` by default) and set `APP_URL` to the public HTTPS URL so generated links and webhooks are correct.

## Health and monitoring

Expose the instance to an **external** uptime check and configure a dead-man's-switch — the incident platform must not be its own only observer. See [Monitoring Skylogs itself](/guides/monitoring-skylogs).

## Upgrading

```bash
git fetch --tags
git checkout <new-release-tag>
docker compose pull
docker compose up -d
```

Read the release notes before upgrading. For zero-downtime upgrades you need an [HA cluster](/deployment/multi-zone-ha) — a single-node compose deployment has a brief restart window.

## When to move beyond single-node Compose

Single-node Docker Compose is appropriate for evaluation and small teams that accept a restart window during upgrades and a single point of failure. Move to [HA mode](/deployment/multi-zone-ha) when a missed page is unacceptable, and add [multi-zone federation](/deployment/multi-zone-ha#multi-zone-mode-sentinel) when you need to survive a datacenter outage. Kubernetes users: see [Kubernetes / Helm](/deployment/kubernetes).
