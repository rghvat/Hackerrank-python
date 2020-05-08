if __name__ == '__main__':
    q1, q2, q3 = 0, 0, 0
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    upper = []
    lower = []
    # calculating q2
    if n%2 == 1:
        q2 = arr[n//2]
        lower = arr[:n//2]
        upper = arr[n//2 + 1: ]
    else:
        q2 = (arr[n//2] + arr[n//2 - 1]) // 2
        lower = arr[:n//2]
        upper = arr[n//2: ]

    # calculating q1
    if len(lower)%2 == 1:
        q1 = lower[len(lower)//2]
    else:
        q1 = (lower[len(lower)//2] + lower[len(lower)//2 -1]) // 2
    
    # calculating q3
    if len(upper)%2 == 1:
        q3 = upper[len(upper) // 2]
    else:
        q3 = (upper[len(upper) // 2] + upper[len(upper) // 2 - 1]) // 2

    print(q1, q2, q3, sep='\n')
