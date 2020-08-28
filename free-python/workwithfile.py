'''
# Searching through file
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From: '):
        print(line)
'''
'''
#Skipping
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From: '):
        continue
    print(line)
'''

'''

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za'in line:
       continue
    print(line)
'''

#Bad file name
while True:
    fhand = input('Enter a file: ')
    try:
        _fhand = open(fhand)
    except:
        print('No such file! Enter again! ', fhand)
        continue

    count = 0
    for _list in _fhand:
        if _list.startswith('Subject: '):
             count += 1
    print('There are',count,'subject lines in your file')

