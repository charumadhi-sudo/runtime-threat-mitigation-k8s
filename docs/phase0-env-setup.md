# Phase 0: Environment Setup & Cluster Provisioning

## Objective
Establish a reproducible local Kubernetes environment with eBPF kernel tracing capabilities, package management (Helm), and Python dependencies required for the closed-loop Runtime Threat Mitigation pipeline.

---

## Toolchain Verification Matrix

| Tool | Minimum Version | Installation Command (Windows Winget) | Purpose |
| :--- | :--- | :--- | :--- |
| **Docker Desktop** | 24.0+ | `winget install Docker.DockerDesktop` | Container engine & Kind node runner |
| **kubectl** | v1.28+ | `winget install Kubernetes.kubectl` | K8s cluster administration CLI |
| **Kind** | v0.20+ | `winget install Kubernetes.kind` | Local K8s cluster provisioner with eBPF extraMounts |
| **Helm** | v3.12+ | `winget install Helm.Helm` | K8s package manager for Falco, Kyverno & Prometheus |
| **Python** | 3.11+ | `winget install Python.Python.3.11` | Runtime environment for Phase 3 policy controller |

---

## Step-by-Step Cluster Setup

### 1. Execute Setup Audit
Run the automated PowerShell audit script:
```powershell
.\scripts\setup-env.ps1
```

### 2. Configure Helm Repositories
Add the official Helm repositories for threat detection, admission control, and telemetry:
```bash
helm repo add falcosecurity https://falcosecurity.github.io/charts
helm repo add kyverno https://kyverno.github.io/kyverno/
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

### 3. Provision Kind Cluster with eBPF Mounts
Deploy the two-node Kubernetes cluster using the custom configuration:
```bash
kind create cluster --config ./scripts/kind-config.yaml
```

Verify cluster status:
```bash
kubectl cluster-info --context kind-rtm-k8s-cluster
kubectl get nodes -o wide
```

---

## Controller Python Environment Setup
Navigate to the `controller/` directory and set up a Python virtual environment:
```powershell
cd controller
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## Phase 0 Sign-Off Checklist
- [x] Repository structure & Git workflow established (`main`, `develop`, `feat/*`)
- [x] Kind cluster configuration (`scripts/kind-config.yaml`) prepared with eBPF host mounts
- [x] Controller requirements (`controller/requirements.txt`) populated
- [x] Automated PowerShell environment checker script (`scripts/setup-env.ps1`) created
