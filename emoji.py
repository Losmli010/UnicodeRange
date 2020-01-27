"""
unicode编码范围和正则表达式
参考网站：http://www.unicode.org/charts/
"""
import re


# Emoji & Pictographs
# Dingbats, 丁巴特
# Range: 2700–27BF
DINGBATS = re.compile(u"[\u2700-\u27BF]", re.UNICODE)
# Ornamental Dingbats
# Range: 1F650–1F67F
ORNAMENTAL_DINGBATS = re.compile(u"[\U0001F650-\U0001F67F]", re.UNICODE)
# Emoticons, 表情符号
# Range: 1F600–1F64F
EMOTICONS = re.compile(u"[\U0001F600-\U0001F64F]", re.UNICODE)
# Miscellaneous Symbols, 杂项符号
# Range: 2600–26FF
MISCELLANEOUS_SYMBOLS = re.compile(u"[\u2600-\u26FF]", re.UNICODE)
# Miscellaneous Symbols and Pictographs, 象形文字
# Range: 1F300–1F5FF
PICTOGRAPHS = re.compile(u"[\U0001F300-\U0001F5FF]", re.UNICODE)
# Supplemental Symbols and Pictographs
# Range: 1F900–1F9FF
SUPPLEMENTAL_PICTOGRAPHS = re.compile(u"[\U0001F900-\U0001F9FF]", re.UNICODE)
# Symbols and Pictographs Extended-A
# Range: 1FA70–1FAFF
SYMBOLS_PICTOGRAPHS = re.compile(u"[\U0001FA70-\U0001FAFF]", re.UNICODE)
# Transport and Map Symbols
# Range: 1F680–1F6FF
TRANSOORT_MAP = re.compile(u"[\U0001F680-\U0001F6FF]", re.UNICODE)
# 汇总
EMOJI = re.compile(u"["
                   "\u2600-\u26FF"                # Miscellaneous Symbols, 杂项符号
                   "\u2700-\u27BF"                # Dingbats, 丁巴特
                   u"\U0001F300-\U0001F5FF"       # Miscellaneous Symbols and Pictographs, 象形文字
                   u"\U0001F600-\U0001F64F"       # Emoticons, 表情符号
                   u"\U0001F650-\U0001F67F"       # Ornamental Dingbats
                   u"\U0001F680-\U0001F6FF"       # Transport and Map Symbols
                   u"\U0001F900-\U0001F9FF"       # Supplemental Symbols and Pictographs
                   u"\U0001FA70-\U0001FAFF"       # Symbols and Pictographs Extended-A
                   u"]", re.UNICODE)

# Other Symbols
# Alchemical Symbols, 炼金术符号
# Range: 1F700–1F77F
ALCHEMICAL_SYMBOLS = re.compile(u"[\U0001F700-\U0001F77F]", re.UNICODE)
# Ancient Symbols, 古代符号
# Range: 10190–101CF
ANCIENT_SYMBOLS = re.compile(u"[\U00010190-\U000101CF]", re.UNICODE)
# Currency Symbols, 货币符号
# Range: 20A0–20CF

# Game Symbols
# Chess Symbols
# Range: 1FA00–1FA6F
CHESS_SYMBOLS = re.compile(u"[\U0001FA00-\U0001FA6F]", re.UNICODE)
# Domino Tiles, 多米诺瓷砖
# Range: 1F030–1F09F
DOMINO_TILES = re.compile(u"[\U0001F030-\U0001F09F]", re.UNICODE)
# Mahjong Tiles, 麻将牌
# Range: 1F000–1F02F
MAHJONG_TILES = re.compile(u"[\U0001F000-\U0001F02F]", re.UNICODE)
# Playing Cards, 扑克牌
# Range: 1F0A0–1F0FF
PLAYING_CARDS = re.compile(u"[\U0001F0A0-\U0001F0FF]", re.UNICODE)
# Miscellaneous Symbols and Arrows, 箭头
# Range: 2B00–2BFF
ARROWS = re.compile(u"[\u2B00-\u2BFF]", re.UNICODE)
# Yijing Hexagram Symbols, 易经六卦符号
# Range: 4DC0–4DFF
YIJING_HEXAGRAM = re.compile(u"[\u4DC0-\u4DFF]", re.UNICODE)
# Tai Xuan Jing Symbols, 太玄经符号
# Range: 1D300–1D35F
TAI_XUAN_JING = re.compile(u"[\U0001D300-\U0001D35F]", re.UNICODE)

# Specials
# Tags
# Range: E0000–E007F
TAGS = re.compile(u"[\U000E0000-\U000E007F]", re.UNICODE)


def check():
    start = int("E0000", 16)
    end = int("E007F", 16)
    for i in range(start, end + 1):
        char = chr(i)
        # print(char, hex(i), ord(char), i)
        if TAGS.search(char):
            print("匹配成功", char)
        else:
            print("匹配失败", char)
    print(len(range(start, end + 1)))

if __name__ == '__main__':
    check()
