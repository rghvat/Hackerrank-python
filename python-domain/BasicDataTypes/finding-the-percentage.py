# https://www.hackerrank.com/challenges/finding-the-percentage/problem
students = dict()
for _ in range(int(input())):
    name, *line = input().split()
    scores = tuple(map(float, line))
    students[name] = scores
query_name = input().strip()
print("{:.2f}".format(sum(students[query_name])/len(students[query_name])))
