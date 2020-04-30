input()
set_a = set(map(int, input().split()))
for _ in range(int(input())):
    command, arg = input().split()
    set_b = set(map(int, input().split()))
    getattr(set_a, command)(set_b)
print(sum(set_a))
