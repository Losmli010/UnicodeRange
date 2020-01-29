"""
unicode编码范围和正则表达式
参考网站：http://www.unicode.org/charts/
"""
import re


# European Scripts
# Armenian, 亚美尼亚
# Range: 0530–058F
ARMENIAN_LETTERS = re.compile(u"[\u0531-\u0588]", re.UNICODE)
ARMENIAN_PUNCTUATION = re.compile(u"[\u0589-\u058A]", re.UNICODE)
ARMENIAN_SYMBOLS = re.compile(u"[\u058D-\u058F]", re.UNICODE)

def check():
    start = int("0530", 16)
    end = int("058F", 16)
    for i in range(start, end + 1):
        char = chr(i)
        # print(char, hex(i), ord(char), i)
        if ARMENIAN_SYMBOLS.search(char):
            print("匹配成功", char)
            # pass
        # else:
        #     print("匹配失败", char)
    print(len(range(start, end + 1)))

if __name__ == '__main__':
    check()
