---
id: installation
title: Installation
sidebar_position: 1
slug: /installation
---

# Installation

This guide takes you from zero to a running Skylogs instance. Target time: under 10 minutes. When you're done, continue to the [Quick start](/quick-start) to fire your first test alert.

For production deployments, multi-zone federation, and high availability, see [Deployment](/deployment).

## Requirements

- **Docker** 24+ and **Docker Compose** v2
- 2 CPU cores, 4 GB RAM minimum (single-node evaluation) {/* TODO: verify real minimums */}
- Outbound access for the notification channels you plan to use (SMTP, SMS/voice gateway, Slack, Telegram, Microsoft Teams)

Skylogs runs entirely in containers. You do not need PHP, Node.js, Go, or MongoDB installed on the host.

## Install with Docker Compose

```bash
git clone https://github.com/skylogsio/skylogs.git
cd skylogs
docker compose up -d --build
```

This starts the full stack:

| Container | Role |
|---|---|
| `skylogs-app` | Web UI and API |
| `skylogs-worker` | Queue workers: escalations, notifications, schedulers |
| `skylogs-mongo` | Alert and incident storage (MongoDB) |
| `skylogs-redis` | Queues and caching |

{/* TODO: confirm actual service names and stack components */}

When all containers report healthy:

1. Open `http://localhost:PORT` {/* TODO: real port */}
2. Log in with the default credentials: `USERNAME` / `PASSWORD` {/* TODO: real defaults */}
3. **Change the default password immediately.**

## Configuration

All configuration is done through environment variables in `.env` (copy `.env.example` to start). The most important settings:

```env
APP_URL=https://skylogs.example.com
APP_KEY=                      # generate with: docker compose exec skylogs-app php artisan key:generate

# Database
MONGO_URI=mongodb://skylogs-mongo:27017/skylogs

# Notification channels (configure the ones you use)
MAIL_HOST=
MAIL_PORT=587
SLACK_BOT_TOKEN=
TELEGRAM_BOT_TOKEN=
SMS_GATEWAY_URL=
VOICE_GATEWAY_URL=
```

{/* TODO: replace with the real variable names from .env.example */}

See the [Admin guide](/admin-guide) for the full configuration reference.

## Upgrading

```bash
git pull
docker compose pull
docker compose up -d --build
```

Database migrations run automatically on startup. {/* TODO: confirm */} Always read the [release notes](https://github.com/skylogsio/skylogs/releases) before upgrading a production instance.

## Uninstalling

```bash
docker compose down          # stop the stack, keep data
docker compose down -v       # stop the stack and delete all data volumes
```

## Troubleshooting

**Containers start but the UI is unreachable** — check that the port is not already in use (`docker compose logs skylogs-app`) and that no firewall blocks it.

**Login fails with default credentials** — the initial admin user is seeded on first boot only. If you recreated volumes, wait for the seeder to finish; check logs for `Seeding completed`. {/* TODO: verify */}

Still stuck? Open an [issue](https://github.com/skylogsio/skylogs/issues) or ask in [Discussions](https://github.com/skylogsio/skylogs/discussions).
