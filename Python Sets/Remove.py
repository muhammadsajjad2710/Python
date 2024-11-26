myset = {23,44,32,233,23}
myset.remove(23)
print(myset)
myset.discard(23)
print(myset)
removed_element = myset.pop()
print(removed_element)
print(myset)
removed_element = myset.pop()
print(removed_element)
print(myset)
removed_element = myset.pop()
print(removed_element)
print(myset)
# removed_element = myset.discard()
# print(removed_element)
# print(myset)

newset = {1,2,4,5}
print(newset)
newset.clear()
print(newset)
newset.clear()
print(newset)
s1 = {23,2,4,3}
s2 = {32,2,5,2,3}
s1.difference_update(s2)
print("removed common element using difference-update method",s1)

# s1 -= s2
# print(s2)
# s2.symmetric_difference(s1)
# print(s1)

s3 = {34,34,23,23,32,67,99,98}
s4 = {34,23,32,23,233,232}
s3 -= s4
print(s3)

s5 = {3,3,345,23,23,234}
s6 = {3,234,234,342,3424,3244}
differentelements = s5 ^ s6
print("differentelements :", differentelements)
s6.symmetric_difference(s5)
print(s6)

s5.intersection_update(s6)
print("common elements between s5 and s6 is : ", s5)

s7 = s5.intersection(s6)
print(s7)

a = {1,2,3,4}
b = {4,3,5,6,8}
print("a: ",a, "b: ",b)
# a.symmetric_difference_update(b)
c = a.symmetric_difference(b)
print(c)
