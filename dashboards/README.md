# Grafana & Loki Dashboards (`dashboards/`)

This directory contains exported Grafana dashboard JSON models and log query configurations for Phase 4 observability.

## Key Metrics & Visualizations
- **Threat Event Timeline**: Real-time count of Falco alerts categorized by severity.
- **Graduated Mitigation Tracking**: Active state of workloads (Normal -> Restricted -> Quarantined -> Terminated).
- **Controller Latency**: Time elapsed from eBPF detection event to policy enforcement applied in K8s.
