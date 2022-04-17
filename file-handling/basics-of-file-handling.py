#How to read a file in python
"""
Python has a built-in function open() that we can use to open a file in python

Python file reading methods:
read() : It reads all lines in python and print
readline() : It reads just one line
readlines() : It reads all lines in python and return python list of lines

"""

#Example to open a file in python
#It will open a file named script.txt in read mode only. Note we didn't pass the
#fully qualified path to the file that we want to open. Python will automatically
#look into the directory where the script is saved. If it doesn't find the file
# it will throw an IOError
handle=open("script.txt")

#Second example is fully qualified path of the file
# Note in window the back slash is used to specify any location so we have to use
# 'r' before the file path to treat the string as raw string and to escape the
#special character
handle=open(r"C:\Users\kamle\OneDrive\Desktop\COMPUTER SCIENCE PLAYGROUND\PYTHON_PROJECTS\file-handling\script.txt","r")



#3 different method to read the file in python

#Method 1:
handle=open("script.txt","r")
data=handle.read() #it read all lines in python and print
print(data)
handle.close()

#Method 2:
handle=open("script.txt","r")
data=handle.readline() #read just one line
print(data)
handle.close()


#Method 3:
handle=open("script.txt","r")
data=handle.readlines()  #It returns a python list of all lines present in file
print(data)
handle.close()

"""
Read file in python piece by piece
Instead of reading the whole file, we'll read a file in a small chunk, if file size
is very large
"""
#Reading all data at once
handle=open("script.txt")
for line in handle:
    print(line)
handle.close()

#Let's read the file in chunk

handle=open("script.txt")
while True:
    data=handle.read(1024)
    print(data)
    if not data:
        break


#Lazy method in python to read a large file(e.g. 4GB)
def read_in_chunks(file_object,chunk_size=1024):
    """Lazy function (generator) to read a file by piece.
    Default chunk size is : 1K """
    while True:
        data=file_object.read(chunk_size)
        if not data:
            break
        yield data

with open('script.txt') as f:
    piece=read_in_chunks(f,1024)
    print(piece)
    print(next(piece)) #It will print first 1024 KB data
    #print(next(piece)) #It will print next 1024 KB data
    for piece in read_in_chunks(f,1024):
        print(piece)



































#
