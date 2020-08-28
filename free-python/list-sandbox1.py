'''
x = [1,2,3,'egg', 99, True]

# find position of a list item
for y in range(len(x)):
    if x[y] == 'egg':
        print(y)

# Check if a list item exists
found = False
for i in x:
    if i == 'egg':
        found = True
print(found)
'''
x = [1,2,3,4,5,19,72]
biggest = None
for i in x:
    if biggest is None or biggest < i:
        biggest = i

print('Biggest Number is',biggest)