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
| npm | _anthropic-ai_sdk | 565 | 14 (ELEVATED:14) | 3 | &mdash; | &mdash; | &mdash; |
| npm | _google_generative-ai | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _langchain_core | 142 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | _mistralai_mistralai | 3873 | 45 (ELEVATED:45) | 3 | &mdash; | &mdash; | &mdash; |
| npm | ai | 345 | 229 (ELEVATED:229) | 2 | &mdash; | &mdash; | &mdash; |
| npm | axios | 71 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | body-parser | 7 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | chalk | 3 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | cohere-ai | 1665 | 3 (ELEVATED:3) | 1 | &mdash; | &mdash; | &mdash; |
| npm | commander | 8 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | cors | 1 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | dayjs | 445 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | debug | 4 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | dotenv | 6 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | eslint | 414 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | express | 7 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | glob | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | groq-sdk | 160 | 2 (ELEVATED:2) | 1 | &mdash; | &mdash; | &mdash; |
| npm | inquirer | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | jest | 1 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | langchain | 16 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | lodash | 1048 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | mocha | 47 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | moment | 394 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | ollama | 6 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | openai | 966 | 11 (ELEVATED:11) | 2 | &mdash; | &mdash; | &mdash; |
| npm | prettier | 31 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | react | 24 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | react-dom | 40 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | rxjs | 252 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | semver | 49 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | tslib | 5 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | typescript | 3 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | uuid | 22 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | vite | 17 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | vue | 10 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | webpack | 813 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | ws | 15 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | yargs | 1 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| npm | zod | 570 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | aider-chat | 161 | 23 (ELEVATED:23) | 4 | &mdash; | &mdash; | &mdash; |
| pypi | aiohttp | 169 | 2 (ELEVATED:2) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | anthropic | 1547 | 165 (ELEVATED:158 HIGH:7) | 5 | &mdash; | &mdash; | &mdash; |
| pypi | anthropic-bedrock | 31 | 2 (ELEVATED:2) | 1 | &mdash; | &mdash; | &mdash; |
| pypi | attrs | 54 | 1 (HIGH:1) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | boto3 | 40 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | browser-use | 160 | 38 (ELEVATED:35 HIGH:3) | 15 | &mdash; | &mdash; | &mdash; |
| pypi | certifi | 6 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | charset-normalizer | 31 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | click | 65 | 1 (ELEVATED:1) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | cohere | 358 | 16 (ELEVATED:16) | 3 | &mdash; | &mdash; | &mdash; |
| pypi | crewai | 788 | 634 (ELEVATED:52 HIGH:582) | 21 | &mdash; | &mdash; | &mdash; |
| pypi | cryptography | 351 | 3 (ELEVATED:2 HIGH:1) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | django | 2950 | 25 (ELEVATED:23 HIGH:2) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | dspy | 157 | 134 (ELEVATED:128 HIGH:6) | 8 | &mdash; | &mdash; | &mdash; |
| pypi | fastapi | 1137 | 6 (ELEVATED:6) | 1 | &mdash; | &mdash; | &mdash; |
| pypi | flask | 83 | 2 (ELEVATED:1 HIGH:1) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | gradio | 1173 | 31 (ELEVATED:26 HIGH:5) | 8 | &mdash; | &mdash; | &mdash; |
| pypi | grpcio | 4329 | 5 (ELEVATED:5) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | guardrails-ai | 179 | 6 (ELEVATED:5 HIGH:1) | 4 | &mdash; | &mdash; | &mdash; |
| pypi | httpx | 60 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | huggingface-hub | 264 | 176 (ELEVATED:168 HIGH:8) | 12 | &mdash; | &mdash; | &mdash; |
| pypi | idna | 23 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | instructor | 549 | 443 (ELEVATED:420 HIGH:23) | 26 | &mdash; | &mdash; | &mdash; |
| pypi | jinja2 | 52 | 3 (ELEVATED:3) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | langchain | 132 | 87 (ELEVATED:74 HIGH:13) | 4 | &mdash; | &mdash; | &mdash; |
| pypi | langchain-community | 2035 | 156 (ELEVATED:137 HIGH:19) | 41 | &mdash; | &mdash; | &mdash; |
| pypi | langchain-core | 355 | 23 (ELEVATED:21 HIGH:2) | 6 | &mdash; | &mdash; | &mdash; |
| pypi | langgraph | 149 | 63 (ELEVATED:59 HIGH:4) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | litellm | 2559 | 1734 (ELEVATED:1681 HIGH:53) | 45 | &mdash; | &mdash; | &mdash; |
| pypi | llama-index | 0 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | mcp | 835 | 624 (ELEVATED:619 HIGH:5) | 5 | &mdash; | &mdash; | &mdash; |
| pypi | mistralai | 1194 | 1044 (ELEVATED:1041 HIGH:3) | 3 | &mdash; | &mdash; | &mdash; |
| pypi | numpy | 2434 | 66 (ELEVATED:62 HIGH:4) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | ollama | 41 | 40 (ELEVATED:35 HIGH:5) | 3 | &mdash; | &mdash; | &mdash; |
| pypi | openai | 1801 | 225 (ELEVATED:219 HIGH:6) | 5 | &mdash; | &mdash; | &mdash; |
| pypi | openai-agents | 863 | 433 (ELEVATED:299 HIGH:134) | 12 | &mdash; | &mdash; | &mdash; |
| pypi | packaging | 58 | 2 (ELEVATED:2) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | pillow | 323 | 9 (ELEVATED:8 HIGH:1) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | protobuf | 203 | 1 (ELEVATED:1) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | pyautogen | 1 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | pydantic | 272 | 8 (ELEVATED:8) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | pytest | 271 | 24 (ELEVATED:23 HIGH:1) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | python-dateutil | 39 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | pyyaml | 47 | 5 (ELEVATED:5) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | requests | 35 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | rich | 100 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | semantic-kernel | 555 | 453 (ELEVATED:414 HIGH:39) | 18 | &mdash; | &mdash; | &mdash; |
| pypi | sentence-transformers | 211 | 11 (ELEVATED:10 HIGH:1) | 1 | &mdash; | &mdash; | &mdash; |
| pypi | setuptools | 333 | 13 (ELEVATED:10 HIGH:3) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | six | 4 | 1 (HIGH:1) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | smolagents | 44 | 36 (ELEVATED:21 HIGH:15) | 10 | &mdash; | &mdash; | &mdash; |
| pypi | sqlalchemy | 720 | 22 (ELEVATED:21 HIGH:1) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | tiktoken | 20 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | tqdm | 65 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | transformers | 2657 | 749 (ELEVATED:742 HIGH:7) | 4 | &mdash; | &mdash; | &mdash; |
| pypi | typing-extensions | 3 | 2 (ELEVATED:1 HIGH:1) | 0 | &mdash; | &mdash; | &mdash; |
| pypi | urllib3 | 82 | 0 | 0 | &mdash; | &mdash; | &mdash; |
| pypi | wheel | 26 | 0 | 0 | &mdash; | &mdash; | &mdash; |
<!-- RESULTS:END -->

---

Produced with [CodeDelta](https://codedelta.app) — deterministic code churn
measurement and AI threat detection. The detection methods, limits included,
are documented at [codedelta.app](https://codedelta.app/ai-agent-dangers.html).
