# Files handling
'''
# Counting number of lines
fhand = open('mbox.txt')
count = 0
for chees in fhand:
    count += 1
print(count)
'''
fhand = open('mbox.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])