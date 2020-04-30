from itertools import  combinations

input()
arr = list(input().split())
k = int(input())
all_combination = list(combinations(arr, k))
desired = 0
for ele in all_combination:
    if 'a' in ele:
        desired += 1
print(desired/len(all_combination))
