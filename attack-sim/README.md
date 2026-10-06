# Attack Simulation Scripts (`attack-sim/`)

This directory contains automated scripts and exploit payloads used to validate detection and response (Phase 1.5 & Phase 5).

## Test Scenarios
1. **Interactive Shell Execution**: Spawns `/bin/bash` or `/bin/sh` inside running container.
2. **Sensitive Data Exfiltration**: Attempts to read `/etc/shadow`, `/var/run/secrets/kubernetes.io/serviceaccount/token`.
3. **Privilege Escalation**: Attempts capability abuse or namespace escape.
4. **Reconnaissance & Scanning**: Executes internal port scans or unauthorized network egress.
