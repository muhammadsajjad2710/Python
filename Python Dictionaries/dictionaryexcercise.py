student_details  = {
    'Name':'Malik',
    'RegistrationId':'19PWCSE1817',
    'Department':'ComputerSystemEngineering'
    
} 

keys = ['Name','Department']

d2 = {}

for k in keys:
    d2[k]= student_details[k]
print(d2)

dictionary = {'a' :'b', 'k':'v'}
#newdictionary = dictionary.popitem()
#print(newdictionary)
listnew = list(dictionary.items())
print(listnew)

newdictionary = dictionary.popitem()
print(newdictionary)
newdictionary = dictionary.popitem()
print(newdictionary)
