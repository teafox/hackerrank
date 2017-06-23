from collections import namedtuple


n = int(raw_input())
Student = namedtuple('Students', raw_input())
total = 0
for _ in range(n):
    total += int(Student(*raw_input().split()).MARKS)
print total/float(n)
