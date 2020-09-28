import csv
import sys

FILENAME = "movies_test.csv" #Changing the filename in the global constant from "movies.csv" to "movies_test.csv". This is in order to test the program that allows the user to create a new file for the movies that's newly added by the user. Plus, the connection here is that all this comes after commenting out the two statements in the except clause for the "FileNotFoundError". Note: All this means is that anytime you change the filename in the global constant, this will allow you to create a new file when you "add" a new movie to the movies list on the Python console.   

def exit_program():
    print("Terminating program.")
    sys.exit()

def read_movies():
    try:
        movies = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        return movies
    except FileNotFoundError as e:
##        print("Could not find " + FILENAME + " file.") #Commenting out the first statement in the except clause for FileNotFoundError. Note: Used pages 230-231, 236-237, 242-243
##        exit_program()  #Commenting out the second statement in the except clause for FileNotFoundError.
        return movies #Use of a "return statement" in the except clause to return the empty movies list that's initialized in the try block of statements. Also, use of the "return statement" will cause the program to continue if the file can't be found by allowing the program to create a new file for the movies that the user adds. 
    except Exception as e:
        print(type(e), e)
        exit_program()

def write_movies(movies):
    try:
        with open(FILENAME, "w", newline="") as file:
##            raise BlockingIOError("Error message raised for testing an exception handler.") #Note: Used pages 242-243 #Use of a raise statement to raise an exception to test an exception handler. 
            writer = csv.writer(file)
            writer.writerows(movies)
    except OSError as e: #Modifying the "write_movies () function" that uses an except clause that handles the child "OSError class" as exception object "e". Note: Used pages 232-239
        print(type(e), e) #Use of the "print () function" to display the class name as well as the error message of the exception object. 
        exit_program() #Use of the "exit_program () function" that calls to exit(stop execution) the program. 
    except Exception as e:
        print(type(e), e)
        exit_program()

def list_movies(movies):
    for i in range(0, len(movies)):
        movie = movies[i]
        print(str(i+1) + ". " + movie[0] + " (" + str(movie[1]) + ")") #Use of the "str() function" to convert the year to a string before it can be displayed. Otherwise, you'd get a "TypeError" because you can't convert an "integer" to a "string value" without using a "str() function" in this print statement. Note: Pages 226-227 
    print()
    
def add_movie(movies):
    name = input("Name: ")
    while True: #Use of an infinite while loop. 
        try:#Use of a try statement that catches an exception. 
            year = int(input("Year: "))#Use of the "int() function" converting the string input to an "integer value". (Note: Used pages 228, 230 and 238 data validation)
        except ValueError: #Use of an "except clause" that handles a ValueError exception. Note: "ValueError" is the name of the exception. 
            print("Invalid integer. Please try again.")
            continue  #Use of a "continue statement" that continues the "try statement" in the while loop if the user's input is an "Invalid integer entry". 
        if year <= 0: #Use of an "if statement" that checks for "data validation" by checking the condition in this statement if the user's integer entry is greater than zero. If "less than or equal to" zero, then the user gets an error message that states an "Invalid entry" and the while loop continues by executing the "try statement" again. If "greater" than zero, the while loop "breaks". Therefore, the entry is "Valid" and the rest of the statements in the function are executed.  
            print("Year must be greater than zero. Please try again.")
            continue #Use of a "continue statement" that continues the "try statement" in the while loop if the user's entry is "less than or equal to" zero. 
        else: #Use of an "else clause" that checks the condition in the "if statement" of the while loop if the user's entry is "greater than" zero. If this is the case, this allows the use of a "break statement" that occurs during this "add_movies() function".
            break #Use of a "break statement" that breaks out of the while loop and allows the rest of the statements in the function to be executed. 
    movie = []
    movie.append(name)
    movie.append(year)
    movies.append(movie)
    write_movies(movies)
    print(name + " was added.\n")

def delete_movie(movies):
    while True:
        try:
            number = int(input("Number: "))
        except ValueError:
            print("Invalid integer. Please try again.")
            continue
        if number < 1 or number > len(movies):
            print("There is no movie with that number. " +
                  "Please try again.")
        else:
            break
    movie = movies.pop(number - 1)
    write_movies(movies)
    print(movie[0] + " was deleted.\n")

def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

def main():
    display_menu()
    movies = read_movies()
    while True:        
        command = input("Command: ")
        if command == "list":
            list_movies(movies)
        elif command == "add":
            add_movie(movies)
        elif command == "del":
            delete_movie(movies)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()


#Reference pages for this exercise include: Pages 226-229 for examples on using a "try statement to handle a ValueError exception as well as taking a user entry and convering from "string" to an "integer" value with the help of the "str() function".  
#Pages 230-231 on examples working with "data validation" as well as working with "return statements" to return the values in calculation checking that they are all "valid" entries by the user.
#Pages 238-239 on examples using "complete data validation" as well as working with both the "try clause" and "except clause" checking for ValueError inside of the while loop.
#Pages 236-237 on examples working with the "FILENAME" in a global constant. Plus, working with the "exit_program() function" as well examples using the except clause for the "FileNotFoundError" child class.  
#Pages 242-243 on examples working with a "raise statement" that shows how to raise an exception to test an exception handler. 
