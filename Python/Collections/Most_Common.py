from collections import Counter

s = 'qwertyuiopasdfghjklzxcvbnm'
for key, value in sorted(sorted(Counter(s).most_common(3)), key=lambda x: x[1], reverse=True):
    print key, value
