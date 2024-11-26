set1 = {23,32,234,2342}
set2 = {94,4,23,32,435,66,67}
set3 = {34,324,23,32,67,232}
union_set1 = set1.union(set2)
union_set2 = set1 | set3
print(union_set1)
print(union_set2)
interset1 = set1.intersection(set2)
interset2 = set1 & set3
print(interset1)
print(interset2)

differenceset1 = set1.difference(set2)
differenceset2 = set1 - set3

print("difference set",differenceset1)
print("difference set",differenceset2)
symdifferenceset1 = set1.symmetric_difference(set2)
symdifferenceset2 = set1 ^ set3
print("symetic difference",symdifferenceset1)
print("symetic difference",symdifferenceset2)

a = {1,2,3,4}
b = {1,4}
c = {1,2,5}
issubset1 = b.issubset(a)
print(issubset1)
issubset2 = a.issubset(b)
print(issubset2)