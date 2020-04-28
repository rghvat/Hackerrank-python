members_per_group = int(input())
array = list(map(int, input().split(' ')))
single = set()
mulitple = set()
for ele in array:
    if ele in mulitple:
        continue
    if ele in single:
        single.discard(ele)
        mulitple.add(ele)
    else:
        single.add(ele)
print(*single)
