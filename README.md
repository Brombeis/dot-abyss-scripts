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

Table generate via git pre-commit hook. After cloning enable via: `git config core.hooksPath .githooks`

<!-- translation-status-start -->
### Translation Progress

| Type | Files | Files Done | Lines | Translated | Progress |
|------|------:|----------:|------:|-----------:|----------|
| Main Story | 114 | 111 | 5305 | 5302 | ██████████ 100% |
| R18 Scenes | 384 | 1 | 13872 | 80 | ░░░░░░░░░░ 1% |
| Normal Scenes | 153 | 0 | 13988 | 0 | ░░░░░░░░░░ 0% |
| Mini Events | 127 | 0 | 632 | 0 | ░░░░░░░░░░ 0% |
| Event Story | 8 | 0 | 674 | 0 | ░░░░░░░░░░ 0% |
| **Total** | **786** | **112** | **34471** | **5382** | ██░░░░░░░░ **16%** |
<!-- translation-status-end -->
