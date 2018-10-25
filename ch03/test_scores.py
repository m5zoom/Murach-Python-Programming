#!/usr/bin/env python3

# display a welcome message
print("The Test Scores program")
print()

another_tests = "y" #initialize variable outside of outer while loop for the loop to work

while another_tests.lower() == "y": #Beginning of outer while loop that continues on as long as the user enters 'y' or 'Y'.
    print("Enter test scores")
    print("Enter 'end' to end input")
    print("======================")

# initialize variables outside of inner while loop for loop to work.
    counter = 0
    score_total = 0
    test_score = 0

    while True: #The inner while loop code that causes an infinite loop
        test_score = input("Enter test score: ")#A prompt that ask you to enter your test score.
        if test_score.lower() == "end": #A condition if the user enters "end" or "End" as an input to end a set of score entries.
            break #Exits the infinite while loop after the user enters "end" or "End" to end a set of score entries. 
        else:
            test_score = int(test_score) #The condition that the test score variable will become an "integer value" if the user enter an integer value.

            if test_score >= 0 and test_score <= 100: #The condition that the test score must between "0 and 100". 
                score_total += test_score #The conditon that the score total is the "sum of all test scores". 
                counter += 1 #A counter variable that prints the value of the number of "counted test scores" to the console. 

            else: #An else clause that allows the printing of a statement whenever the test score isn't between "0 and 100". 
                print("Test score must be from 0 through 100. Score discarded. Try again.")

# calculate average score
    average_score = round(score_total / counter)
                
# format and display the result
    print("======================")
    print("Total Score:", score_total, #Prints the total score to the console
      "\nAverage Score:", average_score)#Prints the average score to the console
    print()
    another_tests = input("Enter another set of test scores (y/n)? ")
    print()                     
    print("Bye K. Zoom")

#Reference pages for answers to this solution are: 71, 73, 75, 84, 85, 89, 91 and 95.


