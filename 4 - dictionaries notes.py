#Dictionaries Guided Notes

# Dictionaries: an object that stores a collection of data.
#     Each element in a dictionary has ________ parts:
#     a _____________ and a ______________.
#     Often referred to as mappings


# 1) Creating a dictionary
#     you create a dictionary using curly braces { }
#     you seperate a key from it's value using a colon :
#     you seperate elements using a comma

phonebook = {
    "Chris": "555-1111",
    "Katie": "555-2222",
    "Joanne": "555-3333",
    "Andy": "555-4444"
              }


print phonebook #Notice that elements are not stored
                        #in a particular order. They display differently.
                        #So we can not use indexing/slicing.

# 2) Retrieving a value
print phonebook["Chris"]

# 3) in & not in
if "Katie" in phonebook:
    print phonebook["Katie"]

if "James" not in phonebook:
    print "James is not in the phonebook"

# 4) Adding elements to an existing Dictionary
phonebook["Joe"] = "555-5555"
# if the key exists then it doesn't add it, it updates it
phonebook["Chris"] = "555-0001"
print phonebook
# Keys must be unique, No duplicates
# won't give you a syntax error, just ignores duplicate

# 5) Deleting elements from an existing dictionary
del phonebook["Chris"]
print phonebook

# 6) Getting the number of elements in a dictionary
print len(phonebook)

# 7) adding to a dicitonary with user input
# YOU TRY!
name=raw_input("What is the person name to add? ")
number=raw_input("What is the persons #? ")
phonebook[name] = number
print phonebook

# 8)- get() Gets the value associated with a specified key.
#               Returns a default value if not found
dial = phonebook.get("Andy")
print dial
print
dial = phonebook.get("Douglas", "That name isn't here")
print dial
print

# 9) Other dictionary methods

# A- sort()
# the sort method does not work with dictionaries.
# You do not need to know how to sort dictionaries.

# B- clear() Clears the contents of a dictionary
### phonebook.clear()
### print phonebook








