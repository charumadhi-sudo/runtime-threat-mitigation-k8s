# Demo Application Manifests (`manifests/demo-app/`)

This directory contains Kubernetes deployment, service, and pod specs for the target application used during research testing.

## Purpose
- Provide a realistic containerized workload (e.g., multi-tier web application).
- Serve as the execution target for attack simulations (Phase 1.5).
- Receive dynamic runtime policy adjustments (capabilities removal, network restriction, pod quarantine) applied by the policy-decision controller.
