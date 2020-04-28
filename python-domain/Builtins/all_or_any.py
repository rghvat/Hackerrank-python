input()
rows = list(map(int, input().split()))
print(all(map(lambda num:num>0,rows)) and \
        any(map(lambda num:str(num) == str(num)[::-1], rows)))
