def my_gen():
    n=1
    print("printing n value first time")
    yield n
    n+=1
    
    print("printind n+1 value second time")
    yield n
    n+=1
    
    print("printind n+1 value third time")
    yield n

a=my_gen()
print(next(a))
print(next(a))
print(next(a))
#print(my_gen)   # it will display the generator object