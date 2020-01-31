"""
unicode编码范围和正则表达式
参考网站：http://www.unicode.org/charts/
"""
import re
from string import ascii_letters

# European Scripts
# Armenian, 亚美尼亚语
# Range: 0530–058F
ARMENIAN_LETTERS = re.compile(u"[\u0531-\u0588]", re.UNICODE)
ARMENIAN_PUNCTUATION = re.compile(u"[\u0589-\u058A]", re.UNICODE)
ARMENIAN_SYMBOLS = re.compile(u"[\u058D-\u058F]", re.UNICODE)
# Alphabetic Presentation Forms, 字母表示形式
# Range: FB00–FB4F
ARMENIAN_LIGATURES = re.compile(u"[\uFB13-\uFB17]", re.UNICODE)
# Carian, 卡里安语
# Range: 102A0–102DF
CARIAN_LETTERS = re.compile(u"[\U000102A0-\U000102D0]", re.UNICODE)
# Caucasian Albanian, 高加索阿尔巴尼亚语
# Range: 10530–1056F
CAUCASIAN_ALBANIAN_LETTERS = re.compile(u"[\U00010530-\U00010563]", re.UNICODE)
CAUCASIAN_ALBANIAN_PUNCTUATION = re.compile(u"[\U0001056F]", re.UNICODE)
# Cypriot Syllabary, 塞浦路斯音节
# Range: 10800–1083F
CYPRIOT_SYLLABARY_LETTERS = re.compile(u"[\U00010800-\U0001083F]", re.UNICODE)
# Cyrillic, 西里尔
# Range: 0400–04FF
# Cyrillic Supplement
# Range: 0500–052F
# Cyrillic Extended-A
# Range: 2DE0–2DFF
# Cyrillic Extended-B
# Range: A640–A69F
# Cyrillic Extended-C
# Range: 1C80–1C8F
# Elbasan, 尔巴桑
# Range: 10500–1052F
ELBASAN_LETTERS = re.compile(u"[\U00010500-\U00010527]", re.UNICODE)
# Georgian, 格鲁吉亚语
# Range: 10A0–10FF
GEORGIAN_LETTERS = re.compile(u"[\u10A0-\u10FA\u10FC-\u10FF]", re.UNICODE)
GEORGIAN_PUNCTUATION = re.compile(u"[\u10FB]", re.UNICODE)
# Georgian Extended
# Range: 1C90–1CBF
GEORGIAN_EXTENDED_LETTERS = re.compile(u"[\u1C90-\u1CBF]", re.UNICODE)
# Georgian Supplement
# Range: 2D00–2D2F
GEORGIAN_SUPPLEMENT_LETTERS = re.compile(u"[\u2D00-\u2D2F]", re.UNICODE)
# Glagolitic, 格拉哥里语
# Range: 2C00–2C5F
GLAGOLITIC_LETTERS = re.compile(u"[\u2C00-\u2C5F]", re.UNICODE)
# Glagolitic Supplement
# Range: 1E000–1E02F
GLAGOLITIC_SUPPLEMENT_LETTERS = re.compile(u"[\U0001E000-\U0001E02F]", re.UNICODE)
# Gothic, 哥特
# Range: 10330–1034F
GOTHIC_LETTERS = re.compile(u"[\U00010330-\U0001034F]", re.UNICODE)
# Greek and Coptic, 希腊和科普特语
# Range: 0370–03FF
# Greek Extended
# Range: 1F00–1FFF
GREEK_EXTENDED_LETTERS = re.compile(u"[\u1F00-\u1FFF]", re.UNICODE)
# Ancient Greek Numbers
# Range: 10140–1018F
GREEK_NUMBERS = re.compile(u"[\U00010140-\U0001018B]", re.UNICODE)
GREEK_SYMBOLS = re.compile(u"[\U0001018C-\U0001018E]", re.UNICODE)
# C0 Controls and Basic Latin
# Range: 0000–007F
BASIC_LATIN_LETTERS = re.compile(r"[{}]".format(ascii_letters))
# C1 Controls and Latin-1 Supplement
# Range: 0080–00FF
LATIN1_LETTERS = re.compile(u"[\u00C0-\u00D6\u00D8-\u00F6\u00F8-\u00FF]", re.UNICODE)
# Latin Extended-A
# Range: 0100–017F
LATIN_EXTENDED_A_LETTERS = re.compile(u"[\u0100-\u017F]", re.UNICODE)
# Latin Extended-B
# Range: 0180–024F
LATIN_EXTENDED_B_LETTERS = re.compile(u"[\u0180-\u024F]", re.UNICODE)
# Latin Extended-C
# Range: 2C60–2C7F
LATIN_EXTENDED_C_LETTERS = re.compile(u"[\u2C60-\u2C7F]", re.UNICODE)
# Latin Extended-D
# Range: A720–A7FF
LATIN_EXTENDED_D_LETTERS = re.compile(u"[\uA720-\uA7FF]", re.UNICODE)
# Latin Extended-E
# Range: AB30–AB6F
LATIN_EXTENDED_E_LETTERS = re.compile(u"[\uAB30-\uAB6F]", re.UNICODE)
# Latin Extended Additional
# Range: 1E00–1EFF
LATIN_EXTENDED_ADDITIONAL_LETTERS = re.compile(u"[\u1E00-\u1EFF]", re.UNICODE)
# Alphabetic Presentation Forms
# Range: FB00–FB4F
LATIN_LIGATURES_LETTERS = re.compile(u"[\uFB00-\uFB06]", re.UNICODE)
# Halfwidth and Fullwidth Forms
# Range: FF00–FFEF
# IPA Extensions
# Range: 0250–02AF
IPA_LETTERS = re.compile(u"[\u0250-\u02AF]", re.UNICODE)
# Phonetic Extensions
# Range: 1D00–1D7F
PHONETIC_EXTENSIONS_LETTERS = re.compile(u"[\u1D00-\u1D7FF]", re.UNICODE)
# Phonetic Extensions Supplement
# Range: 1D80–1DBF
PHONETIC_EXTENSIONS_SUPPLEMENT_LETTERS = re.compile(u"[\u1D80-\u1DBF]", re.UNICODE)
# Linear A
# Range: 10600–1077F
LINEAR_A_LETTERS = re.compile(u"[\U00010600-\U0001077F]", re.UNICODE)
# Linear B Syllabary
# Range: 10000–1007F
LINEAR_B_SYLLABARY_LETTERS = re.compile(u"[\U00010000-\U0001007F]", re.UNICODE)
# Linear B Ideograms
# Range: 10080–100FF
LINEAR_B_IDEOGRAMS_LETTERS = re.compile(u"[\U00010080-\U000100FF]", re.UNICODE)
# Aegean Numbers
# Range: 10100–1013F
AEGEAN_NUMBERS_LETTERS = re.compile(u"[\U00010100-\U0001013F]", re.UNICODE)
# Lycian, 利西亚语
# Range: 10280–1029F
LYCIAN_LETTERS = re.compile(u"[\U00010280-\U0001029F]", re.UNICODE)
# Lydian, 吕底安
# Range: 10920–1093F
LYDIAN_LETTERS = re.compile(u"[\U00010920-\U0001093F]", re.UNICODE)
# Ogham, 奥格姆
# Range: 1680–169F
OGHAM_LETTERS = re.compile(u"[\u1680-\u169F]", re.UNICODE)
# Old Hungarian, 老匈牙利语
# Range: 10C80–10CFF
OLD_HUNGARIAN_LETTERS = re.compile(u"[\U00010C80-\U00010CFF]", re.UNICODE)
# Old Italic
# Range: 10300–1032F
OLD_ITALIC_LETTERS = re.compile(u"[\U00010300-\U0001032F]", re.UNICODE)
# Old Permic
# Range: 10350–1037F
OLD_PERMIC_LETTERS = re.compile(u"[\U00010350-\U0001037F]", re.UNICODE)
# Phaistos Disc
# Range: 101D0–101FF
PHAISTOS_DISC_SIGNS = re.compile(u"[\U000101D0-\U000101FF]", re.UNICODE)
# Runic, 符文
# Range: 16A0–16FF
RUNIC_LETTERS = re.compile(u"[\u16A0-\u16FF]", re.UNICODE)
# Shavian, 沙维亚语
# Range: 10450–1047F
SHAVIAN_LETTERS = re.compile(u"[\U00010450-\U0001047F]", re.UNICODE)


