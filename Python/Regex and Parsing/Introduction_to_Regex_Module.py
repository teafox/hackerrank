import re

for _ in range(int(raw_input())):
    print re.match('(-|\+)?\d*\.\d+$', raw_input()) is not None
