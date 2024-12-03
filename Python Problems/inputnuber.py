n = int(input("Enter number n :"))
print(n)

if n%2 != 0:
    print("Weird")
else:
    if n%2 == 0  in range(2, 5):
        print("Not Weird")
    elif n%2 == 0  in range(6,21):
        print("Weird")
    else:
        if n>20 and n%2 == 0 :
        
            print("Not Weird")
            
        else:
            print("Nothing")