# East Asian Scripts
# 中文
# Bopomofo
# Range: 3100–312F
BOPOMOFO_LETTERS = re.compile(u"[\u3100-\u312F]", re.UNICODE)
# Bopomofo Extended
# Range: 31A0–31BF
BOPOMOFO_EXTENDED_LETTERS = re.compile(u"[\u31A0-\u31BF]", re.UNICODE)
# CJK Unified Ideographs, 中日韩统一表意文字
# Range: 4E00–9FEF
CJK_LETTERS = re.compile(u"[\u4E00-\u9FEF]", re.UNICODE)
# CJK Unified Ideographs Extension A
# Range: 3400–4DB5
CJK_EXTENSION_A_LETTERS = re.compile(u"[\u3400-\u4DB5]", re.UNICODE)
# CJK Unified Ideographs Extension B
# Range: 20000–2A6D6
CJK_EXTENSION_B_LETTERS = re.compile(u"[\U00020000-\U0002A6D6]", re.UNICODE)
# CJK Unified Ideographs Extension C
# Range: 2A700–2B734
CJK_EXTENSION_C_LETTERS = re.compile(u"[\U0002A700-\U0002B734]", re.UNICODE)
# CJK Unified Ideographs Extension D
# Range: 2B740–2B81D
CJK_EXTENSION_D_LETTERS = re.compile(u"[\U0002B740-\U0002B81D]", re.UNICODE)
# CJK Unified Ideographs Extension E
# Range: 2B820–2CEA1
CJK_EXTENSION_E_LETTERS = re.compile(u"[\U0002B820-\U0002CEA1]", re.UNICODE)
# CJK Unified Ideographs Extension F
# Range: 2CEB0–2EBE0
CJK_EXTENSION_F_LETTERS = re.compile(u"[\U0002CEB0-\U0002EBE0]", re.UNICODE)
# CJK Compatibility Ideographs
# Range: F900–FAFF
CJK_COMPATIBILITY_LETTERS = re.compile(u"[\uF900-\uFAFF]", re.UNICODE)
# CJK Compatibility Ideographs Supplement
# Range: 2F800–2FA1F
CJK_COMPATIBILITY_SUPPLEMENT_LETTERS = re.compile(u"[\U0002F800-\U0002FA1F]", re.UNICODE)
# Kangxi Radicals
# Range: 2F00–2FDF
KANGXI_RADICALS_LETTERS = re.compile(u"[\u2F00-\u2FDF]", re.UNICODE)
# CJK Radicals Supplement
# Range: 2E80–2EFF
CJK_RADICALS_LETTERS = re.compile(u"[\u2E80-\u2EFF]", re.UNICODE)
# CJK Strokes
# Range: 31C0–31EF
CJK_STROKES_LETTERS = re.compile(u"[\u31C0-\u31EF]", re.UNICODE)
# Ideographic Description Characters
# Range: 2FF0–2FFF
IDEOGRAPHIC_DESCRIPTION_LETTERS = re.compile(u"[\u2FF0-\u2FFF]", re.UNICODE)

