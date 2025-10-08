#use of integer division and remainder
print(f'86 seconds is equivalent to {86//60} minute(s) and {86%60} seconds.')

#operator precedence
#()
#**
# /, //, %, *
# +, -
# =

a = 10
#update to same variable
a = a + 1
print(a)

#compound assignment
a += 15 # a = a + 15
print(a)

b = 2
a *= b + 4 # a = a * (b + 4)
print(a)

#percent formatting
rate = 0.3
print(f'{rate:%}') #format a decimal to percentage
print(f'{rate:.1%}')


#input
a = input('Enter an integer: ') #input a string
b = input('Enter another integer: ')
print(int(a + b)) #string + string = string

#to convert, use int(a) + int(b)

a = int(input())
b = float(input())
print(a + b) #output a float






