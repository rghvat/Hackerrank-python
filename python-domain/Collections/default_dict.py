from collections import defaultdict

rows, items = map(int, input().split(' '))
store = defaultdict(list)
for i in range(1, rows+1):
    store[input()].append(i)
for i in range(items):
    a = input()
    if len(store[a]) != 0:
        print(*store[a], sep=' ')
    else:
        print('-1')

