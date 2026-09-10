---
id: kubernetes
title: Kubernetes / Helm
sidebar_position: 2
slug: /deployment/kubernetes
---

# Kubernetes / Helm

The [Quick Start](/quick-start) and [Docker Compose (production)](/deployment/docker-compose) pages cover single-host installs. This page covers running Skylogs on **Kubernetes** with the official Helm chart — for evaluation clusters and for production, with real resource limits, ingress/TLS, and external datastores.

Chart source and configuration reference: [github.com/skylogsio/helm-charts](https://github.com/skylogsio/helm-charts). Application source: [github.com/skylogsio/skylogs](https://github.com/skylogsio/skylogs).

## Architecture

The chart deploys Skylogs as one release, with no external chart dependencies:

```
                        Ingress (skylogs.example.com)
                                   |
                     Service: <release>-frontend :80
                                   |
                          [ frontend / Next.js ]
                                   | BASE_URL
                     Service: <release>-backend :80
                                   |
              +--------------- backend pod ----------------+
              |  [nginx :80]  --fastcgi-->  [php-fpm :9000] |
              |        \___ shared emptyDir /var/www/html __/
              +---------------------------------------------+
                       |                        |
        Service: <release>-mongodb :27017   <release>-redis :6379
              [ MongoDB StatefulSet+PVC ]   [ Redis Deployment ]

   [ horizon ]  [ crontab ]  — backend image, DEPLOY_TYPE env, shared env Secret
   [ sentinel ] — watchdog, config.yaml from ConfigMap, Service :9191
```

Notable design decisions, compared to the [Docker Compose](/deployment/docker-compose) layout:

- `backend` and its nginx sidecar run in **one pod**; the compose `skylogs_back` shared volume becomes a pod-local `emptyDir`, and `fastcgi_pass` targets `127.0.0.1:9000`.
- One shared Secret (`<release>-env`) carries the Laravel env; `backend`, `horizon`, and `crontab` all consume it via `envFrom`. Deployments carry a checksum annotation, so editing config/secrets rolls the pods automatically — no Reloader needed.
- MongoDB ships as a **single-replica StatefulSet** with a `volumeClaimTemplate` and a headless Service — this mirrors Compose, not an HA database. See [Things to verify before production](#things-to-verify-before-production).
- Redis keeps `requirepass` in a mounted `redis.conf` (from a Secret) rather than in container args, so the password doesn't show up in the pod spec.
- All resource names derive from the release name, so multiple releases can coexist in one namespace.

## Chart installation and repo

```bash
helm repo add skylogs https://skylogsio.github.io/helm-charts/
helm repo update

helm install skylogs skylogs/skylogs \
  --namespace skylogs --create-namespace \
  -f my-values.yaml
```

Useful before installing:

```bash
helm show values skylogs/skylogs > values.yaml   # inspect the full default values
helm template skylogs skylogs/skylogs -f my-values.yaml | less   # render manifests without installing
```

Minimum `my-values.yaml` for a real deployment — at least the URLs, secrets, image tags, and ingress host:

```yaml
config:
  appUrl: https://skylogs.example.com/api
  frontendUrl: https://skylogs.example.com
  nextauthUrl: https://skylogs.example.com

secrets:
  dbPassword: "<strong password>"
  redisPassword: "<strong password>"
  jwtSecret: "<openssl rand -hex 32>"
  nextauthSecret: "<openssl rand -base64 32>"

backend:
  image:
    tag: "<release tag>"      # pin — see the releases page
frontend:
  image:
    tag: "<release tag>"
  ingress:
    className: nginx
    host: skylogs.example.com
    tls:
      - secretName: skylogs-tls
        hosts: [skylogs.example.com]
```

Keep secret values out of git — use a separate values file, `helm secrets`, SOPS, or point `secrets.existingSecret` at a Secret managed by external-secrets/sealed-secrets.

:::warning Change the default login
Fresh installs ship with `admin` / `SkylogsAdmin`. Change it immediately — before exposing the instance to your network.
:::

## values.yaml reference

The chart is organized per component (`backend`, `frontend`, `horizon`, `crontab`, `sentinel`, `mongodb`, `redis`, `migrations`). Each supports `resources`, `nodeSelector`, `tolerations`, and `affinity` individually, so you can pin the database differently from the stateless workers.

### Resources

Every component defaults to `resources: {}` (no requests/limits) — set them explicitly before production:

```yaml
backend:
  resources:
    requests: { cpu: 250m, memory: 256Mi }
    limits: { memory: 1Gi }
```

### Persistence

MongoDB is the only component with a PVC by default:

```yaml
mongodb:
  enabled: true
  persistence:
    size: 8Gi
    storageClass: ""        # "" = cluster default
    accessModes: [ReadWriteOnce]
```

To use a managed or operator-run MongoDB / Redis instead of the bundled ones:

```yaml
mongodb:
  enabled: false
externalMongodb:
  host: mongo.example.internal
  port: 27017

redis:
  enabled: false
externalRedis:
  host: redis.example.internal
  port: 6379
```

### Ingress and TLS

The frontend ingress is enabled by default; the backend ingress is off (the frontend reaches the API in-cluster, so exposing the API directly is only needed for inbound webhooks / external integrations):

```yaml
frontend:
  ingress:
    enabled: true
    className: nginx
    annotations:
      cert-manager.io/cluster-issuer: letsencrypt
    host: skylogs.example.com
    tls:
      - secretName: skylogs-tls
        hosts: [skylogs.example.com]

backend:
  ingress:
    enabled: false
    host: api.skylogs.example.com
```

### Migrations

Disabled by default, because the backend image's entrypoint may already run migrations when `DEPLOY_TYPE=web`. Enable it as a Helm hook Job (runs pre-install and pre-upgrade) if it doesn't:

```yaml
migrations:
  enabled: true
  # defaults to: cd /opt/skylogs-api && php artisan migrate --force
```

### Custom nginx vhost

The backend's nginx sidecar config can be fully overridden — paste your `apps/backend/nginx.conf`, keeping `fastcgi_pass 127.0.0.1:9000` since php-fpm runs in the same pod:

```yaml
backend:
  nginx:
    serverConfig: |
      server {
        ...
      }
```

## Running HA

The chart schedules one replica per component by default (`replicas: 1` for `backend`, `frontend`, `horizon`, `sentinel`; a single-node StatefulSet for `mongodb`). It does not ship pod disruption budgets, anti-affinity rules, or topology spread constraints out of the box — set them yourself via each component's `affinity`/`tolerations`/`nodeSelector` fields and your own `PodDisruptionBudget` objects if you scale `replicas` up.

For resilience across whole datacenters/regions rather than within a cluster, see [Multi-zone federation](#multi-zone-on-multiple-clusters) below and [Multi-zone & HA](/deployment/multi-zone-ha).

## Multi-zone on multiple clusters

**Sentinel** is the cross-zone heartbeat watchdog — see [Multi-zone & HA → Multi-zone mode (Sentinel)](/deployment/multi-zone-ha#multi-zone-mode-sentinel) for the concept. It's disabled by default in the chart (mirrors the `multizone` profile in Docker Compose) because it needs real peer/heartbeat configuration before it can start:

```yaml
sentinel:
  enabled: true
  image:
    tag: "<release tag>"
  env:
    SENTINEL_ID: dc2-sentinel
    SENTINEL_ROLE: secondary
    MAIN_SKYLOGS_HEARTBEAT_URL: http://<primary-site>/heartbeat
    ALERT_WEBHOOK_URL: http://<primary-site>/internal/alerts/sentinel
  config: |
    # contents of apps/sentinel/config.yaml — peers list and shared secret
```

Each zone is its own Helm release (its own cluster or namespace), running the full stack; Sentinel is what ties them together into the heartbeat topology described in [Multi-zone & HA](/deployment/multi-zone-ha).

## Upgrades with Helm

```bash
helm repo update
helm upgrade skylogs skylogs/skylogs \
  --namespace skylogs \
  -f my-values.yaml
```

Pin `backend.image.tag` / `frontend.image.tag` / `sentinel.image.tag` to a release rather than `latest`, and read the release notes before upgrading. Because Deployments carry a config/secret checksum annotation, a values change alone (not just an image tag bump) also triggers a rolling restart of the affected pods.

## Things to verify before production

- Whether your backend image already runs `php artisan migrate` on boot (`DEPLOY_TYPE=web`) — if so, leave `migrations.enabled: false`.
- The path assumption in `migrations.command` (`/opt/skylogs-api`) matches your image.
- Sentinel's heartbeat/webhook URLs — the compose default (`skylogs-core:8080`) doesn't exist in a Kubernetes deployment; point it at your real primary site.
- Resource requests/limits — empty by default; set them for every component before production.
- MongoDB HA — the bundled StatefulSet is single-node, same as Compose. For production, consider the MongoDB Community Operator or a managed database and set `mongodb.enabled: false`.

## Health and monitoring

As with Compose, expose the instance to an **external** uptime check and dead-man's-switch — the incident platform must not be its own only observer. See [Monitoring Skylogs itself](/guides/monitoring-skylogs).
