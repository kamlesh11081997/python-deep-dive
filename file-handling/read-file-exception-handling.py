#Ref : https://www.programiz.com/python-programming/file-operation

#Error prone way to read a file
with open('script.txt','r') as file:
    for line in file.readlines():
        print(line)


#Exception handling
import os
if os.path.exists('script.txt'):
    with open('script.txt','r') as file:
        for each_line in file:
            try:
                (role,line_spoken)=each_line.split(':',1)
                print(role,end='')
                print(' said: ',end='')
                print(line_spoken,end='')
            except:
                pass

#Usig try and except instead if and specifying the exception type
try:
    with open('script.txt','r') as data:
        for each_line in data:
            try:
                (role,line_spoke)=each_line.split(':',1)
                print(role,end='')
                print(' said: ',end='')
                print(line_spoken,end='')
            except ValueError:
                pass
except IOError:
    print("The data file is missing!")
