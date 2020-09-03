# Search for lines that start with 'Details: rev='
# followed by numbers and '.'
# Then print the number if it is greater than zero
# Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^Details: .*rev=([0-9.]+)', line)
    if len(x) > 0:
        print(x)