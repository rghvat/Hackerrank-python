#!/bin/python3
# https://www.hackerrank.com/challenges/30-binary-numbers/problem
import re

if __name__ == '__main__':
    num = int(input())
    num = bin(num)[2:]
    consecutive_ones = 0
    for match in re.findall(r'1+', num):
        consecutive_ones = max(consecutive_ones, len(match))
    print(consecutive_ones)
