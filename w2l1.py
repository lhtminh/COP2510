print('Hello')
print() #create a skipped line
print('again')

print('\n') #\n newline escape sequence
            #effect of two skipped lines
print('Welcome\nback')
print('Welcome\t back') #\t - tab
print('Welcome', 'back')

#effect of changing the values in sep and end
print(4, 3, 2, 1, sep = '...')
print('I', 'am', sep = '...')
print('Hello', end = '  ')
print('again')

#variables - name spaced in memory
#identifier - names of components in program
# = is assignment operator
number = 45 #initializing a variable
print(number) #echo printing

number = 555

print(f"number is {number}") #using an f-string

number = "twenty three"
print(f"number is {number}")

stud3nts = 5
students_in_class = 100
_ = 78 #this works, but is a bad name
num2 = 89
numSections = 14


