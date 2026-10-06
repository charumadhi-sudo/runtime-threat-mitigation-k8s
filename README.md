# Runtime Threat Mitigation in Kubernetes

## Overview
**Runtime Threat Mitigation in Kubernetes** is a research and SDP project that constructs an automated, closed-loop runtime security pipeline for Kubernetes workloads. The pipeline integrates eBPF-based threat detection using **Falco** and **Falcosidekick**, alert routing, a custom **Python Policy-Decision Controller**, graduated response enforcement via **Kyverno** and **Istio/Otterize**, and end-to-end observability via **Grafana & Loki**. Unlike existing literature and baseline solutions that rely solely on crude pod deletion upon threat detection, this project introduces a severity-aware, graduated response model (Alert-Only -> Restrict -> Quarantine -> Terminate) that mitigates active runtime threats while preserving application availability and system stability.

## Architecture Pipeline
```
+-------------------+      +------------------+      +-------------------------------+
|  Target Workload  | ---> |   Falco (eBPF)   | ---> |          Falcosidekick        |
|    (demo-app)     |      | Threat Detection |      |       Alert Forwarder         |
+-------------------+      +------------------+      +---------------+---------------+
                                                                     | Webhook
                                                                     v
+-------------------+      +------------------+      +-------------------------------+
|   Grafana + Loki  | <--- | Kyverno / Istio  | <--- |    Python Policy-Decision     |
|   Observability   |      | Policy Enforcer  |      |   Controller (Graduated)      |
+-------------------+      +------------------+      +-------------------------------+
```

## Tech Stack
- **Container Orchestration**: Kubernetes (Kind / Minikube)
- **Runtime Detection**: Falco (eBPF probes / Kernel module)
- **Alert Routing**: Falcosidekick
- **Policy Decision Engine**: Python 3.11+ (Flask/FastAPI, Kubernetes Client Library)
- **Policy Enforcement**:
  - **Kyverno**: Admission control & dynamic policy enforcement (capabilities removal, security context restriction)
  - **Istio / Otterize**: Microsegmentation & network isolation (AuthorizationPolicy / NetworkPolicy quarantine)
- **Observability & Metrics**: Grafana, Loki, Prometheus
- **Attack Simulation**: Custom Bash & Python exploit scripts

## Project Phases Checklist
- [ ] **Phase 0: Environment Setup & Scaffolding**
  - [ ] Local K8s cluster provisioned (Kind / Minikube)
  - [ ] Helm & CLI toolchain configured
  - [ ] Repository structure & Git workflow established
- [ ] **Phase 1: Threat Detection & Alert Routing**
  - [ ] Falco deployed with eBPF driver
  - [ ] Custom Falco threat rules defined (shell execution, privilege escalation, suspicious file access)
  - [ ] Falcosidekick configured for webhook dispatching
- [ ] **Phase 1.5: Attack Simulation Baseline**
  - [ ] Vulnerable demo workload deployed
  - [ ] Attack scripts created (reverse shell, `/etc/shadow` access, network port scanning)
  - [ ] Detection rule trigger verification completed
- [ ] **Phase 2: Graduated Response Mechanism Design**
  - [ ] Severity mapping schema established (Low, Medium, High, Critical)
  - [ ] Enforcement policy templates developed for Kyverno & Istio/Otterize
- [ ] **Phase 3: Python Policy-Decision Controller**
  - [ ] Webhook listener service implemented
  - [ ] State tracking & threat counter logic built
  - [ ] Severity classification & K8s API enforcement dispatcher implemented
- [ ] **Phase 4: Observability & Telemetry Integration**
  - [ ] Loki & Prometheus logging/metrics stack deployed
  - [ ] Grafana threat mitigation dashboards imported and validated
- [ ] **Phase 5: End-to-End Evaluation & Benchmarking**
  - [ ] Closed-loop threat mitigation workflows tested
  - [ ] Response latency & overhead measured
  - [ ] Comparative evaluation against pod-deletion baseline performed

---
*Maintained by the Runtime Threat Mitigation Research Team.*
