## Guessing Game
print("Think of a number between 1 and 100")

def guess():
    max = 100
    min = 0
    count = 0
    finish = False
    while finish == False:
        middle = int((max + min)/2)
        answer = input("Is your number [H]igher, [L]ower or the [S]ame as {} ".format(middle)).upper()
        count += 1
        for guess in answer:
            if answer == "H":
              min = middle
            elif answer == "L":
              max = middle
            else:
              print("Your number is {}, it took me".format(middle),count," guess")
              finish = True

guess()