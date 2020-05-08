#!/bin/python3
import os

# Complete the factorial function below.
def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1)*n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    result = factorial(n)
    fptr.write(str(result) + '\n')
    fptr.close()
