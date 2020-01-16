a=[1,2,3,1,2,3,34,3,3,2]
count=0
for i in a:
   for j in range(0,i+1):
       if i==j:
           count=count+i
           print(i,":",count)