# concanetating tuples 
tup1 = (23,25,6,'gf',2,6,3,8,2,6,4,52,32,5,342,8)
tup2 = ('sd','sa')
print("concatenation of two tuples is ",  tup1 + tup2)
print("slicing in tup1 is : ", tup1[1::7])

# converting tup to list and then doing changes in the list and then again convet it into the tuple 
list1 = list(tup1)
print(type(list1))
list1 [3] = ["changes"]
list1.append('ali')
list1.insert(243433,212355353)
print(list1)
print(tup1)
tup1 = tuple(list1)
print(tup1)

# Original tuple
T1 = (10, 20, 30, 40)
# Convert tuple to list
list_T1 = list(T1)
# Elements to be added
new_elements = [50, 60, 70]
# Updating the list using append()
for element in new_elements:
    list_T1.append(element)
# Converting list back to tuple
updated_tuple = tuple(list_T1)
# Printing the updated tuple
print("Original Tuple:", T1)
print("Updated Tuple:", updated_tuple)