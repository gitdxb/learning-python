count = 0
total = 0
while True:
    get_num = input('Enter a number: ')
    if get_num == 'done':
        break
    try:
       num = float(get_num)
    except:
        print('Invalid input')
        continue
    count = count + 1
    total = total + num

print(count, total, total/count)