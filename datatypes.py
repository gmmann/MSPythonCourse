# to get the current date and time
# we need to use the datetime library
from datetime import datetime, timedelta

current_date = datetime.now()

# the now function returns a datetime object
# print('Today is: ' + str(current_date))

today = datetime.now()
# print('Today is: ' + str(today))


# timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
tomorrow = today + one_day
print('Yesterday was    : ' + str(yesterday))
print()
print('Today is         : ' + str(today))
print()
print('Tomorrow will be : ' + str(tomorrow))
print()

print('Day     : ' + str(current_date.day))
print('Month   : ' + str(current_date.month))
print('Year    : ' + str(current_date.year))


# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
# error handling added too

birthday = input('When is your birthday (dd/mm/yyyy)? ')
print(str(birthday))
birthday_date = datetime.strptime(birthday, '%d/%m/%Y' )
print()
print('Birthday             : ' + str(birthday_date))
birthday_eve = birthday_date - one_day
print('Day before birthday  : ' + str(birthday_eve))



