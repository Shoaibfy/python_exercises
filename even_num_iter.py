my_list=[1,2,3,4,5,6,7,8,9,10]
list2=[]
for i in  my_list:
    if i%2==0:
        list2.append(i)
print(list2)
x=iter(list2)
print(next(x))
print(next(x))
print(next(x))
