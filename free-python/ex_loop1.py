mylist = []

while True:
    num = input('Enter a number: ')
    if num == 'done':
        print(sum(mylist), len(mylist), sum(mylist)/len(mylist))
        break
    try:
        mylist.append(int(num))
    except:
        print('bad data')





