import re


def replace(m):
    if m.group(0) == '&& ':
        return 'and '
    if m.group(0) == '|| ':
        return 'or '

for _ in range(int(raw_input())):
    print re.sub('(?<= )(&&|\|\|) ', replace, raw_input())
