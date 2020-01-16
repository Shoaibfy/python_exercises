with open ("shoib.txt","a") as file:
    # print(file.read())     # read all content in a file
    # print(file.readline())     #read first line from the file
   # print(file.readlines())         #read all lines line by line \n the entire content
   file.write('Tendulkar')
   print(file.seek(4))              # takes pointer to given index seek(4)
   file.write('p')                  # replace seek(4) index with given char