# Keiland Pullen
# DSC 430: Python Programming
# Due Date 10/22/2019
# Link to video:https://youtu.be/Ad-tvzP8uvo
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Assignment 0502: Cups and Dice


from KCPullen_HW_0501 import *    # import Classes from Dice and Cups python assignment

def main():
    ''' This will be the main function for Cups and Dice game'''

    def greeting():
        ''' This function will offer the user a simple greeting'''
        print("\nHello and welcome to the Cups and Dice game. You will begin with a balance of $100.\n")


    def promptUser():
        ''' Prompt the user if they would like to play the game'''

        import random     

        name = input("Hello Friend, what is your name ? ")
        print ("\n{}, your beginning Balance in this game is: $100".format(name) )

        play = input("\nWould you like to play the Cups and Dice Game (yes or no)? ")   
        if (play.lower() == "no"):      # Doesnt matter if user enters any mixed case of NO.
            print ("\nThank You and Good Bye")
            return

        currBalance = 100

        playAgain = True
        
        while playAgain:      # Loop used to determine if user wants to play again.
            goal = random.randint(1,100)    # Use Random to generate a random amount between 1 and 100.
            print("\nYour goal is {}.".format(goal) )

            checkBet = True
            while checkBet:   # While and try to prevent user from entering negative numbers
                try:
                    bet = int(input("How much would you like to bet ?"))
                    if bet <= 0:
                        raise ValueError  # user defined exception
                    else:
                        checkBet = False
                except ValueError:
                    print ("Please do not enter any negative amounts!")
                    
                    
            currBalance = currBalance - bet
            print ("Your current balance is now ${}.".format(currBalance) )
            sixDie = int(input("How many 6-sided die would you like to roll? ") )
            tenDie = int(input("How many 10-sided die would you like to roll?") )
            tweDie = int(input("How many 20-sided die would you like to roll?") )

            newCup = Cup(sixDie,tenDie,tweDie)  # User of classes from Dice and Cups assignment code
            roll = newCup.roll()
            getSum = newCup.getSum()
            getDice = newCup
            print ("\nThe results of your roll are ",getSum)
            print ("Goal is ",goal)

            getSum = int(getSum)
            
            if (getSum == goal):   # Calculate the amount won which will be added to the Current Balance
                winMoney = bet * 10
            elif (getSum <= goal + 3) and (getSum >= goal - 3):
                winMoney = bet * 5
            elif (getSum < goal + 10) and (getSum > goal - 10):
                winMoney = bet + bet
            else:
                winMoney = 0

            currBalance = currBalance + winMoney
            
            print ("\nHi {}, the results of your roll were {}, and your current balance is {}".format(name,getSum,currBalance) )

            playAgainQuestion = input ("Would you like to play again (yes/no) ? ")
            if (playAgainQuestion.lower() == "no"):
                print ("\nThank You and Good Bye")
                playAgain = False
                return playAgain
            
        
    greeting()
    promptUser()
main()

        
        
        
