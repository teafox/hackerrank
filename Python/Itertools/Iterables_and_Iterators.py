from itertools import combinations

n = int(raw_input())
s = raw_input().replace(' ', '')
k = int(raw_input())

id = [i+1 for i in range(n) if s[i] == 'a']
c = list(combinations(range(1, n+1), k))

a_sum = 0
for el in c:
    if set(el) & set(id):
        a_sum += 1
print a_sum / float(len(c))
