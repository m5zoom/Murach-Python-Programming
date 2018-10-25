#!/usr/bin/env python3

# display a welcome message
print("The Test Scores application")#Display of The Test Scores Application
print()#Printing a blank line
print("Enter test scores")#Display of test scores prompt
print("Enter 'x' to end input")#Display 'x' prompt that asks the user to end input of data. Therefore, it ends the while loop and the program.
print("======================")

# initialize variables
counter = 0 #The initial value of the "counter" variable
score_total = 0 #The initial value of the "score_total" variable.
test_score = 0 #The initial value of the "test_scores" variable.

while True:
    test_score = input("Enter test score (or 'x' to quit): ")
    if test_score != "x":#Use of "if statement" that says when "x" is entered as an entry for the "test_score" value that the program is to quit as a result using the "break" statement to end infinite while loop.
        test_score = int(test_score)#Use of "if statement" that allows for an "integer" value to be entered as the "test_score" value as long as "x" is not entered as an input. 
        #counter += 1 #Note: This will "double" the actual counter reading for every input that was entered in the prompt. Here, Python counts twice per input(entry) if this statement wasn't commented out. Next, since the "round() function" doesn't have any specified "digits" in its argument for the "number" to be rounded to, Python then rounds down to nearest whole "integer". This extra "counter +=1" statement is where the error lies in this program in which it needed to be debugged by testing the program with valid data, followed by "commenting out" the "counter" variable to get more accurate results using valid data. 
    else:
        break #Use of "break" statement that exits infinite while loop. 
    if test_score >= 0 and test_score <= 100: #Use of the "AND" logical operator within the "if statement" that checks if both expressions are True. If so, then the "test_score" input(entry) is valid and therefore can be added to the "score_total" variable calculation.  
        score_total += test_score #The adding of "test_score" variable to the "score_total" variable. This statement is saying that you take all the "test_score" values and put it together to get the sum(total) to now become the "score_total" variable value. 
        counter += 1 #Use of a "counter" variable that adds 1 to the counter. All this statement is says is that the counter variable accounts for all entries meaning one count per input(entry) made by the user. This is a more accurate calculation for a counter in which it gets the total amount of counts for each individual test score input(entry). 
    else:
        print("Test score must be from 0 through 100. Score discarded. Try again.")#Display of error message when you enter "invalid" data that doesn't meet the conditions of the expressions. 

# calculate average score
average_score = round(score_total / counter) #Use of the "round() function" that calculates the "average_score" to the nearest whole integer. It does this by rounding down to nearest whole integer since there's no specified "digits" value in the digits argument of the "round() function". 
                
# format and display the result
print("======================")
print("Total Score:", score_total, #Display of Total Score
      "\nAverage Score:", average_score) #Display of Average Score
print()
print("Bye K. Zoom")


#Reference pages for this exercise includes: 142, 143, 144, 145, 146, and 147. 

