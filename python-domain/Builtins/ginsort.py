# https://www.hackerrank.com/challenges/ginorts/problem
import string
index = string.ascii_lowercase+string.ascii_uppercase+'13579'+'02468'
string = input()
print(''.join(sorted(string, key = lambda x: index.find(x) )))

