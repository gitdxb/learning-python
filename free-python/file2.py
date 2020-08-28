# Use mbox.txt as the file name
# This program print each line in upper case
fname = input("Enter file name: ")
fh = open(fname)
for each_line in fh:
    up_case = each_line.upper().rstrip()
    print(up_case)