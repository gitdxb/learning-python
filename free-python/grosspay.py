# Gross pay calculation
i = 1
while i > 0:
    i += 1
    get_hours = input('Hours: ')
    get_rate = input('Pay rate: ')
    try:
        gh = float(get_hours)
        gr = float(get_rate)

    except:
        print("Error, Please only enter numeric input!")
        break

    if gh > 40:
            pay = 40.0 * gr
            ot = (gh - 40.0)* 15
            gross_pay = pay + ot
            print("You got overtime pay! Your pay is: ",gross_pay)
    else:
            gross_pay = gh * gr
            print("Your gross pay is:",gross_pay)
