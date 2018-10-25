#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
gas_costpergallon = float(input("Enter cost per gallon:\t\t"))



# calculate miles per gallon
mpg = miles_driven / gallons_used
mpg = round(miles_driven / gallons_used, 1)

#calculate total gas cost
total_gascost = round(gallons_used * gas_costpergallon, 1)

#calculate cost per mile
cost_permile = round(total_gascost / miles_driven, 1)

            
# format and display the result
print()
print("Miles Per Gallon:\t" + str(mpg))
print("Total Gas Cost:\t\t" + str(total_gascost))
print("Cost Per Mile:\t\t" + str(cost_permile))
print("Bye K. Zoom")


