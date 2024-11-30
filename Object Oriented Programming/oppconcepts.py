# # class Smartphone:
# #     # constructor
# #     def __init__(self,device, brand):
# #         self.device = device
# #         self.brand = brand
        
# #     # method of the class
    
# #     def description(self):
# #         return f"{self.device} of {self.brand} supports Android 14"
    
# # # creating object of the class

# # phoneObj = Smartphone("Smartphone", "Samsung")
# # print(phoneObj.description())

# # class Desktop:
# #     def __init__(self):
# #         self.__max_price = 25000
        
# #     def sell(self):
# #         return f"Selling Price: {self.__max_price}"
# #     def set_max_price(self, price):
# #         if price > self.__max_price:
# #             self.__max_price = price
            
# # # Object 
# # desktopObj = Desktop()
# # print(desktopObj.sell())

# # # modifying the price directly 
# # desktopObj.__max_price = 35000

# # print(desktopObj.sell())

# # # modifying the price using setter function
# # desktopObj.set_max_price(35000)
# # print(desktopObj.sell())

# # class Parent:
# #     parentAttr = 100
# #     def __init__(self):
# #         print("Calling parent constructor")
        
# #     def parentMethod(self):
# #         print("Calling parent method ")
# #     def setAttr(self, attr):
# #         Parent.parentAttr = attr
        
# #     def getAttr(self):
# #         print("Parent attribute :",Parent.parentAttr)
        
# # # define child class 
# # class Child(Parent):
# #     def __init__(self):
        
# #         print("Calling child constructor")
            
# #     def childMethod(self):
# #         print("Calling child method")
        
# # # instance of child 
# # c = Child()
# # # child call its method
# # c.childMethod()
# # # calls parent's method
# # c.parentMethod()
# # # again call parent's method
# # c.setAttr(200)
# # # again call parent's method 
# # c.getAttr()

# #!/usr/bin/python
# # define parent class
# class Parent:        
#    parentAttr = 100
#    def __init__(self):
#       print ("Calling parent constructor")

#    def parentMethod(self):
#       print ("Calling parent method")

#    def setAttr(self, attr):
#       Parent.parentAttr = attr

#    def getAttr(self):
#       print ("Parent attribute :", Parent.parentAttr)

# # define child class
# class Child(Parent): 
#    def __init__(self):
#       print ("Calling child constructor")

#    def childMethod(self):
#       print ("Calling child method")

# # instance of child
# c = Child()  
# # child calls its method        
# c.childMethod() 
# # calls parent's method     
# c.parentMethod()  
# # again call parent's method   
# c.setAttr(200)  
# # again call parent's method     
# c.getAttr() 

# class Animal:
#     def speak(self):
#         return "I make a sound"

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# # Polymorphism
# def make_animal_speak(animal):
#     print(animal.speak())

# dog = Dog()
# cat = Cat()

# make_animal_speak(dog)  # Output: Woof!
# make_animal_speak(cat)  # Output: Meow!

# class Parent:
#     def myMethod(self):
#         print("Calling parent method")    
        
# class Child(Parent):
#     def myMethod(self):
#         print("Calling child method")  
        
# c = Child()
# p = Parent()
# p.myMethod()
# c.myMethod()   

class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
    
    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(4,3)
v2 = Vector(5,6)
print(v1+v2)