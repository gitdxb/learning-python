'''
1. Prompt a file name 'mbox-short.txt'
2. Open and read
3. Look for "X-DSPAM-Confidence: 0.8475"
4. Count the lines
5. Extract the floating point
6. Compute average
'''
while True:
    fhandle = input('Enter a file: ')
    try:
        fread = open(fhandle)
    except:
        print('Please input valid file ')
        continue
    count = 0
    total = 0
    #ls = []
    for i in fread:
        i = i.rstrip()
        if i.startswith('X-DSPAM-Confidence:'):
            count += 1
            for item in i:
                item = i.find(':')
                get_float = float(i[item+1:])
            total = total + get_float
    print('Average spam confidence:',total/count)