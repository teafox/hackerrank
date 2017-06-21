a = raw_input()
A = set(map(int, raw_input().split()))
N = int(raw_input())

for _ in range(N):
    operation, n = raw_input().split()
    S = set(map(int, raw_input().split()))
    eval('A.' + operation + '(' + 'S' + ')')
print sum(A)
