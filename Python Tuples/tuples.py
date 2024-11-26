tup1 = (223,23,24,5,'ssffs',332,[3232,232],32)
print(tup1)
print(type(tup1))
tup2 = ()
print(tup2)
print(type(tup2))
tup3 = (32,)
print(tup3)
print(type(tup3))
print("tup1 values at index[2]  is : ",tup1[2] )
print("tupe1 values from index [1] to index is [4] is accessed by using the slicing operator : ",tup1[1:4])
tup3 = tup1 + tup2
print("tup3 is concatenations of tup1 and tup2", tup3)
tup4 = tup2 * 5
print("tup4 is repetition of tup2 ", tup4)
print("23 is prsent in tup3 or not checking the membership ",23 not in  tup3)
#del tup1;

# # print(tup1)
# print type(('abc', -4.24e93, 18+6.6j, 'xyz'));
# x, y = 1, 2;
# print ("Value of x , y : ", x,y);
print("tup3 vlaue at index [2] is : ", tup3[2:4])
print("tup3 vlaue at index [2] is : ", tup3[1:-2])

tup5 = (223,2332,23,2,2,233,'afas',2323)
tup6 = ('sdf','ssf',['sdfsf','sfsf'])
print("tup1 slicing till end tup5 [1:]",tup5[1:])
print("slicing form start to index[3]",tup5[:3])
print("slicing element form 0 index to the last index ",tup5[:])

print ('items from index 0 to 3 in tup5',tup5[0:3])
print ('items from index 2 to 4 in tup5',tup5[2:4])
