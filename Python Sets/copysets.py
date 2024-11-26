seta= {3,3,42,42,23,234,2}
print("seta: ",seta, "id of seta",id(seta))
setb = seta.copy()
print("setb: ",setb, "id of seta",id(setb))
seta.update([4])
print("seta: ",seta, "id of seta",id(seta))

setc = set(seta)
print(setc)
setc.update([6])
print(setc)

orignalset = {3,4,5,6,7}
copiedset = {x for x in orignalset}
print("copiedset",copiedset)

