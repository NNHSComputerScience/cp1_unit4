# Ocean's Four Heist Activity
# Creating nested sequences and working with lists.
import random

#1. create nested sequence with your team; each member's info is a list nested in one big list
theFour = [
    ["Danny Ocean", "potato", 4, 1],
    ["Basher Tarr", "banana", 4, 2],
    ["Linus Caldwell", "taco", 3, 3], 
    ["Tess Ocean", "salad", 1, 4]
]
print(theFour)
print()

#2. loop and test to see if each alias has an "A";
#   print a message saying the name of each member with a good alias
#   randomly assign a good alias if the alias does not have an A

for i in theFour:
    if "a" in i[1].lower():
        print(i[0], "has a good alias")
    else:
        i[1] = random.choice(("orange", "pasta", "tomato", "beans", "steak"))

print()
print(theFour)

#3. remove the moles using the .pop() list method
#   .pop() method - removes an element from a list and returns it - list.pop(index_value)
#   .index() method - will return a list item's index value - list.index(value)

#counter = 0
for i in theFour: 
    if i[3] == 3:
        print("\n" + i[0], "is a mole and has been removed from the team")
        theFour.pop(theFour.index(i))
    #counter += 1

print()
#4. replace any moles you deleted by concatenating new members
theFour.append(["Isabel Lahiri", "Quesadilla", 3, 1])
print(theFour[-1][0], "has been added to the team to replace a mole.") # indexing nested elements
print()
print(theFour)
print()

#5. check to see if your team has one of each specialty
specs = [1, 2, 3, 4] # list of each specialty number 
for i in theFour:
    for j in specs:
        if i[2] == j:
            specs.pop(specs.index(j)) # remove specialty from specs list if in team

# check strength of team
if len(specs) == 0: # if no specialties left in specs list, then all were found in team
    print("Your four have a good mix of specialties.")
elif len(specs) == 1:
    print("Your four are missing one specialty.")
else:
    print("Your four are missing", len(specs), "specialties")

    
input("\nPress enter to exit.") 