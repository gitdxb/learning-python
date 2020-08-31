try:
    with open('highscore.txt','r') as f:
        highscore = f.read()
        highscore = int(highscore)
        print('Highest score: ',highscore)
except FileNotFoundError:
    print('Creating a new highscore.txt')
    f = open('highscore.txt','w')
    f.write('0')
    f.close()
    highscore = 0

finish = False
while finish == False:
    score = 0

    print('Welome to the Maths Quiz')
    print('Can you answer three questions and score maximum points?')
# Q1
    print('\nQ1: What is the product of 2x2x2?')
    x = int(input('Your answer :>> '))

    if x == 8:
        print('Correct!')
        score += 1
        print('Your score is ', score)
    else:
        print('Incorrect, try again!')
        print('Your score is ', score)

# Q2
    print('\nWhat is 1 + 1?')
    x2 = int(input('Your answer: '))

    if x2 == 2:
        print('Correct!')
        score += 1
        print('Your score is ', score)
    else:
        print('Incorrect, try again!')
        print('Your score is ', score)

# Q3
    print('\nWhat is 1 + 2?')
    x3 = int(input('Your answer: '))

    if x3 == 3:
        print('Correct!')
        score += 1
        print('Your score is ', score)
    else:
        print('Incorrect, try again!')
        print('Your score is ', score)


    if score >= highscore:
        highscore = score
        print('You\'ve set a new high score: ', highscore)
        with open('highscore.txt','w') as f:
            f.write(str(highscore))
    else:
        print('Better luck next time!')

    again = input('Would you like to play again? (Y/N)')
    again.lower()
    if again == 'n':
        finish = True
    else:
        print('Good luck this time!')