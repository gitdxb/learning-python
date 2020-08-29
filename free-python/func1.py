'''
def intro():
    print("Let's do some coding!")
    name = input("What's your name? ")
    print("Welcome " + name)

intro()
'''

def do_calculation():
    print('let\'s ' + command + ' some numbers')
    input1 = input('Number 1> ')
    input2 = input('Number 2> ')
    number1 = int(input1)
    number2 = int(input2)
    if command == 'add':
        result = number1 + number2
        operator = ' + '
    elif command == 'subtract':
        result = number1 - number2
        operator = ' - '
    output = str(result)
    print(input1 + operator + input2 + ' = ' + output)

finish = False
while finish == False:
    print('Hi I\'m Marvin, your personal bot!')
    command = input('How can I help? ')
    if command == 'add':
        do_calculation()
    elif command == 'subtract':
        do_calculation()
    if command == 'bye':
        finish = True