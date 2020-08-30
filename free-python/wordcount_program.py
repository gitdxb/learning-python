# Word count program
name = input('Enter a file...')
fhand = open(name)

word_dict = {}
for line in fhand:
    words = line.split()
    for word in words:
        word_dict[word] = word_dict.get(word,0) + 1
#print(word_dict)

bigword = None
bigcount = None
for word,count in word_dict.items():
    if bigcount is None or bigcount < count:
        bigcount = count
        bigword = word
print(bigword, bigcount)