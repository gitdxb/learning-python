'''
Exercise 2: Change your socket program so that it counts the number of characters
it has received and stops displaying any text after it has shown 3000 characters.
The program should retrieve the entire docu-ment and count the total number of
characters and display the count of the number of characters at the end of the document.
'''
# http://data.pr4e.org/romeo.txt
import socket

url = input('Enter URL: ')
if len(url) < 1: url = 'http://data.pr4e.org/romeo.txt'
host = url.split('/')[2]

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
cmd = cmd.encode()
mysock.send(cmd)

received = b""
while True:
        data = mysock.recv(512)
        if len(data) < 1:break
        received += data

received = received.decode()
#print('Here are the characters: ', received)
print('printed words: ', received[:250])
print(len(received), 'characters copied')

mysock.close()



