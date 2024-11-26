s1 = {1,2,3}
s2 = {3,5}
s3 = s1 | s2
print(s3)
s4 = s1.union(s3)
print(s4)
s1.union(s2)
print(s1)
s5 = s1.update(s2)

print(s5)

set1 = {1,2,3,4,4}
set2 = {4,5,6,3,2}
s3 = {*set1,*set2}
print(s3)

jionedset = {x for s in [set1,set2] for x in s }
print(jionedset)

x = {1,2,3}
y = { 3,4}
combinset = set()
for n in x:
    combinset.add(n)

for p in y:
    combinset.add(p)
    
print(combinset)