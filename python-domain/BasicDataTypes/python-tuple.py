# https://www.hackerrank.com/challenges/python-tuples/problem
if __name__ == '__main__':
    n = int(input())
    integer = tuple(map(int, input().split()))
    print("{}".format(hash(integer)))
