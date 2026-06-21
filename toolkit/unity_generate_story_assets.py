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
MESSAGE_CHARS_PER_LINE = 68

DOTMESSAGE_FONT_SIZE = 24

# useProportional renders spaces at nearly zero width; repeat them to compensate.
PROPORTIONAL_MODE = True
PROPORTIONAL_SPACE = " " * 7

# messageTextCenter is intentionally excluded — translated as plain text.
MESSAGE_COMMANDS = frozenset({
    "dotmessage", "message", "l2dmessage", "messageTextUnder",
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
    loaded_charas = []  # chara slot ids seen in charaload, in order
    out_lines = []
    for line_no, raw in enumerate(text.splitlines()):
        if not raw.strip() or raw.lstrip().startswith("//"):
            out_lines.append(raw)
            continue
        parts = raw.split(",")
        cmd = parts[0]

        if cmd == "charaload" and len(parts) > 1 and parts[1] not in loaded_charas:
            loaded_charas.append(parts[1])

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
                        if "<user>" in replacement.lower():
                            raise ValueError(
                                f"{scene_name} line {line_no}, field {field_idx}: "
                                f"translated text contains <user> which crashes the game. "
                                f"Rephrase to avoid it.\n"
                                f"  Text: {replacement}"
                            )
                        replacement = re.sub(r'…+', '...', replacement)
                        if cmd == "dotmessage":
                            parts[field_idx] = format_dotmessage_text(replacement)
                        elif cmd in MESSAGE_COMMANDS:

                            parts[field_idx] = format_message_text(replacement)
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


def format_message_text(en):
    """Wrap and size-tag a message text field.

    Passes through unchanged if already tagged. If the translation contains a
    <br> and both halves fit within CPL, the manual split is respected.
    Otherwise the text is re-wrapped.
    """
    en_safe = common._comma_safe(en).replace('"', '""')

    if re.search(r'<size=', en_safe, re.IGNORECASE):
        return en_safe

    fs = MESSAGE_FONT_SIZE
    cpl = MESSAGE_CHARS_PER_LINE

    br_match = re.search(r'<br>', en_safe, re.IGNORECASE)
    if br_match:
        half1 = en_safe[:br_match.start()]
        half2 = en_safe[br_match.end():]
        if display_len(half1) <= cpl and display_len(half2) <= cpl:
            line1, line2 = half1, half2
        else:
            stripped = half1 + ' ' + half2
            line1, line2 = word_wrap_at(stripped, cpl)
    else:
        line1, line2 = word_wrap_at(en_safe, cpl)

    if PROPORTIONAL_MODE:
        line1 = _expand_spaces(line1)
        line2 = _expand_spaces(line2) if line2 else ""
        if line2:
            return f"{line1}<br>{line2}<br> "
        else:
            return f"{line1}<br> "
    else:
        if line2:
            line1_padded = pad_to(line1, cpl)
            return f"<size={fs}>{line1_padded}<br><size={fs}>{line2}<br> "
        else:
            return f"<size={fs}>{line1}<br> "


def word_wrap_at(text, per_line):
    """Split text at the last word boundary within per_line display chars."""
    if display_len(text) <= per_line:
        return text, ""

    words = text.split(" ")
    current = ""
    last_good_split = 0

    for i, word in enumerate(words):
        candidate = current + (" " if current else "") + word
        if display_len(candidate) <= per_line:
            current = candidate
            last_good_split = i + 1
        else:
            break

    if last_good_split == 0:
        # First word already too long; hard-split at per_line chars.
        pos = 0
        dlen = 0
        while pos < len(text):
            if pos + 1 < len(text) and text[pos:pos + 2] == '""':
                dlen += 1
                pos += 2
            else:
                dlen += 1
                pos += 1
            if dlen >= per_line:
                break
        return text[:pos], text[pos:].lstrip()

    return current, " ".join(words[last_good_split:])


def pad_to(text, target_display_len):
    current = display_len(text)
    if current < target_display_len:
        text += " " * (target_display_len - current)
    return text


def display_len(text):
    """Character count for wrap purposes: doubled quotes \"\" count as 1 char."""
    return len(re.sub(r'""', 'X', text))


if __name__ == "__main__":
    main()
