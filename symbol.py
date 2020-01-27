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

def check():
    start = int("1D100", 16)
    end = int("1D24F", 16)
    for i in range(start, end + 1):
        char = chr(i)
        # print(char, hex(i), ord(char), i)
        if SYMBOLS.search(chr(i)):
            print("匹配成功", char)
            # pass
        else:
            print("匹配失败", char)
    print(len(range(start, end + 1)))

if __name__ == '__main__':
    check()
