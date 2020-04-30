from collections import Counter

input()
shoes = Counter(map(int, input().split(' ')))
amount = 0
for _ in range(int(input())):
    a, b = map(int, input().split(' '))
    quantity = shoes.get(a, 0)
    if quantity >0:
        shoes[a] = quantity -1
        amount += b
print(amount)
