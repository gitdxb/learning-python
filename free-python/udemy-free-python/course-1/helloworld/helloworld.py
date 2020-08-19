def helloworld():
    print("Hello world")

helloworld()

def Sum(a,b):
    print(a + b)
Sum(10,50)

def Sum(a,b):
    return (a + b)
returnAdd = Sum(2,3)
print(returnAdd)
class Person:
    def getName(self):
        print("avi")
    def getAge(self):
        print("16")

p = Person()
p.getName()
Person.getAge(p)
Person.getName(p)

#Create Car objects
class Car:

   def __init__ (self, make, year):
       self.make = make
       self.year = year
   def getMake(self):
      print("So your favourite car model is: " + self.make)
   def getYear(self):
      print("And your fav model year is: " + self.year)
w = Car("Toyota Yaris", "2020")
w.getMake()
w.getYear()

#Create Person object
class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        print("Your name is: " + self.name)
    def getAge(self):
        print("Your age is: " + self.age)
p = Person("Bob", "34")
p.getName()
p.getAge()

