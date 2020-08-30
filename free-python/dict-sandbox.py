'''
word = 'brontosaurus'
dct = dict()
for i in word:
    if i not in dct:
        dct[i] = 1
    else:
        dct[i] = dct[i] + 1
print(dct)
'''
# end comment
# Better solution
word = 'brontosaurus'
dct = dict()
for i in word:
    dct[i] = dct.get(i,0) + 1
print(dct)