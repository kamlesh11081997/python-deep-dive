"""
*args and *kwargs in python
Special Symbols Used for passing arguments:-
1.)*args (Non-Keyword Arguments) : We don't need keyword to pass the argument
2.)**kwargs (Keyword Arguments)  : We need keyword to pass the argument

We use *args and **kwargs as an argument when we are unsure about the number of
arguments to pass in the functions.

"""

#General function to add numbers:
def adder(x,y,z):
    print("Sum: ",x+y+z)

adder(1,2,3)
#what if we pass 5 arguments
#adder(1,2,3,4,5) #Error
"""Traceback (most recent call last):
  File ".\args-kwargs.py", line 18, in <module>
    adder(1,2,3,4,5)
TypeError: adder() takes 3 positional arguments but 5 were given"""


# *args : if we are not sure about the no. of arguments we use *args
def adder(*num):
    sum=0
    for n in num:
        sum+=n
    print("Sum: ",sum)
adder(1,2,3)
adder(1,2,3,4)
adder(1,2,3,4,5)

# **kwargs , to pass the keyword argument having variable length we use it
def intro(**data):
    print(" Data type of argument: ",type(data))

    for key,value in data.items():
        print("{} is {}: ".format(key,value))

intro(Firstname="kamlesh",lastname="Kumar",address="hazaribag")
intro(Firstname="Ramesh",lastname="Sharma",address="Ranchi")


"""
Ref: https://www.programiz.com/python-programming/args-and-kwargs 
Things to Remember:
*args and **kwargs are special keyword which allows function to take variable length argument.
*args passes variable number of non-keyworded arguments and on which operation of the tuple can be performed.
**kwargs passes variable number of keyword arguments dictionary to function on which operation of a dictionary can be performed.
*args and **kwargs make the function flexible.
"""
