# Method 1: Sorting key in dict:
print('Sorting with keys in dictionary: \n')
d = {'a':10,'c':22,'b':1}
t = sorted(d.items())
print('Before: ',t)

for length,word in t:
    print('After: ',length,word)

# Method 2: Sorting with value
print('Sorting with value instead of key in dictionary:\n')
x = {'a':10,'c':22,'b':1}
tnp = list()
for k,v in x.items():
    tnp.append((v,k))
print('Before: ',tnp)

tnp = sorted(tnp, reverse=True)
# tnp.sort(reverse=True)
print('After: ',tnp)