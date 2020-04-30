from collections import namedtuple
rows = int(input())
students = []
record = namedtuple('student', input().split())
for _ in range(rows):
    students.append(record(*input().split()))
print("{:.2f}".format(sum(int(ele.MARKS) for ele in students)/len(students)))
