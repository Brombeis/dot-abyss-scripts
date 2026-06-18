# dot-abyss-scripts

Toolkit for extracting bundle files for Dot Abyss, translating and re-packaging them.

Quickstart:
```
// about 2GB DL, unless you already have bundles_cache
python ./toolkit/download_bundles.py --match .txt_ --match r18-only-novel_assets

// .bundle -> .json (/translations)
python ./toolkit/extract_story.py

// .json -> .txt (/unity)
python ./toolkit/unity_generate_story_assets.py
```
