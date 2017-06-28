import re

for line in re.split('\.|,', raw_input()):
    if line.isdigit():
        print line
