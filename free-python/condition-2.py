i = 1
while i > 0:
    i += 1
    get_ready = input("Press 'OK' to start! ")
    _ready = get_ready.lower()
    if _ready == 'ok':
        get_num = input("Enter number: ")
        x = int(get_num)
        print("You entered", x)
        if x < 5:
            print("Smaller than 5")
        elif x < 10:
            print("Smaller than 10")
        elif x == 10:
            print("equal 10")
        else:
            print("Bigger than 10")