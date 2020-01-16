import os
with open("hd senaries.jpg","rb") as ref:
    x = ref.read()
    with open("sh.png","wb") as wef:
    # for line in ref:
        wef.write(x)
    
    # with open("shoib.txt","wb") as wef:
       