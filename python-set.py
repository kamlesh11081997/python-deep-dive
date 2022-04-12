"""
Set:
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is unordered, unchangeable*, and unindexed.
Sets cannot have two items with the same value.(No duplicate allowed)
Ref: https://www.w3schools.com/python/python_sets.asp
     https://docs.python.org/3/tutorial/datastructures.html#sets

Topics:
1. Structure
2. Creating a Set : The set() constructor
3. Adding elements
4. Deleting elements
5. Iterating a set
"""

#Creating a set
random_set = {"Kamlesh", 1408, 3.142, (True, False)}
print(random_set)
#Output: {'Educative', (True, False), 3.142, 1408}
print(len(random_set)) # Length of the set
#Output: 4

#The set() constructor
empty_set = set()  #It's a way to initialize an empty set which returns a set object
print(empty_set)
#Output: set()
random_set = set({"Kamlesh", 1408, 3.142, (True, False)})
print(random_set)
#Output: {'Educative', (True, False), 3.142, 1408}



#Adding elements
"""
add(): to add a single item
update(): to add multiple value in set, input must be another set, list or tuple or string
"""
empty_set = set()
print(empty_set)
empty_set.add(1)
print(empty_set)
empty_set.update([2, 3, 4, 5, 6])
print(empty_set)


#Deleting items
"""
discard() : it don't generate error if element is not found
remove()  : it generates an error if element is not found
"""
random_set = set({"Educative", 1408, 3.142, (True, False)})
print(random_set)
random_set.discard(1408)
print(random_set)
random_set.remove((True, False))
print(random_set)


#Iterating a set
"""
The for loop can be used on unordered data structures like sets. However, we
wouldn’t know the order in which the iterator moves meaning elements will be
picked randomly.
"""
odd_list = [1, 3, 5, 7]
unordered_set = {9, 10, 11, 12, 13, 14, 15, 16, 17}
print(unordered_set)
for num in unordered_set:
    if(not num % 2 == 0):
        odd_list.append(num)
print(odd_list)
#Output: [1, 3, 5, 7, 9, 11, 13, 15, 17]




































#
