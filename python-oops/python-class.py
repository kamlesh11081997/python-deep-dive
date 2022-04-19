"""
Everything in python is an object.
What this means is that every
thing in Python has methods and values. The reason is that everything is
based on a class. A class is the blueprint of an object.
"""
x="Kamlesh"
attrs=dir(x)
print(attrs)
#Output : It will print all the methods and attributes associated with object x
"""
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
'__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
'__iter__', '__le__', '__len__', '__lt__','__mod__', '__mul__', '__ne__',
'__new__', '__reduce__', '__reduce_ex__','__repr__', '__rmod__', '__rm
ul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize',
'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
'isdigit', 'isidentifier','islower', 'isnumeric', 'isprintable', 'isspace',
 'istitle', 'isupper', 'join','ljust', 'lower', 'lstrip', 'maketrans', 'partition',
 'replace', 'rfind', 'rindex', 'rjust', 'rpartition','rsplit', 'rstrip',
 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate',
'upper', 'zfill']
"""


# Python class :
"""
The class name must follow standard Python variable naming
rules (it must start with a letter or underscore, and can
only be comprised of letters, underscores, or numbers). In
addition, the Python style guide (search the web for PEP 8)
recommends that classes should be named using what PEP 8
calls CapWords notation (start with a capital letter; any subsequent
words should also start with a capital).
"""

#Simplest class in python
class MyFirstClass:
    pass

a=MyFirstClass()
b=MyFirstClass()
print(a)
print(b)
#output:
#<__main__.MyFirstClass object at 0x000001D4EF547910>
#<__main__.MyFirstClass object at 0x000001D4EF6DF250>

print(a is b) #output: False

#Adding attributes :
"""We can set arbitrary attributes on an instantiated object using dot notation"""

class Point:
    pass

#adding attribute at run time
p1=Point()
p2=Point()

p1.x=5
p1.y=6

p2.x=3
p2.y=7

print(p1.x,p1.y)  #output : 5 6
print(p2.x,p2.y)  #output : 3 7



""" Adding method to the class"""
class Point:
    def reset(self):   # Adding a method to python class
        self.x = 0
        self.y = 0
p=Point()
p.reset()
print(p.x,p.y)  #Output: 0 0


"""
Self in python class :
Ref : https://www.geeksforgeeks.org/self-in-python-class/
Self represents the instance of the class. By using the self keyword we can
access the attributes and methods of the class in python.
'self is always pointing to Current Object.'
'self is a convention and not a python keyword'
'self is the first argument to be passed in constructor and instance method'
"""

class Check:
    def __init__(self):
        print("Address of self: ",id(self))
obj=Check()
print("Address of class object:",id(obj))
#Output:
#Address of self:  2593621551328
#Address of class object: 2593621551328


"""
Never name a method of your own with leading and trailing
double underscores. It may mean nothing to Python today, but
there's always the possibility that the designers of Python will add
a function that has a special purpose with that name in the future.
When they do, your code will break.
"""
#sample class to find distance between two points
import math
class Point:
    def move(self,x:float,y:float)->None:
        self.x = x
        self.y = y
    def reset(self)->None:
        self.x = 0
        self.y = 0
    def calculate_distance(self,other:Point)->float:
        return math.hypot(self.x-other.x,self.y-other.y)


point1=Point()
point2=Point()
point1.reset()
point2.move(5,0)
print("Distance: ",point1.calculate_distance(point2))



"""
python __init__ method
Ref: https://www.geeksforgeeks.org/__init__-in-python/
The __init__ method is similar to constructors in C++ and Java. Constructors are
used to initialize the object’s state. The task of constructors is to
initialize(assign values) to the data members of the class when an object of
class is created. Like methods, a constructor also contains collection of
statements(i.e. instructions) that are executed at time of Object creation.
"""

class Point:
    def __init__(self,x:float,y:float)->None:
        self.move(x,y)
    def move(self,x:float,y:float)->None:
        self.x = x
        self.y = y
    def reset(self)->None:
        self.x = 0
        self.y = 0
    def calculate_distance(self,other:Point)->float:
        return math.hypot(self.x-other.x,self.y-other.y)
point1=Point(3,5)
point2=Point(5,3)
print("x={} : y={}".format(point1.x,point1.y))
print("x={} : y={}".format(point2.x,point2.y))
print("Distance : ",point1.calculate_distance(point2))


"""
Python : __repr__ method
Ref: https://medium.com/swlh/understanding-repr-and-str-in-python-65dd41538943
Ref : https://stackoverflow.com/questions/1535327/how-to-print-instances-of-a-class-using-print
In Python, __repr__ is a special method used to represent a class's objects as
a string. __repr__ is called by the repr() built-in function. You can define
your own string representation of your class objects using the __repr__ method.
Special methods are a set of predefined methods used to enrich your classes.

__repr__ method is just like toString() method in java to get string representation
of a java object.
"""
from typing import Optional
class Sample:
    def __init__(
    self,
    sepal_length:float,
    sepal_width:float,
    petal_length:float,
    petal_width:float,
    species: Optional[str]=None
    )->None:
        self.sepal_length=sepal_length
        self.sepal_width=sepal_width
        self.petal_length=petal_length
        self.petal_width=petal_width
        self.species=species
        self.classification : Optional[str]=None

    def __repr__(self) -> str:
        if self.species is None:
            known_unknow="UnknownSample"
        else:
            known_unknown="KnownSample"
        if self.classification is None:
            classification= ""
        else:
            classification=f", {self.classification}"
            return (
                f"{known_unknown}("
                f"sepal_length={self.sepal_length}, "
                f"sepal_width={self.sepal_width}, "
                f"petal_length={self.petal_length}, "
                f"petal_width={self.petal_width}, "
                f"species={self.species!r}"
                f"{classification}"
                f")"
                )
s1 = Sample(
sepal_length=5.1, sepal_width=3.5, petal_length=1.4,
petal_width=0.2, species="Iris-setosa")
#>>>s1
#output: KnownSample(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_
#         width=0.2, species='Iris-setosa')














































#





























#
