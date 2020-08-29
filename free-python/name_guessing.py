# Guessing name game
name = input('Guess a name: ')
count = 1
while name != 'Martin':
    name = input('wrong! guess again> ')
    count += 1
print('Yayy~! You got it right after ' + str(count) + ' time!')

if count > 5:
    print('Quite a lot of guesses huh!')