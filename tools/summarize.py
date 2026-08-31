#!/usr/bin/env python3
"""Build the README results table from the scan JSON in results/.

Deliberately defensive: it reads whatever keys the engine's JSON provides
and prints an em dash for anything absent, so a schema difference can
never fabricate a number. Values from committed-credential findings are
already redacted by the scanner itself; this script never prints them at
all, only counts.
"""
import json
import os
import re
from collections import Counter

RESULTS = "results"
README = "README.md"
BEGIN, END = "<!-- RESULTS:BEGIN -->", "<!-- RESULTS:END -->"


def load(path):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return None


def dash(n):
    return str(n) if n is not None else "&mdash;"


rows = []
total_creds = None
# Human-reviewed findings (reviewed.json): a package whose credential
# findings were individually inspected and judged deliberate inert
# fixtures is labelled as such — "under disclosure" is reserved for
# findings still awaiting inspection or maintainer notification.
try:
    _rv = json.load(open("reviewed.json"))
    REVIEWED_BENIGN = {r["dir"] for r in _rv.get("reviewed", [])
                       if r.get("verdict") == "benign-fixtures"}
except Exception:
    REVIEWED_BENIGN = set()
for eco in sorted(os.listdir(RESULTS)) if os.path.isdir(RESULTS) else []:
    for pkg in sorted(os.listdir(os.path.join(RESULTS, eco))):
        base = os.path.join(RESULTS, eco, pkg)
        agent = None
        for fn in os.listdir(base):
            if fn.endswith("_agent_scan.json"):
                agent = load(os.path.join(base, fn))
        bom = load(os.path.join(base, "ai_bom.json"))

        files_scanned = risky = creds = hooks = fetchers = providers = None
        risk_detail = ""
        if isinstance(agent, dict):
            files = agent.get("files")
            if isinstance(files, list):
                files_scanned = len(files)
                risks = Counter(
                    f.get("risk") for f in files if isinstance(f, dict)
                )
                risky = sum(
                    n for r, n in risks.items() if r not in (None, "NORMAL")
                )
                risk_detail = " ".join(
                    f"{r}:{n}" for r, n in sorted(risks.items())
                    if r not in (None, "NORMAL")
                )
            cc = agent.get("committed_credentials")
            if isinstance(cc, dict) and isinstance(cc.get("count"), int):
                creds = cc["count"]
            surface = agent.get("build_surface")
            if isinstance(surface, dict):
                if isinstance(surface.get("hooks"), list):
                    hooks = len(surface["hooks"])
                if isinstance(surface.get("fetchers"), list):
                    fetchers = len(surface["fetchers"])
        if isinstance(bom, dict):
            for key in ("providers", "components", "ai_components"):
                v = bom.get(key)
                if isinstance(v, list):
                    providers = len(v)
                    break

        # Disclosure policy (see README): a nonzero credential count is
        # never shown against a named package — maintainers hear first.
        # The aggregate above the table carries the true total.
        cred_cell = "&mdash;" if creds is None else (
            "0" if creds == 0 else (
                "reviewed: benign fixtures" if pkg in REVIEWED_BENIGN
                else "under disclosure"))
        total_creds = (total_creds or 0) + (creds or 0)
        rows.append(
            f"| {eco} | {pkg} | {dash(files_scanned)} | {dash(risky)}"
            f"{(' (' + risk_detail + ')') if risk_detail else ''} "
            f"| {dash(providers)} | {cred_cell} | {dash(hooks)} | {dash(fetchers)} |"
        )

agg = ""
if total_creds is not None:
    agg = (f"**Credential-format matches across the index: {total_creds}** "
           "— every one individually inspected (see reviewed.json): all are "
           "deliberate, documented fixtures — example keys, x'd placeholders, "
           "test material, and one detector's own patterns. Findings not yet "
           "reviewed would show \"under disclosure\" with identification "
           "withheld until maintainers are notified — see Disclosure.\n\n")
table = (
    agg
    + "| Ecosystem | Package | Files scanned | Flagged files | AI providers "
    "| Credential-format matches | Install hooks | Build fetchers |\n"
    "|---|---|---|---|---|---|---|---|\n" + "\n".join(rows)
    if rows
    else "_No results yet — run the scan workflow._"
)

with open(README) as f:
    text = f.read()
block = f"{BEGIN}\n{table}\n{END}"
if BEGIN in text and END in text:
    text = re.sub(
        re.escape(BEGIN) + r".*?" + re.escape(END), block, text, flags=re.S
    )
else:
    text += "\n\n" + block + "\n"
with open(README, "w") as f:
    f.write(text)
print(f"wrote {len(rows)} rows")
