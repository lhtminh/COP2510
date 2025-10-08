#loop concepts (application of RNG and basic graphics)
'''
import turtle as t
import random as rd

t.bgcolor('black')
t.shape('turtle')
t.speed(5)

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'white']

while True:
    try:
        numshape = int(input('Enter the number of shapes to draw (1 - 10): '))
        if 1 <= numshape <= 10:
            break
        else:
            print('Try another number')
    except Exception as e:
        print('INvalid entry. Please enter a whole number')

for i in range(numshape):
    sides = rd.randint(3, 8)
    size = rd.randint(30, 100)
    t.color(rd.choice(colors))

    #try to draw but break if it is too large
    for j in range(sides):
        if size > 90:
            print('Skipping oversize shape')
            break
        t.forward(size)
        t.left(360/sides)
    else:
        t.penup()
        t.goto(rd.randint(-200, 200), rd.randint(-200, 200))
        t.pendown()
t.done()
'''
for n in range(1, 25):
    if n == 4 or n == 13:
        continue #toggle between break and continue
else:
    print('done')