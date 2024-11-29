# import array as array_name
# obj = array_name.array(typecode[, intializer])

# obj = array_name.array(typecode[, initializer])

# import array as arr

# a = arr.array('i',[1,2,3])
# print (type(a),a)
# a = arr.array('u','Bat')
# print(type(a),a)
# a = arr.array("d",[1.1,2.2,3.3])
# print(type(a),a)

# from array import *
# array1 = array('i', [10,20,30,40,50])
# print(array1[-1])
# array1.insert(1,60)
# for x in array1:
#     print(x)

from array import *
array1 = array('i',[10,20,30,40,50])
array1.remove(40)

for x in array1:
    print(x)
    
print(array1.index(30))
print(array1)
array1[2] = 90
print(array1)