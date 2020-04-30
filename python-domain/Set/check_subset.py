for _ in range(int(input())):
    input()
    set_a = set(map(int, input().split()))
    input()
    set_b = set(map(int, input().split()))
    if set_a.issubset(set_b):
        print("True")
    else:
        print("False")
