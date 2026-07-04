---
id: multi-zone-ha
title: Multi-zone & HA
sidebar_position: 1
slug: /deployment
---

# Deployment — Multi-zone & HA

This page covers running Skylogs in production: high availability within a zone, multi-zone federation across datacenters, and the production checklist. For the design rationale behind the two layers, read [Architecture](/architecture) first.

## High-availability mode (Raft)

### Requirements

- **3 nodes minimum** (Raft requires a majority; 3 nodes tolerate 1 failure, 5 tolerate 2). Never run an even number of nodes.
- Low-latency network between nodes (same datacenter / zone). Do **not** stretch an HA cluster across a WAN — that is what multi-zone mode is for.
- Time synchronization (NTP/chrony) on all nodes.

### Setup

{/* TODO: replace with real configuration once finalized */}

```yaml
# cluster.yaml (example)
zone: eu-west-dc1
ha:
  node_id: node-1
  bind: 10.0.1.11:7000
  peers:
    - 10.0.1.11:7000
    - 10.0.1.12:7000
    - 10.0.1.13:7000
```

Start the nodes; the cluster bootstraps and elects a leader automatically. Verify with:

```bash
skylogs-cluster status
```

{/* TODO: replace with the real status command / endpoint */}

### Behavior during failures

- **Leader fails** → new election completes in seconds; in-flight escalations resume from replicated state. A brief election also occurs during rolling upgrades — normal, and no alerts are lost.
- **One follower fails (3-node cluster)** → no impact; the cluster keeps a majority.
- **Two nodes fail (3-node cluster)** → the surviving node cannot form a majority and stops accepting critical writes to protect consistency. Restore a second node to resume. {/* TODO: confirm read-only behavior */}

## Multi-zone mode (Sentinel)

### Requirements

- 2+ zones, each with its own complete Skylogs deployment (standalone or HA)
- Network connectivity between zones for Sentinel heartbeat + sync traffic {/* TODO: document ports/protocol */}
- Mutual TLS between zones (recommended) {/* TODO: confirm */}

### Setup

{/* TODO: replace with real configuration once finalized */}

```yaml
# cluster.yaml (example)
zone: eu-west-dc1
federation:
  peers:
    - name: eu-central-dc2
      endpoint: sentinel.dc2.example.com:7100
    - name: us-east-dc3
      endpoint: sentinel.dc3.example.com:7100
```

### Organizational writes and conflicts

Organizational changes (editing a team, changing a schedule) are low-frequency and human-driven. Designate a **primary zone** for organizational writes; other zones receive updates via sync. {/* TODO: confirm the actual conflict-resolution model */}

### Behavior during failures

- **Zone loses connectivity** → it continues ingesting, escalating, and notifying with local alert data and its synced copy of organizational data. Other zones raise a zone-down alert. On reconnection, organizational data re-syncs.
- **Zone is destroyed** → its local alert history is lost with it (alert data is zone-local by design); organizational data survives everywhere. Rebuild and rejoin; org data syncs back automatically. If alert history must survive zone loss, configure per-zone backups.

## Production checklist

- [ ] 3-node HA per zone (or a documented decision to accept single-node zones)
- [ ] NTP on all nodes
- [ ] TLS on all external endpoints and between zones
- [ ] Per-zone backups of MongoDB data and configuration, restore-tested
- [ ] Monitoring of Skylogs itself from *outside* Skylogs (external uptime check + dead-man's-switch)
- [ ] A rehearsed rolling upgrade proving zero lost alerts during leader elections
- [ ] Default credentials changed; RBAC configured ([Admin guide](/admin-guide))

## FAQ

**Can I run HA with 2 nodes?** No — 2 nodes cannot tolerate any failure under Raft (majority of 2 is 2). Use 1 or 3.

**Can I stretch one HA cluster across two datacenters?** No. One HA cluster per zone; connect zones with multi-zone mode. Stretching Raft across a WAN degrades every write and loses quorum on partition — the exact moment you need it most.

**Do zones share alert data?** No, intentionally. Each zone owns the alerts it ingests; organizational data is what's shared.
