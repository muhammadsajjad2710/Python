# # t1 = (23,24,55,3243,23442,13,23,32,23,32,23,32,23,32,45,54,54,56,45)
# # t2 = ()
# # for x in t1:
# #     if x not in t2:
# #         t2+=(x,)

# # print("Original Tuple",t1)
# # print("Unique Numbers",t2)
# t1 = (1,2,4,7,5,2)
# ttl = 0
# for x in t1:
#     ttl+=x

# print("Sum of all numbers using loop:", ttl)

# ttl = sum(t1)


# print("Sum of all numbers sum() function:",ttl)
import random
t1 = ()
for i in range(5):
    x = random.randint(0,100)
    t1+=(x,)
print(t1)
    
    