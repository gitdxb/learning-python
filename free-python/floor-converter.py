# Convert elevator floors
i = 1
while i > 0:
    i += 1
    x = input('European floor: ')
    try:
        y = int(x) + 1
    except:
        y = -1

    if y >= 0:
        print('US floor: ',y)
    else:
        print("enter number")