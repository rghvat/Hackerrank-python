no_students, rows = map(int, input().split(' '))
l = []
for _ in range(rows):
    l.append(list(map(float, input().split(' '))))
for ele in zip(*l):
    print(sum(ele)/len(ele))

