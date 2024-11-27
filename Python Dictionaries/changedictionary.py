person = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# modifying the value associated with the key 'age'
person['age'] = 26
print(person)
person['name'] = 'ali'
print(person)

person.update({'name':"usman","age":23})
print(person)

if person['age'] == 23:
    person['age'] = 27
print(person)

person['city'] = 'Islambad'
print(person)
person.setdefault("height",181)
print(person)
del person['age']
print(person)
# del person['age']|
remove_name = person.pop('name')
print("remove name:",person)
remove_item = person.popitem
print("remove item",remove_item)
print(person)
remove_item = person.popitem
print("remove item",remove_item)
#print(person)

player = {'name':'ali','age':25, 'sport':'cricket'}
print(player)
removeitem = player.popitem()
print(removeitem)
print(player)
removeitem = player.popitem()
print(removeitem)
print(player)
removeitem = player.popitem()
print(removeitem)
print(player)