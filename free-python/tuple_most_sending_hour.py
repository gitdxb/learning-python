name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hr = dict()
lst = []
for line in handle:
    if line.startswith('From '):
        line = line.split()
        hours = line[5].split(':')[0]
        lst.append(hours)
for hour in lst:
    hr[hour] = hr.get(hour, 0) + 1
for key,val in sorted(hr.items()):
    print(key, val)