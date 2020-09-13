from random import randint

scores = []
count = 0
for x in range(300):
    scores.append(randint(0,10))

for score in scores:
    if score == 10:
        count += 1

print('Top 10:',count)
print(count * '###')