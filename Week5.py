#Week 5 Lecture 1
'''
temp = int(input('Enter the temperature: '))
rain = input('Is it raining? (Yes/No): ')
raining = False #boolean variable

#one way selection - if statement
if rain.lower() == 'yes':
    raining = True

#two way selection - if else statement
if temp >= 65 and not raining:
    print('Go to the park')
else:
    print('Watch TV')

#alternate form of the if-else - ternary (conditional) statement
print('Go to the park' if temp >= 65 and not raining else 'Watch TV')
print('Go to the park') if temp >= 65 and not raining else print('Watch TV')

#You can use the walrus operator with ternary form
#note () use in both examples
print('Yay, you pass' if (    (score := float(input('Enter score: '))) >= 70    ) else 'Try again')
print(score) #store the value
print('Yay, you pass') if (    score := float(input('Enter score: ')) >= 70      ) else print('Try again')
print(score) #store the boolean outcome
'''
#multiple selection
newscore = float(input("Enter a score (0 - 100): "))

#input validation
while newscore < 0 or newscore > 100: newscore = float(input('Invalid. Enter a score from 0 to 100:')) #This works

#nested if else structure
if newscore >= 90:
    grade = 'A'
else:
    if newscore >= 80:
        grade = 'B'
    else:
        if newscore >= 70:
            grade = 'C'
        else:
            if newscore >= 60:
                grade = 'D'
            else:
                grade = 'F'
print(f'The grade for the score of {newscore} is {grade}')


#if elif else
if newscore >= 90:
    grade = 'A'
elif newscore >= 80:
    grade = 'B'
elif newscore >= 70:
    grade = 'C'
elif newscore >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f'The grade for the score of {newscore} is {grade}')

#series of if
if newscore >= 90:
    grade = 'A'
if newscore >= 80 and newscore < 90:
    grade = 'B'
if newscore in range(70, 80): #This works for integers because 65.0 == 65
    grade = 'C'
if 60 <= newscore < 70:
    grade = 'D'
if newscore < 60:
    grade = 'F'
print(f'The grade for the score of {newscore} is {grade}')

#match case
score = int(newscore)
match score // 10:
    case 9 | 10:
        grade = 'A'
    case 8: 
        grade = 'B'
    case 7:
        grade = 'C'
    case 6:
        grade = 'D'
    case _: #default (wildcard) - same as trailing else
        grade = ''

print(f'The grade for the score of {score} is {grade}')

#input validation with walrus operator
while (number := int(input('Enter a positive number: ')) < 0):
    print('Invalid number')

#count controlled while loop
i = 1
while i <= 5:
    print(i)