# Write your code here :-)
import urllib.request

hand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in hand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print(counts)
