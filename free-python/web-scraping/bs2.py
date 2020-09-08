import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL: ')
if len(url) < 1: url = 'http://www.dr-chuck.com/page1.htm'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all anchor tags
tags = soup('a')
for tag in tags:
    #print(tag)
    print(tag.get('href', None))