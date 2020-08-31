# Write your code here :-)
'''
d = dict()
d['a'] = 2
d['b'] = 3
tups = d.items()
print(tups)
'''
# end
#Counting the longest word and shortest
txt = 'but soft light in yonder window breaks'
words = txt.split()
lst = list()
for word in words:
    lst.append((len(word),word))

lst.sort(reverse=True)

res = list()
for length, word in lst :
    res.append(word)
print(res)
print('Longest word: ', res[0])
print('Shortest word: ', res[-1])

