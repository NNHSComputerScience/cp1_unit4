#list method traps
'''
  TRAP 1 
  You can not use a print statement with the sort method.
    The sort method is an action that sorts the contents of a list.
    You cannot print this action because it does not return a value
    as part of its action, it simply sorts the list in its stored place.
    If you try to use the print statement with the sort method
    you will get "None" returned as the value. See Below.
'''
##print ("_____TRAP 1 Example_____")
##listA = ["D", "C", "B", "A"] 
##print (listA.sort()) 
##This is also true with the reverse method... 
##print (listA.reverse()) 


''' 
  TRAP 2
  Do not use the reverse method in a for loop. If you do,
    it will reverse the order of the list each time through
    the loop, likely displaying your results inaccurately.
    This is a logic error, and will not result in a syntax error.
''' 
print ("\n\n_____TRAP 2 Example_____")
numlist = [1,2,3,4,5]
for num in numlist:
    numlist.reverse()
    print (num)

# The correct way 
print("\n\nThe correct way of displaying this list element by element in reverse")
numlist2= [1,2,3,4,5]
numlist2.reverse()
for num in numlist2:
    print(num) 
    
'''
  TRAP 3 
  Careful using concatenation with lists. You must be sure to that you are
  adding 2 lists for it to work properly. The preferred way to add to a list is 
  by using the list's append method, .append().
'''
numlist3 = [1,2,3,4,5]
###incorrect way
##result = numlist3 + numlist4 
print("\n\nThe correct way...")
numToAdd = [6]
result = numlist3 + numlist4
print("\n\nThe preferred way...")
numlist3.append(6)
print(result)
print(numlist3)

input("\nPress enter to exit.")
