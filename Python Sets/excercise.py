list1 = [1,2,3,4,5,6]
list2 = [4,5,3]

set1 = set(list1)
set2 = set (list2)
commonelements = set1 & set2
commonlist = list(commonelements)
print("common elements of the list",commonelements)
issubset = commonelements.issubset(set1)
print(issubset)

list4 = [1,2,4,5,6,7,84,2,6,7,2,3,3]
print(list4)
set4 = set(list4)
print(set4)
newlist = list(set4)
print("unique elements of the list is: ",newlist)