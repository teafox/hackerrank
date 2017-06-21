T = int(raw_input())
for _ in range(T):
    a = raw_input()
    A = set(raw_input().split())
    b = raw_input()
    B = set(raw_input().split())
    print A <= B
