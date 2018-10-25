#!/usr/bin/env python3
        
def get_number(prompt, low, high): #Definition of a "get_number() function" that calls upon 3 arguments of a prompt, along with low and high validity values. 
    while True: #Code for infinite while loop that checks for entry into the "get_number()" function until value is greater than "0" and less than or equal to "1000". If it is, then it's "valid" and holds as a "True" value. If not, then error statement appears.
        number = float(input(prompt))#Variable "number" thats connected to the "get_float() function" that accepts one argument which is a (prompt). In this case, the prompt that's passed to it is the first argument of the "get_float() function" which displays a "prompt" that asks the user to "Enter monthly investment" through the use of the "input" function. As the user enters a monthly investment, the entry is then converted to a "float" value. This number variable makes use of a "chain function" through the "input" and "float" functions. 
        if number > low and number <= high:#An "if statement" that uses an "AND" logical operator that evaluates the expressions on the left and right and returns a "True" value if both expressions are True.  
            is_valid = True #The variable "is_valid" is set to True only when it meets the conditions of both expressions of the "AND" logical operator before it in the "if statement". This also checks for data validation.  
            return number #A "return statement" that returns the result(value) of the calculation to the calling statement of the function. In other words, an entry being greater than "0" is valid and is returned back to the "get_float() function" where the result is a "float" value.  
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high,
                  "Please try again.")#An appropriate error message that's displayed when the user enters a value that's "not valid". 
            
def get_integer(prompt, low, high): #Definition of a "get_integer() function" that calls upon 3 arguments of a prompt, along with low and high validity values. 
    while True: #Code for infinite while loop that checks for entry into the "get_integer()" function until value is greater than "0" and less than or equal to "50". If it is, then it's "valid" and holds as a "True" value. If not, then error statement appears. 
        number = int(input(prompt)) #Variable "number" thats connected to the "get_integer() function" that accepts one argument which is a (prompt). In this case, the prompt that's passed to it is the first argument of the "get_integer() function" which displays a "prompt" that asks the user to "Enter number of years" through the use of the "input" function. As the user enters a number of years, the entry is then converted to an "integer" value. This number variable makes use of a "chain function" through the "input" and "integer" functions.
        if number > low and number <= high: #An "if statement" that uses an "AND" logical operator that evaluates the expressions on the left and right and returns a "True" value if both expressions are True. 
            is_valid = True #The variable "is_valid" is set to True only when it meets the conditions of both expressions of the "AND" logical operator before it in the "if statement". This also checks for data validation. 
            return number #A "return statement" that returns the result(value) of the calculation to the calling statement of the function. In other words, an entry being greater than "0" is valid and is returned back to the "get_integer() function" where the result is an "integer" value. 
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high,
                  "Please try again.")#An appropriate error message that's displayed when the user enters a value that's "not valid". 
            
def calculate_future_value(monthly_investment, yearly_interest, years):
    #print("Entering calculate_future_value()") # A print function that displays a message of the execution of the program from the "calculate_future_value() function". 
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100  #Logic Error 1: Here, division by 100 needed to be added.
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(1, months +1): #Logic Error 2: There are 2 ways to do this exercise and it includes using the Python shell as in "answer check" to make sure the value is correct. The way to "answer check" is by entering a value for "number of years" from page 102. That way each year coresponds to a particular "Future Value" calculation. Also, put in a small note that the given "Solutions for this Chapter 5 Future Value exercise is incorrect" and explain why. Next, there are 2 ways to have the calling argument in the range function to always come out with the correct answer. The first way is to have the calling argumment in the range function become (1, months +1). Here, Python started at "1" and stopped at "months +1". So, instead of stopping at "months" in which this argument is normally not included, it's now included with the help of the "+1" calling argument. The second way for the calling argument in the range function to come out with the correct answer is to set the calling argument as (months) in the range function. By doing this, Python understands that it starts at "0" and stops at a value that's one less than the stop value "months" in which this value is not included. So both calling arguments of (1, months +1) and (months) return the correct "Future values" when you enter the corresponding years in the "Python shell". These values depend on how they were called in the calling arguments of the "range function". Last, when you enter integer values such as "120" in the "range function" and then do an "Answer check" using the "Python shell" you're going to get errors in the "Future value" calculations as you enter in multiple values for "number of years" from page 102 in the "Python shell". So in other words, stick to the "named variables" as calling arguments and not "integer" values in the range function when calculatiing the "Future Value" for the correct answer. 
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest
        #print("i =", i, "future value =", future_value) # A print function that displays the values of the variables "i and future value" as it changes each time through the "for loop". 
    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_number("Enter monthly investment:\t", 0, 1000) # After you run the program and select "n" for No to exit the main program, you then test the three functions using "Figure 5-6" from page 153. The "three" functions that are being tested here are the ones to the left. The "first function" is for the "monthly_investment" function which can be written on the "Python shell" as new_value = get_number("Enter Number: ", 0, 1000). This will check the function for the "monthly investment" amount being inbetween "0 and less than or equal to 1000". So, if the user entry meets the requirements stated in the arguments of the function, then the result will be a float. Also, this answer satisfies questions #5 and #6 of page 161. 
        yearly_interest_rate = get_number("Enter yearly interest rate:\t", 0, 15) # After you run the program and select "n" for No, to exit the main program, you then test the three functions using "Figure 5-6" from page 153. The "three" functions that are being tested here are the ones to the left. The "second function" is for the "yearly_interest_rate" function which can be written on the "Python shell" as new_value = get_number("Enter Number: ", 0, 10). This will check the function for the "yearly interest rate" amount being inbetween "0 and less then or equal to 10". So, if the user entry meets the requirements stated in the arguments of the function, then the result will be a float. Also, this answer satisfies questions #5 and #6 of page 161.        
        years = get_integer("Enter number of years:\t\t", 0, 50)                    

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years) # After you run the program and select "n" for No, to exit the main program, you then test the three functions using "Figure 5-6" fro page 153. The "three" functions that are being tested here are the ones to the left. The "third function" is for the "calculate_future_value" function which can be written on the "Python shell" as calculate_future_value(100, 12, 1). This will check the function for the "future value" amount. So, if the user meets the requirements stated in the arguments of the function that corresponds to the statements(rules) of the "monthly_investment, yearly_interest_rate, and number of years" functions then the result will be float value. Also, this answer satisfies questions #5 and #6 of page 161. 
        
        print()
        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye K. Zoom!")
    
if __name__ == "__main__":
    main()

#Reference pages that were used in Exercise 5-2 include: 96 for reminder when working with arguments of the range function in the "Future Value Program", 142, 144, 145, 146, 147, 148, 149, 150, 151, 152, and 153.
#Reference pages that were used in Exercise 5-3 include: 154, 155, 156, 157 which is very useful in learning more about the "Debug Control" toolbar and stepping through the code. Note: sometimes you have to hit the "Go" button twice to run the program. Also pages 158 and 159.
