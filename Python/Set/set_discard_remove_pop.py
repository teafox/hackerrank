n = int(raw_input())
s = set(map(int, raw_input().split()))
N = int(raw_input())

for _ in range(N):
    c = raw_input().split()
    command = c[0]
    args = c[1:]
    if command == "pop":
        s.pop()
    else:
        eval(''.join(['s.', command, '(', ','.join(args), ')']))
print sum(s)
