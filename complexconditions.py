# A student makes honour roll if their average is >= 85
# and their lowest grade is not below 70





gpa = float(input('What is your Grade Point Average? '))
lowest_grade = input('What is your lowest grade? ')
lowest_grade = float(lowest_grade)


if gpa >= .85:
    if lowest_grade >= .70:
        print('You made the honour roll!')


if gpa >= .85 and lowest_grade >= .70:
    print('You made the honour roll!')




if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False
#Somewhere later in your code
if honour_roll:
    print('You made the honour roll!')
else:
    print('Sorry next time!')

