"""
Ref: https://docs.python.org/3/tutorial/datastructures.html#
Topic covered:
1. Creating a list
2. Slicing a list
3. Adding item to a list
4. Searching for values in a list
5. Removing items from a list
6. Removing items from a list: Bonus Round
7. List in a boolean context
"""
"""
List Definition:
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets: ['a','b','c'] or [1,2,3] or [1,'a','4']
# List items are ordered, changeable and allow duplicates
# List items are indexed, the first item has index [0], the second item has index [1] etc.
"""

#Creating a list
a_list=['a','b','mpilgrim','z','example']
print(a_list)
#output : ['a', 'b', 'mpilgrim', 'z', 'example']
print(a_list[0])
#output : a
print(a_list[4])
#output: example
print(a_list[-1])
#output: example
print(a_list[-3])
#output: mpilgrim


#Slicing a list
a_list=['a','b','mpilgrim','z','example']
print(a_list)
#output : ['a', 'b', 'mpilgrim', 'z', 'example']
print(a_list[1:3])
#output : ['b','mpilgrim']
print(a_list[1:-1])
#output: ['b','mpilgrim','z']
print(a_list[0:3]) #a_list[0:3]==a_list[:3]
#output: ['a','b','mpilgrim']
print(a_list[:3])
#output: ['a','b','mpilgrim']
print(a_list[:])
#output : ['a', 'b', 'mpilgrim', 'z', 'example']

#Adding items to a list
"""
Method to add element in list:
1. append(data) :It takes a single argument, which can be any datatype. Thus it can append a single value or append a list or any object.
2. insert(index,data) : It insert a single item at the given index of list
3. extend(data) :It takes a single argument which is always a list, and adds each of the items of that list to a_list
"""
a_list=['a']
a_list=a_list+[2.0,3]
print(a_list)
#Output: ['a',2.0,3]

a_list.append(True)
print(a_list)
#Output: ['a',2.0,3,True]

a_list.extend(['four','/'])
print(a_list)
#Output: ['a',2.0,3,True,'four','Ω']

a_list.insert(0,'/') #It insert the element at zero index
print(a_list)
#Output: ['Ω', 'a', 2.0, 3, True, 'four', 'Ω']

"""
Searching for a vlues in a list
"""
a_list=['a', 'b', 'new', 'mpilgrim', 'new']
print(a_list.count('new'))  #It returns count of given elements
#Output: 2

print('new' in a_list)
#Output : True

print('c' in a_list)
#Output: False

print(a_list.index('mpilgrim'))
#Output: 3 (index of element)

print(a_list.index('c'))
#Traceback (most recent call last):
# File "/usercode/__ed_file.py", line 17, in <module>
# print (a_list.index('c') ) #\u2464
#ValueError: 'c' is not in list


"""
Removing items from a list
del list[index] : We can use the del statement to delete a specific item from a list.
remove(): We can remove the item by their value if it exists in a list using remove() method
pop() : pop() list method removes the last element in the list and returns the value it removed.
"""
a_list = ['a', 'b', 'new', 'mpilgrim', 'new']
print(a_list[1])
#Output: 'b'
del a_list[1]
print (a_list)
#Output: ['a', 'new', 'mpilgrim', 'new']
print (a_list[1])
#Output: new

a_list = ['a', 'new', 'mpilgrim', 'new']
a_list.remove('new')
print (a_list)
#Output: ['a', 'mpilgrim', 'new']
a_list.remove('new')
print (a_list)
#Output: ['a', 'mpilgrim']
print (a_list.remove('new'))
#Traceback (most recent call last):
# File "/usercode/__ed_file.py", line 10, in <module>
# print (a_list.remove('new'))
#ValueError: list.remove(x): x not in list

a_list = ['a', 'b', 'new', 'mpilgrim']
print (a_list.pop())
#Output: mpilgrim
print (a_list)
#Output: ['a', 'b', 'new']
print (a_list.pop(1) )
#Output: b
print (a_list)
#Output: ['a', 'new']
print (a_list.pop())
#Output: new
print (a_list.pop())
#Output: a
print (a_list.pop())
#Traceback (most recent call last):
# File "/usercode/__ed_file.py", line 20, in <module>
# print (a_list.pop()) #\u2462
#IndexError: pop from empty list


"""
List in boolean context
In a boolean context, an empty list is false.
Any list with at least one item is true.
Any list with at least one item is true. The value of items is irrelevant.
"""
def is_it_true(anything):
    if anything:
        print("Yes,  it's true")
    else:
        print("No it's false")
print(is_it_true([]))
#Output: no,it's false

print(is_it_true['a'])
#Output: yes,it's true

print(is_it_true([False]))
#Output: yes,it's true


"""
Sort a list : [34, 23, 67, 100, 88, 2]
sort(): a method in the list used to sort the elements in python
Note: sort() method don't return anything. SO if we try to store the value it returns None (null in other languages)
"""
alpha_list=[34, 23, 67, 100, 88, 2]
alpha_list.sort()
print(alpha_list)
#Output: [2, 23, 34, 67, 88, 100]

"""
List comprehension :
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
Example:
Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
Without list comprehension you will have to write a for statement with a conditional test inside:
"""

#Without list comprehension :
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
#Output: ['apple', 'banana', 'mango']


#With List comprehension :
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
#Output: ['apple', 'banana', 'mango']


#Other examples of python list comprehensions
x = [i for i in range(5)]
print(x)
#Output : [0, 1, 2, 3, 4]

x=['1','2','3','4','5']
y=[int(i) for i in x]
print(y)
#Output:[1,2,3,4,5]

#Flattening the list using list comprehensions
vec=[[1,2,3],[4,5,6],[7,8,9]]
flatvec=[num for elem in vec for num in elem]
print(flatvec)
#Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Iterating over list of string
myStringList = [
' Hello how are you?',
'I\'m good ',
' I\'m good too ']
myStrings = [s.strip() for s in myStringList]
print(myStrings)
#Output: ['Hello how are you?', "I'm good", "I'm good too"]





























##
