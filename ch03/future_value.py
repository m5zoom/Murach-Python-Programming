#!/usr/bin/env python3

# display a welcome message
print("Welcome to the Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y": #A while loop that continues as long as the user enter "y" or "Y" using the "lower string method".

    # Get input or "entry" from the user and perform "data validation for monthly investment entry"
    is_valid = True #When data validation is a "True" value when monthly investment entry is valid.
    while is_valid == True: #While loop that checks validity of the entry is "True" only if monthly investment is greater than "0" and less than or equal to "1000".
        monthly_investment = float(input("Enter monthly investment:\t"))#The value of the input from monthly investment entry that will result in a "float" value
        if monthly_investment > 0 and monthly_investment <=1000:#An "if statement" that uses the "AND" logical operator to evaluate the experessions on the left and right are "True". This also performs "data validation" that returns a "True" value since it meets the conditions of both expressions.
            is_valid = False #When data validation is a "False" value when the monthly investment entry is not valid.
        else:
            print("Entry must be greater than 0. Please try again.")#Error message that's displayed when the monthly investment entry is "False" as the entry is "less than 0 or greater than 1000".


    # Get input or "entry" from the user and perform "data validation for yearly interest rate"
    is_valid = True #When data validation is a "True" value when yearly interest rate is valid.
    while is_valid == True: #While loop that checks validity of the entry is "True" only if yearly interest rate is greater than "0" and less than or equal to "15".
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))#The value of the input from yearly interest rate that will result in a "float" value.
        if yearly_interest_rate > 0 and yearly_interest_rate <= 15:#An "if statement" that uses the "AND" logical operator to evaluate the expressions on the left and right are "True". This also performs "data validation" that returns a "True" value since it meets the conditions of both expressions.
            is_valid = False #When data validation is a "False" value when the yearly interest rate entry is not valid.
        else:
            print("Entry must be greater than 0 and less than or equal to 15.",
                  "Please try again.")#Error message that's displayed when the yearly interest rate entry is "False" as the entry is "less than 0 or greater than 15".

    #Get input or "entry" from the user and perform "data validation for number of years"
    is_valid = True #When data validation is a "True" value when number of years is valid.
    while is_valid == True: #While loop that checks validity of the entry is "True" only if the input from number of years is greater than "0" and less than or equal to "50".
        years = int(input("Enter number of years:\t\t"))#The value of the input from number of years that will result in a "integer" value.
        if years > 0 and years <= 50:#An "if statement" that uses the "AND" logical operator to evaluate the expressions on the left and right are "True". This also performs "data validation" that returns a "True" value since it meets the conditions of both expressions.
            is_valid = False #When data validation is a "False" value when the number of years entry is not valid.
        else:
            print("Entry must be greater than 0 and less than or equal to 50.",
                  "Please try again.")#Error message that's displayed when the number of years entry is "False" as the entry is "less than 0 or greater than 50".

    print()

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100 #The formula for "monthly interest rate"
    months = years * 12 #The formula for "months". Here you would use the "number of years entered" multiplied by 12 to get the "months" value. 

    # calculate the future value
    future_value = 0
    for i in range(1, months +1):#A "for loop" that executes(counts) the exact number of times based on the "number of years entered" in which "years" is converted into "months" from the "months = years * 12" formula. Also, the "range" counted is from "1-600 months" or 50 years.
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount #The "future value" here is the sum(total) of all the monthly interest amounts in a given year or "12 month period". 

    # display the results for each year
        if i % 12 == 0: #An "if statement with only an if clause" that uses a Boolean expression by using the "==" (equal to) relational operator to evaluate a "True" value only if the value of "i" divided by 12 using "remainder division" equals "0". Plus, since the "if statement" here evaluates to a "True" value, only the first 'print function' is executed in which the "Year" and "Future Value" is displayed on the console. 
            print("Year = ", i // 12, #The "Year" is displayed. Here the "i" variable is taken from the argument of the "range" function in which "i" then is divided by 12 using the "integer division process" which drops the decimal portion of the answer. 
                  "\tFuture value = ", round(future_value, 2))#The "Future Value" is displayed rounded to 2 decimal places. 
    print()

    # see if the user wants to continue
    choice = input("Continue (y/n)? ")#This prompt comes up after entering number of years in which the "Year" and "Future Value" are executed. This also signals if you want to continue or end the program. 
    print()

print("Bye K. Zoom!")
#To be most efficent follow these rules
#Read, understand, and execute.
#Read exercise problem, next the solution followed by initial program as I fill in the blanks with comments.
#Fill in the blanks with solutions through reading corresponding examples that meet each exercise objective
#Use chapter examples with comments that provide answers as to what the program is doing in sequence along the way in 20-30 min
#Note: Use comments to address/answer each objective of the exercise problems
#Always have reference pages for quick review that correspond with where I found the answers to each problem of the exercise.
#Reference pages used were: 66, 67, 68, 69, 71, 72, 73, 74, 75, 84, 85, 86, 87, 88, 89, 90, 91, and 96. 
