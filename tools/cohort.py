#!/usr/bin/env python3
"""Compute the YOUNG & RELIED-UPON cohort — mechanically, not editorially.

The rule, in one sentence: every package in the registry, ranked by lifetime
downloads, whose FIRST release was published within the cutoff window; take
the top N per registry.

Nobody picks the packages. Change the cutoff or N and anyone re-derives the
same list from the same public data (packages.ecosyste.ms, which aggregates
the registries' own metadata).

One deliberate conservatism: the filter uses FIRST release, so a long-dormant
package name that was recently repurposed for new code counts as OLD and is
excluded. That under-counts the cohort rather than inflating it.

Usage:  python3 tools/cohort.py [months] [per_registry]
Writes: packages.csv (eco,name) and cohort.json (the evidence per package).
"""
import csv
import json
import sys
import urllib.request
from datetime import datetime, timedelta, timezone

API = "https://packages.ecosyste.ms/api/v1/registries/{reg}/packages"
REGISTRIES = [("npm", "npmjs.org"), ("pypi", "pypi.org")]
MAX_PAGES = 60          # backstop; the young tail thins out fast
PER_PAGE = 100


def get(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": "ai-threat-index (codedelta.app)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def main():
    months = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    want = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    cutoff = (datetime.now(timezone.utc) - timedelta(days=30 * months))
    cutoff_s = cutoff.strftime("%Y-%m-%d")
    print(f"cohort: first release on/after {cutoff_s}, top {want} per registry")

    rows, evidence = [], []
    for eco, reg in REGISTRIES:
        found = 0
        for page in range(1, MAX_PAGES + 1):
            url = (f"{API.format(reg=reg)}?sort=downloads&order=desc"
                   f"&per_page={PER_PAGE}&page={page}")
            try:
                batch = get(url)
            except Exception as e:
                print(f"  {eco}: page {page} failed ({e}) — stopping")
                break
            if not batch:
                break
            for p in batch:
                first = p.get("first_release_published_at") or ""
                name = p.get("name")
                if not name or first[:10] < cutoff_s:
                    continue
                rows.append((eco, name))
                evidence.append({
                    "ecosystem": eco,
                    "name": name,
                    "downloads": p.get("downloads"),
                    "first_release": first,
                    "latest_release": p.get("latest_release_published_at"),
                    "repository_url": p.get("repository_url"),
                })
                found += 1
                if found >= want:
                    break
            print(f"  {eco}: page {page} -> {found}/{want}")
            if found >= want:
                break

    with open("packages.csv", "w", newline="") as fh:
        csv.writer(fh).writerows(rows)
    with open("cohort.json", "w") as fh:
        json.dump({
            "generated_utc": datetime.now(timezone.utc).isoformat(),
            "rule": (f"first release on/after {cutoff_s} ({months} months); "
                     f"top {want} per registry by lifetime downloads"),
            "source": "https://packages.ecosyste.ms",
            "packages": evidence,
        }, fh, indent=2)
    print(f"wrote {len(rows)} packages")


if __name__ == "__main__":
    main()
