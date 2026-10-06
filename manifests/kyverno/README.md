# Kyverno Policy Manifests (`manifests/kyverno/`)

This directory contains Kyverno `ClusterPolicy` and `Policy` manifests used for container-level security enforcement.

## Purpose
- Enforce dynamic security posture changes without immediately terminating workloads.
- Apply security context restrictions (e.g., dropping `LinuxCapabilities`, setting `readOnlyRootFilesystem`, revoking service account tokens).
- Label compromised pods dynamically to trigger downstream mesh isolation rules.
