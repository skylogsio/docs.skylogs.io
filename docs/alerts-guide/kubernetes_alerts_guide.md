# Standard Kubernetes & Prometheus Alerts  

This document explains all standard alerts used in **kube-prometheus**, **kube-prometheus-stack**, and **Prometheus Operator**, grouped by category with meanings, causes, and resolutions.

---

# 🟦 1. Pod-Level Alerts

## 🔹 KubePodCrashLooping
**Meaning:** Pod is repeatedly crashing (CrashLoopBackOff).  
**Cause:** Application failure, wrong config, bad image, missing dependency.  
**Fix:** Check `kubectl logs`, readiness/liveness probes, startup scripts.

---

## 🔹 KubePodNotReady
**Meaning:** Pod stays in NotReady for too long.  
**Cause:** ReadinessProbe failing, app not ready.  
**Fix:** Fix readiness probes, check application initialization.

---

## 🔹 KubePodInitializing
**Meaning:** Pod stuck in init phase.  
**Cause:** InitContainer failing or image pull error.  
**Fix:** Check init container logs; verify registry.

---

## 🔹 KubePodImagePullBackOff
**Meaning:** Kubernetes cannot pull the container image.  
**Cause:** Wrong image tag, private registry, missing pull secret.  
**Fix:** Check imagePullSecrets, fix image name.

---

## 🔹 KubePodPending
**Meaning:** Pod cannot be scheduled to a node.  
**Cause:** Insufficient CPU/Memory, taints, node affinity mismatch.  
**Fix:** Check scheduler events, increase resources.

---

## 🔹 KubePodContainerTerminated
**Meaning:** Container terminated unexpectedly.  
**Fix:** Inspect termination message & exit code.

---

## 🔹 KubePodUnschedulable
**Meaning:** Scheduler cannot place pod on any node.  
**Fix:** Fix taints, tolerations, requests/limits mismatch.

---

# 🟦 2. Node-Level Alerts

## 🔹 KubeNodeNotReady
**Meaning:** Node is in NotReady status.  
**Cause:** Node offline, kubelet down, networking failure.  
**Fix:** Check node status, kubelet service.

---

## 🔹 KubeNodeUnreachable
**Meaning:** Prometheus cannot reach the node.  
**Fix:** Validate network, cloud route tables, firewalls.

---

## 🔹 KubeNodeMemoryPressure
**Meaning:** Node experiencing memory pressure.  
**Fix:** Increase node size, reduce workload memory.

---

## 🔹 KubeNodeDiskPressure
**Meaning:** Disk too full to run pods safely.  
**Fix:** Cleanup disk or resize volume.

---

## 🔹 KubeNodeOutOfDisk
**Meaning:** Node reported out-of-disk.  
**Fix:** Remove old images/containers, expand disk.

---

## 🔹 KubeNodeCPUHigh
**Meaning:** High CPU usage on node.  
**Fix:** Add nodes, enable autoscaling.

---

# 🟦 3. Workload Alerts (Deployment, StatefulSet, DaemonSet, Jobs)

## 🔹 KubeDeploymentReplicasMismatch
**Meaning:** Deployment desired replicas ≠ available replicas.  
**Cause:** Pod startup issues, crash loops, scheduling issues.  
**Fix:** Check pods for errors.

---

## 🔹 KubeStatefulSetReplicasMismatch
**Meaning:** StatefulSet not running requested replica count.  
**Cause:** PVC issues, startup delays.  
**Fix:** Inspect pods & storage.

---

## 🔹 KubeDaemonSetRolloutStuck
**Meaning:** DaemonSet cannot complete rollout.  
**Cause:** Node taints, readiness failures.  
**Fix:** Investigate daemonset pods on each node.

---

## 🔹 KubeJobFailed
**Meaning:** Job failed or backoff limit exceeded.  
**Fix:** Inspect job logs and restart.

---

## 🔹 KubeCronJobTooLong
**Meaning:** CronJob running longer than expected.  
**Fix:** Optimize workload, increase resources.

---

# 🟦 4. API Server Alerts

## 🔹 KubeAPIDown
**Meaning:** Prometheus cannot reach the API server.  
**Fix:** Check control-plane nodes, LB, network.

---

## 🔹 KubeAPIServerHighLatency
**Meaning:** API server taking too long to respond.  
**Cause:** Overloaded control plane, slow etcd.  
**Fix:** Check CPU usage, webhooks, etcd latency.

---

