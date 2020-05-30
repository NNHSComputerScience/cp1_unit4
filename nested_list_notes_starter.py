"""
  nested lists notes 
  this program continues to use the idea of a row of cars as a list

  What are nested lists?
    A nested list is a two-dimensional list, or a list containing 
      other lists or sequences. Think of like a matrix with rows and columns,
      or in the case of a row of cars, a parking lot.
      e.g.:
      
            col1    col2    col3    col4
    row1    ford    toyota  buick   gm
    row2    nissan  lexus   jeep    ford
    row3    bmw     honda   toyota  gm
    row4    tesla   bmw     jeep    toyota
    
    The more general term is a nested sequence (applies to tuples as well).
"""
#1 Creating a nested list (our parking lot)
lot = [
    ["ford", "toyota", "buick", "gm"],
    ["nissan", "lexus", "jeep", "ford"],
    ["bmw", "honda", "toyota", "gm"],
    ["tesla", "bmw", "jeep", "toyota"]
]


#2 Accessing nested elements (rows of cars)


#3 Accessing an individual element within a nested element

# On your own: display each of the following...
print("\nThe 1st car in row 4:", end="") 

print("\nThe 2nd car in row 2:", end="") 

print("\nAll cars in the 3rd column:") 
 
print("\nAll cars in the 4th row with a tab inbetween them:")


# Challenge!
print("\nTry changing the first ford to an audi and then display it: ")


input("\nPress Enter to Continue...")

# Challenge!
print("\nTry printing the lot in column format with a single tab in between each car. \n \
Also, display row and column headings accordingly, without hardcoding:")


input("\nPress Enter to Continue...")

#4 Unpacking a sequence
#  Unpacking a sequence means assigning each element
#   its own variable in a single line of code.

# Another nested list example: 
a_row = [["Ford", "Fusion"], ["Audi", "A4"], ["BMW", "3 Series"],["Jeep", "Wrangler"]] 


#5 Appending a new sequence
 

#6 Sorting a nested sequence
print("\nRow of cars sorted by make:")


#7 Sorting a nested sequence by elements other than the first
#  We have a new module that we need to use... operator (and the itemgetter function).
print("\nRow of cars sorted by model:")
 

#8 Reverse
print("\nRow of cars reverse sorted by model:") 
 

#9 Searching in and the break keyword
#   You have to loop through to find if an indvidual element is in a nested sequence


input("\nPress Enter to Exit") 