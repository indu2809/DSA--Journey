
a = [1, 2, 3, 2, 1]
i=1
t=0
j=len(a)//2
flag=0
while (i<=j):
   if (a[t] == a[- i] ) :
        i+=1
        t+=1
   else: 
        flag=1
        break
if flag==0:
  print("True")
else:
  print("False")
  