# Hangul Jamo, 朝鲜文/韩文
# Range: 1100–11FF
HANGUL_JAMO_LETTERS = re.compile(u"[\u1100-\u11FF]", re.UNICODE)
# Hangul Jamo Extended-A
# Range: A960–A97F
HANGUL_JAMO_EXTENDED_A_LETTERS = re.compile(u"[\uA960-\uA97F]", re.UNICODE)
# Hangul Jamo Extended-B
# Range: D7B0–D7FF
HANGUL_JAMO_EXTENDED_B_LETTERS = re.compile(u"[\uD7B0-\uD7FF]", re.UNICODE)
# Hangul Compatibility Jamo
# Range: 3130–318F
HANGUL_JAMO_COMPATIBILITY_LETTERS = re.compile(u"[\u3130-\u318F]", re.UNICODE)
# Halfwidth and Fullwidth Forms
# Range: FF00–FFEF
# Hangul Syllables
# Range: AC00–D7AF
HANGUL_SYLLABLES_LETTERS = re.compile(u"[\uAC00-\uD7AF]", re.UNICODE)
# Hiragana, 平假名
# Range: 3040–309F
HIRAGANA_LETTERS = re.compile(u"[\u3040-\u309F]", re.UNICODE)
# Kana Extended-A, 假名
# Range: 1B100–1B12F
KANA_EXTENDED_LETTERS = re.compile(u"[\U0001B100-\U0001B12F]", re.UNICODE)
# Kana Supplement
# Range: 1B000–1B0FF
KANA_SUPPLEMENT_LETTERS = re.compile(u"[\U0001B000-\U0001B0FF]", re.UNICODE)
# Small Kana Extension
# Range: 1B130–1B16F
KANA_EXTENSION_LETTERS = re.compile(u"[\U0001B130-\U0001B16F]", re.UNICODE)
# Kanbun
# Range: 3190–319F
KANBUN_LETTERS = re.compile(u"[\u3190-\u319F]", re.UNICODE)
# Katakana
# Range: 30A0–30FF
KATAKANA_LETTERS = re.compile(u"[\u30A0-\u30FF]", re.UNICODE)
# Katakana Phonetic Extensions
# Range: 31F0–31FF
KATAKANA_PHONETIC_LETTERS = re.compile(u"[\u31F0-\u31FF]", re.UNICODE)
# Lisu
# Range: A4D0–A4FF
LISU_LETTERS = re.compile(u"[\uA4D0-\uA4F7]", re.UNICODE)
# Miao
# Range: 16F00–16F9F
MIAO_LETTERS = re.compile(u"[\U00016F00-\U00016F9F]", re.UNICODE)
# Nushu
# Range: 1B170–1B2FF
NUSHU_LETTERS = re.compile(u"[\U0001B170-\U0001B2FF]", re.UNICODE)
# Tangut
# Range: 17000–187F7
TANGUT_LETTERS = re.compile(u"[\U00017000-\U000187F7]", re.UNICODE)
# Tangut Components
# Range: 18800–18AFF
TANGUT_COMPONENTS_LETTERS = re.compile(u"[\U00018800-\U00018AFF]", re.UNICODE)
# Yi Syllables
# Range: A000–A48F
YI_SYLLABLES_LETTERS = re.compile(u"[\uA000-\uA48F]", re.UNICODE)
# Yi Radicals
# Range: A490–A4CF
YI_RADICALS_LETTERS = re.compile(u"[\uA490-\uA4CF]", re.UNICODE)


def check():
    start = int("A490", 16)
    end = int("A4CF", 16)
    for i in range(start, end + 1):
        char = chr(i)
        # print(char, hex(i), ord(char), i)
        if YI_RADICALS_LETTERS.search(char):
            print("匹配成功", char)
            # pass
        # else:
        #     print("匹配失败", char)
    print(len(range(start, end + 1)))

if __name__ == '__main__':
    check()
