# cal total and average


def do_cal():
    get_num = int(input('How many numbers? '))
    total = 0
    count = 0
    for num in range(get_num):
        input_num = int(input())
        total = total + input_num
        count += 1
    if command == 'total':
       print('Total is',total)
    elif command == 'average':
        print('Average is', total/count)

finish = False
while finish == False:
    command = input('How can I help? ')
    if command == 'total':
        do_cal()
    elif command == 'average':
        do_cal()
    elif command == 'quit':
        finish = True

