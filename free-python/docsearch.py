# Write your code here :-)
import re
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if re.search('^From: .+@', line):
        print(line)