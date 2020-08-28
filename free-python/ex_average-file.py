'''
1. Prompt a file name 'mbox-short.txt'
2. Open and read
3. Look for "X-DSPAM-Confidence: 0.8475"
4. Count the lines
5. Extract the floating point
6. Compute average
'''
fhandle = input('Enter a file: ')
fread = open(fhandle)
count = 0
for i in fread:
    i = i.rstrip()
    if i.startswith('X-DSPAM-Confidence:'):
        count += 1
        print(i)
print(count)
