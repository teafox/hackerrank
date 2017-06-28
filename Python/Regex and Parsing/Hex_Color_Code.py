import re

p = re.compile('[\s:](#[0-9a-f]{6}|#[0-9a-f]{3})', re.I)
for _ in range(int(raw_input())):
    for m in p.findall(raw_input()):
        if m:
            print m
