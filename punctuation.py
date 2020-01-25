"""
unicode编码范围和正则表达式
参考网站：http://www.unicode.org/charts/
"""
import re


# Emoji & Pictographs
# Dingbats, 丁巴特
# Range: 2700–27BF
DINGBATS = re.compile(u"[\u2700–\u27BF]", re.UNICODE)


def check():
    start = int("2700", 16)
    end = int("27BF", 16)
    for i in range(start, end + 1):
        char = chr(i)
        print(char, hex(i), ord(char))


if __name__ == '__main__':
    check()
