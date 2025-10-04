a= [0,1,0,3,2]
b=[]
count=0
for i in a: 
   if i !=0:
     b.append(i)
   else:
     count += 1
for i in range(count):
     b.append (0)
print(b)
