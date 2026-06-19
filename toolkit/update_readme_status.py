"""Regenerate the translation-status tables in README.md from translation JSONs."""

import json
import os
import re
import sys
from collections import Counter, defaultdict

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRANSLATIONS_DIR = os.path.join(REPO_ROOT, "translations", "story")
NAMES_PATH = os.path.join(REPO_ROOT, "translations", "names.json")
README_PATH = os.path.join(REPO_ROOT, "README.md")

PREFIXES = {
    "mas": "Main Story",
    "hmr": "R18 Scenes",
    "hmn": "Normal Scenes",
    "men": "Mini Events",
    "evs": "Event Story",
}

CHARACTER_PREFIXES = {
    "hmr": "R18",
    "hmn": "Normal",
    "men": "Mini",
}

MARKER_START = "<!-- translation-status-start -->"
MARKER_END = "<!-- translation-status-end -->"


def load_names():
    with open(NAMES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def normalize_character(jp_name, names):
    base_jp = jp_name
    for sep in ("<", "[", "（"):
        if sep in base_jp:
            base_jp = base_jp.split(sep)[0]
    en = names.get(base_jp, "") or names.get(jp_name, "")
    if en:
        for suffix in (" (Brothel)", " (Casual Outfit)", " (Normal)", " (Memorial Blazer)", " (NPC)"):
            if en.endswith(suffix):
                en = en[: -len(suffix)]
                break
        for prefix_marker in (" [",):
            if prefix_marker in en:
                en = en[: en.index(prefix_marker)]
                break
    return en if en else base_jp


def primary_character(data, names):
    speakers = Counter()
    for line in data.get("lines", []):
        n = line.get("name", "")
        if n and n != "<user>":
            speakers[n] += 1
    if not speakers:
        return ""
    top_jp = speakers.most_common(1)[0][0]
    return normalize_character(top_jp, names)


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


def gather_character_stats(names):
    char_stats = defaultdict(lambda: {p: {"total": 0, "translated": 0} for p in CHARACTER_PREFIXES})
    for prefix in CHARACTER_PREFIXES:
        for fname in sorted(os.listdir(TRANSLATIONS_DIR)):
            if not fname.startswith(prefix + "_") or not fname.endswith(".json"):
                continue
            with open(os.path.join(TRANSLATIONS_DIR, fname), "r", encoding="utf-8") as f:
                data = json.load(f)
            char = primary_character(data, names)
            if not char:
                continue
            lines = data.get("lines", [])
            t = sum(1 for l in lines if l.get("en"))
            char_stats[char][prefix]["total"] += len(lines)
            char_stats[char][prefix]["translated"] += t
    return char_stats


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


def build_character_table(char_stats):
    rows = []
    rows.append("| Character | R18 | Normal | Mini | Total |")
    rows.append("|-----------|-----|--------|------|-------|")

    main_chars = sorted(
        c for c, cs in char_stats.items()
        if cs["hmn"]["total"] > 0 or cs["men"]["total"] > 0
    )

    for char in main_chars:
        cs = char_stats[char]
        cells = []
        total_all = 0
        translated_all = 0
        for prefix in CHARACTER_PREFIXES:
            t = cs[prefix]["total"]
            tr = cs[prefix]["translated"]
            total_all += t
            translated_all += tr
            if t == 0:
                cells.append("—")
            else:
                pct = tr / t * 100
                bar = progress_bar(pct, width=5)
                cells.append(f"{bar} {tr}/{t}")

        pct = (translated_all / total_all * 100) if total_all else 0
        bar = progress_bar(pct, width=5)
        total_cell = f"{bar} {translated_all}/{total_all}"

        rows.append(f"| {char} | {cells[0]} | {cells[1]} | {cells[2]} | {total_cell} |")

    return "\n".join(rows)


def progress_bar(pct, width=10):
    filled = round(pct / 100 * width)
    return "█" * filled + "░" * (width - filled)


def update_readme(table, char_table):
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    block = (
        f"{MARKER_START}\n### Translation Progress\n\n{table}\n\n"
        f"### Per-Character Progress\n\n{char_table}\n{MARKER_END}"
    )

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
    names = load_names()
    stats = gather_stats()
    char_stats = gather_character_stats(names)
    table = build_table(stats)
    char_table = build_character_table(char_stats)
    changed = update_readme(table, char_table)
    if changed:
        print("README.md: translation status updated", file=sys.stderr)
    return changed


if __name__ == "__main__":
    main()
