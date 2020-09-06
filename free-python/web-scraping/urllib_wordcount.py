import urllib.request, urllib.parse, urllib.error

url = input('Enter URL: ')
if len(url) < 1: url = 'http://data.pr4e.org/mbox-short.txt'
hand = urllib.request.urlopen(url).read()
hand  = hand.decode()
print('This is the first 100 characters:\n',hand[:100])
print('Total characters: ', len(hand))