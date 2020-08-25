# Score grade
i = 1
while i > 0:
    i += 1
    get_score = input("Enter score \n")
    try:
        grade = float(get_score)
        if grade > 1.0:
            print("Score is limited to 1.0! Please enter again!")
        if grade >= 0.9 and grade <= 1.0:
            print("Your grade is: A")
        elif grade >= 0.8 and grade <= 1.0:
            print("Your grade is: B")
        elif grade >= 0.7 and grade <= 1.0:
            print("Your grade is: C")
        elif grade >= 0.6 and grade <= 1.0:
            print("Your grade is: D")
        elif grade < 0.6 and grade <= 1.0:
            print("Your grade is: F")
    except:
        print("Bad score")