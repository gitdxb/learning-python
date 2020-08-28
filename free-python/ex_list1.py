# romeo.txt
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    lst.append(line.split())
lst = list(set(lst[0]+lst[1]+lst[2]+lst[3]))
lst.sort()
print(lst)