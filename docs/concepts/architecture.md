---
id: architecture
title: Architecture
sidebar_position: 2
slug: /architecture
---

# Architecture

Skylogs is designed around a simple principle: **the incident platform is the last thing allowed to go down.** Most self-hosted alerting tools have a single point of failure — themselves. Skylogs removes it with two independent resilience layers.

The mental model:

> **HA inside the zone. Federation across zones.**

## The two layers

### High availability (Raft) — inside a zone

Within a zone, Skylogs nodes form a cluster built on the **Raft consensus algorithm**. All critical state changes — alert status transitions, acknowledgments, escalation timer state, on-call assignments — are committed through a replicated log before they take effect, and every node holds an identical copy of critical state.

If the leader node fails, the remaining nodes elect a new leader within seconds and processing continues. No manual failover, no lost escalations, no dropped pages.

This layer is a **CP system**: it prioritizes consistency and requires a majority quorum (3 nodes tolerate 1 failure). It assumes low-latency links and must never be stretched across a WAN.

### Multi-zone federation (Sentinel) — across zones

Each zone runs a complete Skylogs deployment. Zones are connected by **Sentinel**, a lightweight Go service with two jobs:

1. **Heartbeat monitoring** — every zone continuously verifies the health of every other zone. If a zone goes dark, surviving zones detect it and can alert your team about the zone failure itself.
2. **Organizational data sync** — users, teams, endpoints, clusters, schedules, and escalation policies are replicated to all zones.

**Alert data is intentionally not replicated.** It stays in the zone that ingested it, so the zone closest to a failing system keeps ingesting, escalating, and notifying on its own data even when fully cut off from the rest of the world.

This layer is an **AP system**: it prioritizes availability. During a datacenter disaster or network partition, no zone ever waits for another zone's permission to page someone — and every surviving zone has the complete organizational context (who is on call, how to reach them) to run a full response alone.

## Why two separate layers?

Because the two problems demand opposite trade-offs. Strong consistency (Raft) requires a quorum — which is exactly what you *cannot* demand across datacenters, where a partition would take the minority side offline at the worst possible moment. Availability-first federation (Sentinel) tolerates partitions — but can't give the lost-page-is-unacceptable guarantees needed inside the escalation engine.

So the layers are strictly separated by design:

- A network partition between zones never blocks alerting inside a zone.
- A degraded Raft cluster inside a zone never stops the cross-zone heartbeat — other zones can still distinguish "zone degraded" from "zone destroyed."

This mirrors how mature infrastructure is built (e.g., Kubernetes runs etcd per cluster and treats cross-cluster federation as a separate, looser layer).

## Deployment topologies

| Topology | Protects against | Minimum footprint |
|---|---|---|
| Single node | — (evaluation only) | 1 server |
| HA cluster | Server failure within a zone | 3 servers, one zone |
| Multi-zone | Datacenter/region failure | 2 zones × 1 server |
| Multi-zone + HA | Both | 2–3 zones × 3 servers |

Setup instructions, failure behavior, and the production checklist are in [Deployment](/deployment).
