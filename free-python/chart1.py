import matplotlib.pyplot as plot
from random import randint

scores = []
for x in range(20):
    scores.append(randint(0,10))


plot.bar(range(20), scores, align='center', alpha=0.5)

plot.xticks(range(20))
plot.ylabel('Score frequency')
plot.title('Scores on a quiz')

plot.show()
plot.savefig(fname="Quiz Chart1.png")