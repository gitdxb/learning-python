# Write your code here :-)
print('Hello, I\'m Marvin. Your virtual bot!')
uname = input('Please enter your username: ')
print('Awesome',uname,'! Access granted!')
finished = False
while finished == False:
    print('\nHow can I help you?')
    print('I can do only 3 things for you so far')
    command = input('Choose: \n 1. add\n 2. subtract\n 3. count average\n 4. quit\n ')
    if command == '1':
        print('Enter numbers, type "done" when complete')
        total = 0
        while True:
            num = input('Enter a number: ')
            if num == 'done': break
            try:
               total = total + int(num)
            except:
                print('Silly, it\'s not a number!')
                continue
        print('Your sum is',total)
    elif command == '2':
        # fail logic
        total = 0
        while True:
            num = input('Enter a number: ')
            if num == 'done': break
            total = int(num) - total
        print('Your total is',total)
    elif command == '3':
        num = int(input('How many numbers? '))
        count = 0
        total = 0
        for i in range(num):
            get_num = input('Enter number ' + str(i) + ': ')
            total = total + int(get_num)
            count += 1
        print('Average is:',total/count)
    elif command == '4':
        finished = True