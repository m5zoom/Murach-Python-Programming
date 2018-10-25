#!/usr/bin/env python3

#Note: This "future_value.py" program works in conjunction with the "validation.py" module where both programs work together in sharing the load performing multiple tasks between related instructions of similiarly coded functions. A good example of this explanation is how the one argument calls in the main() function of the "future_value.py" program calls on the main() function from the "validation.py" module where the similarly coded functions in this module execute or "follow" the rules of operation from the 2 function definitions that are coded before the "main() function definition" of the "validation.py" program.

## def get_float(prompt, low, high):#Enhanced "get_float() function" with 3 arguments of a prompt, along with a low and high validity values. 
##    while True:#Code for infinite while loop that checks for entry into the "get_float()" function until value is greater than "0" and less than or equal to "1000". If it is, then it's "vaild" and holds as a "True" value. If not, then error statement appears.
##        number = float(input(prompt))#Variable "number" thats connected to the "get_float() function" that accepts one argument which is a (prompt). In this case, the prompt that's passed to it is the first argument of the "get_float() function" which displays a "prompt" that asks the user to "Enter monthly investment" through the use of the "input" function. As the user enters a monthly investment, the entry is then converted to a "float" value. This number variable makes use of a "chain function" through the "input" and "float" functions. 
##        if number > low and number <= high:#An "if statement" that uses an "AND" logical operator that evaluates the expressions on the left and right and returns a "True" value if both expressions are True. 
##            is_valid = True #The variable "is_vaild" is set to True only when it meets the conditions of both expressions of the "AND" logical operator before it in the "if statement". This also checks for data validation.
##            return number#A "return statement" that returns the result(value) of the calculation to the calling statement of the function. In other words, an entry being greater than "0" is valid and is returned back to the "get_float() function" where the result is a "float" value. 
##        else:
##            print("Entry must be greater than", low,
##                  "and less than or equal to", high,
##                  "Please try again.")#An appropriate error message that's displayed when the user enters a value that's "not valid".
            
## def get_int(prompt, low, high):#Enhanced "get_int() function" with 3 arguments of a prompt, along with a low and high validity values.
##    while True:#Code for infinite while loop that checks for entry into the "get_int() function" until value is greater than "0" and less than or equal to "50". If it is, then it's "valid" and holds as a "True" value. If not, then error statement appears.
##        number = int(input(prompt))#Variable "number" that connected to the "get_int() function" that accepts one argument which is a (prompt). In this case, the prompt that's passed to it is the first argument of the "get_int() function" which displays a "prompt" that asks the user to "Enter number of years" through the use of the "input" function. As the user enters a number of years, the entry is then converted to an "integer" value. This number variable makes use of a "chain function" through the "input" and "int" functions. Also, this function or "get_int() function" is called from the "main() function" to get the "years" entry.  
##        if number > low and number <= high:#An "if statement" that uses an "AND" logical operator that evaluates the expressions on the left and right and returns a "True" value if both expressions are True.
##           is_valid = True #The variable "is_valid" is set to True only when it meets the conditions of both expressions of the "AND" logical operator before it in the "if statement". This also checks for data validation.
##           return number #A "return statement" that returns the result(value) of the calculation to the calling statement of the function. In other words, an entry being greater than "0" is valid and is returned back to the "get_int() function" where the result is an "integer" value.
##        else:
##            print("Entry must be greater than", low,
##                  "and less than or equal to", high,
##                  "Please try again.")#An appropriate error message that's displayed when the user enters a value that's "not valid". 

import validation as v #Adding an import statement that imports the validation module. Also, this is an example of "importing a module into a specified namespace". This is also how you know that this "future_value.py" module is the main module because it's importing another module as a namespace within its own program. 

