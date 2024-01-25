# First Go at Turtle Party Learning [01/25/2024]
# by Onlee Retta

import turtle
turtle.color("purple")

def back(len):
 turtle.penup()
 turtle.backward(len)
 turtle.pendown()
 
def move(len):
  back(-1*len)

def polygon(num, size):
 for i in range(num):
  turtle.forward(size)
  turtle.left(360 / num)
  
for n in range(3, 12):
  move(50)#forward
  polygon(n, 100 / n)
  back(75)
  turtle.right(360 / 12)
