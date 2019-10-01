pi = 3.14159265359
print(pi)


first_num = 6
second_num = 2
print(first_num + second_num)
print(first_num ** second_num)

days_in_feb = 28
# need to do a type conversion.. turn integer to string
print(str(days_in_feb) + ' days in February')

first_num = '5'
second_num = '6'
print(first_num + second_num)


first_num = input('Enter first number ')
second_num = input('Enter second number ')
# to convert to an integer
print(int(first_num) + int(second_num))
# to convert to a floating number
print(float(first_num) + float(second_num))


radius =  input('Enter the radius of the circle in mm ')
r_squared = int(radius) ** 2
print(r_squared)

area = pi * r_squared
print('The area of a circle with a ' + (radius) + 'mm radius is ' + str(area)) 