def calculate_future_value(monthly_investment, yearly_interest, years): #Calculation that defines the "future value" as it calls upon three arguments: which is the monthly investment entry, yearly interest rate and number of years.  
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100 #Calculation for monthly interest rate
    months = years * 12 #Calculation for number of months

    # calculate future value
    future_value = 0.0 #Future_value is a local variable. A "local variable" is a variable that is defined within a function. In this case the "future_value" function is defined within the "calculate_future_value() function". Plus, this is an example of "Functions that use local variables".
    #Note: If you're making changes to a function that has a "global variable" this means that you're able to access the global variable by coding the keyword "global" before the variable name and therefore allows you to change the function with the use of calling the "main() function". But if you have a "local variable that shadows a global variable", since you're not able to access the global variable by not using the keyword "global" before the variable name, you won't be able to make any changes to the value of the original funcion of that variable. So, in other words, only the "local variable" value will be calculated and the "global variable" value of the original function will remain unchanged regardless of calculation in that "main() function". 
    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest #This "for statement" executes the "future value of a monthly investment with interest" calculated each month.
                                         #Here "monthly investment" is added to future value. Next, the second statement calculates "monthly interest".
                                         #Last, the third statement adds the sum of the "monthly interest" to the future value. 

    return future_value #A "return statement" that returns the result(value) of the calculation to the calling statement of the function. In other words, the "future value" takes the monthly investment entry, the yearly interest rate and number of years converted to "monthly_interest" over a total period of time(months) based on range in the "for statement" that results in a "float" value returned by the function. Note: The function here takes these 4 variables in account for its calculation: "monthly_interest", "months", "future_value" and "monthly_interest_rate".

def main(): #Definition of the "main" function that executes the statements below when the "main() function" is called. Here, this "main() function" definition has "zero" arguments inside of the parentheses. Also, this "main() function" definition is an example of "a function that doesn't accept arguments". 
    #Note: When you code a calling statement, the names that you use for the arguments don't have to be the same as the names that are used in the function definition.
    choice = "y"
    while choice.lower() == "y":
        # get input from the user. Also, code in this "main() function" is "modified" to use the functions from the "validation.py" module. Thus, the code below calls it's functions from both the "get_float()" and "get_int()" functions. Last, these functions accept "One" argument, and that argument is whatever string that's in the " " which in turn will become the prompt message(value).  
        monthly_investment = v.get_float("Enter monthly investment:\t", 0, 1000) #Modification of the monthly investment entry in the "main() function" in which the low and high arguments are between 0 and 1000 for first entry. This test the function and the result is a float. 
        yearly_interest_rate = v.get_float("Enter yearly interest rate:\t", 0, 15) #Modification of the yearly interest rate entry in the "main() function" in which the low and high arguments are between 0 and 15 for the second entry. The result is a float. 
        years = v.get_int("Enter number of years:\t\t", 0, 50) #Modification for number of years entry. The result is an integer. Also, in the "main() function" you call the "get_int() function" from here to get the "years" entry.

         # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)#The variable "future value" is defined as a function that calls upon 3 arguments: "monthly investment", "yearly interest rate" and "number of years". 

        print("Future value:\t\t\t" + str(round(future_value, 2)))#The display of the "Future value" which uses a "chain function" that rounds the future value to 2 decimal places and converts this value to a "string" value. 
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")#The continuation or end of while loop in which it give the user the option to enter "yes" or "no". "Yes" continues the program. "No" ends the while loop and then prompts the user "goodbye". 
        print()

    print("Bye K. Zoom!")
    
if __name__ == "__main__": #Use of the "if statement" that checks if this program is the main module. Because this module is run without being imported, Python sets the "__name__" variable equal to "__main__". Plus, the use of the "if statement" checks if this module is the main module. Because it is the main module you call on the "main() function" to start the operation of the main program. 
   main() #The calling of the "main() function" to start the operation of the main program. Also, the "main() function" is a function that stores all of the code that isn't in specific functions and then starts the operations of a program. 


#Reference pages for this exercise includes pages: 104, 105, 106, 107, 112, 113, 118, 119, 126 and 127
