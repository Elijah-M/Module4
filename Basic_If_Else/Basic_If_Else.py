"""
Author: Elijah Morishita
elmorishita@dmacc.edu
9/14/2020
This is a program that gathers input from a user to find out
which Programmer's Toolkit Monthly Subscription Box item they want
"""

#  Basic Menu
print("\n========== Programmer's Toolkit Monthly Subscription ==========\n",
      "Subscription Levels:\n",
      "1) Platinum\n",
      "2) Gold\n",
      "3) Silver\n",
      "4) Bronze\n",
      "5) Free Trial")

#  Request User input (an int)
choice = int(input("Please pick a subscription level (1-5):"))

#  Checks to make sure the user input is between 1 - 5
while choice < 1 or choice > 5:
    print("Invalid input, please try again\n")
    choice = int(input("Please pick a subscription level (1-5):"))

#  Once the user input is between 1 - 5 their results are printed
if choice == 1:
    print("Congrats you are now a PLATINUM member!\n",
          "Your monthly fee will be $60.00")
elif choice == 2:
    print("Congrats you are now a GOLD member!\n",
          "Your monthly fee will be $50.00")
elif choice == 3:
    print("Congrats you are now a SILVER member!\n",
          "Your monthly fee will be $40.00")
elif choice == 4:
    print("Congrats you are now a BRONZE member!\n",
          "Your monthly fee will be $30.00")
elif choice == 5:
    print("Congrats you are now a FREE TRIAL member!\n",
          "You have 30 days from today before your membership ends")

