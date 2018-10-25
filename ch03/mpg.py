#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

another_trip = "y"
while another_trip == "y": # Using a while loop statement to allow the user to make multiple(repeat) entries and get the miles per gallon for more than one trip.
    

        # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon:      "))
        
    if miles_driven <= 0:
            print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
            print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
            print("Cost per gallon must be greater than zero. Please try again.")
    else:
            print() # Prints a blank line between Enter cost per gallon and Miles Per Gallon statement entries
            
        # calculate and display miles per gallon
            mpg = round((miles_driven / gallons_used), 2)
        # calculate and display total gas cost
            total_gas_cost = round((gallons_used * cost_per_gallon), 1)
        # calculate and display cost per mile
            cost_per_mile = round(total_gas_cost / miles_driven, 1)
            print("Miles Per Gallon:          ", mpg)
            print("Total Gas Cost:            ", total_gas_cost)
            print("Cost Per Mile:             ", cost_per_mile)
            print() # Prints a blank line between Cost Per Mile and Enter miles driven statement entries

    another_trip = input("Get entries for another trip (y/n?) ") # Allows user to repeat entries using while loop
    print() # Prints a blank line between "Get entries for another trip?" and "Enter miles driven" statements


print()
print("Bye K. Zoom")



