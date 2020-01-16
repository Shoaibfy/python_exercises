x=[]
y=[]
even_squrs_1_10=[]
odd_squrs_1_10=[]
for i in range(1,10):
    # if i%2==0:
    #     print(i*i)        to print  squares of even numbers 
    x.append(i*i) 
print (sum(x),"sum of 10 natural numbers")
for j in range(1,100):
    y.append(j)
print(sum(y),"sum of 100 natural numbers")
diff=sum(y)-sum(x)
print("the difference b/w 10 & 100  squares of ",diff)
for k in range(1,10):
    if k%2==0:
        print(k,":",k*k,"even squares of 10")
    else:
        print(k,":",k*k,"odd squares of 10")