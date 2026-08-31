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
**Credential-format matches across the index: 0** (per-package identification withheld until maintainers are notified and findings resolved — see Disclosure).

| Ecosystem | Package | Files scanned | Flagged files | AI providers | Credential-format matches | Install hooks | Build fetchers |
|---|---|---|---|---|---|---|---|
| npm | _aws-sdk_nested-clients | 355 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _babel_helper-globals | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _eslint_config-helpers | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _jridgewell_remapping | 5 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _oxc-project_types | 1 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_number | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_primitive | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-arrow | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-collection | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-compose-refs | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-context | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-dialog | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-direction | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-dismissable-layer | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-focus-guards | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-focus-scope | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-id | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-popper | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-portal | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-presence | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-primitive | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-roving-focus | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-slot | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-use-callback-ref | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-use-controllable-state | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-use-effect-event | 2 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-use-layout-effect | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-use-previous | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-use-rect | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-use-size | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_react-visually-hidden | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _radix-ui_rect | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _rolldown_pluginutils | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _standard-schema_spec | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _tailwindcss_node | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _typescript-eslint_project-service | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _typescript-eslint_tsconfig-utils | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | baseline-browser-mapping | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | call-bind-apply-helpers | 13 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | dunder-proto | 7 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | get-proto | 7 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | google-logging-utils | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | math-intrinsics | 31 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | own-keys | 3 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | safe-push-apply | 3 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | set-proto | 7 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | side-channel-list | 4 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | side-channel-map | 3 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | side-channel-weakmap | 3 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | use-sync-external-store | 15 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | agent-client-protocol | 82 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | ast-serialize | 660 | 1 (ELEVATED:1) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | backports.zstd | 107 | 4 (ELEVATED:4) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | browser-use | 160 | 38 (ELEVATED:35 HIGH:3) | 15 | &mdash; | &mdash; | &mdash; |
| pypi | claude-agent-sdk | 88 | 67 (ELEVATED:12 HIGH:55) | 3 | &mdash; | &mdash; | &mdash; |
| pypi | dbt-protos | 82 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | fastapi-cloud-cli | 108 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | fastapi-mcp | 44 | 12 (ELEVATED:12) | 2 | &mdash; | &mdash; | &mdash; |
| pypi | fastar | 12 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | fastmcp | 846 | 699 (ELEVATED:661 HIGH:38) | 9 | &mdash; | &mdash; | &mdash; |
| pypi | fastmcp-slim | 257 | 212 (ELEVATED:200 HIGH:12) | 8 | &mdash; | &mdash; | &mdash; |
| pypi | fastspec | 6 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | genai-prices | 12 | 1 (ELEVATED:1) | 5 | &mdash; | &mdash; | &mdash; |
| pypi | google-adk | 787 | 329 (ELEVATED:277 HIGH:52) | 17 | &mdash; | &mdash; | &mdash; |
| pypi | google-genai | 527 | 40 (ELEVATED:39 HIGH:1) | 3 | &mdash; | &mdash; | &mdash; |
| pypi | griffelib | 78 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | hf-xet | 292 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | httpcore2 | 31 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | httpx2 | 30 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | ipython-pygments-lexers | 2 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | langchain-classic | 1582 | 79 (ELEVATED:73 HIGH:6) | 17 | &mdash; | &mdash; | &mdash; |
| pypi | langchain-protocol | 2 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | langgraph-prebuilt | 25 | 12 (ELEVATED:10 HIGH:2) | 1 | &mdash; | &mdash; | &mdash; |
| pypi | librt | 37 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | llama-cloud-services | 28 | 8 (ELEVATED:7 HIGH:1) | 1 | &mdash; | &mdash; | &mdash; |
| pypi | mlflow-tracing | 601 | 61 (ELEVATED:47 HIGH:14) | 29 | &mdash; | &mdash; | &mdash; |
| pypi | nest-asyncio2 | 14 | 1 (ELEVATED:1) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | openai-agents | 863 | 433 (ELEVATED:299 HIGH:134) | 12 | &mdash; | &mdash; | &mdash; |
| pypi | polars-runtime-32 | 2067 | 1 (ELEVATED:1) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | prek | 210 | 1 (ELEVATED:1) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | propcache | 19 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | py-key-value-aio | 119 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | pydantic-ai-slim | 298 | 219 (ELEVATED:130 HIGH:89) | 23 | &mdash; | &mdash; | &mdash; |
| pypi | pydantic-graph | 14 | 2 (ELEVATED:2) | 1 | &mdash; | &mdash; | &mdash; |
| pypi | python-discovery | 32 | 3 (ELEVATED:2 HIGH:1) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | pytokens | 7 | 1 (ELEVATED:1) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | rfc3987-syntax | 5 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | strands-agents | 628 | 354 (ELEVATED:325 HIGH:29) | 19 | &mdash; | &mdash; | &mdash; |
| pypi | typing-inspection | 10 | 1 (ELEVATED:1) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | uncalled-for | 21 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | uv-build | 108 | 2 (ELEVATED:2) | 0 | &mdash; | &mdash; | &mdash; |
<!-- RESULTS:END -->

---

Produced with [CodeDelta](https://codedelta.app) — deterministic code churn
measurement and AI threat detection. The detection methods, limits included,
are documented at [codedelta.app](https://codedelta.app/ai-agent-dangers.html).
