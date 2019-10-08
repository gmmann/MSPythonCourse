

def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial


first_name = input('Enter your first name: ')
# middle_name = input('Enter your middle name: ')
# last_name = input('Enter your last name: ')

first_name_initial = get_initial(first_name, False)
# middle_name_iniital = get_initial(middle_name)
# last_name_iniital = get_initial(last_name)

print('Your initials are: ' + first_name_initial)
# print()
# print('Your initials are via function: ' + get_initial(first_name) + get_initial(middle_name) + get_initial(last_name))
# print()



def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial


first_name = input('Enter your first name: ')
# middle_name = input('Enter your middle name: ')
# last_name = input('Enter your last name: ')

first_name_initial = get_initial(first_name, False)
first_name_initial_ForceUpper = get_initial(first_name)
first_name_initial_forceupper = get_initial(force_uppercase=True,  name=first_name)

# middle_name_iniital = get_initial(middle_name)
# last_name_iniital = get_initial(last_name)

print('Your initials are: ' + first_name_initial)
print('Your initials are in upper: ' + first_name_initial_ForceUpper)

print('Your initials are in upper with both fields defined: ' + first_name_initial_forceupper)
# print()
# print('Your initials are via function: ' + get_initial(first_name) + get_initial(middle_name) + get_initial(last_name))
# print()



def error_logger(error_code, error_severity, log_to_db, error_message, source_module):
    print('Oh no error: ' + error_message)
    # Imagine code here that logs our error to a database file

first_number = 10
second_number = 5
if first_number > second_number:
    error_logger(error_code=45, error_severity=1, log_to_db=True, error_message='Second number greater than first', source_module='my_math_method')
