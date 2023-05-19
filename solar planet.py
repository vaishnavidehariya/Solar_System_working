import turtle
import math
from math import *
Screen = turtle.Screen()
Screen.tracer(50)
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
class planet(turtle.Turtle):
    def __init__(self,name,radius,color):
        super().__init__(shape = "circle")
        self.name = name
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.up()
        self.pd()
        self.angle = 0
    def move(self):
        x = self.radius*cos(self.angle)
        y = self.radius*sin(self.angle)
        self.goto(sun.xcor()+x,sun.ycor()+y)
mercury = planet("mercury",40,"orange")
venus = planet("venus",80,"black")
earth = planet("earth",100,"blue")
mars = planet("mars",150,"red")
jupiter = planet("jupiter",180,"dark red")
saturn = planet("saturn",230,"pink")
uranus = planet("uranus",250,"light blue")
neptune = planet("neptune",280,"green")
mylist = [mercury,venus,earth,mars,jupiter,saturn,uranus,neptune]
while True:
    Screen.update()
    for i in mylist:
        i.move()
    mercury.angle += 0.05
    venus.angle += 0.03
    earth.angle += 0.01
    mars.angle += 0.007
    jupiter.angle += 0.02
    saturn.angle += 0.018
    uranus.angle += 0.016
    neptune.angle += 0.005