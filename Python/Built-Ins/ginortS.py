def new_order(x):
    if ord('z') >= ord(x) >= ord('a'):
        return ord(x)
    if ord('Z') >= ord(x) >= ord('A'):
        return ord(x) + 100
    if ord('9') >= ord(x) >= ord('0'):
        return ord(x) + 210 if not ord(x) % 2 else ord(x) + 200

print reduce(lambda x, y: x + y, sorted(raw_input(), key=new_order))

