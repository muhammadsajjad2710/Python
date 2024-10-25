import keyword
print ("Hello World")

amount = 100

if amount>500:
    rate =10
    
else: 
    rate = 5
    
interest = amount*rate/100 

print ("interest = ",  interest)

abc = keyword.iskeyword("else")
print(abc)