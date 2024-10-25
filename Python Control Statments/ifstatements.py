# marks = 80
# result = ""
# if marks < 30:
#     print("Student result is fail")
# elif marks < 60:
#     print("Student result is passed ")
# else:
#     print ("Student result is excellent")
marks = int(input("Please enter the marks : "))
result = ""

if marks < 30 : 
    result = "Student is failed in exams"
elif marks >70:
    result = "Student is passed with distinction in exams"
else:
    result = "Student is passed in exams"
    
print(result)