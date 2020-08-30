# Search and print email list
'''
fhand = open('mbox-short.txt')
count = 0
for lines in fhand:
    lines = lines.rstrip()
    if lines.startswith('From: '):
        count += 1
        line = lines.split()
        print(line[1])
print('There were ' + str(count) + ' lines in the file with From as the first word')
'''
# End of above
str = 'From stephen.marquard@gmail.com Sat Jan 5 09:25:30 2008'
spstr = str.split()
_date = spstr[2] +' '+ spstr[3] +' '+ spstr[4] +' '+ spstr[-1]
print(_date)