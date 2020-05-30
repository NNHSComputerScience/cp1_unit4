# Ocean's Five Heist Activity
# Creating nested sequences and working with lists.
import random

# create nested sequence with your team; each member's info is a list nested in one big list
theFive = [
    ["Danny Ocean", "potato", 4, 1],
    ["Basher Tarr", "banana", 4, 2],
    ["Linus Caldwell", "taco", 3, 3],
    ["Reuben Tishkoff", "fish", 2, 4],
    ["Tess Ocean", "salad", 1, 5]
]
print(theFive)
print()

# loop and test to see if each alias has an "A";
#   print a message saying the name of each member with a good alias
#   randomly assign a good alias if the alias does not have an A

for agent in theFive:
    if "a" in agent[1].lower():
        print(agent[0], "has a good alias")
    else:
        agent[1] = random.choice(("orange", "pasta", "tomato", "beans", "steak"))

print()
print(theFive)

# remove the moles using the del keyword
#   del can remove an element from a list by using an index value - del list[index]
#   index method - list.index(value) will return a list item's index value

counter = 0
for agent in theFive:
    if agent[3] == 3:
        mole = theFive.pop(counter)
        print("\n" + mole[3], "is a mole and has been removed from the team")
    counter += 1

print()
# replace any moles you deleted by concatenating new members
new = [("Isabel Lahiri", "Quesadilla", 3, 1),]
theFive += new
print(new[0][0], "has been added to the team to replace a mole.") # indexing nested elements
print()
print(theFive)
print()

# check to see if your team has one of each specialty
specs = [1, 2, 3, 4, 5] # list of each specialty number
for agent in theFive:
    for spec in specs:
        if agent[2] == spec:
            specs.pop[specs.index(spec)] # remove specialty from specs list if in team

# check strength of team
if len(specs) == 0: # if no specialties left in specs list, then all were found in team
    print("Your five have a good mix of specialties.")
elif len(specs) == 1:
    print("Your five are missing one specialty.")
else:
    print("Your five are missing", len(specs), "specialties")

    
input("\nPress enter to exit.")



           


