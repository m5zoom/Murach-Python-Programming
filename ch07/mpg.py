#!/usr/bin/env python3

import csv #Import of the "CSV module" that allows you to use writer functions and writer objects to write a list to disk.

# A file in the current working directory
FILENAME = "trips.csv" #Definition of a global constant named "FILENAME" that stores the name of the CSV file named "trips.csv".

def write_trips(trips): #Addition of a "write_trips()" function that writes the data from a two-dimensional list named "trips" that's passed to it as an argument. This list contains the data for each trip that's entered and is written to a CSV file named "trips.csv". 
    with open(FILENAME, "w", newline="") as file: #Use of the "with statement" as well as the "open() function" to open the CSV file. And in this open function you have the "w" (write) mode that writes data in the list to a file. Last, you have a third argument, "newline" with a value of an empty string. This enables "universal newlines mode", which allows the CSV module to read and write new lines correctly for all operating systems. 
        writer = csv.writer(file) #Here inside the "with statement", you have this first statement that calls the "writer() function" of the CSV module to get a CSV writer object for the file. This writer object converts the data into comma separated values. 
        writer.writerows(trips) #Here inside the "with statement", you have the second statement that calls the "writerows() method" of the CSV writer object to write all specified rows of the "trips" list to the CSV file. This method also automatically handles the formatting of the CSV records that are written to the disk.

def read_trips(): #Addition of a "read_trips()" function that reads the data from the "trips.csv" file and returns the data for the trips in a two-dimensional list named "trips". 
    trips = [] #Creation of an empty "trips" list. 
    with open(FILENAME, newline="") as file: #Use of the "with statement" as well as the "open() function" to open the CSV file. And in this open function, since this code doesn't specify the mode for opening the file, Python uses the default mode, which is the "read" mode. Last, you have a third argument, "newline" with a value of an empty string. This enables "universal newlines mode", which allows the CSV module to read and write new lines correctly for all operating systems. 
        reader = csv.reader(file) #Here inside the "with statement" you have this first statement that calls the "reader() function" of the CSV module to get a CSV reader object for the file. This reader object gets the data from the CSV file. 
        for row in reader: #Here use of a "for statement" to read each row in the reader object.
            trips.append(row) #After reading each row, it's then appended each row to the "trips" list.
    return trips #Use of a "return statment" that returns the "trips" list back to the function after it finishes appending all of the trips to the "trips" list. 
    
def get_miles_driven(): #Definition of a "get_miles_driven()" function that gets user input for the number of miles driven.
    while True: #Use of an infinite while loop. 
        miles_driven = float(input("Enter miles driven :     ")) #Use of the "input() function" that allows the user to enter data returned back as a "float" value from a "str" value.                     
        if miles_driven > 0: #Use of an "if statement" that evaluates the condition to be "True" if the value of "miles_driven" is greater than 0.       
            return miles_driven #Use of a "return statement" that returns the result of the calculation back to the calling statement if the "miles_driven" value is greater than 0. 
        else: #Use of an "else clause" that evaluates the condition to be "False" if the value of the "miles_driven" is less than 0. 
            print("Entry must be greater than zero. Please try again.\n") #Statement that is displayed on the console when the "miles_driven" value is less than 0.
            continue #Use of a "continue statement" that continues a loop by causing the execution to jump to the top of the loop. Also, this causes the loop to execute again by reevaluating its condition. 
    
def get_gallons_used(): #Definition of a "get_gallons_used()" function that gets user input for the number of gallons used.
    while True: #Use of an infinite while loop
        gallons_used = float(input("Enter gallons of gas:     ")) #Use of the "input() function" that allows the user to enter data returned back as a "float" value from a "str" value.                     
        if gallons_used > 0: #Use of an "if statement" that evaluates the condition to be "True" if the value of "gallons_used" is greater than 0.      
            return gallons_used #Use of a "return statement" that returns the result of the calculation back to the calling statement if the "gallons_used" value is greater than 0. 
        else: #Use of an "else clause" that evaluates the condition to be "False" if the value of the "gallon_used" is less than 0. 
            print("Entry must be greater than zero. Please try again.\n") #Statement that is displayed on the console when the "gallons_used" value is less than 0.
            continue #Use of a "continue statement" that continues a loop by causing the execution to jump to the top of the loop. Also, this causes the loop to execute again by reevaluating its condition. 

