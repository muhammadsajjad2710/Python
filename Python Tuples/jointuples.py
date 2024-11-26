t1 = (34,65,3)
t2 = ("ds","sf",24)
# t3 = t1 + t2
# print("t3:",t3)
# t4 = [item for subtuple in [t1,t2] for item in subtuple]

# print("Joined Tuple",t4)

l1 = list(t1)
l2 = list(t2)

l1.extend(l2)
print("combined List :",l1)
t1 = tuple(l1)
print("combined tuple : ",t1)

t3 = sum((t1,t2),())
print("combined tuple using sum function:", t3)
t4 = (2,21)
for t in t4:
    t4+=(t,)
print (t4)