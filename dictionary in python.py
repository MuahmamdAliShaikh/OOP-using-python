d={'a':'apple','b':'bat','c':'cat','d':'dog'}
print(d.keys())
print(d.items())
print(d.values())
print(d["a"]) #for access items
d.update({'b':'Balloon'}) #for change items
print(d)
print(d.get("c")) #for access items
d["color"]='red'  #for add items
print(d)
del d['a']  #for delete items. Pop is also used inplace of del
print(d)

for i in d: #or for i in d.keys():
    print(i) #this will only access keys
for i in d: #or for i in d.values
    print(d[i]) #this will access values only

for x, y in d.items():
  print(x, y)

print(d.copy()) #for the copy of dictionary
