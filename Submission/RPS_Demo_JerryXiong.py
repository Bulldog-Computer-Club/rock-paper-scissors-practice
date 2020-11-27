# Jerry Xiong
# November 26, 2020
# Rock Paper Scissors Git Practice

import random

user_option = input("Please input your choice. Rock, Paper, or Scissors: ")
print()

option_list = ["Rock","Paper","Scissors"]

while user_option not in option_list:
    print("Only from Rock, Paper, or Scissors!")
    print()
    user_option = input("Please input your choice. Rock, Paper, or Scissors: ")
    print()

c = random.choice (option_list)

print ("You chose:",user_option)
print()
print ("The computer chose:",c)

if user_option == "Rock" and c == "Paper" or user_option == "Paper" and c == "Scissors" or user_option == "Scissors" and c == "Rock":
  print()
  print("Computer Wins")

elif user_option == "Rock" and c == "Scissors" or user_option == "Paper" and c == "Rock" or user_option == "Scissors" and c == "Paper":
  print()
  print("User Wins")

elif user_option == c:
  print()
  print("Ties")
    
    

    
