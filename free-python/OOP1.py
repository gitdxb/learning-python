class PartyAnimal:
    x = 0

    def __init__(self, name):
        self.name = name
        print(self.name, 'I am constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

    def __del__(self):
        print('I am destructed', self.x)

#an = PartyAnimal()
#an.party()
#an.party()
#an.party()
#an = 42
#PartyAnimal.party(an)
#print('an contains ',an)

# Check dir(an)

# from party import PartyAnimal

class CricketFan(PartyAnimal):
    points = 0
    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.name, 'points', self.points)

s = PartyAnimal('Sally')
s.party()
j = CricketFan('Jim')
j.party()
j.six()
#print(dir(j))