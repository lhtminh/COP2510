'''
valid = False

while not valid:
    try:
        num = int(input('Enter a positive number: '))

        if num > 0:
            print(f'You entered {num}')
            valid = True
        else:
            print('Oops! Enter a number greater than 0.')
    except ValueError:
        print('Oops! That wasn\'t a valid number.')

#for loop with range function
for j in range(6):
    print(j)

for j in range(1, 8):
    print(j)

for j in range(10, 55, 5):
    print(j)

for j in range(40, 10, -4):
    print(j)

count = int(input('Enter number of times to repeat: '))
for c in range(count):
    print('Repeat')

name = 'ABCDEFG'
for i in name:
    print(i)

names = ['a', 'b', 'dm']
for i in names:
    print(i)

for i in range(len(names)):
    print(names[i])
'''

abbr = {1: 'one', 2: 'two', 3: 'three'}
for a in abbr:
    print(abbr[a])

#enumerate - retries the index and the element of a list
for x, y in enumerate(abbr):
    print(x, y, abbr[y])