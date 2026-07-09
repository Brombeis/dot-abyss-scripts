"""
Extract per-character advance widths from the TMP_FontAsset the game actually
uses for dialogue text, so word-wrapping can be width-aware instead of
counting characters.

The dialogue box (CharaBalloon "Text" GameObject) and the dot-mode balloon
both reference the same font asset: FOT-UDMarugo_SmallPr6-E SDF. This was
confirmed by resolving the TMP text component's m_fontAsset PathID
(-8992918330047748211) against the SDF asset bundle's CAB hash.

Usage:
    PYTHONUTF8=1 python toolkit/extract_font_metrics.py
"""

import json
import os
import sys

import UnityPy

sys.path.insert(0, os.path.dirname(__file__))
import common

FONT_BUNDLE = os.path.join(
    common.BUNDLES_CACHE,
    "general-textmeshpro_assets_assets_project_lazyassets_general_textmeshpro_"
    "materials_sdf_fot-udmarugo_smallpr6-esdf.asset_dcd6466df63233b2c3a7e8cc6933f429.bundle",
)
OUT_PATH = os.path.join(common.REPO_ROOT, "data", "font_metrics.json")


def main():
    if not os.path.exists(FONT_BUNDLE):
        print(f"Font bundle not found: {FONT_BUNDLE}")
        print("Run download_bundles.py first (it's part of the general-textmeshpro asset group).")
        return

    env = UnityPy.load(FONT_BUNDLE)
    font_asset = None
    for obj in env.objects:
        if obj.type.name == "MonoBehaviour":
            tree = obj.read_typetree()
            if "m_CharacterTable" in tree and "m_GlyphTable" in tree:
                font_asset = tree
                break

    if font_asset is None:
        print("Could not find a TMP_FontAsset MonoBehaviour in the bundle.")
        return

    glyph_advance = {
        g["m_Index"]: g["m_Metrics"]["m_HorizontalAdvance"]
        for g in font_asset["m_GlyphTable"]
    }

    spacing_offset = font_asset.get("normalSpacingOffset", 0.0)
    face_info = font_asset["m_FaceInfo"]

    widths = {}
    for c in font_asset["m_CharacterTable"]:
        advance = glyph_advance.get(c["m_GlyphIndex"])
        if advance is None:
            continue
        ch = chr(c["m_Unicode"])
        # Effective advance TMP uses when laying out text: glyph advance plus
        # the font asset's normal-style character spacing offset.
        widths[ch] = advance + spacing_offset

    out = {
        "source": "FOT-UDMarugo_SmallPr6-E SDF",
        "point_size": face_info["m_PointSize"],
        "units_per_em": face_info["m_UnitsPerEM"],
        "widths": dict(sorted(widths.items())),
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    print(f"Wrote {len(widths)} glyph widths to {OUT_PATH}")
    print(f"Reference point size: {face_info['m_PointSize']}")


if __name__ == "__main__":
    main()
