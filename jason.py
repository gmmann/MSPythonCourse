# import json

# person = {'first': 'Jason', 'last':'Friedrich'}
# print(person)
# # print(json.dumps(person_dict))

# # person_json = json.dumps(person_dict)
# # print(person_json)


import json

person_dict = {'FirstName': 'Jason', 'LastName': 'Friedrich'}


person_dict['City']='Bochum'
staff_dict ={}
staff_dict['Evil Creator']=person_dict
staff_json = json.dumps(staff_dict)
staff_json10 = json.dumps(staff_dict, indent=10)

# last_name = staff_json('LastName')
# print(staff_json)
# print(staff_json10)
print(person_dict['LastName'])
last_name = person_dict['LastName'] 

# last_name = staff_json.upper()
# last_name10 = staff_json10.upper()
last_nameUP = last_name.upper()
print(last_nameUP)
print('!')
print('!')
print('!')
# print(last_name10)
print(last_name)


# person_dict['first']='Christopher'

