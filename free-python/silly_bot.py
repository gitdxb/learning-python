# Write your code here :-)
print('Hello, I\'m Polako. Your virtual bot!')
uname = input('Please enter your username: ')
print('Awesome',uname,'! Access granted!')
print('How can I help you?')
print('I can do only 2 things so far, add or subtract some numbers')
command = input('Choose "1" to add, "2" to subtract: ')
print('Enter numbers, type "done" when complete')
if command == '1':
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
