from collections import OrderedDict


product = OrderedDict()
n = int(raw_input())
for _ in range(n):
    line = raw_input().split()
    item_name = ' '.join(line[:-1])
    net_price = int(line[-1])
    product.setdefault(item_name, default=0)
    product[item_name] += net_price
for name, price in product.items():
    print name, price
