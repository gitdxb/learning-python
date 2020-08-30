'''
def chop(s):
    del s[0]
    del s[-1]
    #return None
letters = ['a','b','c']
rest = chop(letters)
print(rest)
'''
'''
# End of comment
def middle(s):
    return s[1:-1]

letters = ['z','b','c','d']
rest = middle(letters)
print(rest)
'''
# End of comment
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    #print('Debug: ',words)
    #if len(words) == 0: continue
    if len(words) == 0 or words[0] != 'From': continue
    count += 1
    print(words[2])
print(count)