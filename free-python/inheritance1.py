class Cat:
    talk = False

    def __init__(self, name, mood, hungry, energy):
        self.name = name
        self.mood = mood
        self.hungry = hungry
        self.energy = energy

    def show(self):
        print('His name is', self.name)
        print('His mood is', self.mood)
        print('He feels', self.hungry, 'and',self.energy)

    def sleep(self):
        print('He feels', self.mood)
        print('and also', self.energy)
c = Cat('Bob','Dowsy','very hungry','low energy')
c.sleep()
c.show()