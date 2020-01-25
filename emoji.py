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
                   "\u2600-\u26FF"
                   "\u2700-\u27BF"
                   u"\U0001F300-\U0001F5FF"
                   u"\U0001F600-\U0001F64F"
                   u"\U0001F650-\U0001F67F"
                   u"\U0001F680-\U0001F6FF"
                   u"\U0001F900-\U0001F9FF"
                   u"\U0001FA70-\U0001FAFF"
                   u"]", re.UNICODE)


def check():
    start = int("1F900", 16)
    end = int("1FAFF", 16)
    for i in range(start, end + 1):
        char = chr(i)
        # print(char, hex(i), ord(char), i)
        if EMOJI.search(chr(i)):
            # print("匹配成功", char)
            pass
        else:
            print("匹配失败", char)
    print(len(range(start, end + 1)))

if __name__ == '__main__':
    check()
