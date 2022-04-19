"""
Ref: https://www.w3schools.com/python/python_scope.asp
A variable is only available from inside the region it is created. This is called scope.
"""

#1. Local scope
"""
A variable created inside a function belongs to the local scope of that function,
and can only be used inside that function.
"""
def my_fun():
    x=300
    print(x)

my_fun()


#2. Function inside function
"""As explained in the example above, the variable x is not available outside
 the function, but it is available for any function inside the function:"""

def myfunc():
    x=300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()


#3. Global scope :
"""
A variable created in the main body of the Python code is a global variable
and belongs to the global scope.
Global variables are available from within any scope, global and local.
"""
x=500  #x has global scope
def myfunc():
    print(x)

myfunc()
print(x)


#Naming a variable :
"""
Naming Variables
If you operate with the same variable name inside and outside of a function,
Python will treat them as two separate variables, one available in the global
scope (outside the function) and one available in the local scope (inside the function):
"""
x = 300   #It is the different variable with global scope
def myfunc():
  x = 200  # it is different variable and scope  : inside the function
  print(x)

myfunc()
print(x)




# Global keyword :
"""
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
The global keyword makes the variable global.
"""

def myfunc():
  global x
  x = 300

myfunc()
print(x)

# Also, use the global keyword if you want to make a change to a global variable inside a function.
x = 300

def myfunc():
  global x
  x = 200

myfunc()
print(x)
