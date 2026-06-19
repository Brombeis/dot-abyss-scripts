# CLAUDE.md — Developer / agent guide

Everything an agent needs to work on the **dot abyss translation scripts**.
This repo is a stripped-down toolkit for extracting story dialogue from the
game's Unity asset bundles and generating translated `.txt` files for use with
a Unity plugin.

---

## 1. What this project does

dot abyss is a **Unity WebGL** game on DMM. Its text lives inside Unity asset
bundles, not in the DOM or API. This repo extracts that text into editable JSON,
then generates translated `.txt` script files ready for a Unity plugin to load.

The pipeline has three steps:
1. **Download** story bundles from the CDN → `bundles_cache/`
2. **Extract** translatable text → `translations/story/*.json` + `names.json`
3. **Generate** Unity plugin `.txt` files → `unity/assets/unnamed_assetbundle/`

---

## 2. The game's architecture (relevant subset)

**Target build:** the **R18 build** on DMM (`play.games.dmm.co.jp`), assets on
host `api.abyss-prod-r18.dotabyss.dmmgames.com` under channel `r18`.

- **Asset delivery = Unity Addressables.** Bundles live under
  `.../resources/webgl/r18/aas/3494/aa/<name>_<hash>.bundle`. The `3494` is a
  catalog/build version; it changes on game updates (see §7).
- **Text rendering:** TextMeshPro with JP SDF font atlases. ASCII/Latin glyphs
  are included.
- The CDN host / channel / version live in `common.py` (`CDN_HOST` /
  `CDN_CHANNEL` / `CDN_VERSION`).

### Where story text lives

| Text type | Bundle pattern | Prefix |
|---|---|---|
| Main story dialogue | `*_mas_<id>.txt_*.bundle` | `mas_` |
| R18 adult scenes | `*_hmr_<id>.txt_*.bundle` | `hmr_` |
| Main-chara normal scenes | `*_hmn_<id>.txt_*.bundle` | `hmn_` |
| Main-chara mini-events | `*_men_<id>.txt_*.bundle` | `men_` |
| Event story scenes | `*_evs_<id>.txt_*.bundle` | `evs_` |

All share the same CSV-like script format inside a `TextAsset`.

---

## 3. Repository layout

```
toolkit/
  common.py                      Shared: CDN paths, script format, bundle read, JSON I/O
  download_bundles.py             CDN → bundles_cache/*.bundle (catalog-driven)
  extract_story.py                story bundles → translations/story/*.json + names.json
  unity_generate_story_assets.py  translations → unity/assets/unnamed_assetbundle/*.txt
  requirements.txt                UnityPy

translations/                    SOURCE OF TRUTH (hand-edited, version this)
  names.json                     { jp_name: en_name } shared character name glossary
  story/<scene>.json             { scene, bundle, lines:[{line,cmd,field,name,jp,en}] }

bundles_cache/                   GENERATED: original JP bundles from the CDN
unity/assets/unnamed_assetbundle/ GENERATED: translated .txt files for Unity plugin

data/                            Stats / indexes
  translation_status.json        per-file line counts by script type
```

`.gitignore` excludes `bundles_cache/` and other generated data. The translation
JSON under `translations/` is the durable artifact.

---

## 4. Environment & commands

- **Python 3.10+**. On Windows the console is cp1252 and will crash on
  Japanese prints — **always run with `PYTHONUTF8=1`**.

```bash
pip install -r toolkit/requirements.txt

# Step 1: download story bundles (~2GB)
PYTHONUTF8=1 python toolkit/download_bundles.py --match .txt_ --match r18-only-novel_assets

# Step 2: extract to translation JSONs
PYTHONUTF8=1 python toolkit/extract_story.py

# Step 3: generate Unity plugin .txt files
PYTHONUTF8=1 python toolkit/unity_generate_story_assets.py
```

There are no automated tests.

---

## 5. File formats

### 5.1 The story script (custom CSV inside a TextAsset)

Each story bundle contains exactly **one `TextAsset`**. Its `m_Script` payload
is **UTF-8 text with a BOM**, line-based. Each line is `command,arg1,arg2,...`.
Blank lines and `//` comments exist and must be preserved.

The script splits **strictly on ASCII commas** — there is no quoting. **Translated
text must never contain an ASCII comma** or it shifts every following field and
corrupts the line. `common._comma_safe()` auto-converts `,` → fullwidth `，`.

Translatable fields (defined in `common.TRANSLATABLE`):

| Command | Field index → kind | Notes |
|---|---|---|
| `dotmessage` | 1 = name, 2 = text | dot-mode dialogue |
| `message` | 1 = name, 2 = text | standard dialogue |
| `l2dmessage` | 1 = name, 2 = text | Live2D-scene dialogue (dominant in `hmr_`) |
| `messageTextCenter` | 2 = text | centered narration |
| `messageTextUnder` | 1 = name, 2 = text | bottom narration box |
| `title` | 1 = text | scene/section title card |
| `objectload` | 4 = name | character roster display name |
| `charaload` | 3 = name | character display name |

