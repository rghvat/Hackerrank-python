# https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
    lst = list()
    for _ in range(N):
        inp = input()
        if 'insert' in inp:
            inp, a, b = inp.split()
            a = int(a)
            b = int(b)
            lst.insert(a, b)
        elif 'print' in inp:
            print(lst)
        elif 'pop' in inp:
            lst.pop()
        elif 'reverse' in inp:
            lst.reverse()
        elif 'append' in inp:
            inp, a = inp.split()
            a = int(a)
            lst.append(a)
        elif 'remove' in inp:
            inp, a = inp.split()
            a = int(a)
            lst.remove(a)
        elif 'sort' in inp:
            lst.sort()
        

