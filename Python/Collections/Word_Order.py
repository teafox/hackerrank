from collections import OrderedDict


n = int(raw_input())
words = OrderedDict()
for _ in range(n):
    new = raw_input()
    if new not in words:
        words[new] = 0
        # words.setdefault(new, 0)
    words[new] += 1

print len(words)
print ' '.join(map(str, words.values()))
