capitals = {('cities'):['lahore',"peshawar",'quiadabad'], 'capitals':("islambad","New York")}
print("cities: ",capitals[('cities')])

print("capitals names:",capitals.get('capitals','Not Found'))

student_info = {
    "name" : "ali",
    'age': 23,
    'subject':'computer science'
    
}
keys = student_info.keys()
print("keys of student_info",keys)
print("values of student_info",student_info.values())

name = student_info['name']
print("name: ",name)
age = student_info['age']
print("age: ",age)

subject = student_info['subject']
print("subject",subject)
graduationyear = student_info.get('graduationyear',2024)
print(graduationyear)
print(student_info)

print("All keys of student_info:",student_info.keys())
print("All values of student_info:",student_info.values())
print("all itmes of student_info:",student_info.items())

print("now iterating items throug keys and its values")
for value,keys in student_info.items():
    # print("Keys",keys, "Values",value)
    print(keys,":",value)