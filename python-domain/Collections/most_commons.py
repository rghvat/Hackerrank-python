#!/bin/python3
from collections import Counter


if __name__ == '__main__':
    s = Counter(sorted(input()))
    for ele in s.most_common(3):
        print("{} {}".format(*ele))

