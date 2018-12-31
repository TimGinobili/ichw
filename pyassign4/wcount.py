#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Niuxiao"
__pkuid__  = "1800011701"
__email__  = "1800011701@pku.edu.cn"
"""

import sys
import urllib.request
from collections import Counter


def wcount(lines, topn=10):
    """count words from lines of text string,
    then sort by their counts in reverse order,
    output the topn (word count), each in one line.
    """
    for i in [',', '.', ':', ';', '"', "'", '?', '!', '(', ')', '/', "-", '_', '--', '/r', '/n', "'s", "'re", "'ll"]:
        lines = lines.replace(i, " ")
    lines = lines.lower()
    words = lines.split()
    ans = Counter(words).most_common(topn)
    for (word, num) in ans:
        print(word + '\t' + str(num))
    pass

def main():
    """main函数，运行计数函数，若出错则捕获几种错误并打印
    """
    try:
        doc = urllib.request.urlopen(sys.argv[1])
        lines = doc.read().decode()
        doc.close()
        if len(sys.argv) <= 2:
            wcount(lines, topn=10)
        else:
            topn = int(sys.argv[2])
            wcount(lines, topn)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('url: URL of the txt file to analyze ')
        print('topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    else:
       main()
