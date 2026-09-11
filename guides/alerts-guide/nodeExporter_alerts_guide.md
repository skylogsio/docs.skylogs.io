# Node Exporter Alerts Guide

A comprehensive guide for monitoring system metrics using Node Exporter in Prometheus/Alertmanager.

> ✅ MDX-safe version: All PromQL queries are placed inside fenced code blocks to avoid `{}` or `< >` parsing issues in Docusaurus.

---

# 1. CPU Alerts

## NodeCPUHigh

**Description:** CPU usage is consistently high
**Severity:** critical

```promql
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 85
```

## NodeCPULoadHigh

**Description:** System load is high compared to CPU cores
**Severity:** warning

```promql
node_load1 / count(node_cpu_seconds_total{mode="idle"}) > 1.5
```

## NodeCPULoadVeryHigh

**Description:** Load is much higher than capacity
**Severity:** critical

```promql
node_load5 / count(node_cpu_seconds_total{mode="idle"}) > 2
```

---

# 2. Memory Alerts

## NodeMemoryLow

**Description:** Available memory is low
**Severity:** critical

```promql
(node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) < 0.15
```

## NodeMemorySwapHigh

**Description:** Swap usage is high
**Severity:** warning

```promql
(node_memory_SwapUsed_bytes / node_memory_SwapTotal_bytes) > 0.20
```

---

# 3. Disk Alerts

## NodeDiskFull

**Description:** Disk usage exceeds threshold
**Severity:** critical

```promql
(node_filesystem_avail_bytes{fstype!~"tmpfs|overlay"} / node_filesystem_size_bytes{fstype!~"tmpfs|overlay"}) < 0.10
```

## NodeDiskAlmostFull

**Description:** Disk usage approaching full
**Severity:** warning

```promql
(node_filesystem_avail_bytes{fstype!~"tmpfs|overlay"} / node_filesystem_size_bytes{fstype!~"tmpfs|overlay"}) < 0.20
```

## NodeDiskIOHigh

**Description:** High disk I/O time
**Severity:** warning

```promql
rate(node_disk_io_time_seconds_total[5m]) > 0.9
```

---

# 4. Network Alerts

## NodeNetworkErrorRateHigh

**Description:** High network error rate
**Severity:** warning

```promql
rate(node_network_receive_errs_total[5m]) > 0 or rate(node_network_transmit_errs_total[5m]) > 0
```

## NodeNetworkDropHigh

**Description:** High packet drop
**Severity:** warning

```promql
rate(node_network_receive_drop_total[5m]) > 0 or rate(node_network_transmit_drop_total[5m]) > 0
```

## NodeNetworkBandwidthHigh

**Description:** Network link saturation (replace SPEED with interface bytes/sec)
**Severity:** warning

```promql
(rate(node_network_transmit_bytes_total[5m]) + rate(node_network_receive_bytes_total[5m])) > 0.9 * SPEED
```

---

# 5. Filesystem & Inodes Alerts

## NodeInodesFull

**Description:** Inodes usage high
**Severity:** critical

```promql
(node_filesystem_files{fstype!~"tmpfs|overlay"} - node_filesystem_files_free{fstype!~"tmpfs|overlay"}) / node_filesystem_files{fstype!~"tmpfs|overlay"} > 0.85
```

## NodeInodesAlmostFull

**Description:** Inodes approaching full
**Severity:** warning

```promql
(node_filesystem_files{fstype!~"tmpfs|overlay"} - node_filesystem_files_free{fstype!~"tmpfs|overlay"}) / node_filesystem_files{fstype!~"tmpfs|overlay"} > 0.70
```

---

# 6. System & Hardware Alerts

## NodeFilesystemReadOnly

**Description:** Filesystem became read-only
**Severity:** critical

```promql
node_filesystem_readonly == 1
```

## NodeTempHigh

**Description:** CPU or system temperature high
**Severity:** critical

```promql
node_thermal_zone_temp > 80
```

## NodeBootTimeChanged

**Description:** Node reboot detected
**Severity:** warning

```promql
changes(node_boot_time_seconds[1h]) > 0
```

---

# 7. Availability Alerts

## NodeExporterDown

**Description:** Node exporter not reachable
**Severity:** critical

```promql
up{job="node_exporter"} == 0
```

## NodeHighContextSwitches

**Description:** Too many context switches
**Severity:** warning

```promql
rate(node_context_switches_total[5m]) > 10000
```

## NodeHighInterrupts

**Description:** High interrupts per second
**Severity:** warning

```promql
rate(node_intr_total[5m]) > 10000
```

---

# Best Practices

* Use alert durations (for: 5m) to avoid flapping
* Separate warning vs critical
* Add runbooks for remediation
* Group alerts in Alertmanager
* Filter tmpfs/overlay filesystems

---

This format is fully compatible with Docusaurus + MDX.
