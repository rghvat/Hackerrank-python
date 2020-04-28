n, m = map(int, input().split())
array = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
happiness = 0
for ele in array:
    if ele in set_a:
        happiness += 1
    if ele in set_b:
        happiness -= 1
print(happiness)

