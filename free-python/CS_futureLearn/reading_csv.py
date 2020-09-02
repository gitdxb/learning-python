import csv
name = 'Portia'
food = 'Steak'

with open('food.csv', mode = 'a') as csvfile:
    fav = csv.writer(csvfile, delimiter=',')
    #fav.writerow([name,food])

fh = open('food.csv')
for line in fh:
    line = line.strip()
    print(line)