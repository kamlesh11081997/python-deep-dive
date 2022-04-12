"""
A tuple is similar to a list, but you create them with parentheses instead of
square brackets. You can also use the tuple built-in. The main difference is
that a tuple is immutable while the list is mutable.

Topics:
1. Structure
2. Creating a tuple
3. Merging tuples
4. Nested tuples
5. Search
6. Immutability
"""

# Structure : The contents of a tuple are enclosed in parentheses, () .
# They are also ordered, and hence, follow the linear index notation.
car = ("Ford", "Raptor", 2019, "Red")
print(car)
#Output: ('Ford', 'Raptor', 2019, 'Red')

# Length
print(len(car))
#Output: 4

# Indexing
print(car[1])
#Output: Raptor

# Slicing
print(car[2:])
#Output: (2019,'Red')


#Merging tuples
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = hero1 + hero2
print(awesome_team)
#Output: ('Batman', 'Bruce Wayne', 'Wonder Woman', 'Diana Prince')

#Nested tuples
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = (hero1, hero2)
print(awesome_team)
#Output: (('Batman', 'Bruce Wayne'), ('Wonder Woman', 'Diana Prince'))


#Search in tuples:
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Moscow" in cities)
#Output: False

cities = ("London", "Paris", "Los Angeles", "Tokyo")
print(cities.index("Tokyo")) #Using index function to find the element in a tuple
#Output: 3

#Casting a tuple to a list
abc = tuple([1, 2, 3])
abc_list = list(abc)
print(abc_list)
#Output: [1,2,3]






























#
