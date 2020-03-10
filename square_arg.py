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
  
square(300)  
square(150) 
square(100) 
square(50) 
