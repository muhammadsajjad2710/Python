marks = {'ali':34,'usman':93,'ahmad':43}
print(marks)
marks['ahmad'] = 87
print(marks)
marks['ahmad'] = 'usman'
print(marks)

marks.update({'ahmad':56,'akbar':48,'iftikhar':89})
print(marks)

marks1 = {"sharad": 51, "Mushtaq":61,"Laxman": 89,'akbar':42}
newmarks = {**marks, **marks1 }
print('**marks dictionary after update: \n',newmarks)

fruits1 = {"apple":3,'Mango':2}
fruits2 = {'apple':4,'Mango':5,"orange":8}
fruits = fruits1 | fruits2
print(fruits)
marks |= marks1
print("marks dictionary after the update",marks)
marksupdate = marks.setdefault("malik" , 49)
print(marks)
print(marks.setdefault("awan",342))
print(marks)

from collections import defaultdict
d = defaultdict(int)
d["a"] += 1
print(d)

d = defaultdict(list)

d['b'].append(1)
print(d)

def defaultvalue():
    return "N/A"
d = defaultdict(defaultvalue)
 
print(d)