for _ in range(int(input())):
    is_even = True
    even = ''
    odd = ''
    for ele in input():
        if is_even:
            even += ele
        else:
            odd += ele
        is_even = not is_even
    print("{} {}".format(even, odd))
