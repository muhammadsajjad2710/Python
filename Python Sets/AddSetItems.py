language = set()
print(language)
print(type(language))
language.add('C')
language.add("C++")
language.add('Python')
print(language)
language.update({"kguryd"})
print(language)
myset = {1,3,5}
myset.add(4)
#myset.update(8)
print(myset)
myset.update([9])
print(myset)

myset.update(language)
print(myset)
set2 = {"hello"}
print(set2)
set1 = set("hello")
print(set1)
set1.update("world")
print(set1)

set1 = {1,2,3,5,6}
set2 = {4,2,7}
set3 = {8,9}
set4 = set1.union(set2)
set5 = set1 | set3
print(set4)
print(set5)

square_set = {num ** 4 for num in set5}
print("square set:", square_set)