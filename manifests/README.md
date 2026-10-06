# Kubernetes Manifests (`manifests/`)

This directory contains declarative Kubernetes YAML manifests for all components of the Runtime Threat Mitigation pipeline.

## Directory Layout
- **`demo-app/`**: Sample web workload used as the target for attack simulation and threat mitigation testing.
- **`falco/`**: Helm values, custom Falco eBPF detection rules, and Falcosidekick alert forwarder configurations.
- **`mesh/`**: Service mesh and microsegmentation policies (Istio `AuthorizationPolicy` / Otterize `ClientIntents`) for network quarantine.
- **`kyverno/`**: Admission control and `ClusterPolicy` manifests for fine-grained runtime process and container restriction.
