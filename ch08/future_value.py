#!/usr/bin/env python3
        
def get_number(prompt, low, high):
    while True:
        try: #Use of a "try statement" that allows you to code any statement that may throw(raise) an exception. 
            number = float(input(prompt))
        except ValueError: #Use of an "except clause" that catches(handles) any exception that occurs after the user's input in order to prevent a program from crashing. This is an example of "Exception Handling" with "ValueError" as the name of the exception. Plus, you get a "ValueError" exception when you can't convert the data argument to a "float" value.   
            print("You entered an invalid number.") #Display of an invalid number entry to the Python console. 
            continue #Use of a "continue statement" that continues execution of the "while loop" for the user to make another entry in the prompt after performing "Exception Handling" checking for any "ValueErrors".
        if number > low and number <= high: #Use of the "if statement", the "and" logical operator , and '>' '<=' relational operators that checks for "data validation" of the user's enteries meeting the conditions within the "if statement". 
            is_valid = True
            return number #Use of the "return statement" of the number being returned back to the function when the user enters a valid input and meets all conditions. 
        else: #Use of the "else clause" that is executed when the user's entry doesn't meet the conditions of the "if statement". In other words, the value is "False". 
            print("Entry must be greater than " + str(low) #Display message when the user's input doesn't meet the conditions within the "if statement". 
                  + " and less than or equal to " + str(high) + ".")
            
def get_integer(prompt, low, high):
    while True:
        try: #Use of a "try statement" that allows you to code any statement that may throw(raise) an exception.
            number = int(input(prompt))
        except ValueError: #Use of an "except clause" that catches(handles) any exception that occurs after the user's input in order to prevent a program from crashing. This is an example of "Exception Handling" with "ValueError" as the name of the exception. Plus, you get a "ValueError" exception when you can't convert the data argument to an "int" value.   
            print("You entered an invalid integer.") #Display of an invalid integer entry to the Python console.
            continue #Use of a "continue statement" that continues execution of the "while loop" for the user to make another entry in the prompt after performing "Exception Handling" checking for any "ValueErrors".
        if number > low and number <= high: #Use of the "if statement", the "and" logical operator , and '>' '<=' relational operators that checks for "data validation" of the user's enteries meeting the conditions within the "if statement". 
            is_valid = True 
            return number #Use of the "return statement" of the number being returned back to the function when the user enters a valid input and meets all conditions. 
        else: #Use of the "else clause" that is executed when the user's entry doesn't meet the conditions of the "if statement". In other words, the value is "False". 
            print("Entry must be greater than " + str(low) #Display message when the user's input doesn't meet the conditions within the "if statement". 
                  + " and less than or equal to " + str(high) + ".")

def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_number("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = get_number("Enter yearly interest rate:\t", 0, 15)
        years = get_integer("Enter number of years:\t\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)
        
        print()
        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()

#Reference pages use for this exercise include: pages 226 and 227 for explanation on how exception handling works. Plus, it provides code that can cause a "ValueError" exception and "two functions" that can cause a "ValueError" exception. 
#Pages 228 and 229 for explanation and examples on how to use the "try statement" to catch an exception, how to handle a "ValueError" exception along with the "data validation" of valid and invalid integers. Last, how to handle all exceptions.
#Page 230 and 231 for explanation and example code on how to check for "data validation" and code in "Exception Handling". 
