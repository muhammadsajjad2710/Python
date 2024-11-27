capitals = {"Islambad": "Pakistan", "New York" : "USA", "Sydney" : "Australia" }
numbers = {10: "ten", 20:"twenty",30:"Thirty",40:"Forty"}
marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print(capitals)
print(type(capitals))

d1 = {"fruits":["apple","Bannana","Mango"], "numbers":(1,2,3,4,5,6)}

d2 = {("Islambad","Lahore","Karachi","Peshawar"):["cities"], ("Ali","Usman","akbar"):"names"}
print("d1 :",d1, "d1 datatype: ",type(d1))
print("d2 :",d2, "d2 datatype: ",type(d2))
# d3 = {["names","list"]:"ali", ("flowers"): "beautiful"}
# print(d3)

d3 = {"ali" :"names", "usman": "names", "Iftikhar Ahmad": "names"}
d4 = {"fruit":"Banana", "fruit":"Mango", "fruit":"apple", "list of people": ["ali","usman"]}
print(d3)
print(d4)


student_dictionary = {
    "name": "Malik Sajjad",
    "Registration No": "19PWCSE1817",
    "Department": "ComputerSystemEngineering",
    "Graduation Year": "2024"
}

print("student dictionary",student_dictionary)

palyer_info = dict(name = "ali", sport = "cricket", age = 32)
print(palyer_info)

name = palyer_info["name"]
print("Name :",name)

registration_no = student_dictionary["Registration No"]
print("Registration No: " ,registration_no)

department = student_dictionary.get("Department")
print("Department :",department)
print("age of the player ", palyer_info.get("age"))

student_dictionary["Department"] = "Civil"
palyer_info["age"] = 24
print(student_dictionary)
print(palyer_info)

del student_dictionary["Department"]
print(student_dictionary)
palyer_info.pop('age')
print(palyer_info)

for key in student_dictionary:
    print("keys:",key)

for value in student_dictionary.values():
    print("values:",value)

for key,value in student_dictionary.items():
    print("items:key: ",key,"items:value:",value)
    
dictonary = {['name']:'sajjad','age':22, }

print("Name in dictonary is:",dictonary["name"])