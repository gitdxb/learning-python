try:
    print('The 10 highest scores previously were:')
    with open('highscore.txt','r') as f:
        highscore = f.read()
        print(highscore)
except:
    print('Creating a new highscore file')
    f = open('highscore.txt','w')
    f.close()

finish = False
while finish == False:
    scores = []
    names = []

    with open('highscore.txt','r') as file:
        for line in file:
            line = line.strip('\n')
            line = line.split(' ')
            names.append(line[0])
            scores.append(int(line[1]))
    # Q1,2,3
        score = 0
        name = input('Enter player name: ')

        print('Welome to the Maths Quiz')
        print('Can you answer three questions and score maximum points?')
    # Q1
        print('\nQ1: What is the product of 2x2x2?')
        x = int(input('Your answer :>> '))

        if x == 8:
            print('Correct!')
            score += 1
        else:
            print('Incorrect, try again!')

    # Q2
        print('\nWhat is 1 + 1?')
        x2 = int(input('Your answer: '))

        if x2 == 2:
            print('Correct!')
            score += 1
        else:
            print('Incorrect, try again!')

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


    # Ranking
    position = 0
    for compare_score in scores:
        if score < compare_score:
            position += 1
    scores.insert(position, score)
    names.insert(position, name)
    print("HIGHSCORES")
    with open("highscore.txt", 'w') as file:
        for i in range(len(scores)):
            file.write(names[i] + " " + str(scores[i]) + "\n")
            print(names[i] + " " + str(scores[i]))