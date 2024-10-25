
# # # # # # # # # # # # b=int("100")
# # # # # # # # # # # # b=int(10.232)
# # # # # # # # # # # # print(b)
# # # # # # # # # # # x = int(10.23)

# # # # # # # # # # a=0b101
# # # # # # # # # # print ("a:",a, "type:",type(a))

# # # # # # # # # # b=int("0b101011", 2)
# # # # # # # # # # print ("b:",b, "type:",type(b))

# # # # # # # # # a = 43 
# # # # # # # # # b = bin(a)
# # # # # # # # # print("a is decimal : ",a ,"b is binary number : ", b, sep=",")

# # # # # # # # # c = int('25',8)
# # # # # # # # # print(c)
# # # # # # # # # x = 0o107
# # # # # # # # # print (x, type(x))
# # # # # # # # # d = c+x
# # # # # # # # # print(d,type(d))


# # # # # # # # a = 0x0803
# # # # # # # # print(a)
# # # # # # # # print(type(a))
# # # # # # # # c = 0x223e4
# # # # # # # # print(c)

# # # # # # # #num_string = "A1"
# # # # # # # num_string = "A1X001"
# # # # # # # number = int(num_string, 16)
# # # # # # # print("num_string : ",num_string, "number : ", number)

# # # # # # a = hex(161)
# # # # # # print("hexadecimal for a : ", a)

# # # # # a = 2223
# # # # # b=0b10 #binary
# # # # # c=0O10 #octal
# # # # # d=0XA #Hexadecimal
# # # # # e = a+b+c+d
# # # # # print(e)
# # # # # print (type(a))
# # # # # print (type(b))
# # # # # print (type(c))
# # # # # print (type(d))

# # # # a=float(0b10)
# # # # b=float(0O10)
# # # # c=float(0xA)

# # # # print (a,b,c, sep=",")

# # # # a = float("-1213.42")
# # # # b = float("3.2e4")
# # # # print ("a = ",a, "b =", b)
# # # # a = float("Infinity")
# # # # print(type(a))

# # # # a= float('Nan')
# # # # print(a)

# # # a = 35 + 4e-2j
# # # b = 2 + 33e23j
# # # print (a , type(a))
# # # c = a+b
# # # print ( c, type(c))

# # a = complex(2+ 4j, 5 + 3j)
# # #b = complex(232e2,223e-2)
# # b = complex(223+ 32j)
# # print("a number is : ", a, "b number is : ", b )

# # a=complex(1+2j, 2-3j)
# # print (a, type(a))
# a = "5.5+.3j"
# b = complex(a)
# print("Complex number : ", b)
# print("real part ",b.real, "imgainary part ",b.imag)
# print(b.conjugate)

a =  4 + 5j
print(a.conjugate())
