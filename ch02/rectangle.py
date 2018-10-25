#!/usr/bin/env python3

# display a welcome message
print("The Area and Perimeter program")
print()

# get input from the user
length = int(input("Please enter the length: "))#used 1 space by spacebar in order to line up the length entry with the width entry below. 
width = int(input("Please enter the width:  "))#used 2 spaces by spacebar in order to line up the width entry with the length entry above.

# calculate area and perimeter of rectangle
area = length * width
perimeter = (2 * length) + (2 * width)
            
# format and display the result
print()
print("Area = ", area)
print("Perimeter = ", perimeter)
print()
print("Thanks K. Zoom for using this program!")


