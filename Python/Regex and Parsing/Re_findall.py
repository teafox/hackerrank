import re

v = 'AEIOUaeiou'
c = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
s = 'match a single character not present in the list below'
m = re.findall('(?<=[%s])([%s]{2,})[%s]' % (c, v, c), s)
print '\n'.join(m or ['-1'])
