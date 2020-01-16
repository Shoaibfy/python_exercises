import os

file=open("shoib.txt","a+")
# file_read= file.read()        #mode=="r"
# print(file_read)

# file_write= file.write("my name is shoaib")       # mode="w"
# print(file_write)

file_write= file.read()    #mode="a"
print(file_write)