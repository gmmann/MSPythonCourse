import json

results = {"req_data":{"requestId": "33290a37-ad67-42af-b647-c5a236ecd202","name":"George","last":"Mann"}}

# print(results['req_data'])
name_results = results('req_data')
print(name_results['name'])




import json
person_dict = {'first': 'Christopher', 'last':'Harrison'}
person_dict['City']='Seattle'
staff_dict ={}
staff_dict['Program Manager']=person_dict
staff_json = json.dumps(staff_dict)
print(staff_json)


person_dict['first']='Christopher'