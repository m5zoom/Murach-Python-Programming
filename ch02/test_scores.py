#!/usr/bin/env python3

# display a welcome message
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user
total_score = 0       # initialize the variable for accumulating scores
score1 = int(input("Enter test score: ")) # input for integer entries
score2 = int(input("Enter test score: "))
score3 = int(input("Enter test score: "))
# adding the the 3 variables to the total_score variable without ever saving them as integer entries
total_score += score1
total_score += score2
total_score += score3

# calculate average score
average_score = round(total_score / 3)
             
# format and display the result
print("======================")
print("Your Score:", score1, score2, score3)
print("Total Score:  ", total_score,
      "\nAverage Score:", average_score)
print()
print("Bye K. Zoom")


# My own version of getting scores from the user 
# total_score = 0       # initialize the variable for accumulating scores
# score1 = 75
# score2 = 85
# score3 = 95
# total_score == or != score1 + score2 + score3 # Got this program to
                # work by setting total_score == score1 + score2 + score3
                # or by setting total_score != score1 + score2 + score3

# total_score += int(input("Enter test score: "))
# total_score += int(input("Enter test score: "))
# total_score += int(input("Enter test score: "))
