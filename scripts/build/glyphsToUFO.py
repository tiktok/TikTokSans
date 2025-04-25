import os
import glyphsLib
import math
from pathlib import Path
import vttLib
from fontTools.ttLib import TTFont

# import yaml
# from fontTools.designspaceLib import (DesignSpaceDocument, SourceDescriptor, RuleDescriptor)
from fontParts.world import OpenFont


# ------------------------ Build UFO from designspace ------------------------ #

SOURCES_DIR = Path("sources")
BUILD_DIR = SOURCES_DIR / "build"
DARK_VALUE = 12
SLANT_ANGLE = 6
OPSZ_MIN_SB_ADD_LIGHT = 10
OPSZ_MIN_SB_ADD_BLACK = 8

EXCLUDED_GLYPHS_FROM_SLANT = [
    "zero.blackCircled",
    "one.blackCircled",
    "two.blackCircled",
    "three.blackCircled",
    "four.blackCircled",
    "five.blackCircled",
    "six.blackCircled",
    "seven.blackCircled",
    "eight.blackCircled",
    "nine.blackCircled",
    "zero.circled",
    "one.circled",
    "two.circled",
    "three.circled",
    "four.circled",
    "five.circled",
    "six.circled",
    "seven.circled",
    "eight.circled",
    "nine.circled",
    "zero.blackCircled.cv03",
    "zero.circled.cv03",
    "three.blackCircled.cv05",
    "three.circled.cv05",
    "four.blackCircled.cv06",
    "four.circled.cv06",
    "blackCircle",
    "whiteCircle",
]

EXCLUDED_GLYPHS_FROM_RESPACING = [
        ".null",
        "CR",
        "emspace",
        "enspace",
        "figurespace",
        "fourperemspace",
        "hairspace",
        "punctuationspace",
        "thinspace",
        "threeperemspace",
        "zeroWidthNoBreakSpace",
        "zerowidthspace",
    ]


def decompose_glyph_components(glyph):
    """Decomposes components in a glyph if necessary."""
    modified = False
    has_contours = len(glyph.contours) > 0
    has_components = len(glyph.components) > 0

    # Decompose if the glyph has both contours and components
    if has_contours and has_components:
        for component in glyph.components:
            component.decompose()
        modified = True

    # Decompose transformed components
    # Check if any component in the glyph has a scale transformation
    if any(component.transformation[0] != 1.0 or component.transformation[3] != 1.0 for component in glyph.components):
        for component in glyph.components:
            component.decompose()

        modified = True

    # Correct direction only if something changed
    if modified:
        glyph.correctDirection()


def interpolateFont(value3, lerp1, lerp2, font1, font2, base_font, suffix):
    font3 = base_font.copy()

    for layer in font3.layers:
        for glyph_name in layer.keys():
            glyph3 = font3.getLayer(layer.name)[glyph_name]
            if "{" not in layer.name:
                font3_factor = 0 + (value3 - lerp1) * (1 - 0) / (
                    lerp2 - lerp1
                )
                glyph1 = font1.getLayer(layer.name)[glyph_name]
                glyph2 = font2.getLayer(layer.name)[glyph_name]
            else:
                value3 = 148 - 12
                font3_factor = 0 + (value3 - lerp1) * (1 - 0) / (148 - lerp1)
                glyph1 = font1[glyph_name]
                glyph2 = glyph3

            glyph3.interpolate(font3_factor, glyph1, glyph2)

            base_font_glyphWidth = base_font.getLayer(layer.name)[glyph_name].width
            f3_glyph_width = glyph3.width
            offset = (base_font_glyphWidth - f3_glyph_width) / 2

            # Adjust glyph width to match sources
            f3_LSB = 0 if glyph3.leftMargin is None else glyph3.leftMargin
            glyph3.leftMargin = f3_LSB + offset
            glyph3.width = base_font_glyphWidth

    # Modify font info data
    font3.info.styleName = f"{font3.info.styleName} {suffix}"
    font3.styleMapFamilyName = f"{font3.info.familyName} {font3.info.styleName}"

    # Save font
    font3_path = BUILD_DIR / f"{font3.info.familyName}-{font3.info.styleName}.ufo".replace(" ", "")
    font3.save(str(font3_path))


def export_ufo():
    """Convert Glyph app sources to .ufo for later modification."""

    # saves to temp "build" directory
    for file_path in SOURCES_DIR.glob("*.glyphspackage"):
        glyphsLib.build_masters(str(file_path), str(BUILD_DIR), write_skipexportglyphs=True)

    for ufo_path in BUILD_DIR.glob("*.ufo"):
        font = OpenFont(ufo_path)
        for glyph in font:
            decompose_glyph_components(glyph)
        font.save(str(ufo_path))


