# Service Mesh & Microsegmentation Manifests (`manifests/mesh/`)

This directory contains network isolation and service mesh policy definitions for graduated threat response.

## Purpose
- **Istio AuthorizationPolicies**: Enforce fine-grained HTTP/gRPC ingress and egress restrictions when a workload reaches a **Medium/High** threat level.
- **Otterize ClientIntents / NetworkPolicies**: Apply automated zero-trust network policies to quarantine compromised pods from accessing sensitive internal microservices or external command-and-control (C2) servers.
