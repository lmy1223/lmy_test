# !/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import print_function
import sys
import collections as coll


# lower
def get_word_to_list(file_name):
    word_list = []
    with open(file_name, 'r') as f:
        for line in f:
            lines = line.lower()
            word_list.append(lines.strip('\n'))
    return word_list


def get_argument_word(word_list):
    if len(sys.argv) == 2:
        rack = sys.argv[1]
        lower_word = rack.lower()
        c = coll.Counter(lower_word)
        return [word for word in word_list if not (coll.Counter(word) - c)]
    else:
        print('Usage: scrabble_change.py ABC')
        sys.exit()


def get_scores(words):
    word_dic = coll.defaultdict(int)
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
              "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
              "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
              "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
              "x": 8, "z": 10}
    for word in words:
        for s in word:
            word_dic[word] += scores[s]
    return word_dic


# def get_scores(*args):
#     dict_set1 = {}  
#     if 'key' not in dict_set1:  
#         dict_set1['key'] = set()  
#     scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
#               "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
#               "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
#               "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
#               "x": 8, "z": 10}
#     for word in args:
#         for s in word:
#             total_scores += scores[s]
#     return total_scores, word


def main():
    word_list = get_word_to_list('E:\\56\python_code\\class\\c4\\sowpods.txt')
    valid_words = get_argument_word(word_list)
    d = get_scores(valid_words)
    for key, val in sorted(d.items(), key=lambda item: item[1], reverse=True):
        print(val, key)


if __name__ == '__main__':
    main()
