set_a = set(map(int, input().split()))
flag = 'True'
for _ in range(int(input())):
    set_b = set(map(int, input().split()))
    if not set_a.issuperset(set_b):
        flag = 'False'
        break
print(flag)
