"""
Dictionaries:
A dictionary stores key-value pairs, where each unique key is an index
which holds the value associated with it.

The keys and values can have any of the basic data types or structures we’ve
studied.

Dictionaries are unordered because the entries are not stored in a linear
structure.

Topics:
1. Structure  :{key:value,key:value,key:value}
2. Creating a dictionary
3. Operations on dictionary
"""

# Empty dictionary
empty_dict = {}
print(empty_dict)
#Output: {}

phone_book = {"Batman": 468426,
"Cersei": 237734,
"Ghostbusters": 44678}
print(phone_book)
#Output: {'Batman': 468426, 'Cersei': 237734, 'Ghostbusters': 44678}

# The dict() constructor can be used to create an empty dictionary
# A popular practice is to create an empty dictionary and add entries later.

# Empty dictionary
empty_dict = dict()
print(empty_dict)

phone_book = dict(Batman=468426, Cersei=237734, Ghostbusters=44678)
# Keys will automatically be converted to strings
print(phone_book)
#Output: {'Batman': 468426, 'Cersei': 237734, 'Ghostbusters': 44678}

# Alternative approach
phone_book = dict([('Batman', 468426),
('Cersei', 237734),
('Ghostbusters', 44678)])
print(phone_book)
#Output: {'Batman': 468426, 'Cersei': 237734, 'Ghostbusters': 44678}

#Accessing the values
phone_book = {"Batman": 468426,
"Cersei": 237734,
"Ghostbusters": 44678}
print(phone_book["Cersei"])
#Output: 237734
print(phone_book.get("Ghostbusters"))
#Output: 44678


#Checking if a key exists in a python dictionary or not
my_dict = {"name":"Mike", "address":"123 Happy Way"}
print("name" in my_dict) # True
print ("state" in my_dict) # False

#Extracting the python keys : In python 2 keys() method returns python list while in python 3 it returns view object
my_dict = {"name":"Mike", "address":"123 Happy Way"}
print(my_dict.keys())
#Output:  dict_keys(['name', 'address'])

"name" in my_dict # this is good
"name" in my_dict.keys() # this works too, but is slower

#Adding and updating the values in dictionary
phone_book = {"Batman": 468426,
"Cersei": 237734,
"Ghostbusters": 44678}
print(phone_book)
phone_book["Godzilla"] = 46394 # New entry
print(phone_book)
#Output: {'Batman': 468426, 'Cersei': 237734, 'Ghostbusters': 44678, 'Godzilla': 46394}
phone_book["Godzilla"] = 9000 # Updating entry
print(phone_book)
#Output: {'Batman': 468426, 'Cersei': 237734, 'Ghostbusters': 44678, 'Godzilla': 9000}

#Removing entries from dictionary
phone_book={"Batman":468426,
            "Cersei":234398,
            "Ghostbustes":354687}
print(phone_book)
#Output: {'Batman': 468426, 'Cersei': 234398, 'Ghostbustes': 354687}
del phone_book["Batman"]
print(phone_book)
#Output: {'Cersei': 234398, 'Ghostbustes': 354687}

#Deleting items can be done using pop() method or popitem() also
phone_book = {"Batman": 468426,
"Cersei": 237734,
"Ghostbusters": 44678}
print(phone_book)
cersei = phone_book.pop("Cersei")  #It returns the key of deleted item
print(phone_book)
print(cersei)
# Removes and returns an arbitrary pair as a tuple
lastAdded = phone_book.popitem()
print(lastAdded)


#Dictionary comprehensions
houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
new_houses = {n**2: house + "!" for (n, house) in houses.items()}
print(houses)
#Output: {1: 'Gryffindor', 2: 'Slytherin', 3: 'Hufflepuff', 4: 'Ravenclaw'}
print(new_houses)
#Output: {1: 'Gryffindor!', 4: 'Slytherin!', 9: 'Hufflepuff!', 16: 'Ravenclaw!'}



























#
