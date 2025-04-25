import os
from utils import makeVFfileName, get_name_record, scale_unit_string
from renameFonts import renameFonts
from fontTools.ttLib import TTFont


def makeTVFont(master_fontPath):
    OUTPUT_DIR = "./fonts/tv"

    TV_FONTS_DATA = [
        {"name": "TikTok Sans 2x", "factor": 2},
        {"name": "TikTok Sans 4x", "factor": 4}
    ]

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for font_data in TV_FONTS_DATA:
        master_ttFont = TTFont(master_fontPath)
        newFileName = makeVFfileName(master_ttFont, font_data["name"])
        tv_font_outputpath = os.path.join(OUTPUT_DIR, newFileName)

        # Modify opsz axis values
        fvar = master_ttFont['fvar']
        for axis in fvar.axes:
            if axis.axisTag == 'opsz':
                new_minValue = axis.minValue * font_data["factor"]
                new_defaultValue = axis.defaultValue * font_data["factor"]
                new_maxValue = axis.maxValue * font_data["factor"]

                axis.minValue = new_minValue
                axis.defaultValue = new_defaultValue
                axis.maxValue = new_maxValue

        # Modify instances coordinates
        for instance in fvar.instances:
            instance.coordinates['opsz'] = new_defaultValue

        # Modify STAT table records for opsz axis
        if "STAT" in master_ttFont:
            stat = master_ttFont["STAT"].table

            designAxes = [designAxis.AxisTag for designAxis in stat.DesignAxisRecord.Axis]
            
            if hasattr(stat, "DesignAxisRecord"):
                for axisValue in stat.AxisValueArray.AxisValue:
                    if designAxes[axisValue.AxisIndex] == 'opsz':
                        axisValueName = get_name_record(master_ttFont, axisValue.ValueNameID)
                        record_newtext = scale_unit_string(axisValueName, font_data["factor"])
                        master_ttFont['name'].setName(record_newtext, axisValue.ValueNameID, 3, 1, 0x409)

                        axisValue.Value = axisValue.Value * font_data["factor"]
            else:
                print("No DesignAxisRecord found in the STAT table.")

        # Save the font
        master_ttFont.save(tv_font_outputpath)
        master_ttFont.close()
        renameFonts("TikTok VF", font_data["name"], [tv_font_outputpath])


if __name__ == "__main__":
    MASTER_VF_OTF = "./fonts/TikTok-VF.otf"
    MASTER_VF_TTF = "./fonts/variable/TikTokSans[opsz,slnt,wdth,wght].ttf"

    makeTVFont(MASTER_VF_TTF)
