import turtle

my_turtle=turtle.Turtle()

def square(length):
  my_turtle.forward(length)
  my_turtle.right(90)
  my_turtle.forward(length)
  my_turtle.right(90)
  my_turtle.forward(length)
  my_turtle.right(90)
  my_turtle.forward(length)

for i in range(100):  
     square(50)
     my_turtle.right(11)
