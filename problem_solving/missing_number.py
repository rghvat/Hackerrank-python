#!/bin/python3
# https://www.hackerrank.com/challenges/missing-numbers/problem
import os

# Complete the missingNumbers function below.
def create_freq(arr):
    freq = dict()
    for ele in arr:
        freq[ele] = freq.get(ele, 0) + 1
    return freq

def missingNumbers(arr, brr):
    first = create_freq(arr)
    second = create_freq(brr)
    missing = []
    for ele in second:
        if ele not in first:
            missing.append(ele)
        elif second[ele] != first[ele]:
            missing.append(ele)
    missing.sort()
    return missing

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    m = int(input())
    brr = list(map(int, input().rstrip().split()))
    result = missingNumbers(arr, brr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

