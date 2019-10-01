# if province == 'Alberta':
#     tax = 0.05
# if province == 'Nunavut':
#     tax = 0.05
# if province == 'Ontario':
#     tax = 0.13



# if province == 'Alberta':
#     tax = 0.05
# elif province == 'Nunavut':
#     tax = 0.05
# elif province == 'Ontario':
#     tax = 0.13
# else:
#     tax = 0.15

# province = input('What province are you buying goods: ')
# if province == 'Alberta' or province == 'Nunavut':
#     tax = 0.05
# elif province == 'Ontario':
#     tax = 0.13
# else:
#     tax = 0.15
    
# print(float(tax))


# province = input('What province are you buying goods: ')
# if province in ('Alberta', 'Nunavut', 'Yukon'):
#     tax = 0.05
# elif province == 'Ontario':
#     tax = 0.13
# else:
#     tax = 0.15
# print(float(tax))


country = input('What country are you from? ')
province = input('What province are you buying goods: ')
tax = 0
if country == 'Canada':
    if province in ('Alberta', 'Nunavut', 'Yukon'):
        tax = 0.05
    elif province == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0.0
print(float(tax))




