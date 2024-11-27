studentDetails= {"name":"Iftikhar",'age':32,'class':"8th"}
print(studentDetails)
del studentDetails["class"]
print(studentDetails)
del studentDetails
# print(studentDetails)
studentDetails= {"name":"Iftikhar",'age':32,'class':"8th"}
value = studentDetails.pop('class')
print(studentDetails)
print(value)

itemspairs = studentDetails.popitem()
print(studentDetails)
print(itemspairs)
studentDetails.clear()
print(studentDetails)
studentDetails= {"name":"Iftikhar",'age':32,'class':"8th"}
removekeys = ["name","age"]
for key in removekeys:
    studentDetails.pop(key,None)

print(studentDetails)

studentDetails= {"name":"Iftikhar",'age':32,'class':"8th"}

for key,value in studentDetails.items():
    print(key,value)

