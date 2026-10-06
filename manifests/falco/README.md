# Falco & Falcosidekick Manifests (`manifests/falco/`)

This directory contains configuration files and deployment manifests for runtime threat detection.

## Key Components
- **Falco DaemonSet**: Deployed using eBPF probes for kernel-level system call inspection without kernel module compilation.
- **Custom Rule Sets (`rules.yaml`)**: Custom Falco rules detecting privilege escalation, shell spawning in containers, unauthorized file read/write (`/etc/shadow`, service account tokens), and unexpected outbound connections.
- **Falcosidekick**: Event router configured to forward JSON-formatted Falco alerts to the Python Policy-Decision Controller via HTTP webhook.
