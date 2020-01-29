"""
unicode编码范围和正则表达式
参考网站：http://www.unicode.org/charts/
"""
import re


# Notational Systems
# Braille Patterns， 盲文图案
# Range: 2800–28FF
BRAILLE_PATTERNS = re.compile(u"[\u2800-\u28FF]", re.UNICODE)
# Musical Symbols, 音乐符号
# Range: 1D100–1D1FF
MUSICAL_SYMBOLS = re.compile(u"[\U0001D100-\U0001D1FF]", re.UNICODE)
# Ancient Greek Musical Notation, 古希腊音乐符号
# Range: 1D200–1D24F
GREEK_MUSICAL_SYMBOLS = re.compile(u"[\U0001D200-\U0001D24F]", re.UNICODE)
# Byzantine Musical Symbols, 拜占庭的音乐符号
# Range: 1D000–1D0FF
BYZANTINE_MUSICAL_SYMBOLS = re.compile(u"[\U0001D000-\U0001D0FF]", re.UNICODE)
# Duployan
# Range: 1BC00–1BC9F
DUPLOYAN = re.compile(u"[\U0001BC00-\U0001BC9F]", re.UNICODE)
# Shorthand Format Controls, 速记格式控件
# Range: 1BCA0–1BCAF
SHORTHAND_FORMAT = re.compile(u"[\U0001BCA0-\U0001BCAF]", re.UNICODE)
# Sutton SignWriting
# Range: 1D800–1DAAF
SUTTON_SIGNWRITING = re.compile(u"[\U0001D800-\U0001DAAF]", re.UNICODE)
# 汇总
SYMBOLS = re.compile(u"["
                     u"\u2800-\u28FF"               # Braille Patterns， 盲文图案
                     u"\U0001BC00-\U0001BC9F"       # Duployan
                     u"\U0001BCA0-\U0001BCAF"       # Shorthand Format Controls, 速记格式控件
                     u"\U0001D000-\U0001D0FF"       # Byzantine Musical Symbols, 拜占庭的音乐符号
                     u"\U0001D100-\U0001D1FF"       # Musical Symbols, 音乐符号
                     u"\U0001D200-\U0001D24F"       # Ancient Greek Musical Notation, 古希腊音乐符号
                     u"\U0001D800-\U0001DAAF"       # Sutton SignWriting
                     u"]", re.UNICODE)

# Alphanumeric Symbols, 字母数字符号
# Letterlike Symbols, 字母符号
# Range: 2100–214F
LETTERLIKE_SYMBOLS = re.compile(u"[\u2100-\u214F]", re.UNICODE)
# Ancient Symbols
# Range: 10190–101CF
ANCIENT_SYMBOLS = re.compile(u"[\U00010190-\U000101CF]", re.UNICODE)
# Mathematical Alphanumeric Symbols, 数学字母数字符号
# Range: 1D400–1D7FF
MATH_ALPHANUMERIC_SYMBOLS = re.compile(u"[\U0001D400-\U0001D7FF]", re.UNICODE)
# Arabic Mathematical Alphabetic Symbols
# Range: 1EE00–1EEFF
ARABIC_MATH_ALPHANUMERIC_SYMBOLS = re.compile(u"[\U0001EE00-\U0001EEFF]", re.UNICODE)
# Enclosed Alphanumerics, 封闭的字母数字
# Range: 2460–24FF
ENCLOSED_ALPHANUMERIC_SYMBOLS = re.compile(u"[\u2460-\u24FF]", re.UNICODE)
# Enclosed Alphanumeric Supplement
# Range: 1F100–1F1FF
ENCLOSED_ALPHANUMERIC_SUPPLEMENT_SYMBOLS = re.compile(u"[\U0001F100-\U0001F1FF]", re.UNICODE)
# Enclosed CJK Letters and Months
# Range: 3200–32FF
ENCLOSED_CJK_LETTERS_SYMBOLS = re.compile(u"[\u3200-\u32FF]", re.UNICODE)
# Enclosed Ideographic Supplement, 意文字增补
# Range: 1F200–1F2FF
ENCLOSED_IDEOGRAPHIC_SUPPLEMENT_SYMBOLS = re.compile(u"[\U0001F200-\U0001F2FF]", re.UNICODE)
# CJK Compatibility, 中日韩兼容
# Range: 3300–33FF
CJK_COMPATIBILITY_SYMBOLS = re.compile(u"[\u3300-\u33FF]", re.UNICODE)

# Technical Symbols
# Miscellaneous Technical
# Range: 2300–23FF
MISCELLANEOUS_TECHNICAL_SYMBOLS = re.compile(u"[\u2300-\u23FF]", re.UNICODE)
# Control Pictures
# Range: 2400–243F
CONTROL_PICTURES_SYMBOLS = re.compile(u"[\u2400-\u243F]", re.UNICODE)
# Optical Character Recognition
# Range: 2440–245F
OCR = re.compile(u"[\u2440-\u245F]", re.UNICODE)

# Mathematical Symbols
# Arrows
# Range: 2190–21FF
ARROWS = re.compile(u"[\u2190-\u21FF]", re.UNICODE)
# Supplemental Arrows-A
# Range: 27F0–27FF
ARROWS_A = re.compile(u"[\u27F0-\u27FF]", re.UNICODE)
# Supplemental Arrows-B
# Range: 2900–297F
ARROWS_B = re.compile(u"[\u2900-\u297F]", re.UNICODE)
# Supplemental Arrows-C
# Range: 1F800–1F8FF
ARROWS_C = re.compile(u"[\U0001F800-\U0001F8FF]", re.UNICODE)
# Miscellaneous Symbols and Arrows
# Range: 2B00–2BFF
ARROWS_MISCELLANEOUS = re.compile(u"[\u2B00-\u2BFF]", re.UNICODE)
# Mathematical Operators
# Range: 2200–22FF
MATH_OPERATORS = re.compile(u"[\u2200-\u22FF]", re.UNICODE)
# Supplemental Mathematical Operators
# Range: 2A00–2AFF
SUPPLEMENTAL_MATH_OPERATORS = re.compile(u"[\u2A00-\u2AFF]", re.UNICODE)
# Miscellaneous Mathematical Symbols-A
# Range: 27C0–27EF
MATH_SYMBOLS_A = re.compile(u"[\u27C0-\u27EF]", re.UNICODE)
# Miscellaneous Mathematical Symbols-B
# Range: 2980–29FF
MATH_SYMBOLS_B = re.compile(u"[\u2980-\u29FF]", re.UNICODE)
# Geometric Shapes, 几何形状
# Range: 25A0–25FF
GEOMETRIC_SHAPES = re.compile(u"[\u25A0-\u25FF]", re.UNICODE)
# Box Drawing
# Range: 2500–257F
BOX_DRAWING = re.compile(u"[\u2500-\u257F]", re.UNICODE)
# Block Elements
# Range: 2580–259F
BLOCK_ELEMENTS = re.compile(u"[\u2580-\u259F]", re.UNICODE)
# Geometric Shapes Extended
# Range: 1F780–1F7FF
GEOMETRIC_SHAPES_EXTENDED = re.compile(u"[\U0001F780-\U0001F7FF]", re.UNICODE)


def check():
    start = int("1F780", 16)
    end = int("1F7FF", 16)
    for i in range(start, end + 1):
        char = chr(i)
        # print(char, hex(i), ord(char), i)
        if GEOMETRIC_SHAPES_EXTENDED.search(chr(i)):
            print("匹配成功", char)
            # pass
        else:
            print("匹配失败", char)
    print(len(range(start, end + 1)))

if __name__ == '__main__':
    check()
