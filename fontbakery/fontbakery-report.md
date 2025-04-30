## FontBakery report

fontbakery version: 0.13.2







## Check results



<details><summary>[16] TikTokSans[opsz,slnt,wdth,wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure smart dropout control is enabled in "prep" table instructions. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#smart-dropout">smart_dropout</a></summary>
    <div>







* 🔥 **FAIL** <p>The 'prep' table does not contain TrueType instructions enabling smart dropout control. To fix, export the font with autohinting enabled, or run ttfautohint on the font, or run the <code>gftools fix-nonhinting</code> script.</p>
 [code: lacks-smart-dropout]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check correctness of STAT table strings <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#STAT-strings">STAT_strings</a></summary>
    <div>







* 🔥 **FAIL** <p>The following AxisValue entries on the STAT table should not contain &quot;Italic&quot;:
['nameID 353: Italic']</p>
 [code: bad-italic]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ʼ</td>
<td align="left">uk_Cyrl (Ukrainian), ha_Latn (Hausa) and uk_Cyrl (Ukrainian)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following mark characters are missing from the font: ̩</td>
<td align="left">yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ҝ, ҹ</td>
<td align="left">az_Cyrl (Azerbaijani (Cyrillic))</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ҥ, ҥ</td>
<td align="left">chm_Cyrl (Mari)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ҥ, ҕ</td>
<td align="left">sah_Cyrl (Sakha)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* ⚠️ **WARN** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ſ</td>
<td align="left">de_Latn (German) and fr_Latn (French)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ʻ</td>
<td align="left">en_Latn (English)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ǥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ʒ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ǯ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ǥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ʒ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ǯ</td>
<td align="left">fi_Latn (Finnish)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѫ</td>
<td align="left">bg_Cyrl (Bulgarian) and bg_Cyrl (Bulgarian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἀ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἄ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἂ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἆ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἁ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἅ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἃ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἇ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ᾶ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἐ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἔ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἒ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἑ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἓ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἠ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἤ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἢ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἡ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἣ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῆ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἰ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἴ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἲ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἶ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἱ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἵ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἳ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἷ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῖ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῗ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὄ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὂ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὃ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὐ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὔ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὒ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὖ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὑ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὓ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὗ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὤ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὢ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὣ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῶ</td>
<td align="left">el_Grek (Greek)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ɵ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ɵ</td>
<td align="left">ig_Latn (Igbo)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: e̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: E̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: é̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: É̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: è̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: È̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ê̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ê̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ě̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ě̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: o̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: O̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ó̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ó̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ò̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ò̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ô̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ô̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ǒ̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ǒ̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: s̩</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: S̩</td>
<td align="left">yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ӊ</td>
<td align="left">mn_Cyrl (Mongolian)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check family name for GF Guide compliance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-family-name-compliance">googlefonts/family_name_compliance</a></summary>
    <div>







* 🔥 **FAIL** <p>&quot;TikTok Sans&quot; is a CamelCased name. To solve this, simply use spaces instead in the font name.</p>
 [code: camelcase]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Copyright notices match canonical pattern in fonts <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-font-copyright">googlefonts/font_copyright</a></summary>
    <div>







* 🔥 **FAIL** <p>Name Table entry: Copyright notices should match a pattern similar to:</p>
<p>&quot;Copyright 2020 The Familyname Project Authors (git url)&quot;</p>
<p>But instead we have got:</p>
<p>&quot;Copyright 2024 TikTok Inc. (<a href="https://github.com/tiktok/TikTokSans">https://github.com/tiktok/TikTokSans</a>)&quot;</p>
 [code: bad-notice-format]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check license file has good copyright string. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-license-OFL-copyright">googlefonts/license/OFL_copyright</a></summary>
    <div>







* 🔥 **FAIL** <p>First line in license file is:</p>
<p>&quot;copyright 2024 tiktok inc. (<a href="https://github.com/tiktok/tiktoksans">https://github.com/tiktok/tiktoksans</a>)&quot;</p>
<p>which does not match the expected format, similar to:</p>
<p>&quot;Copyright 2022 The Familyname Project Authors (git url)&quot;</p>
 [code: bad-format]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Validate STAT particle names and values match the fallback names in GFAxisRegistry. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-STAT-axisregistry">googlefonts/STAT/axisregistry</a></summary>
    <div>







* 🔥 **FAIL** <p>On the font variation axis 'slnt', the name 'Italic' is not among the expected ones (Default) according to the Google Fonts Axis Registry.</p>
 [code: invalid-name]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Axes and named instances fall within correct ranges? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-fvar-regular-coords-correct">opentype/fvar/regular_coords_correct</a></summary>
    <div>







* ⚠️ **WARN** <p>Regular instance has opsz coordinate of 36.0, expected between 10 and 16</p>
 [code: opsz]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- _comb.Cmoney

- _comp.Cmoney.tf

- _cystrokeshortcomb
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, cherokee, tifinagh, coptic</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: hebrew, syriac, tifinagh, malayalam, canadian-aboriginal, old-permic, math, duployan, todhri, tai-le, coptic</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: cherokee, thai, syriac, tifinagh, sunuwar, gothic, caucasian-albanian</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+0338 COMBINING LONG SOLIDUS OVERLAY: try adding math</li>
<li>U+0E3F THAI CURRENCY SYMBOL BAHT: try adding thai</li>
<li>U+2003 EM SPACE: try adding nushu</li>
<li>U+2004 THREE-PER-EM SPACE: try adding symbols2</li>
<li>U+2005 FOUR-PER-EM SPACE: try adding symbols2</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2008 PUNCTUATION SPACE: try adding symbols2</li>
<li>U+200A HAIR SPACE: try adding symbols2</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207A SUPERSCRIPT PLUS SIGN: try adding math</li>
<li>U+207B SUPERSCRIPT MINUS: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208A SUBSCRIPT PLUS SIGN: try adding math</li>
<li>U+208B SUBSCRIPT MINUS: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2100 ACCOUNT OF: try adding math</li>
<li>U+2105 CARE OF: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: mongolian, symbols, yi</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: mongolian, symbols, yi</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: mongolian, symbols, yi</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: mongolian, symbols, yi</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: mongolian, symbols, yi</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: mongolian, symbols, yi</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: mongolian, symbols, yi</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: mongolian, symbols, yi</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: mongolian, symbols, yi</li>
<li>U+24EA CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+24FF NEGATIVE CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: music, warang-citi, mahajani, tagalog, bengali, sinhala, thai, khmer, masaram-gondi, limbu, miao, newa, tibetan, soyombo, syriac, brahmi, manichaean, cham, yi, elbasan, buginese, phags-pa, modi, tifinagh, javanese, mende-kikakui, tagbanwa, hebrew, balinese, telugu, hanunoo, takri, sharada, osage, kharoshthi, bassa-vah, tai-tham, zanabazar-square, buhid, sundanese, malayalam, thaana, hanifi-rohingya, kaithi, tai-le, mongolian, myanmar, batak, khudawadi, lepcha, syloti-nagri, rejang, oriya, dogra, sogdian, gurmukhi, grantha, meetei-mayek, bhaiksuki, armenian, gujarati, wancho, khojki, duployan, symbols, caucasian-albanian, marchen, kannada, devanagari, nko, gunjala-gondi, tamil, new-tai-lue, old-permic, siddham, kayah-li, pahawh-hmong, mandaic, tirhuta, canadian-aboriginal, saurashtra, chakma, adlam, tai-viet, ahom, lao, math, psalter-pahlavi, coptic</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+2776 DINGBAT NEGATIVE CIRCLED DIGIT ONE: try adding symbols</li>
<li>U+2777 DINGBAT NEGATIVE CIRCLED DIGIT TWO: try adding symbols</li>
<li>U+2778 DINGBAT NEGATIVE CIRCLED DIGIT THREE: try adding symbols</li>
<li>U+2779 DINGBAT NEGATIVE CIRCLED DIGIT FOUR: try adding symbols</li>
<li>U+277A DINGBAT NEGATIVE CIRCLED DIGIT FIVE: try adding symbols</li>
<li>U+277B DINGBAT NEGATIVE CIRCLED DIGIT SIX: try adding symbols</li>
<li>U+277C DINGBAT NEGATIVE CIRCLED DIGIT SEVEN: try adding symbols</li>
<li>U+277D DINGBAT NEGATIVE CIRCLED DIGIT EIGHT: try adding symbols</li>
<li>U+277E DINGBAT NEGATIVE CIRCLED DIGIT NINE: try adding symbols</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>greek</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check OFL body text is correct. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-license-OFL-body-text">googlefonts/license/OFL_body_text</a></summary>
    <div>







* ⚠️ **WARN** <p>The OFL.txt body text is incorrect. Please use <a href="https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt">https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt</a> as a template. You should only modify the first line.</p>
<p>Lines changed:</p>
<p>+ with Reserved Font Name &quot;TikTok&quot;.\n</p>
 [code: incorrect-ofl-body-text]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-dotted">soft_dotted</a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ɨ̀ ɨ́ ɨ̂ ɨ̃ ɨ̄ ɨ̈ ɨ̋ ɨ̌ ɨ̧̀ ɨ̧́ ɨ̧̂ ɨ̧̌ ɨ̱̀ ɨ̱́ ɨ̱̈ і́ ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: į̆ į̇ į̈ į̉ į̊ į̋ į̒ į̣̀ į̣́ į̣̂ į̣̃ į̣̄ į̣̆ į̣̇ į̣̈ į̣̉ į̣̊ į̣̋ į̣̌ į̣̒</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-alignment-miss">outline_alignment_miss</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* S (U+0053): X=412.5,Y=703.5 (should be at cap-height 705?)

* Aogonek (U+0104): X=543.0,Y=1.0 (should be at baseline 0?)

* Eogonek (U+0118): X=417.0,Y=1.0 (should be at baseline 0?)

* Iogonek (U+012E): X=68.0,Y=1.0 (should be at baseline 0?)

* uni01EA (U+01EA): X=458.0,Y=1.0 (should be at baseline 0?)

* Sacute (U+015A): X=412.5,Y=703.5 (should be at cap-height 705?)

* Scaron (U+0160): X=412.5,Y=703.5 (should be at cap-height 705?)

* Scedilla (U+015E): X=412.5,Y=703.5 (should be at cap-height 705?)

* Scircumflex (U+015C): X=412.5,Y=703.5 (should be at cap-height 705?)

* uni0218 (U+0218): X=412.5,Y=703.5 (should be at cap-height 705?)

* Uogonek (U+0172): X=380.0,Y=1.0 (should be at baseline 0?)

* f (U+0066): X=346.0,Y=707.0 (should be at cap-height 705?)

* j (U+006A): X=146.0,Y=-1.0 (should be at baseline 0?)

* s (U+0073): X=310.0,Y=506.0 (should be at x-height 507?)

* ae (U+00E6): X=294.0,Y=0.5 (should be at baseline 0?)

* aeacute (U+01FD): X=294.0,Y=0.5 (should be at baseline 0?)

* aogonek (U+0105): X=399.0,Y=1.0 (should be at baseline 0?)

* eogonek (U+0119): X=298.0,Y=1.0 (should be at baseline 0?)

* ij (U+0133): X=331.0,Y=-1.0 (should be at baseline 0?)

* iogonek (U+012F): X=50.0,Y=1.0 (should be at baseline 0?)

* uni006A0301: X=146.0,Y=-1.0 (should be at baseline 0?)

* jcircumflex (U+0135): X=146.0,Y=-1.0 (should be at baseline 0?)

* uni0237 (U+0237): X=146.0,Y=-1.0 (should be at baseline 0?)

* uni01EB (U+01EB): X=301.0,Y=1.0 (should be at baseline 0?)

* thorn (U+00FE): X=230.5,Y=-0.5 (should be at baseline 0?)

* uogonek (U+0173): X=268.0,Y=1.0 (should be at baseline 0?)

* germandbls (U+00DF): X=201.0,Y=2.0 (should be at baseline 0?)

* ogonek (U+02DB): X=138.0,Y=1.0 (should be at baseline 0?)

* three (U+0033): X=188.0,Y=706.5 (should be at cap-height 705?)

* sterling (U+00A3): X=435.0,Y=705.5 (should be at cap-height 705?)

* Euro (U+20AC): X=520.0,Y=-0.5 (should be at baseline 0?)

* uni20B4 (U+20B4): X=226.0,Y=706.0 (should be at cap-height 705?)

* fi (U+FB01): X=346.0,Y=707.0 (should be at cap-height 705?)

* fl (U+FB02): X=346.0,Y=707.0 (should be at cap-height 705?)

* three.tf: X=189.0,Y=706.5 (should be at cap-height 705?)

* sterling.tf: X=432.0,Y=705.5 (should be at cap-height 705?)

* Euro.tf: X=505.5,Y=706.5 (should be at cap-height 705?)

* uni0328 (U+0328): X=138.0,Y=1.0 (should be at baseline 0?)

* uni0190 (U+0190): X=408.0,Y=704.0 (should be at cap-height 705?)

* uni0190 (U+0190): X=419.5,Y=1.5 (should be at baseline 0?)

* uni1E62 (U+1E62): X=412.5,Y=703.5 (should be at cap-height 705?)

* Iogonek.cv01: X=253.0,Y=1.0 (should be at baseline 0?)

* uni1EA3 (U+1EA3): X=286.0,Y=703.5 (should be at cap-height 705?)

* uni01E3 (U+01E3): X=294.0,Y=0.5 (should be at baseline 0?)

* uni1EBB (U+1EBB): X=296.0,Y=703.5 (should be at cap-height 705?)

* uni1EC9 (U+1EC9): X=130.0,Y=703.5 (should be at cap-height 705?)

* uni1ECF (U+1ECF): X=311.0,Y=703.5 (should be at cap-height 705?)

* uni1EDF (U+1EDF): X=311.0,Y=703.5 (should be at cap-height 705?)

* uni1EE7 (U+1EE7): X=286.0,Y=703.5 (should be at cap-height 705?)

* uni1EED (U+1EED): X=286.0,Y=703.5 (should be at cap-height 705?)

* uni1EF7 (U+1EF7): X=276.0,Y=703.5 (should be at cap-height 705?)

* s.sups: X=133.0,Y=704.0 (should be at cap-height 705?)

* uni041B (U+041B): X=8.0,Y=2.0 (should be at baseline 0?)

* uni0409 (U+0409): X=8.0,Y=2.0 (should be at baseline 0?)

* uni0405 (U+0405): X=412.5,Y=703.5 (should be at cap-height 705?)

* uni0402 (U+0402): X=389.0,Y=2.0 (should be at baseline 0?)

* uni0474 (U+0474): X=661.0,Y=703.0 (should be at cap-height 705?)

* uni0458 (U+0458): X=146.0,Y=-1.0 (should be at baseline 0?)

* uni04D5 (U+04D5): X=294.0,Y=0.5 (should be at baseline 0?)

* beta (U+03B2): X=217.0,Y=1.5 (should be at baseline 0?)

* uni2070 (U+2070): X=139.0,Y=703.0 (should be at cap-height 705?)

* uni2070 (U+2070): X=374.0,Y=703.0 (should be at cap-height 705?)

* uni00B2 (U+00B2): X=116.0,Y=703.0 (should be at cap-height 705?)

* uni2070.cv03: X=139.5,Y=703.0 (should be at cap-height 705?)

* uni2070.cv03: X=374.0,Y=703.0 (should be at cap-height 705?)

* at.case: X=479.0,Y=704.0 (should be at cap-height 705?)

* uni20B2 (U+20B2): X=350.0,Y=-1.0 (should be at baseline 0?)

* uni20B2 (U+20B2): X=350.0,Y=-1.0 (should be at baseline 0?)

* uni20B4.tf: X=210.0,Y=706.0 (should be at cap-height 705?)

* hookabovecomb (U+0309): X=173.0,Y=703.5 (should be at cap-height 705?)

* uni0328.alt: X=138.0,Y=1.0 (should be at baseline 0?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-gasp">googlefonts/gasp</a></summary>
    <div>









* ⚠️ **WARN** <p>The gasp table has a range of 8 that may be unneccessary.</p>
 [code: non-ffff-range]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-meta-script-lang-tags">googlefonts/meta/script_lang_tags</a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 7 | 9 | 88 | 6 | 126 | 0 | 
| 0% | 0% | 3% | 4% | 37% | 3% | 53% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
