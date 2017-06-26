t = int(raw_input())

for _ in range(t):
    try:
        a, b = map(int, raw_input().split())
        print a / b
    except (ZeroDivisionError, ValueError) as e:
        print 'Error Code:', e
