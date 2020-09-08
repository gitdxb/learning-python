import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://docs.python.org')

for line in fhand:
    print(line.decode().strip())