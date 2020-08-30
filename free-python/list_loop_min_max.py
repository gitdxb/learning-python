def max_min():
    lst = []
    while True:
        get_num = input('Enter a number: ')
        if get_num == 'done' : break
        try:
            num = int(get_num)
        except:
            print('It is not a number, try again')
            continue
        lst.append(num)
    print('Maximum is ' + str(max(lst)) + '\n' + 'Minimum is ' + str(min(lst)))
max_min()