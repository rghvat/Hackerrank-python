from itertools import combinations

st, m = input().split()
m = int(m)
for i in range(1, m+1):
    for ele in combinations(sorted(st), i):
        print("".join(ele))
