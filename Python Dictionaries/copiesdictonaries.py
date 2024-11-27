studentDetails= {"name":"Iftikhar",'age':32,'class':"8th",'player':["t20,test"]}
print("original copy",studentDetails)

shallowCopy = studentDetails.copy()
print("shallow copy",shallowCopy)

shallowCopy['age'] = 44
print("shallow copy",shallowCopy)
print("original copy",studentDetails)
shallowCopy['player'].append("odi")
print("shallow copy",shallowCopy)
print("original copy",studentDetails)
shallowCopy["player"]= "international"
print(shallowCopy)
print(studentDetails)

original_dict = {"name": "Bob", "age": 30, "skills": ["Java", "C++"]}
ShallowCopy = dict(original_dict)
print(original_dict)
print(ShallowCopy)
ShallowCopy['name']  = 'fob'
ShallowCopy['age'] = 42
ShallowCopy['skills'].append("Python")
print(ShallowCopy)
print(original_dict)

import copy
original_dict = {"name": "Bob", "age": 30, "skills": ["Java", "C++"]}
deepCopy= copy.deepcopy(original_dict)
print(original_dict)
print(deepCopy)
deepCopy['name'] = "stob"
deepCopy['age'] = 32
deepCopy['skills'].append("Python")
print(deepCopy)
print(original_dict)

dict1 = {"name": "Krishna", "age": "27", "doy": 1992}
dict2 = dict1.copy()
print(dict1)
print(dict2)