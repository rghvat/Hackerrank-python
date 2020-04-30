from itertools import combinations_with_replacement

st, l = input().split()
l = int(l)
for ele in combinations_with_replacement(sorted(st), l):
    print("".join(ele))
