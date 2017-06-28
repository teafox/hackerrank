import re

m = re.search("([0-9a-z-A-Z])\\1", raw_input())
print m.group(1) if m else -1
