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
**Credential-format matches across the index: 13** — every one individually inspected (see reviewed.json): all are deliberate, documented fixtures — example keys, x'd placeholders, test material, and one detector's own patterns. Findings not yet reviewed would show "under disclosure" with identification withheld until maintainers are notified — see Disclosure.

| Ecosystem | Package | Files scanned | Flagged files | AI providers | Credential-format matches | Install hooks | Build fetchers |
|---|---|---|---|---|---|---|---|
| npm | _aws-sdk_nested-clients | 355 | 0 | 0 | reviewed: benign fixtures | 0 | 0 |
| npm | _babel_helper-globals | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _eslint_config-helpers | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _jridgewell_remapping | 5 | 0 | 0 | 0 | 0 | 0 |
| npm | _oxc-project_types | 1 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_number | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_primitive | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-arrow | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-collection | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-compose-refs | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-context | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-dialog | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-direction | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-dismissable-layer | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-focus-guards | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-focus-scope | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-id | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-popper | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-portal | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-presence | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-primitive | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-roving-focus | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-slot | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-use-callback-ref | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-use-controllable-state | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-use-effect-event | 2 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-use-layout-effect | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-use-previous | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-use-rect | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-use-size | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-visually-hidden | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_rect | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _rolldown_pluginutils | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _standard-schema_spec | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _tailwindcss_node | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _typescript-eslint_project-service | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | _typescript-eslint_tsconfig-utils | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | baseline-browser-mapping | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | call-bind-apply-helpers | 13 | 0 | 0 | 0 | 0 | 0 |
| npm | dunder-proto | 7 | 0 | 0 | 0 | 0 | 0 |
| npm | get-proto | 7 | 0 | 0 | 0 | 0 | 0 |
| npm | google-logging-utils | 0 | 0 | 0 | 0 | 0 | 0 |
| npm | math-intrinsics | 31 | 0 | 0 | 0 | 0 | 0 |
| npm | own-keys | 3 | 0 | 0 | 0 | 0 | 0 |
| npm | safe-push-apply | 3 | 0 | 0 | 0 | 0 | 0 |
| npm | set-proto | 7 | 0 | 0 | 0 | 0 | 0 |
| npm | side-channel-list | 4 | 0 | 0 | 0 | 0 | 0 |
| npm | side-channel-map | 3 | 0 | 0 | 0 | 0 | 0 |
| npm | side-channel-weakmap | 3 | 0 | 0 | 0 | 0 | 0 |
| npm | use-sync-external-store | 15 | 0 | 0 | 0 | 0 | 0 |
| pypi | agent-client-protocol | 82 | 0 | 0 | 0 | 0 | 0 |
| pypi | ast-serialize | 660 | 1 (ELEVATED:1) | 0 | 0 | 0 | 0 |
| pypi | backports.zstd | 107 | 4 (ELEVATED:4) | 0 | 0 | 0 | 0 |
| pypi | browser-use | 160 | 38 (ELEVATED:35 HIGH:3) | 8 | 0 | 0 | 0 |
| pypi | claude-agent-sdk | 88 | 67 (ELEVATED:12 HIGH:55) | 1 | 0 | 0 | 0 |
| pypi | dbt-protos | 82 | 0 | 0 | 0 | 0 | 0 |
| pypi | fastapi-cloud-cli | 108 | 0 | 0 | 0 | 0 | 0 |
| pypi | fastar | 12 | 0 | 0 | 0 | 0 | 0 |
| pypi | fastmcp | 846 | 699 (ELEVATED:661 HIGH:38) | 3 | reviewed: benign fixtures | 0 | 0 |
| pypi | fastmcp-slim | 257 | 212 (ELEVATED:200 HIGH:12) | 3 | 0 | 0 | 0 |
| pypi | fastspec | 5 | 0 | 0 | 0 | 0 | 0 |
| pypi | genai-prices | 12 | 1 (ELEVATED:1) | 5 | 0 | 0 | 0 |
| pypi | google-adk | 787 | 329 (ELEVATED:277 HIGH:52) | 6 | reviewed: benign fixtures | 0 | 0 |
| pypi | google-genai | 531 | 41 (ELEVATED:40 HIGH:1) | 2 | reviewed: benign fixtures | 0 | 0 |
| pypi | griffelib | 78 | 0 | 0 | 0 | 0 | 0 |
| pypi | hf-xet | 292 | 0 | 0 | 0 | 0 | 0 |
| pypi | httpcore2 | 31 | 0 | 0 | 0 | 0 | 0 |
| pypi | httpx2 | 30 | 0 | 0 | 0 | 0 | 0 |
| pypi | ipython-pygments-lexers | 2 | 0 | 0 | 0 | 0 | 0 |
| pypi | langchain-classic | 1582 | 79 (ELEVATED:73 HIGH:6) | 10 | 0 | 0 | 0 |
| pypi | langchain-protocol | 2 | 0 | 0 | 0 | 0 | 0 |
| pypi | langgraph-prebuilt | 25 | 12 (ELEVATED:10 HIGH:2) | 0 | 0 | 0 | 0 |
| pypi | librt | 37 | 0 | 0 | 0 | 1 | 0 |
| pypi | llama-cloud-services | 28 | 8 (ELEVATED:7 HIGH:1) | 0 | 0 | 0 | 0 |
| pypi | mlflow-tracing | 601 | 61 (ELEVATED:47 HIGH:14) | 6 | 0 | 0 | 0 |
| pypi | nest-asyncio2 | 14 | 1 (ELEVATED:1) | 0 | 0 | 0 | 0 |
| pypi | openai-agents | 863 | 433 (ELEVATED:299 HIGH:134) | 3 | 0 | 0 | 0 |
| pypi | polars-runtime-32 | 2067 | 1 (ELEVATED:1) | 0 | 0 | 0 | 0 |
| pypi | prek | 212 | 1 (ELEVATED:1) | 0 | reviewed: benign fixtures | 0 | 0 |
| pypi | propcache | 19 | 0 | 0 | 0 | 0 | 0 |
| pypi | py-key-value-aio | 119 | 0 | 0 | 0 | 0 | 0 |
| pypi | pydantic-ai-slim | 298 | 219 (ELEVATED:130 HIGH:89) | 15 | 0 | 0 | 0 |
| pypi | pydantic-graph | 14 | 2 (ELEVATED:2) | 0 | 0 | 0 | 0 |
| pypi | python-discovery | 32 | 3 (ELEVATED:2 HIGH:1) | 0 | 0 | 0 | 0 |
| pypi | pytokens | 7 | 1 (ELEVATED:1) | 0 | 0 | 0 | 0 |
| pypi | rfc3987-syntax | 5 | 0 | 0 | 0 | 0 | 0 |
| pypi | strands-agents | 628 | 354 (ELEVATED:325 HIGH:29) | 8 | 0 | 0 | 0 |
| pypi | typing-inspection | 10 | 1 (ELEVATED:1) | 0 | 0 | 0 | 0 |
| pypi | uncalled-for | 21 | 0 | 0 | 0 | 0 | 0 |
| pypi | uv-build | 109 | 2 (ELEVATED:2) | 0 | 0 | 0 | 0 |
<!-- RESULTS:END -->

---

Produced with [CodeDelta](https://codedelta.app) — deterministic code churn
measurement and AI threat detection. The detection methods, limits included,
are documented at [codedelta.app](https://codedelta.app/ai-agent-dangers.html).
