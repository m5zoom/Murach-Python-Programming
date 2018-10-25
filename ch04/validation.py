#!/usr/bin/env python3

#Note: This "validation.py" module is a file that contain resuable code that stores the "get_float()" and "get_int()" functions.

def get_float(prompt, low, high):#Enhanced "get_float() function" with 3 arguments of a prompt, along with a low and high validity values. In other words, the sequence you listed here in the arguments will be the same sequence you'll see on the shell in the order they are called from the function. Here, you're first given a statement that ask for user entry, then followed by the user entering "low" and "high" values. This also corresponds with the function definition as it calls for 3 arguments in a sequencial order. 
    while True:#Code for infinite while loop that checks for entry into the "get_float()" function until value is greater than "0" and less than or equal to "1000". If it is, then it's "vaild" and holds as a "True" value. If not, then error statement appears.
        number = float(input(prompt))#Variable "number" thats connected to the "get_float() function" that accepts one argument which is a (prompt). In this case, the prompt that's passed to it is the first argument of the "get_float() function" which displays a "prompt" that asks the user to "Enter monthly investment" through the use of the "input" function. As the user enters a monthly investment, the entry is then converted to a "float" value. This number variable makes use of a "chain function" through the "input" and "float" functions. 
        if number > low and number <= high:#An "if statement" that uses an "AND" logical operator that evaluates the expressions on the left and right and returns a "True" value if both expressions are True. 
            is_valid = True #The variable "is_vaild" is set to True only when it meets the conditions of both expressions of the "AND" logical operator before it in the "if statement". This also checks for data validation.
            return number#A "return statement" that returns the result(value) of the calculation to the calling statement of the function. In other words, an entry being greater than "0" is valid and is returned back to the "get_float() function" where the result is a "float" value. 
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high,
                  "Please try again.")#An appropriate error message that's displayed when the user enters a value that's "not valid".
            
def get_int(prompt, low, high):#Enhanced "get_int() function" with 3 arguments of a prompt, along with a low and high validity values. In other words, the sequence you listed here in the arguments will be the same sequence you'll see on the shell in the order they are called from the function. Here, you're first given a statement that ask for user entry, then followed by the user entering "low" and "high" values. This also corresponds with the function definition as it calls for 3 arguments in a sequencial order. 
    while True:#Code for infinite while loop that checks for entry into the "get_int() function" until value is greater than "0" and less than or equal to "50". If it is, then it's "valid" and holds as a "True" value. If not, then error statement appears.
        number = int(input(prompt))#Variable "number" that connected to the "get_int() function" that accepts one argument which is a (prompt). In this case, the prompt that's passed to it is the first argument of the "get_int() function" which displays a "prompt" that asks the user to "Enter number of years" through the use of the "input" function. As the user enters a number of years, the entry is then converted to an "integer" value. This number variable makes use of a "chain function" through the "input" and "int" functions. Also, this function or "get_int() function" is called from the "main() function" to get the "years" entry.  
        if number > low and number <= high:#An "if statement" that uses an "AND" logical operator that evaluates the expressions on the left and right and returns a "True" value if both expressions are True.
           is_valid = True #The variable "is_valid" is set to True only when it meets the conditions of both expressions of the "AND" logical operator before it in the "if statement". This also checks for data validation.
           return number #A "return statement" that returns the result(value) of the calculation to the calling statement of the function. In other words, an entry being greater than "0" is valid and is returned back to the "get_int() function" where the result is an "integer" value.
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high,
                  "Please try again.")#An appropriate error message that's displayed when the user enters a value that's "not valid". 

    
def main(): #Definition of the "main" function that calls on the statements below. 
    choice = "y"
    while choice.lower() == "y":
       #get input from user through 2 call statements which are the "get_float()" and "get_int()" functions.
        valid_number = get_float("Enter number: ", 0, 1000)#Function called to test the "get_float() function definiton. It's valid if greater than "0" and less than or equal to "1000". 
        print("Valid number = ", valid_number)#Display of "Valid number" after meeting condidtions of the "get_float()" function defintion. 
        print()

        valid_integer = get_int("Enter integer: ", 0, 50)#Function called to test the "get_int() function definiton. It's valid if greater than "0" and less than or equal to "50". 

        print("Valid integer = ", valid_integer)#Display of "Valid integer" after meeting condidtions of the "get_int()" function defintion. 
        print()
            
        # see if the user wants to continue
        choice = input("Continue? (y/n): ")#The continuation or end of "while" loop, in which it gives the user the option to enter "yes" or "no". "Yes" continues the program. "No" ends the "while" loop and then prompts the user "goodbye". 
        print()

    print("Bye K. Zoom!")
    
if __name__ == "__main__":#Use of the "if statement" that checks if this program is the main module. Because this module is run without being imported, Python sets the "__name__" variable equal to "__main__". Plus, the use of the "if statement" checks if this module is the main module. Because it isn't the main module, you don't call on the "main() function" to start the operation of the main program. 
    main()#The calling of the "main() function" to start the operation of the main program. 
