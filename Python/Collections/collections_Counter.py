from collections import Counter

x = int(raw_input())
shoes = map(int, raw_input().split())
shoes_count = Counter(shoes)
customers = int(raw_input())

profit = 0
for _ in range(customers):
    size, price = map(int, raw_input().split())
    if shoes_count[size]:
        shoes_count[size] -= 1
        profit += price
print profit
