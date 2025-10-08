import turtle

t = turtle.Turtle()

side = int(input("Enter the length of the side of the pentagon: "))

for i in range(0, 5):
    t.forward(side)
    t.left(90)
