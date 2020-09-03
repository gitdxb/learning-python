import re
lst = []
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9.]+)', line)
    if len(x) > 0:
        lst.append(' '.join(x))

# print(lst)
total = 0
count = 0
for i in lst:
    count += 1
    total += int(i)
print('Average: ', int(total/count))