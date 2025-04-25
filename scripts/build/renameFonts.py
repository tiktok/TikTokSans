#!/usr/bin/env python3
"""Find a family name string and replaces with a new one and output fonts to a given directory.
"""
import os
import argparse
import logging
from utils import (
    getFiles,
    get_name_record,
    make_filename,
    FAMILY_RELATED_IDS,
    PS_FAMILY_RELATED_IDS
)
from fontTools.ttLib import TTFont
from fontTools.misc.cliTools import makeOutputFileName

logger = logging.getLogger()


def renameFonts(old_family_name, newFamilyName, font_files, output_dir=False):
    level = "INFO"
    logging.basicConfig(level=level, format="%(message)s")

    for input_name in font_files:
        logger.info("Renaming font: '%s'", input_name)

        font = TTFont(input_name)
        family_name = rename_family_records(font, old_family_name, newFamilyName)

        if output_dir:
            new_fileName = make_filename(input_name, old_family_name, newFamilyName)
            subdirname = os.path.basename(os.path.dirname(new_fileName))
            output_path = makeOutputFileName(
                new_fileName, os.path.join(output_dir, subdirname)
            )
        else:
            output_path = input_name

        if not os.path.exists(os.path.dirname(output_path)):
            os.makedirs(os.path.dirname(output_path))

        font.save(output_path)
        logger.info("Saved font: '%s'", output_path)

        font.close()
        del font

    logger.info("Done!")


def rename_family_records(font, old_family_name, new_family_name):
    table = font["name"]

    logger.info("  Current family name: '%s'", get_name_record(font, 16, 1))

    # postcript name can't contain spaces
    old_ps_familyName = old_family_name.replace(" ", "")
    new_ps_familyName = new_family_name.replace(" ", "")

    familyNameRecordIds = FAMILY_RELATED_IDS.values()
    psFamilyNameRecordIds = PS_FAMILY_RELATED_IDS.values()

    if 'fvar' in font:
        psFamilyNameRecordIds = list(PS_FAMILY_RELATED_IDS.values()) + [instance.postscriptNameID for instance in font['fvar'].instances]

    for rec in table.names:
        name_id = rec.nameID
        if name_id in familyNameRecordIds:
            old, new = rename_record(rec, old_family_name, new_family_name)
        elif name_id in psFamilyNameRecordIds:
            old, new = rename_record(rec, old_ps_familyName, new_ps_familyName)
        else:
            continue
        logger.debug("    %r: '%s' -> '%s'", rec, old, new)

    if 'CFF ' in font:
        font['CFF '].cff.fontNames[0] = font['CFF '].cff.fontNames[0].replace(old_ps_familyName, new_ps_familyName)
        font['CFF '].cff[0].FamilyName = font['CFF '].cff[0].FamilyName.replace(old_family_name, new_family_name)
        font['CFF '].cff[0].FullName = font['CFF '].cff[0].FullName.replace(old_family_name, new_family_name)

    logger.info("  New family name: '%s'", get_name_record(font, 16, 1))
    return old_family_name


def rename_record(name_record, current_nameString, new_nameString):
    string = name_record.toUnicode()
    new_string = string.replace(current_nameString, new_nameString)
    name_record.string = new_string
    return string, new_string


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("-n", "--name", required=True)
    parser.add_argument("-i", "--input-dir")
    parser.add_argument("-d", "--output-dir")
    options = parser.parse_args()

    font_files = getFiles(options.input_dir, ["ttf", "otf", "woff", "woff2"])
    renameFonts("TikTok", options.name, font_files, options.output_dir)
