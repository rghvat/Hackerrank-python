from itertools import product
n, mod = map(int, input().split())
l = list()
for _ in range(n):
    l.append(list(map(int, input().split()[1:])))

lst = []
for ele in product(*l):
    lst.append(sum([a**2 for a in ele])%mod)
print(max(lst))
