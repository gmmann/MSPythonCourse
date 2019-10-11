import json

results = {"req_data":{"requestId": "33290a37-ad67-42af-b647-c5a236ecd202","name":"George","last":"Mann"}}

# print(results['req_data'])
name_results = results('req_data')
print(name_results['name'])

