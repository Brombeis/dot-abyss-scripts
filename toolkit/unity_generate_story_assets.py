"""
Generate Unity-plugin text files from story translation JSONs.

Outputs unity/assets/unnamed_assetbundle/<scene>.txt for each translated scene.
Message commands (dotmessage, message, l2dmessage, messageTextUnder) get
size-tagged and word-wrapped. *shakeall variants that crash the game are
expanded into per-target lines; dot-mode variants are deleted.

Usage:
    PYTHONUTF8=1 python toolkit/unity_generate_story_assets.py
    PYTHONUTF8=1 python toolkit/unity_generate_story_assets.py --match mas_1001
"""

import argparse
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
import common

MESSAGE_FONT_SIZE = 28
DOTMESSAGE_FONT_SIZE = 24

FONT_METRICS_PATH = os.path.join(common.REPO_ROOT, "data", "font_metrics.json")
_font_metrics = common.load_json(FONT_METRICS_PATH, None)
if not _font_metrics:
    raise RuntimeError(
        "data/font_metrics.json not found. Run "
        "`PYTHONUTF8=1 python toolkit/extract_font_metrics.py` first "
        "(needs the general-textmeshpro font bundle in bundles_cache/)."
    )

CHAR_WIDTHS = dict(_font_metrics["widths"])
# Override space width since they're handled differently by the fontSpacing plugin
CHAR_WIDTHS[" "] = 0.4375 * CHAR_WIDTHS["M"]
_AVG_CHAR_WIDTH = sum(CHAR_WIDTHS.values()) / len(CHAR_WIDTHS)

# Max total glyph width per line, in the same units as CHAR_WIDTHS.
# Calibrated in-game: a line of 44 uppercase M's fits without overflowing, 
# so budget = 44 * M's width, minus a small safety margin for rounding. 
MESSAGE_WIDTH_BUDGET = 1530

# useProportional renders spaces at nearly zero width; repeat them to compensate.
PROPORTIONAL_MODE = True
PROPORTIONAL_SPACE = " " * 1

# messageTextCenter and messageTextUnder are intentionally excluded due to not needing spaces duplicated due to
# their proportional text implementation being correct
MESSAGE_COMMANDS = frozenset({
    "dotmessage", "message", "l2dmessage"
})

UNITY_DIR = os.path.join(common.REPO_ROOT, "unity")
UNITY_ASSET_DIR = os.path.join(UNITY_DIR, "assets", "unnamed_assetbundle")


def main():
    parser = argparse.ArgumentParser(
        description="Generate Unity plugin .txt files from story translations."
    )
    parser.add_argument(
        "--match", metavar="SUBSTR",
        help="only process scenes whose name contains SUBSTR"
    )
    parser.add_argument(
        "--outdir", metavar="DIR", default=UNITY_ASSET_DIR,
        help="output directory for .txt files (default: unity/assets/unnamed_assetbundle/)"
    )
    args = parser.parse_args()

    scene_files = sorted(glob.glob(os.path.join(common.STORY_DIR, "*.json")))
    if not scene_files:
        print("No scene files under translations/story/. Run extract_story.py first.")
        return

    outdir = args.outdir
    built = 0
    for scene_path in scene_files:
        name = build_one(scene_path, match=args.match, outdir=outdir)
        if name:
            print(f"  wrote {name}.txt")
            built += 1

    print(f"\nDone. {built} file(s) in {outdir}")

    if OVERFLOW_WARNINGS:
        print(f"\n{len(OVERFLOW_WARNINGS)} line(s) overflow the dialogue box "
              f"(translation too long or has an unbreakable word):")
        for w in OVERFLOW_WARNINGS:
            print(w)


