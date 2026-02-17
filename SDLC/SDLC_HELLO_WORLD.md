# SDLC Starter — Hello World Application

This single-file guide consolidates the SDLC phase templates into a concrete example for a tiny "Hello World" sample application. The focus is documentation of each phase (planning → maintenance); no application code is included here.

**1. Planning**
- Purpose: Define a minimal, demonstrable project that exercises the SDLC.
- Project brief: A tiny, single-process app that prints "Hello, world!" and exposes an optional health check. It serves as a template for teams to follow the SDLC.
- Goals & success: documented requirements, CI that runs tests, and a deployment checklist. Success = passing CI on `main` and a validated deployment checklist run.
- Stakeholders: Product Owner, Developer/Maintainer, QA, Release/OPS.
- Deliverables: this project brief, requirements, implementation plan, tests, CI config, deployment checklist.

**2. Analysis**
- Functional reqs: observable behavior (prints "Hello, world!"), a packaging artifact (container or archive), and a deterministic start/stop behavior.
- Non-functional: quick CI feedback, simple logs, clear health-check semantics.
- Acceptance Criteria: requirements recorded; at least one automated test available; CI runs tests on PRs and `main`.
- Constraints: no external dependencies; keep runtime minimal; prefer env-var config.

**3. Design**
- Architecture: single-process, zero-persistence, config via env vars. Optionally expose `GET /health` returning 200.
- Components: runtime (script/binary), unit tests (fast), an integration/smoke check that validates startup and health.
- Interfaces: CLI start or `CMD` for containers; health endpoint for runtime checks; logs on stdout/stderr.
- Security: no secrets in repo; read from env or CI secret stores.

**4. Development**
- Branching: `main` (protected), `develop` for integration, `feature/<desc>` for work; create `release/X.Y` for formal releases.
- PR checklist: links to AC, tests added, CI green, review approvals.
- Local run: provide a small script or npm `start`/`test` scripts so contributors can validate quickly.
- Versioning: semantic versioning and tags on `main` when releasing.

**5. Testing**
- Unit tests: verify core behavior (e.g., a function returns the expected string).
- Integration/smoke: start the artifact and assert the process exits cleanly and/or health endpoint returns 200.
- CI rules: run tests on every push/PR, fail CI on test failures, keep runtime short (target < 3 minutes for starter projects).
- Test data: none required; use fixtures if expanding examples.

**6. Deployment**
- Packaging: produce a single artifact (container image recommended for portability). Include metadata: commit_SHA, version tag.
- Environments: `dev` → `staging` → `production` (minimal pipelines may skip `dev`).
- Checklist before deploy: CI green, smoke tests pass, health checks validated, logs reviewed for anomalies.
- Rollback: redeploy the previous tagged artifact; document exact steps in runbook.

**7. Maintenance**
- Observability: capture uptime, errors, and deployed version in logs/metrics; provide a health endpoint.
- Incident runbook: steps to restart, run health checks, and roll back to previous artifact.
- Dependency updates: schedule monthly checks; apply security patches promptly and verify via CI.
- Documentation: keep the SDLC docs (`1-planning.md` → `7-maintenance.md`) in sync and require doc updates for relevant PRs.

Appendix: Mapping to SDLC files
- Use the numbered files in this folder for templates and deeper guidance: `1-planning.md` → `7-maintenance.md`.

Example quick-start checklist (for a contributor):
- Read `1-planning.md` to understand scope.
- Implement a tiny script that prints "Hello, world!" and add a unit test.
- Add npm scripts or a run script for local validation.
- Add CI entry to run tests on PRs.
- Tag a release and run the deployment checklist from `6-deployment.md`.
