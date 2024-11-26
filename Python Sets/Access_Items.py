langs = {"C", "C++", "Java", "Python"}

# Accessing set items using a for loop

for lang in langs:
    print (lang)
    
for n in langs:
    print(n)
    
my_set = {1,2,3,4,5}
# Accessing set items using list comprehension

accessed_items = [item for item in my_set]
print(accessed_items)

import itertools

original_set = {1,2,4,5,3}

is_subset = {1,2}.issubset(original_set)
print("{1,2},is a subset of the original set : ",is_subset)

subsets_with_two_elements = [set(subset) for subset in itertools.combinations(original_set,2)]
print("Subsets with two elements: ", subsets_with_two_elements)

subset = {3,4}.issubset(original_set)
print("{3,4} is subset of original set",subset)
powerset = [set(subset) for subset in itertools.combinations(original_set,3)]
print("subset with three elements :",powerset)

if subset in original_set:
    print("subset is present in original set ")
else:
    print("subset is not present in orignal set")
    
if subset not in original_set:
    print("subset is present in original set ")
else:
    print("subset is not present in orignal set")