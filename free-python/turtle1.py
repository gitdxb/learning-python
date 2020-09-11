from turtle import Turtle

tina = Turtle()

def draw(name, r, col):
  name.color(col)
  name.dot(r*2)

draw(tina, 150, "blue")
draw(tina, 100, "red")
draw(tina, 50, "yellow")