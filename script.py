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


def check():
    start = int("FB00", 16)
    end = int("FB4F", 16)
    for i in range(start, end + 1):
        char = chr(i)
        # print(char, hex(i), ord(char), i)
        if LATIN_LIGATURES_LETTERS.search(char):
            print("匹配成功", char)
            # pass
        # else:
        #     print("匹配失败", char)
    print(len(range(start, end + 1)))

if __name__ == '__main__':
    check()
