"""
Extract original .txt files from story bundles in bundles_cache/.

Outputs the raw TextAsset script from each story bundle as a plain .txt file
under original/<scene_name>.txt.

Usage:
    PYTHONUTF8=1 python toolkit/extract_original_txt.py
    PYTHONUTF8=1 python toolkit/extract_original_txt.py --match mas_1001
"""

import argparse
import glob
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import common

ORIGINAL_DIR = os.path.join(common.REPO_ROOT, "original")


def main():
    parser = argparse.ArgumentParser(
        description="Extract original .txt files from story bundles."
    )
    parser.add_argument(
        "--match", metavar="SUBSTR",
        help="only process scenes whose bundle name contains SUBSTR"
    )
    args = parser.parse_args()

    scene_files = sorted(glob.glob(os.path.join(common.STORY_DIR, "*.json")))
    if not scene_files:
        print("No scene files under translations/story/. Run extract_story.py first.")
        return

    os.makedirs(ORIGINAL_DIR, exist_ok=True)
    written = 0
    for scene_path in scene_files:
        scene = common.load_json(scene_path, None)
        if not scene:
            continue

        script_name = scene.get("scene", "")
        if args.match and args.match not in script_name:
            continue

        bundle_name = scene.get("bundle")
        src = os.path.join(common.BUNDLES_CACHE, bundle_name) if bundle_name else None
        if not src or not os.path.exists(src):
            print(f"  skip {script_name}: source bundle not in cache ({bundle_name})")
            continue

        text, _ = common.read_story_text(src)
        out_path = os.path.join(ORIGINAL_DIR, f"{script_name}.txt")
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(text)

        print(f"  wrote {script_name}.txt")
        written += 1

    print(f"\nDone. {written} file(s) in original/")


if __name__ == "__main__":
    main()