**Critical distinction — display name vs. handle.** A character has both:
- a romanized **handle** (e.g. `Sophia`) used as an identifier, and
- a Japanese **display name** (e.g. `ソフィア`) shown on screen.

`objectload,Sophia,CHARA,106501000G,ソフィア` → field 1 = handle (don't touch),
field 4 = display (translate). In `dotmessage,ソフィア,<text>,...,Sophia,TOP,...`
field 1 = display (translate), later field = handle (don't touch). Playable
characters sometimes have a **Japanese handle** (e.g. `ラヴェリア`) — translating
those would break scenes.

Preserve `<user>` (player-name substitution), `<br>`, `<size=N>...</size>`, and
symbols like `♪ ♥ ♡ ～`.

The shared **name glossary** (`translations/names.json`) is applied to ALL name
fields across ALL scenes for consistency. `extract_story.py` auto-seeds
suggestions from `objectload` handles that look name-like (regex
`[A-Z][A-Za-z]+\d*`).

### 5.2 Per-scene translation JSON

```json
{
  "scene": "mas_1001000101",
  "bundle": "<exact .bundle filename>",
  "lines": [
    { "line": 22, "cmd": "messageTextCenter", "field": 2, "name": "", "jp": "...", "en": "" }
  ]
}
```
- Only `text`-kind fields get per-line entries; `name`-kind fields come from the
  glossary.
- `line` is the 0-based line index in the script. If the source script changes,
  line numbers shift and stale translations won't apply (by design —
  `merge_records` matches on `(line, field, jp)` and drops changed entries).
- Empty `en` ⇒ that line stays Japanese. Partial translation is fully supported.

### 5.3 Unity .txt output (unity_generate_story_assets.py)

The generate step produces plain `.txt` files (not `.bundle` reinjection).
Additional processing vs. raw translation:
- **Message commands** (`dotmessage`, `message`, `l2dmessage`, `messageTextUnder`)
  get `<size=N>` tags and word-wrapping to fit the dialogue box (2-line limit).
  `messageTextCenter` is excluded — translated as plain text.
- **`*shakeall` crash fix:** `asyncshakeall` and `shakeall` commands crash the
  Unity plugin, so they're expanded into per-target `asyncshake`/`shake` lines.
  Dot-mode variants (`asyncdotshakeall`, `dotshakeall`) are deleted.
- Name fields are **not** translated in this output (the Unity plugin handles
  names separately).

### 5.4 CDN download mechanics

`download_bundles.py` fetches bundles from the CDN. No auth or session needed.
- Every bundle is at `common.CDN_BASE + filename` (plain GET).
- The filename list comes from `catalog_1.bin`. `common.list_catalog_bundles()`
  extracts length-prefixed strings ending in `.bundle`.
- Only long Addressables names (containing `_assets_` or `_project_`) are real
  CDN paths; the rest 403. `downloadable_only=True` filters accordingly.
- Already-downloaded files are skipped on re-run.

---

## 6. Story dialogue rendering (context for size/wrap logic)

The game has **two rendering surfaces** for dialogue:
- **Conversation Log** = standard TMP_Text. Renders English proportionally, wraps
  cleanly. No special handling needed.
- **Main dialogue box** = a custom monospace renderer (`NovelMessageTextComponent`).
  It lays out one character per fixed-width cell (max 2 lines). Latin glyphs are
  narrower than full-width cells, so English can look gappy or overflow.

`unity_generate_story_assets.py` compensates by word-wrapping text to fit in
2 lines at **73 characters per line**. Lines are padded so `<br>` breaks align.
Dynamic font sizing (previously tiered `<size=N>` tags) is disabled.

---

## 7. When the game updates

The `3494` in `CDN_VERSION` is a catalog version. On a game update:
- Bump `CDN_VERSION` in `common.py`.
- Re-run `download_bundles.py` to fetch updated bundles.
- Re-run `extract_story.py`. The `merge_records` step preserves existing `en`
  translations for unchanged lines; changed lines reset to blank for review.
- Re-run `unity_generate_story_assets.py`.
- `names.json` is content-keyed (jp→en) so it survives version bumps.

---

## 8. Translation workflow

- **Line length limit during translation.** When writing English text for
  `message`, `dotmessage`, `l2dmessage`, and `messageTextUnder` commands,
  each `<br>`-separated segment must fit within **73 characters** (matching
  `MESSAGE_CHARS_PER_LINE`), with a maximum of **2 lines** per dialogue entry.
  `messageTextCenter` and `title` are exempt from this limit.
- **Always update `data/translation_status.json`** after translating files.
  Set `translated` to the number of translated lines and `remaining` to `0`
  (or the correct count for partial translations). Never leave the status file
  out of sync with the actual translation JSONs.

---

## 9. Code style

- **No section-separator comments.** Do not use banner-style dividers like
  `# ---...--- / # Section name / # ---...---` to group functions. Let blank
  lines and well-named identifiers provide structure instead.
