from random import choice # adds the choice function from the random library

items = ['Rock', 'Paper', 'Scissors']

def let_play():
    go = input('You choose [R]ock, [P]aper or [S]cissors? ').upper() # Type: r, p or s
    pkd = choice(items) # randomly picked items
    if go == 'R' and pkd == 'Scissors':
        print('I chose scissors, you won!')
    elif go == 'P' and pkd == 'Rock':
        print('I chose rock, you won!')
    elif go == 'S' and pkd == 'Paper':
        print('I chose paper, you won!')
    elif go == 'R' and pkd == 'Paper':
        print('I chose paper: you lose')
    elif go == 'P' and pkd == 'Scissors':
        print('I chose scissors: you lose')
    elif go == 'S' and pkd == 'Rock':
        print('I chose rock: you lose')
while True:
    let_play()