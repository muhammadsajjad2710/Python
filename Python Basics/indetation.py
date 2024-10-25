num = int(input("enter number"))
if num%2 == 0:
    if num%3 ==0:
        print("Divisible by 3 and 2")
    else:
        print("divisble by 2 not divisible by 3")

else:
    if num%3 == 0:
        print ("divisble by 3 not divisible by 2")
        
    else:
        print ("not divisible by 3 and 2")
        
name = "ravi"

string = "Hello {} \
Welcome to my python tutorial \
from code geeks".format(name)
print(string)

Subjects = ["English", "French", "Sanskrit",
   "Physics", "Maths",
   "Computer Sci", "History"]
print (Subjects)

x = id(Subjects)
print(x)