import re
import os 


gmailmatch= re.compile(r'(\w{1,})(\@)(\w{1,})(.com)')
for i,line in enumerate(open("shoib.txt",1)):
    for j in re.finditer(gmailmatch,line):

        print(j)