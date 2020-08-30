#Who send the most email
fhandle = open('mbox-short.txt')
sender_lst = []
most_sender = {}
for line in fhandle:
    if line.startswith('From: '):
        line = line.split()
        sender_lst.append(line[1])
# print(_line)
for email in sender_lst:
    most_sender[email] = most_sender.get(email, 0) + 1
#print(most_sender)
bigcount = None
bigemail = None
for email,count in most_sender.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigemail = email
print(bigemail, bigcount)
