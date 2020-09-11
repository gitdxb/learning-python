import random
def flip_coin():
  num = random.randint(0, 1)
  if num == 1: return 'heads'
  elif num == 0: return 'tails'

head = 0
tails = 0
for i in range(100):
    x = flip_coin()
    if x == 'heads': head += 1
    else: tails += 1

print('There are: ', head, 'heads and', tails, 'tails')