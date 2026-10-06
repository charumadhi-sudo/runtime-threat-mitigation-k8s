# Falco Rules — Phase 1

## Overview

Phase 1 uses the **default Falco ruleset** shipped with Falco 0.45.0 (`falco_rules.yaml`).  
No custom rules are added in this phase. The default ruleset covers ~130 rules across syscall-based
detection categories including credential access, privilege escalation, lateral movement, and network
anomalies.

---

## Environment

| Property | Value |
|---|---|
| Falco version | 0.45.0 |
| Driver mode | `modern_ebpf` (selected by `kind: auto` at runtime) |
| Kernel | `6.18.33.2-microsoft-standard-WSL2` |
| Cluster | Kind (`rtm-k8s-cluster`) on Docker Desktop / WSL2 backend |
| Chart version | `falcosecurity/falco` v9.2.0 |
| `hostPID` | `true` (patched post-install — required for modern eBPF on Kind/WSL2) |

---

## Rule Verified End-to-End in Phase 1

### `Read sensitive file untrusted`

| Field | Value |
|---|---|
| **Severity** | `Warning` |
| **Source** | `syscall` |
| **MITRE ATT&CK** | T1555 — Credentials from Password Stores |
| **Tags** | `T1555`, `container`, `filesystem`, `host`, `maturity_stable`, `mitre_credential_access` |
| **Syscall** | `openat` |
| **Condition** | A non-trusted process opens a sensitive file (e.g., `/etc/shadow`, `/etc/sudoers`, SSH keys) |
| **Default action** | Alert (forwarded to Falcosidekick → stub-receiver) |

**Trigger used for verification:**
```bash
kubectl exec -n shop deployment/order-service -- sh -c "cat /etc/shadow"
```

**Sample alert output (from stub-receiver):**
```json
{
  "rule": "Read sensitive file untrusted",
  "priority": "Warning",
  "output_fields": {
    "fd.name": "/etc/shadow",
    "proc.cmdline": "cat /etc/shadow",
    "proc.name": "cat",
    "proc.pname": "sh",
    "k8s.ns.name": "shop",
    "k8s.pod.name": "order-service-dc857d654-9qjmk",
    "user.name": "root",
    "user.uid": 0
  }
}
```

---

## Key Default Rules Active in Phase 1

These rules from `falco_rules.yaml` are relevant to the RTM threat model and will be used
as detection signals in later phases:

| Rule | Severity | Trigger |
|---|---|---|
| `Read sensitive file untrusted` | Warning | Read of `/etc/shadow`, `/etc/sudoers`, SSH keys, etc. |
| `Terminal shell in container` | Notice | Interactive shell spawned inside a container (proc.tty != 0) |
| `Launch Privileged Container` | Warning | Container started with --privileged |
| `Container Run as Root User` | Notice | Process running as UID 0 in a container |
| `Write below etc` | Warning | Write to /etc/ from inside a container |
| `Write below root` | Error | Write to / from inside a container |
| `Mkdir binary dirs` | Error | mkdir in system binary directories |
| `Modify binary dirs` | Error | Modification to /bin, /sbin, /usr/bin, etc. |
| `Non sudo setuid` | Warning | setuid called by a non-root process |
| `Outbound or Inbound Traffic not to Authorized Server Process` | Notice | Unexpected network connection |
| `Disallowed SSH Connection` | Notice | SSH connection from unexpected source |

> **Note:** `Terminal shell in container` requires `-t` (TTY allocation) in `kubectl exec` or a
> genuinely interactive shell session. In the Kind/WSL2 environment, TTY-based rules are unreliable
> for automated testing; prefer TTY-independent rules (like `Read sensitive file untrusted`) for
> CI/automated verification.

---

## Known Limitations in WSL2 / Kind

1. **`libpman: disabled BPF iterators`** — This warning appears in every Falco log on this setup.
   It means Falco cannot use BPF iterator programs to enumerate existing processes at startup.
   It is **non-fatal**: ongoing syscall capture works correctly once `hostPID: true` is set.

2. **`hostPID: true` required** — The Falco Helm chart v9.2.0 does not expose `hostPID` as a
   values key. It must be applied as a `kubectl patch` after every `helm upgrade`. See
   `manifests/falco/falco-values.yaml` for the comment documenting this. A post-upgrade patch
   script is tracked as a Phase 2 improvement.

3. **TTY-dependent rules** — Rules with `proc.tty != 0` (e.g., `Terminal shell in container`)
   require explicit TTY allocation and are not reliably triggered by `kubectl exec` without `-t` in
   this environment.

---

## Alert Routing

```
Falco (DaemonSet, each node)
  └─► HTTP output → Falcosidekick (port 2801, falco namespace)
        └─► Webhook → stub-receiver (port 8000, shop namespace)
              └─► Logs alert to stdout (Phase 1 only)
```

Phase 3 will replace the stub-receiver with a real policy-decision engine.
