#how to handle 'constants'
#1: Use a variable
MAX_SEATS = 152 #variable that we leave alone. Use uppercase to distinguish from other variables

MAX_SEATS = 199 #This works

#2: Use a tuple
MaxSeats = (152, )

#MaxSeats[0] = 5 -> This won't work
 
print(f"Number of seats in CIS 1048: {MaxSeats[0]}")

print(f"Number of seats in CIS 1048: {MAX_SEATS}")

#walrus operator := allow assignment and printing

print("The number of students in class on Tuesday was", \
      students := 300)
#use \ to split a line of code

print(f'The number of students in class on Tuesday was \
    {students := 0}')
#:= generate a field width based on value

#To fix the field width issue, use () around the := expression
print(f'The number of students in class on Tuesday was {(students := 10)}')

#multiple assignment
x = y = z = 0
print(f"x is {x}, y is {y}, and z is {z}")

#respective assignment
a, b = 1, 2
print(f"a is {a} and b is {b}")

#role of semicolon
a = 1; b = 2; print(a + b)

#e-notation
full = 67e6
guaranteed = 44E6
eno = 6e-5

#decimal formatting
print(f"Chris Godwin signed a 3-year ${full:.2f} deal with ${guaranteed:.2f} guaranteed in his 2025 contract.")

print(f"Chris Godwin signed a 3-year ${full:,.0f} deal with ${guaranteed:,.0f} guaranteed in his 2025 contract.")



