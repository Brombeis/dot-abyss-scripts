"""Regenerate the translation-status table in README.md from translation JSONs."""

import json
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRANSLATIONS_DIR = os.path.join(REPO_ROOT, "translations", "story")
README_PATH = os.path.join(REPO_ROOT, "README.md")

PREFIXES = {
    "mas": "Main Story",
    "hmr": "R18 Scenes",
    "hmn": "Normal Scenes",
    "men": "Mini Events",
    "evs": "Event Story",
}

MARKER_START = "<!-- translation-status-start -->"
MARKER_END = "<!-- translation-status-end -->"


def gather_stats():
    stats = {}
    for prefix in PREFIXES:
        total_lines = 0
        translated_lines = 0
        file_count = 0
        files_done = 0
        for fname in sorted(os.listdir(TRANSLATIONS_DIR)):
            if not fname.startswith(prefix + "_") or not fname.endswith(".json"):
                continue
            with open(os.path.join(TRANSLATIONS_DIR, fname), "r", encoding="utf-8") as f:
                data = json.load(f)
            lines = data.get("lines", [])
            t = sum(1 for l in lines if l.get("en"))
            total_lines += len(lines)
            translated_lines += t
            file_count += 1
            if t == len(lines) and len(lines) > 0:
                files_done += 1
        stats[prefix] = {
            "total_lines": total_lines,
            "translated_lines": translated_lines,
            "file_count": file_count,
            "files_done": files_done,
        }
    return stats


def build_table(stats):
    rows = []
    rows.append("| Type | Files | Files Done | Lines | Translated | Progress |")
    rows.append("|------|------:|----------:|------:|-----------:|----------|")

    grand_total = grand_translated = grand_files = grand_done = 0
    for prefix, label in PREFIXES.items():
        s = stats[prefix]
        pct = (s["translated_lines"] / s["total_lines"] * 100) if s["total_lines"] else 0
        bar = progress_bar(pct)
        rows.append(
            f"| {label} | {s['file_count']} | {s['files_done']} "
            f"| {s['total_lines']} | {s['translated_lines']} | {bar} {pct:.0f}% |"
        )
        grand_total += s["total_lines"]
        grand_translated += s["translated_lines"]
        grand_files += s["file_count"]
        grand_done += s["files_done"]

    pct = (grand_translated / grand_total * 100) if grand_total else 0
    bar = progress_bar(pct)
    rows.append(
        f"| **Total** | **{grand_files}** | **{grand_done}** "
        f"| **{grand_total}** | **{grand_translated}** | {bar} **{pct:.0f}%** |"
    )
    return "\n".join(rows)


def progress_bar(pct, width=10):
    filled = round(pct / 100 * width)
    return "█" * filled + "░" * (width - filled)


def update_readme(table):
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    block = f"{MARKER_START}\n### Translation Progress\n\n{table}\n{MARKER_END}"

    pattern = re.compile(
        re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END),
        re.DOTALL,
    )
    if pattern.search(content):
        new_content = pattern.sub(block, content)
    else:
        new_content = content.rstrip() + "\n\n" + block + "\n"

    if new_content == content:
        return False

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


def main():
    stats = gather_stats()
    table = build_table(stats)
    changed = update_readme(table)
    if changed:
        print("README.md: translation status updated", file=sys.stderr)
    return changed


if __name__ == "__main__":
    main()
