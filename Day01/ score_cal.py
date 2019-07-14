
"""
Code Challenge
 
  Problem Statement:
    Lets assume there are 3 assignments and 2 exams, each with max score of 100. 
    Respective weights are 10%, 10%, 10%, 35%, 35% . 
    Compute the weighted score based on individual assignment scores.  
  Hint: 
    weighted score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
"""
Score_Assignment1=20
#let's take Score_Assignment1=20
Score_Assignment2=30
#let's take Score_Assignment1=20
Score_Assignment3=45
#let's take Score_Assignment1=20
Score_Exam1=67
#let's take Score_Exam1=67
Score_Exam2=52
#let's take Score_Exam1=52

weighted_score = (Score_Assignment1+Score_Assignment2+Score_Assignment3 ) *0.1 + (Score_Exam1 +Score_Exam2) * 0.35
print(weighted_score)