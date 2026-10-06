# Policy-Decision Controller (`controller/`)

This directory contains the source code for the Phase 3 Python policy-decision engine.

## Responsibilities
1. **Webhook Receiver**: Listens for real-time alert payloads forwarded by Falcosidekick.
2. **Severity & Context Classifier**: Analyzes threat metadata, rule tags, output context, and attack frequency.
3. **Graduated Response Engine**:
   - **Low Severity**: Log event and update telemetry.
   - **Medium Severity**: Apply Kyverno security restriction policy / update pod labels.
   - **High Severity**: Trigger Istio/Otterize microsegmentation network quarantine.
   - **Critical Severity**: Graceful pod termination & node alert.
4. **K8s API Dispatcher**: Interacts with the Kubernetes API server using the official Python client to execute dynamic policy changes.
