# # # # # # # # # # # # # def greetings ():
# # # # # # # # # # # # #     print("Hello Word")
    
# # # # # # # # # # # # # greetings()

# # # # # # # # # # # # def printme ( str ):
    
# # # # # # # # # # # #     print(str)
# # # # # # # # # # # #     return;

# # # # # # # # # # # # printme("I'm first call to user defined function!")
# # # # # # # # # # # # printme("Again second call to the same function")
# # # # # # # # # # # def testfunction(arg):
# # # # # # # # # # #     print("ID inside the function:", id(arg))
    
# # # # # # # # # # # var = "Helllo"
# # # # # # # # # # # print("ID before passing:", id(var))
# # # # # # # # # # # testfunction(var)
# # # # # # # # # # def testfunction(arg):
# # # # # # # # # #    print ("ID inside the function:", id(arg))
# # # # # # # # # #    arg = arg + 1
# # # # # # # # # #    print ("new object after increment", arg, id(arg))

# # # # # # # # # # var=10
# # # # # # # # # # print ("ID before passing:", id(var))
# # # # # # # # # # testfunction(var)
# # # # # # # # # # print ("value after function call", var)
# # # # # # # # # #x = 0
# # # # # # # # # #print (x)
# # # # # # # # # def enternumber():
# # # # # # # # #    x = input("Enter the number :" )
# # # # # # # # #    print ( x)
   
# # # # # # # # # enternumber()
# # # # # # # # # enternumber()
   
# # # # # # # # str = "alissasdfdsa" 
   
# # # # # # # # def statement (str):
# # # # # # # #    str = "oioasiojos"
# # # # # # # #    print(str)
   
# # # # # # # #    return

# # # # # # # # statement(str)
# # # # # # # # statement("oiasojilsfssf")


# # # # # # # def greetings(name):
# # # # # # #    #"This is docstring of greetings function"
# # # # # # #    print("Hello {}".format(name))
# # # # # # #    return

# # # # # # # greetings ("name")
# # # # # # # greetings("Paratima")
# # # # # # # greetings("Steven")


# # # # # # x = 4
# # # # # # d =0 
# # # # # # y = 5 
# # # # # # z = 232
# # # # # # def number (x, name):
# # # # # #    print ("The value of x ",x)
# # # # # #    print("Name of customer is : ",name)
   
# # # # # # number(z, name="ali")
   
   
      
# # # # # def info(name, age = 25):
# # # # #    print("Name of the employee :", name)
# # # # #    print("The age of the user : ", age)
   
   
# # # # # info(name= " ali ", age= 61)
# # # # # info(name="Usman")

# # # # def posFun(x,y, /, z):
# # # #    print(x + y + z)
   
# # # # print("Evaluating positional-only arguments: ")

# # # # posFun( 33, 34 , z = 32)

# # # # keyword argument 

# # # def numbers(*, a , b , c):

# # #    print( a * b * c)

# # # print(" Keyword arguments  :")
# # # numbers ( a = 4, b =7, c=2)

# # # variable function arguments 
# # def numbers (a , *var):
# #    print("variable function arguments")
# #    print(a)
# #    for v in var:
# #       print(var)
   
# # numbers(10,3,4,2)
# # python function with return value 
# def add (x,y):
#    z= x + y
#    return z
# a = 23
# b = 26
# result = add(a,b)
# print ("Result : ", result)

# # annoymynos function
# sum = lambda arg1, agrg2: arg1 + agrg2;
# print("Value of total : ", sum(10,23))
# print("toatl : ", sum(22,232))

total = 32
def sum( a , b ):
   total = a + b
   print("value of total",total)
   return total

sum(4,3)
print("value of total outside the function" , total)

