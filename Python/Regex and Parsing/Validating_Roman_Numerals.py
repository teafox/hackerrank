import re

p = re.compile('^M{0,3}(CM)?C?D?C{0,3}(XC)?X?L?X{0,3}(IX)?I?V?I{0,3}$')
print p.match(raw_input()) is not None
