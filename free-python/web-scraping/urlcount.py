import urllib.request, urllib.parse, urllib.error

url = input('Enter URL: ')
if len(url) < 1: url = 'http://data.pr4e.org/romeo.txt'

fhand = urllib.request.urlopen(url)

mydict = {}
for line in fhand:
    words = line.decode().split()
    for word in words:
        mydict[word] = mydict.get(word, 0) + 1
print(mydict)