def build_one(scene_path, match=None, outdir=UNITY_ASSET_DIR):
    scene = common.load_json(scene_path, None)
    if not scene:
        return None

    script_name = scene.get("scene", "")
    if match and match not in script_name:
        return None

    bundle_name = scene.get("bundle")
    src = os.path.join(common.BUNDLES_CACHE, bundle_name) if bundle_name else None
    if not src or not os.path.exists(src):
        print(f"  skip {script_name}: source bundle not in cache ({bundle_name})")
        return None

    original_text, _ = common.read_story_text(src)
    patched_text = apply_translation_unity(original_text, scene.get("lines", []), script_name)

    os.makedirs(outdir, exist_ok=True)
    out_path = os.path.join(outdir, f"{script_name}.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(patched_text)

    return script_name


def apply_translation_unity(text, scene_records, scene_name=""):
    """Rebuild the full script with translations and crash-fix patches applied."""
    body = {(r["line"], r["field"]): r.get("en", "") for r in scene_records}
    loaded_charas = []  # chara slot ids currently active (loaded, not yet emodeleted), in order
    out_lines = []
    for line_no, raw in enumerate(text.splitlines()):
        if not raw.strip() or raw.lstrip().startswith("//"):
            out_lines.append(raw)
            continue
        parts = raw.split(",")
        cmd = parts[0]

        if cmd in ("charaload", "asynccharashow") and len(parts) > 1 and parts[1] not in loaded_charas:
            loaded_charas.append(parts[1])
        elif cmd == "charashowalpha" and len(parts) > 2 and parts[2] == "1" and parts[1] not in loaded_charas:
            loaded_charas.append(parts[1])
        elif cmd in ("charahide", "asynccharahide", "emodelete") and len(parts) > 1 and parts[1] in loaded_charas:
            loaded_charas.remove(parts[1])

        if cmd == "asyncshakeall":
            out_lines.extend(_expand_asyncshakeall(parts, loaded_charas))
            continue
        if cmd == "shakeall":
            out_lines.extend(_expand_shakeall(parts, loaded_charas))
            continue
        if cmd in ("asyncdotshakeall", "dotshakeall"):
            continue

        spec = common.TRANSLATABLE.get(cmd)
        if spec:
            for field_idx, kind in spec.items():
                if field_idx >= len(parts):
                    continue
                if kind == "name":
                    pass
                else:
                    replacement = body.get((line_no, field_idx), "")
                    if replacement:
                        replacement = re.sub(r'<user>', '%user%', replacement, flags=re.IGNORECASE)
                        replacement = re.sub(r'…+', '...', replacement)
                        if cmd == "dotmessage":
                            parts[field_idx] = format_dotmessage_text(replacement)
                        elif cmd in MESSAGE_COMMANDS:

                            parts[field_idx] = format_message_text(
                                replacement, context=f"{scene_name}:{line_no}"
                            )
                        else:
                            parts[field_idx] = common._comma_safe(replacement)
        out_lines.append(",".join(parts))
    trailing = "\n" if text.endswith("\n") else ""
    return "\n".join(out_lines) + trailing


def _expand_asyncshakeall(parts, loaded_charas):
    """asyncshakeall → asyncshake per target (BACK + each loaded chara slot).

    Field mapping: xAmp(1), freq(4), dur(5), decay(6), loop(8).
    yAmp is always 0; two unknown fields are always off,0.
    """
    xAmp, freq, dur, decay, loop = parts[1], parts[4], parts[5], parts[6], parts[8]
    lines = [f"asyncshake,BACK,,{xAmp},0,{dur},{freq},{decay},off,0,{loop},CONT,0"]
    for slot in loaded_charas:
        lines.append(f"asyncshake,CHARA,{slot},{xAmp},0,{dur},{freq},{decay},off,0,{loop},CONT,0")
    return lines


def _expand_shakeall(parts, loaded_charas):
    """shakeall → shake per target (BACK + each loaded chara slot).

    Field mapping: xAmp(1), freq(4), dur(5), decay(6). yAmp is always 0.
    """
    xAmp, freq, dur, decay = parts[1], parts[4], parts[5], parts[6]
    lines = [f"shake,BACK,,{xAmp},0,{dur},{freq},{decay},off,0"]
    for slot in loaded_charas:
        lines.append(f"shake,CHARA,{slot},{xAmp},0,{dur},{freq},{decay},off,0")
    return lines


def _expand_spaces(text):
    """Replace each space with PROPORTIONAL_SPACE, preserving tags and markup."""
    return text.replace(" ", PROPORTIONAL_SPACE)


def format_dotmessage_text(en):
    """Size-tag a dotmessage text field without adding line breaks."""
    en_safe = common._comma_safe(en).replace('"', '""')
    if re.search(r'<size=', en_safe, re.IGNORECASE):
        return en_safe
    return f"<size={DOTMESSAGE_FONT_SIZE}>{en_safe}"


OVERFLOW_WARNINGS = []


def format_message_text(en, context=""):
    """Wrap and size-tag a message text field.

    Passes through unchanged if already tagged. If the translation contains a
    <br> and both halves fit within CPL, the manual split is respected.
    Otherwise the text is re-wrapped.
    """
    en_safe = common._comma_safe(en).replace('"', '""')

    if re.search(r'<size=', en_safe, re.IGNORECASE):
        return en_safe

    fs = MESSAGE_FONT_SIZE
    budget = MESSAGE_WIDTH_BUDGET

    br_match = re.search(r'<br>', en_safe, re.IGNORECASE)
    if br_match:
        half1 = en_safe[:br_match.start()]
        half2 = en_safe[br_match.end():]
        if display_width(half1) <= budget and display_width(half2) <= budget:
            line1, line2 = half1, half2
        else:
            stripped = half1 + ' ' + half2
            line1, line2 = word_wrap_at(stripped, budget)
    else:
        line1, line2 = word_wrap_at(en_safe, budget)

    # word_wrap_at only guarantees line1 fits; line2 gets whatever's left
    # over (the box only renders 2 lines), so it's the one that can silently
    # overflow when the translation is too long or has an unbreakable word.
    if line2 and display_width(line2) > budget:
        over_pct = (display_width(line2) / budget - 1) * 100
        OVERFLOW_WARNINGS.append(
            f"  [{context}] line 2 overflows by {over_pct:.0f}%: {line2!r}"
        )

    if PROPORTIONAL_MODE:
        line1 = _expand_spaces(line1)
        line2 = _expand_spaces(line2) if line2 else ""
        if line2:
            return f"{line1}<br>{line2}<br> "
        else:
            return f"{line1}<br> "
    else:
        if line2:
            line1_padded = pad_to(line1, budget)
            return f"<size={fs}>{line1_padded}<br><size={fs}>{line2}<br> "
        else:
            return f"<size={fs}>{line1}<br> "


def _tokenize_wrappable(text):
    """Split text into chunks at each literal space and after each fullwidth
    comma. _comma_safe() strips the space that used to follow a comma (since
    ，already has spacing baked into the glyph), so a plain text.split(" ")
    would fuse "behind，spread" into one unbreakable word and miss a valid
    break point. Concatenating the returned chunks reproduces text exactly."""
    tokens = []
    current = ""
    for ch in text:
        current += ch
        if ch == " " or ch == "，":
            tokens.append(current)
            current = ""
    if current:
        tokens.append(current)
    return tokens


def word_wrap_at(text, width_budget):
    """Split text at the last word boundary within width_budget display width."""
    if display_width(text) <= width_budget:
        return text, ""

    tokens = _tokenize_wrappable(text)
    current = ""
    last_good_split = 0

    for i, tok in enumerate(tokens):
        candidate = current + tok
        # A token carries its own trailing space (see _tokenize_wrappable).
        # If this token ends the line, that space is dropped at the <br>, so
        # it must not count against the budget when fit-checking.
        if display_width(candidate.rstrip(" ")) <= width_budget:
            current = candidate
            last_good_split = i + 1
        else:
            break

    if last_good_split == 0:
        # First word already too long; hard-split at width_budget.
        pos = 0
        dlen = 0.0
        while pos < len(text):
            if pos + 1 < len(text) and text[pos:pos + 2] == '""':
                dlen += char_width('"')
                pos += 2
            else:
                dlen += char_width(text[pos])
                pos += 1
            if dlen >= width_budget:
                break
        return text[:pos], text[pos:].lstrip()

    return current.rstrip(" "), "".join(tokens[last_good_split:])


def pad_to(text, target_width):
    current = display_width(text)
    space_w = char_width(" ")
    while current < target_width:
        text += " "
        current += space_w
    return text


def char_width(ch):
    return CHAR_WIDTHS.get(ch, _AVG_CHAR_WIDTH)


def display_width(text):
    """Sum of glyph advance widths for wrap purposes; doubled quotes \"\" count as one '"'."""
    total = 0.0
    i = 0
    while i < len(text):
        if text[i:i + 2] == '""':
            total += char_width('"')
            i += 2
        else:
            total += char_width(text[i])
            i += 1
    return total


if __name__ == "__main__":
    main()
