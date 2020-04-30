from itertools import permutations

st, m = input().split()
m = int(m)
for ele in permutations(sorted(st), m):
    print("".join(ele))