def adjust_spacing():
    """Adds sidebearings to each Text masters."""

    textOpszSources = [
        {"addition": OPSZ_MIN_SB_ADD_LIGHT, "filename": "TikTokSans-TextLight.ufo"},
        {"addition": OPSZ_MIN_SB_ADD_BLACK, "filename": "TikTokSans-TextBlack.ufo"},
    ]

    ligatureGlyphs = ["ij", "IJ", "fi", "fl", "IJ.cv01", "Yeru-cy", "yeru-cy"]
    for textSource in textOpszSources:
        ufoPath = os.path.join(BUILD_DIR, textSource["filename"])
        font = OpenFont(ufoPath)

        for glyph in font:
            if glyph.name not in EXCLUDED_GLYPHS_FROM_RESPACING:
                for layer in glyph.layers:
                    if layer.leftMargin is not None and layer.rightMargin is not None:
                        layer.leftMargin += textSource["addition"]
                        layer.rightMargin += textSource["addition"]

                        if glyph.components:
                            layer.moveBy((-textSource["addition"], 0))

                        if glyph.name in ligatureGlyphs:
                            for component in glyph.components[1:]:
                                component.moveBy((textSource["addition"] * 2, 0))
                                layer.rightMargin += textSource["addition"] * 2

                    else:
                        layer.width += textSource["addition"] * 2
                        print("Glyph with no sideabearings", glyph.name, font)

        font.save(ufoPath)


def generate_dark_masters():
    opszSources = [
        [
            {"xvalue": 65, "filename": "TikTokSans-TextLight.ufo"},
            {"xvalue": 180, "filename": "TikTokSans-TextBlack.ufo"},
        ],
        [
            {"xvalue": 65, "filename": "TikTokSans-Light.ufo"},
            {"xvalue": 180, "filename": "TikTokSans-Black.ufo"},
        ],
    ]
    for weightSources in opszSources:
        # Generate Text Dark Masters
        min_xvalue = weightSources[0]["xvalue"]
        min_font = OpenFont(BUILD_DIR / weightSources[0]["filename"])
        max_xvalue = weightSources[1]["xvalue"]
        max_font = OpenFont(BUILD_DIR / weightSources[1]["filename"])

        # Create Min Dark master
        minDark_xvalue = min_xvalue - DARK_VALUE
        interpolateFont(
            minDark_xvalue, min_xvalue, max_xvalue, min_font, max_font, min_font, "Dark"
        )

        # Create Max Dark master
        maxDark_xvalue = max_xvalue - DARK_VALUE
        interpolateFont(
            maxDark_xvalue, min_xvalue, max_xvalue, min_font, max_font, max_font, "Dark"
        )


def generate_slanted_masters():
    """Generates slanted masters for selected fonts, applying skew transformation."""
    other_support = ['a']
    diagonals_support = [
        "K",
        "M",
        "N",
        "V",
        "W",
        "X",
        "Z",
        "Nhookleft",
        "k",
        "v",
        "w",
        "x",
        "kgreenlandic",
        "Khook",
        "Vturned",
        "vturned",
        "U-cy",
        "Izhitsa-cy",
        "izhitsa-cy",
        "ustraight-cy",
        "Ii-cy",
        "Ka-cy",
        "ii-cy",
        "ka-cy",
        "Kappa",
        "Lambda",
        "kappa",
        "naira",
        "naira.tf",
        "trademark",
    ]

    files_to_slant = {
        "TikTokSans-LightCd.ufo": other_support,
        "TikTokSans-Light.ufo": [],
        "TikTokSans-LightExt.ufo": other_support,
        "TikTokSans-BlackCd.ufo": [],
        "TikTokSans-Black.ufo": [],
        "TikTokSans-BlackExt.ufo": [],
        "TikTokSans-TextLight.ufo": [],
        "TikTokSans-TextBlack.ufo": [],
    }

    for ufo_file in BUILD_DIR.glob("*.ufo"):
        if ufo_file.name not in files_to_slant:
            continue

        font = OpenFont(ufo_file)
        font.info.italicAngle = -SLANT_ANGLE
        italic_offset = math.tan(font.info.italicAngle * math.pi / 180) * (font.info.xHeight * 0.5)

        glyphs_to_keep = set(files_to_slant[ufo_file.name]) or {glyph.name for glyph in font}

        for glyph in font:
            if glyph.name not in EXCLUDED_GLYPHS_FROM_SLANT and len(glyph.contours) > 0:
                for layer in glyph.layers:
                    layer.skewBy(SLANT_ANGLE)
                    layer.moveBy((italic_offset, 0))

        # Collect names of glyphs to delete
        glyphs_to_delete = [glyph.name for glyph in font if glyph.name not in glyphs_to_keep]

        # Delete glyphs
        for glyph_name in glyphs_to_delete:
            del font[glyph_name]

        font.save(str(ufo_file.with_name(ufo_file.stem + "Oblique.ufo")))

def generate_hinting_ttx():
    vttLib.transfer.dump_to_file(TTFont("sources/hinting/TikTok-VTT.ttf"),"sources/hinting/TikTok-VTT.ttx")

if __name__ == "__main__":
    export_ufo()
    adjust_spacing()
    generate_slanted_masters()
    generate_hinting_ttx()
