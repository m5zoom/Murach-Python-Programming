#!/usr/bin/env python3

import csv # Importing the csv module to use it's functions and objects available from the csv module that allows you to write a two-dimensional list stored as a text(CSV) file called "trips.csv" to disk.

# a file in the current directory
FILENAME = "trips.csv" # The use of a global constant called "FILENAME" that stores the name of the CSV file. This file is also in the working directory which is in the same directory as the program file. 

def write_trips(trips): # Definition of a "write_trips() function" that is an enhancement of the program that stores the data in the list, "trips" to a file named "trips.csv" using a CSV file. Note: When a program "writes data to a file", it "saves the data" that's in main memory (or RAM) to disk. In other words, think of this last statement as how a program "stores" data.
    with open(FILENAME, "w", newline="") as file: # Use of the "with statement" to automatically open and close(exit) a file when you're done using it even if an exception(error) occurs, the file will still close(exit) regardless. The opposite is normally the case when you use the "close() function" because this function prevents you from closing(exiting) the file properly when an exception(error) occurs. Plus it still closes(exits) the file after you're finished and after it has executed its block of statements. Also, in using the "with statement", all resources used by the file are released even if an exception occurs to end a program prematurely before properly closing(exiting). Next, in this statement you have the CSV file "trips.csv" along with the "w"(write) mode and the third argument, (newline="") that has an empty string value. This enables "universal newlines mode", which allows the csv module to read and write new lines correctly for all operating systems.  
        writer = csv.writer(file) # Use of the "writer() function" of the CSV module that returns a CSV writer object for the file. Also, this writer object converts the data into comma-separated values. 
        writer.writerows(trips) # Use of the "writerows() method" of the CSV writer object that writes all specified rows to the file, "trips.csv" as specified by the writer object using the CSV file format specified by the writer object. 

def get_miles_driven(): # Definition of the miles driven function which allows you to input values for number of miles driven.
    while True: # Use of a while statement that does an infinite while loop. 
        miles_driven = float(input("Enter miles driven :     "))                    
        if miles_driven > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
    
def get_gallons_used(): # Definition of the gallons of gas used which allows you to input the amount of gas used.
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
        
def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()

    trips = [] # Creation of an empty list of lists(two-dimensional list) that will contain the list of trips for the inputs of each trip. This is important that the empty list, "trips" is outside of the "while loop" because it will allow for the proper storing of data of all the rows(trip) in the list of the Excel spreadsheet program. To check that the program is running properly, when you open the spreadsheet program, you should see at least 3 trips displayed on the Excel spreadsheet in the order of the inputs entered after you ran the "mpg_write.py" program in the Python shell. 

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:\t" + str(mpg))
        print()

    # Enhancement of the program that stores the data for each calculation or trip(row) in a two-dimensional list.
        trip = [] # Creation of an empty list for each trip that adds a trip to the trips list.
        trip.append(miles_driven) #Adding number of miles driven for each trip.
        trip.append(gallons_used) #Adding number of gallons of gas used for each trip.
        trip.append(mpg) # Adding the calculated MPG value for each trip.
        trips.append(trip) #Adding each trip list to the trips list.
        
        more = input("More entries? (y or n): ")

    # Enchancement of the program to save the data in the list to a file named "trips.csv" when the user wants to exit the program.
    write_trips(trips) # Execution of the function, "write_trips(trips)" which stores the data from the list "trips" to the file, "trips.csv". Also, this satisfies the objective of enhancing the program to save the data in the list to a file named "trips.csv" whenever the user wants to exit the program. Last, this will allow you to view the "trips.csv" file using a spreadsheet program like Excel.   

    print("Bye K. Zoom")

if __name__ == "__main__":
    main()


#Reference pages used for this exercise includes: page 176 and 177 to use the "third example" of Figure 6-6 on how to add to a list of lists through programming. 
#Page 196 and 197 (references on writing and storing data to a file, as well as opening and closing files).
#Page 198 and 199 (Opening and closing files, use of the "with statement" with the "open function()". Plus, use of the "modes" of the "open function()").
#Page 210 and 211 (For writing(storing) a CSV file to disk using the "writer() function" of the CSV module and the "writerows() method" of the CSV writer object). The reference here is important becausse in introduces how to write(store) the data of a two-dimensional list to a CSV file. It's also useful for the introduction of importing the CSV module.  
#Page 212 and 213 (For reference on how to read a CSV file as well as how to modify the CSV format). Note: After opening a CSV file, if the code doesn't specify the "mode" for opening the file, Python uses the default mode, which is "read mode" (r) in order to read a CSV file.  
#Page 214 and 215 (For reference on storing data to a file and noting that any changes the user makes to the list are available even if the user chooses to exit and restart the program. Also, the program "mpg_write.py" only works if the file, "trips.csv" already exists. Here, you can use a spreadsheet program like Excel to create the starting file and save it in CSV format, and when you're finished you should be able to read the file without causing an exception. Next, the Python code in this program begins by defining a global constant named, "FILENAME" that stores the name of the CSV file. Then the code in this program defines two functions that return "miles_driven" and "gallons_used" to their respective functions as well as providing the "MPG value" when the "main() function" is executed. Last, since this global constant onlly specifies the name of the file, and not the path, the file must be in the working directory, which is usually the same directory as the program file.   
#Note: When you finish inputing entries for the data, after you hit "N" or "n" instead of "Y" or "y", it's only then the data from the list, "trips" is saved to the CSV file and you can then open up a spreadsheet program like Excel which in turn will also display the time when the "CSV(Excel) file" was last saved. And from there, you should be able to open the CSV file using a spreadsheet program like Excel where you'll be viewing all rows and columns or (trip) from the "trips" list in the "trips.csv" file.   
