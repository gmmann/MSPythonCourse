import datetime
# print timestamps to see how long sections of code 
# take to run

first_name = 'Susan'
print('task completed')
print(datetime.datetime.now())
print()


for x in range(0,10):
    print(x)
print('task completed')
print(datetime.datetime.now())
print()


# move above into a function and can call it out when needed
print('Function time')
print('not a party...')

def print_time():
    print('task completed')
    print(datetime.datetime.now())
    print()
    
first_name = 'Susan'
print_time()


# Import datetime CLASS from the datetime library
print('NOW doing with cleaner class')
from datetime import datetime
# Print the current time
def print_time():
    print('task completed')
    # don't need extra prefix
    print(datetime.now())
    print()



for x in range(0,10):
    print(x)
print_time()






from datetime import datetime
# print timestamps to see how long sections of code
# take to run

first_name = 'Susan'
print('first name assigned')
print(datetime.now())
print()

for x in range(0,10):
    print(x)
print('loop completed')
print(datetime.now())
print()


def print_time(task_name):
    print(task_name)
    print(datetime.now)
    print()
first_name = 'Susan'
print_time('first name assigned with task')

for x in range(0,10):
    print(x)
print_time('loop completed with task')
print()





# first_name = input('Enter your first name: ')
# first_name_iniital = first_name[0:1]
# last_name = input('Enter your last name: ')
# last_name_iniital = last_name[0:1]

# print('Your initials are: ' + first_name_iniital + last_name_iniital)



def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

first_name_iniital = get_initial(first_name)
last_name_iniital = get_initial(last_name)
print('Your initials are: ' + first_name_iniital + last_name_iniital)
print()
print('Your initials are via function: ' + get_initial(first_name) + get_initial(last_name))
print()






