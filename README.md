# The AI Threat Index

**The exposed AI and build surface of the software everyone depends on. Measurements, not verdicts.**

Modern software stands on a small set of packages that almost everything else
imports. This index scans those packages — the actual published source, fetched
from the public registries — and reports the surface that matters to a security
review:

- **AI surface** — agent-SDK imports, model endpoints, and places where model
  output can reach something that executes.
- **Build surface** — files that run code on install, and build files that
  fetch remote content at build time (the xz-class entry route).
- **Committed credential-format matches** — strings matching documented vendor
  key formats. The scanner only ever emits redacted values (first characters
  plus length); this repository publishes **counts only**.
- **AI Bill of Materials** — which model providers, if any, each package's
  code can talk to.

## The method is the workflow

Every number here is produced by [the scan workflow](.github/workflows/scan.yml)
in this repository, running on GitHub-hosted runners with the
[publicly downloadable CodeDelta engine](https://github.com/code-delta-app/releases).
There is no private pipeline: the package list is `packages.csv`, the run logs
are public, and re-running the workflow reproduces the table below. Findings
are pointers for review, not verdicts — a flagged file is a place to look,
never an accusation.

## Disclosure

If a scan surfaces a credential-format match or a finding that could aid an
attacker against a specific package, the maintainers are notified privately
first; this repository publishes aggregate counts and nothing identifying
until the finding is resolved.

## Results

<!-- RESULTS:BEGIN -->
| Ecosystem | Package | Files scanned | Flagged files | AI providers | Credential-format matches | Install hooks | Build fetchers |
|---|---|---|---|---|---|---|---|
| npm | axios | 71 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | chalk | 3 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | commander | 8 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | express | 7 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | lodash | 1048 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | boto3 | 40 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | flask | 83 | 2 (ELEVATED:1 HIGH:1) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | requests | 35 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | rich | 100 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | urllib3 | 82 | 0 | 0 | &mdash; | &mdash; | &mdash; |
<!-- RESULTS:END -->

---

Produced with [CodeDelta](https://codedelta.app) — deterministic code churn
measurement and AI threat detection. The detection methods, limits included,
are documented at [codedelta.app](https://codedelta.app/ai-agent-dangers.html).
