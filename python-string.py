"""
String
Ref : https://docs.python.org/3.8/library/string.html
    : https://docs.python.org/3/library/functions.html#func-str
Source code : https://github.com/python/cpython

Defintion:
Strings are arrays of bytes representing Unicode characters. However, Python
does not have a character data type, a single character is simply a string with
a length of 1. Square brackets can be used to access elements of the string.

Strings are usually created in one of three ways. You can use single, double or
triple quotes.

Python Strigs are immutable i.e. we cannot change a string's content after creating.
e.g. my_string="abc"
    my_string[0]="d"
    Output: TypeError

"""

#Assigning a string
my_string = "Welcome to Python!"
another_string = 'The bright red fox jumped the fence.'
a_long_string = '''This is a
multi-line string. It covers more than
one line'''

print(my_string)
#Output: Welcome to Python!
print(another_string)
#Output: The bright red fox jumped the fence.
print(a_long_string)
"""Output: This is a
multi-line string. It covers more than
one line
"""

my_string = "I'm a Python programmer!"
otherString = 'The word "python" usually refers to a snake'
tripleString = """Here's another way to embed "quotes" in a string"""
print(my_string)
print(otherString)
print(tripleString)


""" Casting a value to string using str() method """
my_number = 123
my_string = str(my_number)
print(my_number)
print(my_string)
print(type(my_number))
#output: <class 'int'>
print(type(my_string))
#output: <class 'str'>

#ValueError : int('ABC')
# ValueError: invalid literal for int() with base 10: 'ABC'

""" Converting string to number """
x = int("123")
print(type(x))
#Output: <class 'int'>
print(x)


""" By checking the id of the object, we can determine that any time we assign a
new value to the variable, its identity changes. """
my_string = "abc"
print(id(my_string)) # 140029410169552
my_string = "def"
print(id(my_string)) # 140029409549312
my_string = my_string + "ghi"
print(id(my_string)) # 140029409549200


"""
Note: In python2.x, strings can only contain ASCII characters. If you require
unicode in python2.x, then we need to precede our string with a 'u'
e.g. my_unicode_string = u"This is unicode!"

But in python3.x all strings are unicode by default
"""


"""Concatenation of String """
string_one = "My dog ate "
string_two = "my homework!"
string_three = string_one + string_two
print(string_one)
print(string_two)
print(string_three)


"""
String methods:
upper() : To convert entire string into uppercase
lower() : To convert entrire string into lowercase
strip() : To remove leading and trailing spaces
capitalize() : Convert the first character to upper case
find() : Search the string for specified value and return the position where it is found
isdigit(): Return True if all characters in the string are digits
split() : Split the string at specified separator, and return a list
"""

string_one="Kamlesh"
print(string_one.upper())
#Output: KAMLESH
print(string_one.lower())
#Output: kamlesh

string_two=" kamlesh Kumar "
print(string_two.strip())
#Output: Kamlesh Kumar

string_three="kamlesh"
print(string_three.capitalize())
#Output: Kamlesh
print(string_three.find('k'))
#Output: 0

string_four="1234"
print(string_four.isdigit())
#Output: True

string_five="Kamlesh,Ramesh,Sita,Lalita,Krishna"
print(string_five.split(','))
#Output: ['Kamlesh', 'Ramesh', 'Sita', 'Lalita', 'Krishna']


"""
String slicing
I |   | l | i | k | e |    | P | y | t | h  | o  | n  | !  |
0 | 1 | 2 | 3 | 4 | 5 | 6  | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
-14|-13|-12|-11|-10|-9|-8  |-7 |-6 |-5 | -4 | -3 | -2 | -1 |

"""

my_string = "I like Python!"
print(my_string[:1]) # 'I'
print(my_string[0:12]) # 'I like Pytho'
print(my_string[0:13]) # 'I like Python'
print(my_string[0:14]) # 'I like Python!'
print(my_string[0:-5]) # 'I like Py'
print(my_string[:]) # 'I like Python!'
print(my_string[2:]) # 'like Python!'


my_string = "I like Python!"
print(my_string[0])
print(my_string[2])
print(my_string[7])
#print(my_string[100]) # IndexError: string index out of range


"""
String formatting : (aka String substitution)

%s is the important piece in the code above.
It tells Python that you may be inserting text soon. If you follow the string
with a percent sign and another string or variable, then Python will attempt to
insert it into the string. You can insert multiple strings by putting multiple
instances of %s inside your string.
"""

my_string="I like %s"%"Python"  #Python will be inserted at the place of %s
print(my_string)
#Output: I like Python

var="cookies"
newString="I like %s"%var
print(newString)
#Output: I like cookies

another_string = "I like %s and %s" % ("Python", var)
print(another_string) # 'I like Python and cookies'
#Output: I like Python and cookies

another_string = "I like %s and %s" % "Python"  #There is two %s, so it required two parameter
print(another_string)
# TypeError: not enough arguments for format string

my_string = "%i + %i = %i" % (1,2,3)
print(my_string) # '1 + 2 = 3'
float_string = "%f" % (1.23)
print(float_string) # '1.230000'
float_string2 = "%.2f" % (1.23)
print(float_string2) # '1.23'
float_string3 = "%.2f" % (1.237)
print(float_string3) # '1.24'


"""
Templates and the New String Formatting Methodology
This new method was actually added back in Python 2.4 as string templates,
but was added as a regular string method via the format method in Python
2.6. So it’s not really a new method, just newer
"""

print("%(lang)s is fun!" % {"lang":"Python"})
# Python is fun!

print("%(value)s %(value)s %(value)s !" % {"value":"SPAM"})
# SPAM SPAM SPAM !
print("%(x)i + %(y)i = %(z)i" % {"x":1, "y":2})
# KeyError: 'z'

print("Python is as simple as {0}, {1}, {2}".format("a", "b", "c"))
# 'Python is as simple as a, b, c'
print("Python is as simple as {1}, {0}, {2}".format("a", "b", "c"))
# 'Python is as simple as b, a, c'
xy = {"x":0, "y":10}
print("Graph a point at where x={x} and y={y}".format(**xy))
# Graph a point at where x=0 and y=10
