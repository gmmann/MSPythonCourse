names = ['Christopher', 'Susan']
print(names)

scores = []
scores.append(98)  # add new item to the end
scores.append(99)
print(scores)
print(scores)
print(scores[1])  #Collections are zero-indexed
scores.append(111)
print(scores)




from array import array
scores = array('d')  # d is for digit in the array
scores.append(97)  # add new item to the end
scores.append(98)
print(scores)
print(scores)
print(scores[1])  #Collections are zero-indexed
scores.append(111)
print(scores)



names = ['Christopher', 'Susan']
print(len(names)) # get the number of items
names.insert(0, 'Bill')  #insert before the index
print(names)
names.sort()
print(names)
print(len(names)) # get the number of items


names = ['Susan','Christopher', 'Bill']
presenters = names[0:2] #get the first two items
#starting index and number of items to retrieve
print(names)
print(presenters)


print(len(names)) # get the number of items
names.insert(0, 'Bill')  #insert before the index
print(names)
names.sort()
print(names)
print(len(names)) # get the number of items



person = {'first': 'Christopher'}
person['last'] = 'Harrison'
print(person)
print(person['first'])




person = {}
person['first'] = 'Christopher'
person['last'] = 'Harrison'

christopher = {}
christopher['first'] = 'Christopher'
christopher['last'] = 'Harrison'

susan = {'first': 'Susan', 'last': 'Ibach'}

print(christopher)
print(susan)

print()
print()
print('BLAH')


people = [christopher, susan]
print(people)


print()
print()
print()

people.append({'first': 'Bill', 'last': 'Gates'})
print(people)

presenters = people[0:2]
print(people)
print()
print(presenters)
print(len(presenters))
print()









