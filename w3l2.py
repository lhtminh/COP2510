
#Multiple input
a, b = input('Enter 2 values (separated by a space): ').split()
a = int(a); b = int(b)
print(f'{a} + {b}  =  {a + b}')

#other formatting options - all rounded
number = float(input('Enter a number: '))
print('The number is', format(number, '.3f'))

temp = 25.46
print("Temperature: {:.1f} degress Celsius".format(temp))

price = 49.99
print("The price is $%.1f" % price)

#types in python - string, tuple, list, set, dictionaries
#string - sequence type
name = 'Schinnel K. Small'
print(name[0]); print(name[-1])
#string slicing
print(name[0:3]); print(name[-6:-3])
print(name * 2)
#name[0] = 'K', strings are immutable

#tuple is a sequence, container, immutable
t1 = (1, 5.7, 'something else', True)
print(t1[1])
#t1[2] = 'never mind'

#list - sequence, container, mutable
items = ['cheese', 7.9, 11, name, t1, ['Tampa', 'Florida']]
print(items)
items[2] = 'bacon'
print(items)
print(items[5][-1]); print(items[5])
print(items[-1][0][0])

#list methods: append, pop, remove
items.pop()
items.remove(7.9)
items.append('last')

#set - unordered collection of unique elements
set1 = {1, 7, 1, 5, 8, 9.0, 'nine'}
#print(set1[2])

#dictionaries
alias = {1: ['one', 1.0, '1'],
         'cat': 'kitty'}
print(alias[1][0])

#importing other modules