def list_trips(trips): #Definition of a "list_trips" function that displays the data in the "trips" list on the console. 
    print("Distance\tGallons\tMPG") #Display of each trip data that provides the distance of miles driven, gallons of gas used, and miles per gallon on the console.
    for i in range(len(trips)): #Use of a "for loop" that displays a numbered list of trips. This "for loop" achieves this by using the "i variable" to number each row(trip).
        trip = trips[i] #Use of a "trip"(row) variable which is assigned to a value "i" that corresponds to an index value from the range in the "trips" list. 
        print(str(trip[0]) + "\t\t" + str(trip[1]) + "\t\t" + str(trip[2])) #Use of the "print() function" that displays the number of miles driven, gallons of gas used and Miles Per Gallon from each column's indexes 0, 1, and 2 respectively for each "trip" (row) from the "trips" list. 
    print()

def main(): #Definition of a "main() function" that gets the data from the CSV file followed by displaying the data from the CSV file for the updated trips list. This is done after the user enters the last trip data to the "trips" list and before it calculates the "MPG" value as it's displayed on the console.  
    # display a welcome message
    print("The Miles Per Gallon application") #Display of the "Miles Per Gallon application" program title. 
    print()

    trips = read_trips() #Enhancement of the "main() function" in which it starts by getting data from the CSV file.
    list_trips(trips) #Enhancement of the "main() function" in which it lists the data after getting it from the CSV file. 

    more = "y" #Use of the "more" variable assigned a value of "y" for later input in the upcoming "while loop". 
    while more.lower() == "y": #Use of a while loop with the "lower() method" that converts uppercase letters to lowercase without changing the string itself as the variable "more" is equal to the value of "Y" or "y". 
        miles_driven = get_miles_driven() #The first statement of the while loop that calculates the number of miles driven from entries by the user. 
        gallons_used = get_gallons_used() #The second statment of the while loop that calculates the number of gallons used from entries by the user. 
                                 
        mpg = round((miles_driven / gallons_used), 2) #Calculation of the "MPG value" rounded to 2 decimal places. 

        print("Miles Per Gallon:\t" + str(mpg))# Display of the "MPG value" converted from a float to a string value. 
        print()

        trip = [] #Creation of an empty list for the next trip.
        trip.append(miles_driven) #Adding number of miles driven to the trip.
        trip.append(gallons_used) #Adding number of gallons used to the trip.
        trip.append(mpg) #Adding the MPG to the trip. 
        trips.append(trip) #Adding the trip list to the "trips" list. 
        write_trips(trips) #Use of a "write_trips() function" that writes the data from a two-dimensional "trips" list passed to it as an argument. Plus, the list contains data for each trip that's entered and written into a CSV file named "trips.csv".

        list_trips(trips) #Display of the data from the updated "trips" list. 
        
        more = input("More entries? (y or n): ") #Use of the "more" variable being assigned a value of "y or n" that will allow a while loop to either "continue" or "break" out of the loop by causing the execution to jump to the top of the loop as the user enters "y" or "n" as in input at the prompt. 
    
    print("Bye")

if __name__ == "__main__": #Use of an "if statement" that checks whether the current module is the main module. 
    main() #Calling of the "main() function" which means that the current module is the main module. Plus, the "main() function" starts the operation of the program.


#Reference pages used for this exercise include: pages 210 and 211 provides examples for how to write data from a two-dimensional list named "trips" to a CSV file called "trips.csv".
#Pages 212-215 on examples how to read data from a CSV file named "trips.csv" using the "reader() function" as well as returning the data for the trips into a two-dimensional list named "trips".    
#Pages 216 and 217 on examples that show how to use a "list_trips() function" that displays the data in the trips list on the console. 
#Page 216 and 217 on example how to enhance the "main() function" to get data from the CSV file and listing it to the console by using a "read_trips() function" as well as a "list_trips() function" before use of the "while loop". 
#Page 216 and 217 on examples how to enhance the "main() function" to add the last trip that's entered to the trips list after it calculates the "MPG value" as well as displaying the data for the updated "trips" list using the "list_trips() function" inside of the "while loop".     
#Note: Also used Chapter 3 for review on relational operators, boolean expressions, string methods, for statements and while loops, the "range() function" and review of the "Miles Per Gallon" program. 
