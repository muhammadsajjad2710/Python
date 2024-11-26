# tup1 = (322,24)
# print(tup1)

# x,y = tup1
# print("x :",x,"y :",y)

# tup1 = (10,20,30)
# x, y,z = tup1
# x, y, p = tup1

f = (32,35,76,97,35,87,4)
# x,y,*z = x
# print("x value is : ",x,"y value is :",y, "z value is : ",z)
x,*y,z = f

print("x value is : ",x,"y value is :",y, "z value is : ",z)

pb = (32,35,76,97,35,87,4)
*x,y,z = pb
print("x value is : ",x,"y value is :",y, "z value is : ",z)

