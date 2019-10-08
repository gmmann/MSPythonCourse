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
