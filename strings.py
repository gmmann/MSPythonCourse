# first_name = 'Christopher'
# last_name = 'Harrison'
# print(first_name)
# print(first_name + last_name)
# print('Hello ' + first_name + ' ' + last_name)




sentence = 'The dog is named Sammy'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))


first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
print('Hello ' + first_name.capitalize() + ' ' + last_name.capitalize())
print('Hello ' + first_name.upper() + ' ' + last_name.upper())
print('Hello ' + first_name.capitalize() + ' ' + last_name.capitalize())

print()
output = 'Hello, ' + first_name + ' ' + last_name
print(output)
print()
output = 'Hello, {} {}'.format(first_name, last_name)
print(output)
print()
output = 'Hello, {0} {1}'.format(first_name, last_name)
# output = 'Hello, {1} {0}'.format(first_name, last_name)
print(output)
print()
# Only available in Python 3
output = f'Hello, {first_name} {last_name}'
print(output)
print()




