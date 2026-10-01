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
**Credential-format matches across the index: 18** — every one individually inspected (see reviewed.json): all are deliberate, documented fixtures — example keys, x'd placeholders, test material, and one detector's own patterns. Findings not yet reviewed would show "under disclosure" with identification withheld until maintainers are notified — see Disclosure.

| Ecosystem | Package | Files scanned | Flagged files | AI providers | Credential-format matches | Install hooks | Build fetchers |
|---|---|---|---|---|---|---|---|
| npm | _aws-sdk_nested-clients | 357 | 0 | 0 | 0 | 0 | 0 |
| npm | _aws_lambda-invoke-store | 7 | 0 | 0 | 0 | 0 | 0 |
| npm | _babel_helper-globals | 6 | 0 | 0 | 0 | 0 | 0 |
| npm | _eslint_config-helpers | 10 | 0 | 0 | 0 | 0 | 0 |
| npm | _jridgewell_remapping | 32 | 0 | 0 | 0 | 0 | 0 |
| npm | _oxc-project_types | 4 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_primitive | 21 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-arrow | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-collection | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-compose-refs | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-context | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-dialog | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-direction | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-dismissable-layer | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-focus-guards | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-focus-scope | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-id | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-popper | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-portal | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-presence | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-primitive | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-roving-focus | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-slot | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-use-callback-ref | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-use-controllable-state | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-use-effect-event | 11 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-use-layout-effect | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-use-rect | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-use-size | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_react-visually-hidden | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _radix-ui_rect | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _rolldown_pluginutils | 8 | 0 | 0 | 0 | 0 | 0 |
| npm | _tailwindcss_node | 11 | 0 | 0 | 0 | 0 | 0 |
| npm | _typescript-eslint_project-service | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | _typescript-eslint_tsconfig-utils | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | baseline-browser-mapping | 9 | 0 | 0 | 0 | 0 | 0 |
| npm | call-bind-apply-helpers | 21 | 0 | 0 | 0 | 0 | 0 |
| npm | dunder-proto | 15 | 0 | 0 | 0 | 0 | 0 |
| npm | get-proto | 15 | 0 | 0 | 0 | 0 | 0 |
| npm | google-logging-utils | 18 | 0 | 0 | 0 | 0 | 0 |
| npm | math-intrinsics | 38 | 0 | 0 | 0 | 0 | 0 |
| npm | obug | 11 | 0 | 0 | 0 | 0 | 0 |
| npm | own-keys | 11 | 0 | 0 | 0 | 0 | 0 |
| npm | safe-push-apply | 11 | 0 | 0 | 0 | 0 | 0 |
| npm | set-proto | 15 | 0 | 0 | 0 | 0 | 0 |
| npm | side-channel-list | 13 | 0 | 0 | 0 | 0 | 0 |
| npm | side-channel-map | 12 | 0 | 0 | 0 | 0 | 0 |
| npm | side-channel-weakmap | 12 | 0 | 0 | 0 | 0 | 0 |
| npm | use-sync-external-store | 18 | 0 | 0 | 0 | 0 | 0 |
| npm | wsl-utils | 6 | 0 | 0 | 0 | 0 | 0 |
| pypi | agent-client-protocol | 123 | 0 | 0 | 0 | 0 | 0 |
| pypi | ast-serialize | 1581 | 1 (ELEVATED:1) | 0 | 0 | 0 | 0 |
| pypi | backports.zstd | 194 | 4 (ELEVATED:4) | 0 | 0 | 0 | 0 |
| pypi | burner-redis | 51 | 7 (ELEVATED:7) | 0 | 0 | 0 | 0 |
| pypi | claude-agent-sdk | 105 | 71 (ELEVATED:16 HIGH:55) | 1 | 0 | 0 | 0 |
| pypi | dbt-protos | 135 | 0 | 0 | 0 | 0 | 0 |
| pypi | fastapi-cloud-cli | 146 | 0 | 0 | 0 | 0 | 0 |
| pypi | fastar | 28 | 0 | 0 | 0 | 0 | 0 |
| pypi | fastmcp | 1738 | 718 (ELEVATED:677 HIGH:41) | 5 | reviewed: benign fixtures | 0 | 0 |
| pypi | fastmcp-slim | 270 | 207 (ELEVATED:194 HIGH:13) | 3 | 0 | 0 | 0 |
| pypi | fastspec | 16 | 2 (ELEVATED:2) | 3 | 0 | 0 | 0 |
| pypi | feedparser-sgmllib | 27 | 0 | 0 | 0 | 0 | 0 |
| pypi | genai-prices | 18 | 1 (ELEVATED:1) | 7 | 0 | 0 | 0 |
| pypi | google-genai | 601 | 36 (ELEVATED:33 HIGH:3) | 2 | reviewed: benign fixtures | 0 | 0 |
| pypi | griffecli | 13 | 0 | 0 | 0 | 0 | 0 |
| pypi | griffelib | 86 | 0 | 0 | 0 | 0 | 0 |
| pypi | hf-xet | 315 | 0 | 0 | 0 | 0 | 0 |
| pypi | httpcore2 | 38 | 0 | 0 | 0 | 0 | 0 |
| pypi | httpx2 | 37 | 0 | 0 | 0 | 0 | 0 |
| pypi | ipython-pygments-lexers | 6 | 0 | 0 | 0 | 0 | 0 |
| pypi | langchain-protocol | 8 | 0 | 0 | 0 | 0 | 0 |
| pypi | langgraph-prebuilt | 36 | 11 (ELEVATED:10 HIGH:1) | 0 | 0 | 0 | 0 |
| pypi | librt | 146 | 0 | 0 | 0 | 1 | 0 |
| pypi | llama-cloud-services | 33 | 8 (ELEVATED:7 HIGH:1) | 0 | 0 | 0 | 0 |
| pypi | mlflow-tracing | 644 | 53 (ELEVATED:43 HIGH:10) | 6 | 0 | 0 | 0 |
| pypi | nest-asyncio2 | 30 | 1 (ELEVATED:1) | 0 | 0 | 0 | 0 |
| pypi | polars-runtime-32 | 2167 | 0 | 0 | 0 | 0 | 0 |
| pypi | prek | 264 | 1 (ELEVATED:1) | 0 | reviewed: benign fixtures | 0 | 0 |
| pypi | py-key-value-aio | 125 | 0 | 0 | 0 | 0 | 0 |
| pypi | pydantic-ai-slim | 370 | 252 (ELEVATED:166 HIGH:86) | 17 | 0 | 0 | 0 |
| pypi | pydantic-graph | 20 | 0 | 0 | 0 | 0 | 0 |
| pypi | python-discovery | 61 | 3 (ELEVATED:2 HIGH:1) | 0 | 0 | 0 | 0 |
| pypi | pytokens | 21 | 1 (ELEVATED:1) | 0 | 0 | 0 | 0 |
| pypi | rfc3987-syntax | 15 | 0 | 0 | 0 | 0 | 0 |
| pypi | sagemaker-studio | 364 | 2 (ELEVATED:2) | 0 | reviewed: benign fixtures | 1 | 0 |
| pypi | strands-agents | 759 | 358 (ELEVATED:333 HIGH:25) | 9 | 0 | 0 | 0 |
| pypi | typing-inspection | 32 | 1 (ELEVATED:1) | 0 | 0 | 0 | 0 |
| pypi | uncalled-for | 33 | 0 | 0 | 0 | 0 | 0 |
| pypi | uv-build | 180 | 1 (ELEVATED:1) | 0 | 0 | 0 | 0 |
<!-- RESULTS:END -->

---

Produced with [CodeDelta](https://codedelta.app) — deterministic code churn
measurement and AI threat detection. The detection methods, limits included,
are documented at [codedelta.app](https://codedelta.app/ai-agent-dangers.html).
