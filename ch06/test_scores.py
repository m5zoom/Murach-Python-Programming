#!/usr/bin/env python3

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = [] # Modification of the "get_scores() function" in which the test scores are stored in an "Empty list" named "scores". 
    while True:
        score = input("Enter test score: ") # Entry of test scores. 
        if score == "x":
            return scores # The list "scores" being returned by the function when all scores have been entered. This takes places after you enter "x" as in input to exit and as a result "test scores" are returned as well as other "individual statistics" such as "Total", "Number of Scores" and etc later in the program.
        else:
            score = int(score) # Coverts the "scores" argument into an "integer" value as it's being used as an entry for test scores.  
            if score >= 0 and score <= 100: # The use of an "if statement" and "and" logical operator that checks if both statements are "True". If that's the case, then each "score" value will be added as a "valid entry" for the "test scores". 
                scores.append(score) # Use of the "append" list method to add each test score entry and it acts as a counter to count every test score entry in the "scores" list. The use of this "append" list method by doing two things at once such as adding a "test score item" and "counting each test score" replaces the need of using the original variables: "score_total += score" and "counter += 1".    
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores): #Modification of the "process_scores() function" so that the scores list is the only argument call.
    # calculate total score
    total = 0 # The initial assignment of the value "0" to the variable "total". 
    for score in scores: # Use of a "for" statement to take each "score" item in the "scores" list and then adds them up to get the "score total".
        total += score #Use of the "+=" compound assignment operator to have the variable "total" to now equal the sum of the number of scores from the "scores" list.  
        
    #number of scores in the list
    length = len(scores) #Use of the "len() function" to call on the "scores" list as an argument to get the "number of scores" in the list.
    
    # calculate average score
    average = round(total / length) #Getting the average by taking the total score and dividing it by the length (number of scores). Then it rounds the value to the nearest integer. 

    # Get the low and high scores
    low = min(scores) # Use of the "min() function" to get the minimum value from the "scores" list.
    high = max(scores) # Use of the "max() function" to get the maximum value from the "scores" list.
    
    #Getting the median score
    median_index = len(scores) // 2 # The use of the "len() function" to call on the "scores" list in its call statement and take the number of scores and divide it by 2 using "integer division". Also, the value of this result is now assigned to the "median_index" variable. This variable will later be used as a reference(argument) in the the "scores" list for the "if statement" that follows this initial statement. Plus, the "median_index" variable is a good variable to have because it allows you to recognize where the "correct index value" is located in which you'll use in order to find the correct "Median Test Score" value from the "scores" list.   
    if len(scores) % 2 == 1: # The use of an "if statement" that checks the value of the expression for an "Odd Number of scores" in the "scores" list. This is established by using the "len() function" divided by 2 leaving only remainder equals 1 is either "True" or "False" using Modulo(Remainder) Division.  
        median = scores[median_index] # The execution of the statement for "Odd Numbers" in the "scores" list because the if statement condition holds a "True" value. Since "remainder 1 of modulo division" is equals to (==) "1", the value is "True" of the expression. Plus, "median" variable is now set to the value of the "scores" function in which the [median_index] is the argument in the calling statement of the function. Also, note the use of "brackets []" around the [median_index] argument and not parenthesis in the calling statement because the value is recognized as an item from the "scores" list. If you use parenthesis such as (median_index) you'll get a TypeError in which the 'list' object is not callable. 

    else: # The use of an "else clause" that checks the value of the expression for an "Even Number of scores" in the "scores" list. This is established by using the "len() function" divided by 2 leaving only remainder equals 1 is either "True" or "False" using Modulo(Remainder) Division.  
        median1 = scores[median_index] # The execution of the statement for "Even Numbers" in the "scores" list because the if statement condition holds a "False" value. Since the "remainder value" of modulo division" is not equal(!=) to "1", the value is "False" of the expression. Plus, "median1" variable is now set to the value of the "scores" function in which the [median_index] is the argument in the calling statement of the function. Also, note the use of "brackets []" around the [median_index] argument and not parenthesis in the calling statement because the value is recognized as an item from the "scores" list. If you use parenthesis such as (median_index) you'll get a TypeError in which the 'list' object is not callable. Last, most important of all, this statement represents the test score value(item) at located at index "2".
        median2 = scores[median_index -1] # The execution of the statement for "Even Numbers" in the "scores" list because the if statement condition holds a "False" value. Since the "remainder value" of modulo division" is not equal(!=) to "1", the value is "False" of the expression. Plus, "median2" variable is now set to the value of the "scores" function in which the [median_index -1] is the argument in the calling statement of the function. Also, note the use of "brackets []" around the [median_index -1] argument and not parenthesis in the calling statement because the value is recognized as an item from the "scores" list. If you use parenthesis such as (median_index -1) you'll get a TypeError in which the 'list' object is not callable. Last, most important of all, this statement represents the test score value(item) at located at index "1".
        median = (median1+median2) / 2 # Finally, the execution of the statement to calculate for the "Median Test Score" value which is the median1 test score value + the median2 test score value divided by 2. Or in other words, this statement is read as "test score (item) at index 2 + (item) at index 1" divided by 2. This here will give you the "Median Score" value. 
        
    # format(enhancement of program) and display of the other statistics
    print()
    print("Total:             ", total)
    print("Number of Scores:  ", length) 
    print("Average Score:     ", average)
    print("Low Score:         ", low)
    print("High Score:        ", high)
    print("Median Scores:     ", median)
    

def main():
    display_welcome() # Calling of the "display_welcome() function" after its been defined and it will display the message "The Test Scores program" on the Python Shell(console).
    scores = get_scores() # Modification of the "main() function" in which the list that's returned by the "get_scores() function" is stored in a variable(list) named "scores".
    process_scores(scores) #Modification of the "process_scores() function" in which the "scores" list is just "passed" to its call statement. 
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


#Reference pages for this exercise includes: 38, 39(review on arithmetic operators and reminder that in integer division the result is always rounded down to nearest whole integer) 40, 41(review on compound assignment operators/focus on the example that shows two ways to increment the number in a variable) 104, 105, 106, 107(for defining and calling functions), 164, 165, 166, 167, 168, 169, 170, and 171(for lists being passed to functions).
#Note: When using the term "pass or passed", all this means is that the "argument" is being called in the "call statement" of a function that in parenthesis () or brackets [] if you will.     
