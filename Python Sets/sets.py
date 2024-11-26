myset = {1,3,3,5,4,26,3,2,4,23,23,12,2}
print(myset)
print(type(myset))
mylist = [1,4,6]
myset = set(mylist)
print(myset)
mixedset = {'ads',32,'sdf','dafd'}
print(mixedset)
mixedset.add(232633424)
print(mixedset)
mixedset.remove(32)
mixedset.discard('adss')
print(mixedset)
print('ads' in mixedset)
if 32 in mixedset:
    print("32 is present")
else:
    print("32 is not prsent in mixedset")

squaredset = {x**2 for x in range(1,6)}
print(squaredset)

squaresetnew = {x**3 for x in range(5,9)}
print(squaresetnew)

evenset = {x for x in range(1,11) if x % 2 ==0}
print(evenset)

nested_set ={(x,y) for x in range(1,3) for y in range(1,3)}
print(nested_set)
nested_set_2 = {(x,y) for x in range(11,54) for y in range (23,53)}
print(nested_set_2)

my_frozen_set = frozenset([1,2,3])
print(my_frozen_set)
my_frozen_set.add(4)
print(my_frozen_set)