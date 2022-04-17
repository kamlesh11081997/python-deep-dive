"""
Ref : https://www.geeksforgeeks.org/writing-to-file-in-python/
Python provides inbuilt functions for creating, writing and reading files.
There are two types of files that can be handled in python, normal text files
and binary files (written in binary language, 0s and 1s).

Text files: In this type of file, Each line of text is terminated with a special
character called EOL (End of Line), which is the new line character (‘\n’)
in python by default.
Binary files: In this type of file, there is no terminator for a line and the
data is stored after converting it into machine-understandable binary language.
"""

"""
Access mode :
read only ('r') : open the file to read only
write only ('w') : open the file for writing
write and read ('w+') : open the file for reading and writing
append only : ('a') : open the file for writing, new data will be appended after old data
read and write ('r+') : open the file for reading and writing
append and read ('a+'): open the file for reading and writing
"""

"""
Writing to a file:
1. write() : Inserts the string 'str1' in a single line in a text file
file_object.write(str1)

2. writelines() : It writes multiple string at a single time from a list of string elements
file_object.writelines(L) for L =[str1,str2,str3]
"""

file=open("filetowrite.txt","w")
L=["This is Hazaribag\n","This is Paris\n","This is London\n"]
file.write("Hello\n")
file.writelines(L)
file.close()

#reading using read() method
print("="*100)
print("Output of read function is: ")
file=open("filetowrite.txt","r")
print(file.read())
file.close()

#reading using readline() method
print("Output of readline() function is : ")
file=open("filetowrite.txt","r")
print(file.readline())
file.close()

#reading using readlines() method
print("Output of readlines() function is : ")
file=open("filetowrite.txt","r")
print(file.readlines())
file.close()