## 🔹 KubeAPIServerErrors
**Meaning:** High rate of API server 5xx errors.  
**Fix:** Fix RBAC issues, API overload, admission webhooks.

---

# 🟦 5. etcd Alerts

## 🔹 EtcdDown
**Meaning:** etcd server unreachable.  
**Fix:** Check etcd pods, certificates, systemd.

---

## 🔹 EtcdHighNumberOfLeaderChanges
**Meaning:** Frequent leader changes, unhealthy cluster.  
**Fix:** Improve network stability.

---

## 🔹 EtcdHighFsyncDurations
**Meaning:** Excessive fsync duration (slow disk).  
**Fix:** Move to SSD/NVMe storage.

---

## 🔹 EtcdHighCommitDurations
**Meaning:** Slow commit performance.  
**Fix:** Reduce load, upgrade CPU/disk performance.

---

# 🟦 6. Kubelet Alerts

## 🔹 KubeletDown
**Meaning:** Prometheus cannot scrape kubelet.  
**Fix:** Restart kubelet, check network.

---

## 🔹 KubeletTooManyPods
**Meaning:** Node reached maximum pod capacity.  
**Fix:** Add nodes or change pod limit.

---

## 🔹 KubeletRuntimeOperationsErrors
**Meaning:** Runtime (containerd/docker) errors occurring.  
**Fix:** Check container runtime logs.

---

## 🔹 KubeletPodStartUpLatencyHigh
**Meaning:** Pods taking too long to start.  
**Cause:** Slow image pulls, huge container image, slow disks.  
**Fix:** Optimize container images.

---

# 🟦 7. Storage Alerts (PVC, PV, CSI)

## 🔹 KubePersistentVolumeUsageCritical
**Meaning:** PV utilization critical.  
**Fix:** Cleanup or expand PVC.

---

## 🔹 KubePersistentVolumeErrors
**Meaning:** Volume experiencing errors.  
**Fix:** Inspect CSI logs, check disk health.

---

## 🔹 KubePersistentVolumeIsReadOnly
**Meaning:** PV remounted read-only.  
**Cause:** Filesystem corruption, node disk issue.  
**Fix:** Repair filesystem or node storage.

---

# 🟦 8. Networking Alerts

## 🔹 KubeProxyDown
**Meaning:** kube-proxy DaemonSet unstable or unreachable.  
**Fix:** Restart kube-proxy, check CNI.

---

## 🔹 KubeDNSDown / CoreDNSDown
**Meaning:** DNS cluster unhealthy.  
**Fix:** Check CoreDNS crash loops or resource limits.

---

## 🔹 KubeNetworkUnavailable
**Meaning:** Network plugin not ready on node.  
**Cause:** CNI error (Calico, Cilium, Flannel).  
**Fix:** Check CNI logs.

---

# 🟦 9. Prometheus Self-Alerts

## 🔹 PrometheusDown
**Meaning:** Prometheus instance unreachable.  
**Fix:** Restart pod, check PVC, TSDB corruption.

---

## 🔹 PrometheusMissingRuleEvaluations
**Meaning:** Rules not being evaluated.  
**Fix:** Prometheus overloaded or high rule count.

---

## 🔹 PrometheusDiskSlow / PrometheusTSDBErrors
**Meaning:** Disk latency or TSDB errors.  
**Fix:** Move Prometheus to SSD/NVMe.

---

## 🔹 AlertmanagerDown
**Meaning:** Alertmanager unreachable.  
**Fix:** Check configuration, certificates, service.

---

# 🟦 10. Resource Usage Alerts

## 🔹 KubeCPUQuotaExceeded
**Meaning:** Pod CPU throttling is high.  
**Fix:** Increase CPU limit or remove limit.

---

## 🔹 KubeMemoryQuotaExceeded
**Meaning:** Pod exceeded memory limit → OOMKilled.  
**Fix:** Increase memory limits.

---

## 🔹 NodeFilesystemSpaceFillingUp
**Meaning:** Disk predicted to fill soon.  
**Fix:** Cleanup logs, rotate files, resize disk.

---

## 🔹 NodeFileDescriptorLimit
**Meaning:** Node nearing file descriptor exhaustion.  
**Fix:** Increase OS ulimit.

---

# 📌 Want More?

Available on request:

- **Full PromQL expressions** for every alert  
- **PrometheusRule YAML** ready for deployment  
- **Export as PDF or DOCX**  
- **Auto-generated visual documentation**

Just ask:

`Give me full PromQL rules`  
or  
`Generate PrometheusRule YAML`

