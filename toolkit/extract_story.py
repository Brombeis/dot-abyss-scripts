"""
Extract story text from bundles into translation JSONs.

Writes translations/story/<id>.json for each scene and translations/names.json.
Re-running is safe — existing translations are preserved (matched on line+field,
even if the jp text at that position changed).

Usage:
    python toolkit/extract_story.py
"""

import glob
import os
import re

import common


def main():
    scene_prefixes = ("mas", "hmr", "hmn", "men", "evs")
    bundles = sorted(
        f
        for prefix in scene_prefixes
        for f in glob.glob(os.path.join(common.BUNDLES_CACHE, f"*{prefix}_*.txt_*.bundle"))
    )
    if not bundles:
        print("No story bundles in bundles_cache/. Run toolkit/har_extract.py first.")
        return

    names = common.load_json(common.NAMES_FILE, {})
    scenes_written = 0

    for bundle_path in bundles:
        filename = os.path.basename(bundle_path)
        scene_id = scene_id_from_filename(filename)

        # Skip debug/non-scene bundles (e.g. hmr_live2dcheck).
        if not re.fullmatch(r"(?:mas|hmr|hmn|men|evs)_\d+", scene_id):
            continue

        text, _asset_name = common.read_story_text(bundle_path)
        records, scene_names = common.parse_story(text)

        for jp, suggestion in scene_names.items():
            if jp not in names or (not names[jp] and suggestion):
                names[jp] = suggestion

        scene_path = os.path.join(common.STORY_DIR, f"{scene_id}.json")
        existing = common.load_json(scene_path, {})
        records = merge_records(existing.get("lines", []), records)

        common.save_json(scene_path, {
            "scene": scene_id,
            "bundle": filename,
            "lines": records,
        })
        scenes_written += 1
        todo = sum(1 for r in records if not r["en"])
        print(f"  {scene_id}: {len(records)} lines ({todo} untranslated) -> {scene_path}")

    common.save_json(common.NAMES_FILE, names)
    name_todo = sum(1 for v in names.values() if not v)
    print(f"\nNames glossary: {len(names)} names ({name_todo} untranslated) -> {common.NAMES_FILE}")
    print(f"Done. {scenes_written} scene file(s) under translations/story/")
    print("Next: fill in the empty \"en\" fields, then run toolkit/build_story.py")


def scene_id_from_filename(filename):
    """Extract scene id from a bundle filename.

    ..._mas_1001000101_mas_1001000101.txt_<hash>.bundle  ->  mas_1001000101
    ..._hmr_10010100011_hmr_10010100011.txt_<hash>.bundle  ->  hmr_10010100011
    """
    m = re.search(r"((?:mas|hmr|hmn|men|evs)_\d+)", filename)
    return m.group(1) if m else os.path.splitext(filename)[0]


def merge_records(old_records, new_records):
    """Carry forward existing translations for the same (line, field), even if jp changed."""
    old_by_key = {(r["line"], r["field"]): r.get("en", "") for r in old_records}
    for rec in new_records:
        key = (rec["line"], rec["field"])
        if old_by_key.get(key):
            rec["en"] = old_by_key[key]
    return new_records


if __name__ == "__main__":
    main()
