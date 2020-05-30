#Starter code for color dictionary
# December 21, 2012 - Mayan Calendar ended and the world should have to
#Hey we are still arround :)
# Color Dictionary
# You would look up color values by the color and not by an inedx
#It is easier to catagorize the R G B values by color than index in a list
# you could use a nested list but this is where a dictionary is very useful
# Variable List:
#   colors - the dictionary of colors and there values
#more colors
#silver 192,192,192
#black 0,0,0
#white 255,255,255
#lemon chiffon 255,250,205
#golen rod 218,165,32



print ("Welcome to The Color Program \n\n")

# creates the dictionary: key color -- value R G B values
colors = {"Red": (255,0,0),
           "Green": (0,255,0),
           "Blue": (0,0,255),
          "Orange": (255,128,0),
          "Purple": (153,51,255)}
           
answer ="y"
while answer != "n":
    #Ask the user for a color
    Acolor = input("\nWhat color are you looking for?")
    Acolor = Acolor.title()

    print(colors.get(Acolor))


    # Display the R G B values if it is in the list
    print(colors.get(Acolor, "I do not know those"),"R G B values for ", Acolor,"\n")



    # If the Color is NOT in the list ask for the R G B values
    # add it to the dictionary of Colors
    answer = input("Would you like to add "+Acolor+" to the list of colors?")

    if answer.lower() in ("y","yes","yea","you bet ya","of course"):
        r = input("Red Value")
        g = input("Green Value")
        b = input("Blue Value")

        colors[Acolor] = (int(r),int(g),int(b))
        
    answer = input("Whould you like to look up another color?")


        
    # Ask the user if they need to look up more colors


#Display the entire dictionary in 2 columns
#Color Key      R G B values
for aShade in colors:
    print("{:10}".format(aShade),colors[aShade])

input("\n\nPress enter to exit.")

    
    
