n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    inp = input()
    if 'pop' in inp:
        s.pop()
    elif 'remove' in inp:
        inp, ele = inp.split(' ')
        ele = int(ele)
        s.remove(ele)
    elif 'discard' in inp:
        inp, ele = inp.split(' ')
        ele = int(ele)
        s.discard(ele)
print(sum(s))
