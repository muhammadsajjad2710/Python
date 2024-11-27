studentDetails= {"name":"Iftikhar",'age':32,'class':"8th"}

for item in studentDetails.items():
    print(item)

for item in studentDetails:
    print(item,studentDetails[item])
    
for keys, values in studentDetails.items():
    print(keys,values)
    
for key in studentDetails.keys():
    print(key)
for value in studentDetails.values():
    print(value)