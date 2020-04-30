from collections import OrderedDict

menu = OrderedDict()
n = int(input())
for _ in range(n):
    a = input().split()
    price = a.pop()
    name = ' '.join(a)
    menu[name] = menu.get(name, 0)+int(price)
for ele in menu:
    print("{} {}".format(ele, menu[ele]))
