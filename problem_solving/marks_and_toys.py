#!/bin/python3
# https://www.hackerrank.com/challenges/mark-and-toys/problem
import os

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    num = 0
    total = 0
    for ele in prices:
        if total + ele <= k:
            num += 1
            total += ele
    return num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    fptr.write(str(result) + '\n')
    fptr.close()

