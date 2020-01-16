a="nalman is rrogrammer"
print(a[::]) # print total string
print(a[::-1])# print total string in reverse 
print(a[-2::-1])#
z=a.split(" ")
count=0
for i in z:
    if i[0]==i[-1]:
        count+=1
        #print(i)  "it will print the word stsrts  ends with same letter"
print(count)    #  "it will give the count of words that stsrts & ends with same charecter"
