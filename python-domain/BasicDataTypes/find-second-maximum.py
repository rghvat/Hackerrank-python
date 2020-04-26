## https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    first = max(lst)
    second = min(lst)
    for ele in lst:
        if ele<first and ele>second:
            second = ele
    print(second)



