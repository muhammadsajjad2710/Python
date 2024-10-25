# var = "3/4"
# print (var)
# var = "\u00BE"
# print (var)
# var = "\u0031\u0030"
# print (var)

string = "Hello"
tobytes = string.encode('utf-8')
print(tobytes)
string = tobytes.decode('utf-8')
print(string)