students = []
total = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    students.append([name, score])
    total.append(score)
total = list(set(total))
total.sort()
lowest = [s[0] for s in students if s[1] == total[1]]
lowest.sort()
for l in lowest:
    print l
