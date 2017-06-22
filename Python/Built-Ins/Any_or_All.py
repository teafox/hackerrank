N = int(raw_input())
A = map(int, raw_input().split())
print all(map(lambda x: x > 0, A)) and any(map(lambda x: str(x) == str(x)[::-1], A))
