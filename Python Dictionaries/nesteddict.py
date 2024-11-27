nestedDic= {
    'outerkey1':{"innerkey1":'value1', 'innerkey2':'value2'},
    'outerkey2':{"innerkey1":'value1', 'innerkey2':'value2'}
}
print(nestedDic)

nested_dict = {}
outerkeys = ["outerkey1",'outerkey2']

for key in outerkeys:
    nested_dict[key] = {'innerkey1':'value1',"innerkey2":'value2'}
print(nested_dict)

nestedDic ['outerkey1']['innerkey3']= 'value3'
print(nestedDic)

nestedDic['outerkey3'] = {'innerkey1':'value1','innerkey2':'value2','innerkey3':'value3'}
print(nestedDic)

students = {
    "Alice": {"age": 21, "major": "Computer Science"},
    "Bob": {"age": 20, "major": "Engineering"},
    "Charlie": {"age": 22, "major": "Mathematics"}
}

alice_major = students['Alice']['major']
print ("alice major",alice_major)
bob_age = students['Bob']['age']
print("bob_age",bob_age)

alice_major = students.get("Alice",{}).get("major","Not Found")
print('alice_major',alice_major)
iftikhar_major = students.get("ifitkhar",{}).get("major","NOt found")
print("iftikhar_major",iftikhar_major)

del students['Charlie']
print(students)

students = {
    "Alice": {"age": 21, "major": "Computer Science"},
    "Bob": {"age": 20, "major": "Engineering"},
    "Charlie": {"age": 22, "major": "Mathematics"}
}
for student,details in students.items():
    print('student',student, "details",details)
    for key,value in details.items():
        print('keys',key,'values',value)