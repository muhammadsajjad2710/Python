# # # # # # a = 21
# # # # # # b = 13
# # # # # # c = a+b 
# # # # # # print ("a+b = ",c)
# # # # # # c = a-b
# # # # # # print ("a-b = ",c)
# # # # # # c = a*b 
# # # # # # print("a*b",c)
# # # # # # c = a/b
# # # # # # print("a/b", c)
# # # # # # c = a//b
# # # # # # print("a//b", c)
# # # # # # c = a&b 
# # # # # # print("a&b", c)
# # # # # # c = a**b
# # # # # # print("a**b",c)

# # # # # a = 3 
# # # # # b =23
# # # # # if a ==b :
# # # # #     print("a ==b")
# # # # # else :
# # # # #     print("a!=b")
# # # # # if a >= b :
# # # # #     print ("a>=b")
# # # # # else :
# # # # #     print("a<=b")

# # # # a = 43 
# # # # b = 32
# # # # c = a + b 
# # # # print ("c = a+b", c)
# # # # c += a
# # # # print("c += a",c)
# # # # c -= a
# # # # print("c -= a",c)
# # # # c *= a
# # # # print("c *= a",c)
# # # # c %= a
# # # # print("c %= a",c)
# # # # c **= a
# # # # print("c **= a",c)
# # # # c //= a
# # # # print("c //= a",c)

# # # a = 10 
# # # b = 20
# # # c = a & b 
# # # print(c)
# # # c = a | b 
# # # print(c)
# # # c = a ^ b
# # # print(c)

# # var = 6
# # print ( var > 3 and var < 10 )
# # print ( not(var > 3 and var < 10) )
# # print ( var > 3 or var < 4 )

# # Membership Operators 
# a = 3
# b = 10
# list = [1,2,3,4,5]
# print ("a", a ,"b",b , "List",list)

# if a in list :
#     print (" a is present in the list ")
# else : 
#     print ("a is not present in the list ")
    
# if b not in list : 
#     print("b is not in list")
# else:
#     print("b is in list")

a = [1,2,3,4,5]
b = [1,2,3,4,5]
c = a 
print(a is c )
print(a is b)

print(a is not c)
print(a is not b)