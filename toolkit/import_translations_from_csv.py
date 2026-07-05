"""
Import translations from CSV files into translation JSON files.

CSV format: LineNumber,Speaker,JP Text,EN Text
- JP Text uses \n for line breaks; JSON uses <br>
- Matching is done by JP text content after normalizing line breaks
- Duplicate JP texts resolved by sequential usage order
- Truncated CSV entries matched by prefix when no exact match found
"""

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
CSV_DIR = ROOT / "csv"
STORY_DIR = ROOT / "translations" / "story"

MIN_PREFIX_LEN = 15


def normalize_jp(text: str) -> str:
    return text.replace("\\n", "<br>")


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def build_indices(lines: list[dict]) -> tuple[dict[str, list[int]], dict[str, list[int]]]:
    exact: dict[str, list[int]] = {}
    for i, entry in enumerate(lines):
        exact.setdefault(entry["jp"].strip(), []).append(i)

    prefix: dict[str, list[int]] = {}
    for jp_key, idxs in exact.items():
        for prefix_len in range(MIN_PREFIX_LEN, len(jp_key) + 1):
            prefix.setdefault(jp_key[:prefix_len], []).extend(idxs)

    return exact, prefix


def find_match(
    csv_jp: str,
    exact_index: dict[str, list[int]],
    prefix_index: dict[str, list[int]],
    used: set[int],
    scene: str,
    dry_run: bool,
) -> tuple[int | None, str]:
    candidates = exact_index.get(csv_jp)
    match_kind = "exact"

    if not candidates and len(csv_jp) >= MIN_PREFIX_LEN:
        candidates = prefix_index.get(csv_jp)
        match_kind = "prefix"

    if not candidates:
        return None, "no_match"

    unused = [i for i in candidates if i not in used]
    if not unused:
        return None, "all_used"

    if len(unused) > 1 and not dry_run:
        pass
    elif len(unused) > 1 and dry_run:
        print(f"  WARN [{scene}] {len(candidates)} {match_kind} matches for JP: {csv_jp[:60]!r} — using first unused")

    return unused[0], match_kind


def import_csv(csv_path: Path, dry_run: bool = False) -> tuple[int, int, int]:
    scene = csv_path.stem
    json_path = STORY_DIR / f"{scene}.json"

    if not json_path.exists():
        print(f"  SKIP: no JSON found for {scene}")
        return 0, 0, 0

    data = load_json(json_path)
    lines = data["lines"]
    exact_index, prefix_index = build_indices(lines)
    used: set[int] = set()

    imported = skipped_empty = unmatched = 0

    with csv_path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            en = row.get("EN Text", "").strip()
            if not en:
                skipped_empty += 1
                continue

            csv_jp = normalize_jp(row.get("JP Text", "").strip())
            idx, match_kind = find_match(csv_jp, exact_index, prefix_index, used, scene, dry_run)

            if idx is None:
                if match_kind == "no_match":
                    print(f"  WARN [{scene}] no match for JP: {csv_jp[:60]!r}")
                elif match_kind == "all_used":
                    print(f"  WARN [{scene}] all candidates already used for JP: {csv_jp[:60]!r}")
                unmatched += 1
                continue

            used.add(idx)
            if not dry_run:
                lines[idx]["en"] = en
            imported += 1

    if not dry_run and imported:
        save_json(json_path, data)

    return imported, skipped_empty, unmatched


def main() -> None:
    dry_run = "--dry-run" in sys.argv

    csv_files = sorted(CSV_DIR.glob("*.csv"))
    if not csv_files:
        print(f"No CSV files found in {CSV_DIR}")
        return

    print(f"Found {len(csv_files)} CSV files{' (dry run)' if dry_run else ''}\n")

    total_imported = total_skipped = total_unmatched = 0
    for csv_path in csv_files:
        imported, skipped, unmatched = import_csv(csv_path, dry_run=dry_run)
        total_imported += imported
        total_skipped += skipped
        total_unmatched += unmatched
        if imported or unmatched:
            status = f"imported={imported}"
            if unmatched:
                status += f"  unmatched={unmatched}"
            print(f"  {csv_path.stem}: {status}")

    print(f"\nDone. imported={total_imported}  skipped_empty={total_skipped}  unmatched={total_unmatched}")


if __name__ == "__main__":
    main()
