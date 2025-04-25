from fontTools.varLib import instancer
import os


WINDOWS_ENGLISH_IDS = 3, 1, 0x409
MAC_ROMAN_IDS = 1, 0, 0

FAMILY_RELATED_IDS = dict(
    LEGACY_FAMILY=1,
    FULL_NAME=4,
    PREFERRED_FAMILY=16,
    WWS_FAMILY=21,
)

PS_FAMILY_RELATED_IDS = dict(
    TRUETYPE_UNIQUE_ID=3,
    POSTSCRIPT_NAME=6,
    VARIATIONS_POSTSCRIPT_NAME=25,
)


def getFiles(path, extensions):
    return [
        os.sep.join((dir, file))
        for (dir, dirs, files) in os.walk(path)
        for file in files
        if file.split(".")[-1] in extensions
    ]


def get_name_record(ttFont, nameID, fallbackID=None, platform=(3, 1, 0x409)):
    """Return a name table record which has the specified nameID.
    Args:
        ttFont: a TTFont instance
        nameID: nameID of name record to return,
        fallbackID: if nameID doesn't exist, use this nameID instead
        platform: Platform of name record. Default is Win US English
    Returns:
        str
    """
    name = ttFont["name"]
    record = name.getName(nameID, 3, 1, 0x409)
    if not record and fallbackID:
        record = name.getName(fallbackID, 3, 1, 0x409)
    if not record:
        raise ValueError(f"Cannot find record with nameID {nameID}")
    return record.toUnicode()


def subspaceFont(ttFont, coordinates, familyName):
    newFont = instancer.instantiateVariableFont(
        ttFont, coordinates, updateFontNames=True
    )
    # nameTable = newFont["name"]

    # Fix usWeightClass https://github.com/fonttools/fonttools/issues/2885
    # default_axis_values = {a.axisTag: a.defaultValue for a in newFont['fvar'].axes}
    # fvar_value = default_axis_values.get('wght')
    # newFont["OS/2"].usWeightClass = fvar_value

    # # Replace name table with new family name and new default instance name
    # old_familyName = newFont['name'].getName(nameID=16, platformID=3, platEncID=1, langID=0x409).toUnicode()
    # old_styleName = newFont['name'].getName(nameID=17, platformID=3, platEncID=1, langID=0x409).toUnicode()
    # old_fullName = newFont['name'].getName(nameID=4, platformID=3, platEncID=1, langID=0x409).toUnicode()
    # old_psFamilyName = old_familyName.replace(" ", "")
    # old_psName = newFont['name'].getName(nameID=6, platformID=3, platEncID=1, langID=0x409).toUnicode()

    # new_familyName = familyName
    # new_styleName = getDefaultInstanceName(newFont)

    # new_fullName = new_familyName + " " + new_styleName
    # new_psFamilyName = new_familyName.replace(" ", "")
    # new_psName = makePostscriptName(new_familyName, new_styleName)

    # oldNames = [old_fullName, old_psName, old_familyName, old_styleName, old_psFamilyName]
    # newNames = [new_fullName, new_psName, new_familyName, new_styleName, new_psFamilyName]

    # # Loop find and replace
    # for record in nameTable.names:
    #     record_text = record.toUnicode()

    #     isMatch = False
    #     for string in oldNames:
    #         if string in record_text:
    #             isMatch = string
    #             break

    #     if isMatch != False:
    #         record_newtext = record_text.replace(isMatch, newNames[oldNames.index(isMatch)] )

    #         newFont['name'].setName(
    #             record_newtext,
    #             record.nameID,
    #             record.platformID,
    #             record.platEncID,
    #             record.langID
    #         )

    return newFont


def make_filename(fileName, old_familyName, new_familyName):
    filename, extension = os.path.splitext(fileName)

    filename = filename.replace(old_familyName, new_familyName)
    ps_name = filename.replace(" ", "")

    return f"{ps_name}{extension}"


def makeVFfileName(ttFont, familyName):
    assert "fvar" in ttFont
    axis_tags = sorted([ax.axisTag for ax in ttFont["fvar"].axes])
    axis_tags = ",".join(axis_tags)
    slugFamilyName = familyName.replace(" ", "")
    return f"{slugFamilyName}[{axis_tags}].ttf"


def remove_substring_with_trailing_space(text, substring):
    # Find the starting index of the substring
    start_index = text.find(substring)

    # If the substring is found, remove it along with any trailing space
    if start_index != -1:
        end_index = start_index + len(substring)
        while end_index < len(text) and text[end_index].isspace():
            end_index += 1

        # Remove the substring and trailing space
        result = text[:start_index] + text[end_index:]
    else:
        result = text

    return result


def check_string_in_list(instanceName, particle_list):
    for string in particle_list:
        if string in instanceName:
            return string
    return False


def scale_unit_string(s, factor):
    import re
    match = re.match(r"(\d+(?:\.\d+)?)([a-zA-Z%]+)", s)
    if match:
        number, unit = match.groups()
        scaled = int(number) * factor
        return f"{scaled}{unit}"
    else:
        raise ValueError("String doesn't match expected format.")