myset = [1,2,3,5,6]

for x in myset:
    print("x :",x)
    
setiterator = iter(myset)

while True:
    try:
        item = next(setiterator)
        print("item:", item)
    except StopIteration:
        break
    
numbers = {1,2,3,4,5}
squarset = {x**3 for x in numbers if x%2 == 0}
print(squarset)

newset = {3,2,5,32,2}
set_list = list(newset)
for index, item in enumerate(set_list):
    print("Index:", index, "Item:", item)
    
myset = set()

for x in range (5):
    myset.add(x)
    
print(myset)
    
    
for x in range (30)  :
    if x%3 == 0:
        myset.add(x)
    else:
        print("emptyset")
print(myset)