#!/bin/python3

import math
import os
import random
import re
import sys
#https://www.hackerrank.com/challenges/capitalize/problem
# Complete the solve function below.
def solve(s):
    names = s.split(' ')
    name = ''
    for ele in names:
        name += ele.capitalize()+' '
    return name[:-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

