"""
unicode编码范围和正则表达式
参考网站：http://www.unicode.org/charts/
"""
import re
from string import punctuation


# General Punctuation
# Range: 2000–206F
GENERAL_PUNCTUATION = re.compile(u"[\u2000-\u206F]", re.UNICODE)
# C0 Controls and Basic Latin, 英语标点
# Range: 0000–007F
BASIC_LATIN_PUNCTUATION = re.compile(r"[{}]".format(punctuation))
# C1 Controls and Latin-1 Supplement, Latin标点
# Range: 0080–00FF
LATIN1_PUNCTUATION = re.compile(u"[\u0080-\u00BF\u00D7\u00F7]", re.UNICODE)
# Supplemental Punctuation, 补充标点
# Range: 2E00–2E7F
SUPPLEMENTAL_PUNCTUATION = re.compile(u"[\u2E00-\u2E7F]", re.UNICODE)
# CJK Symbols and Punctuation, 中日韩标点
# Range: 3000–303F
CJK_PUNCTUATION = re.compile(u"[\u3000-\u301F\u3030\u303B-\u303F]", re.UNICODE)
CJK_SYMBOLS = re.compile(u"[\u3020\u3036\u3037]", re.UNICODE)
# Ideographic Symbols and Punctuation, 表意标点
# Range: 16FE0–16FFF
IDEOGRAPHIC_PUNCTUATION = re.compile(u"[\U00016FE0-\U00016FFF]", re.UNICODE)
# CJK Compatibility Forms, 中日韩兼容标点
# Range: FE30–FE4F
CJK_COMPATIBILITY_PUNCTUATION = re.compile(u"[\uFE30-\uFE4F]", re.UNICODE)
# Halfwidth and Fullwidth Forms, 半角和全角形式
# Range: FF00–FFEF
FULLWIDTH_ASCII_PUNCTUATION = re.compile(u"[\uFF00-\uFF0F\uFF1A-\uFF20\uFF3B-\uFF40\uFF5B-\uFF65]", re.UNICODE)
FULLWIDTH_HALFWIDTH_SYMBOLS = re.compile(u"[\uFFE0-\uFFEE]", re.UNICODE)
# Small Form Variants, 小型变体
# Range: FE50–FE6F
SMALL_VARIANTS_PUNCTUATION = re.compile(u"[\uFE50-\uFE6F]", re.UNICODE)
# Vertical Forms, 垂直形式
# Range: FE10–FE1F
VERTICAL_PUNCTUATION = re.compile(u"[\uFE10-\uFE1F]", re.UNICODE)


def check():
    start = int("FE10", 16)
    end = int("FE1F", 16)
    for i in range(start, end + 1):
        char = chr(i)
        # print(char, hex(i), ord(char), i)
        if VERTICAL_PUNCTUATION.search(chr(i)):
            print("匹配成功", char)
            # pass
        else:
            print("匹配失败", char)
    print(len(range(start, end + 1)))

if __name__ == '__main__':
    check()
