import re
for _ in range(int(raw_input())):
    print 'YES' if re.match('[7-9]\d{9}$', raw_input()) is not None else 'NO'
