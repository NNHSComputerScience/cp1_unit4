"""
  Name: 
  Date:
	Title: 2D lists and nested loops notes 
	Description: Introduces Two-dimensional lists (lists within lists) and nested for loops. This program continues to use the idea of a row of cars to represent a list.
"""
"""
  What are 2D lists or nested lists?
    A 2D list is a two-dimensional list, or a list containing 
      other lists or sequences. Think of it like a matrix with rows and columns, or in the case of a row of cars, a parking lot of rows and spaces.
      e.g.:
      
            col1    col2    col3    col4
    row1    ford    toyota  buick   gm
    row2    nissan  lexus   jeep    ford
    row3    bmw     honda   toyota  gm
    row4    tesla   bmw     jeep    toyota
    
    The more general term is a nested sequence (applies to tuples as well).
"""
#1 Creating a 2D list (i.e. our parking lot of cars)
lot = [
    ["ford", "toyota", "buick", "gm"],
    ["nissan", "lexus", "jeep", "ford"],
    ["bmw", "honda", "toyota", "gm"],
    ["tesla", "bmw", "jeep", "toyota"]
] 

if "ford" in lot:
    print (True)
else:
    print (False)

#2 Accessing a nested list (i.e. a row of cars)
print (lot[0])
print (lot[1])
print (lot[2])
print (lot[3])

#3 Accessing an individual element from a 2D list (i.e. a car)
print (lot[0][1])

# On your own: display each of the following...
print("\nThe 1st car in row 4") 
print (lot[3][0])

print("\nThe 2nd car in row 2") 
print (lot[1][1])

print("\nAll cars in the 3rd column:") 
for row in lot:
    print(row[2])
 
print("\nAll cars in the 4th row with a tab inbetween them:")
for car in lot[3]:
    print(car, end="\t")
print()

count = 0
for row in range(len(lot)): 
    if row == 3:
        for car in lot[row]:
            print(car, end="\t") 
print() 

# Challenge!
print("\nTry changing the first ford to an audi and then display it: ")
lot[0][0] = "audi"
print(lot[0][0]) 

input("\nPress Enter to Continue...")

# Using nested for loops to display the individual elements in row / column format
print("\nPrint the lot in row / column format with a single tab in between each car. \nAlso, display row and column headings accordingly, without hardcoding:")
for col in range(len(lot[0])):
    print("\tcolumn", col+1, end="")
print()
for row in range(len(lot)):
    print("row", row+1, "\t", end="")
    for col in range(len(lot[row])): 
        print (lot[row][col], end="\t\t")
    print()

input("\nPress Enter to Continue...")

#4 Unpacking a sequence - assigning each element of a sequence its own variable in a single line of code.


# Another nested list example: 
a_row = [["Ford", "Fusion"], ["Audi", "A4"], ["BMW", "3 Series"],["Jeep", "Wrangler"]] 
print(a_row)

print ("Make\t\tModel")
for car in a_row:
    make, model = car # unpacking a sequence
    print (make, "\t\t", model)

#5 Appending a new sequence
make = input("What is the car's make? ")
model = input("What is the car's model? ")
spot = [make, model]
a_row.append(spot)
print(a_row) 

#6 Sorting a 2D list
print("Row of cars sorted by make:")
a_row.sort()
print(a_row) 

#7 Sorting a 2D list by elements other than the first
#  We have a new module that we need to use... operator (and the itemgetter function).
print("Row of cars sorted by model:")

from operator import itemgetter     # only importing the function we need
a_row.sort(key=itemgetter(1))
print(a_row) 

#8 Reverse
print("\nRow of cars reverse sorted by model:") 
a_row.sort(key=itemgetter(1), reverse=True)
print(a_row) 

#9 Searching in and the break keyword
#   You have to loop through to find if an indvidual element is in a nested sequence
for car in a_row:
    if "BMW" in car:
        print("There is a BMW in the row.")
        break   # will break out of loop when a BMW is found!
    else:
        print ("Not a BMW.")

input("Press Enter to Exit")
