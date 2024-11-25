# list1 = ["Rohan", "Physics", 21, 69.75]
# print(list1)
# print(type(list1))
# list2 = [1,2,3,4,5]
# list3 = ["a","b","c","d"]
list1 = ['physics','chemistry',1912,22322,'sasd']
list2 = [23,23,23,435,224,635,633,3,23,22]
print("list1 [3] :",list1[3])
print("list2 [2:6] :",list2[1:6])
print(list1)
#updating the list
list1 [3] = [21]
print("list1 [3] :",list1[3])

del list1[3];
print(list1)
print("concatenation of list1 and list2 ",list1+list2)
print("repetiton for list2 is : ", list2 * 3)
print("membership ", [21] not in list2 )
print("clearlist1", list1.clear())
print("list1", list1)
print("list1 appending ", list1.append([32,23,132,'jsks']))
print(list1.append('iososos'))
print("list1", list1)
print(list2.count(23))
list3 = list2.copy()
print(list3)
list4 = list3.copy()
print(list4)
list5 = list4.extend('safs')
print(list4)
print(list4)
print("lowest index variable appeared ",list4.index(23))
list5 = [323,232,52,32,22,224,5252,2322]
print("inserting 4 at index 3",list5.insert(3,4),list5)
print("removing elements from top",list5.pop())
print(list5)
print("removing elements from top",list5.pop())
print(list5)
print("removing elements from top",list5.remove(323))
print(list5)
print("sorting list",list5.sort())
print(list5)
#print("comparing list5 and list4 elements",cmp(list4,list5))
print(len(list5))
print("max of list5",max(list5))
print("min of list5",min(list5))
list6= list1(set)