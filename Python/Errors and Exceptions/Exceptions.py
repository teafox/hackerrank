t = int(raw_input())


class MyException(Exception):
    pass

for _ in range(t):
    try:
        a, b = map(int, raw_input().split())
        print a / b
    except (ZeroDivisionError, ValueError) as e:
        print 'Error Code:', e
    except TypeError as e:
        raise MyException(e)
    else:
        print "All good"
    finally:
        pass
