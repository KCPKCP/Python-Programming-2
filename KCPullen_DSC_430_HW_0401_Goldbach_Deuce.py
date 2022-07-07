# Keiland Pullen
# DSC 430: Python Programming
# Due Date 10/15/2019
# Link to video: https://youtu.be/YkmuOY2wH4c
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Assignment 0401: Goldbach Deuce

def main():
    ''' This is the main function for the Goldbach Deuce program. '''

    def greeting():
        ''' This function is to greet the user and explain the task they are to perform'''
  
        print("The first number entered will be 'i', and it will create a list or random numbers")
        print("We will determine if the sun of any 2 numbers in the list 'i' are equal to the value of 'n'.\n")


    def promptForNumbers():
        ''' This function will prompt the user to enter two numbers - separated by a space. '''
        
        iN = input("Please enter 2 numbers (separated by a space) : \n") 

        return iN



    def processNums(iN):
        ''' This intense function will calculate the list (e.g. the first number entered, then\
perform the binary search on the list and will determine if the sum of any two numbers in that\
list is the 2nd number entered.'''

        import random      # import the random module

        i,n = iN.split()   # split the 2 numbers that were entered.
        i = int(i)
        n = int(n)

        if i > 100:        # a sanity check to ensure that the user entered any number less than 100
            print("The list of numbers must be between 0 and 100")
            promptForNumbers()

        randomList = []

        randomList = random.sample(range(100),i)  # use the random module to generate random numbers less than 100
        randomList.sort()  # here we used the python sort.

        print("Your list is ", randomList)   # displaying the random sorted list to the user.

        x = 0
        y = 0
        low = 0
        high = len(randomList) - 1

        while x < len(randomList):       # Begin our binary search
            while low <= high:
                mid = (low + high)//2
                item = randomList[mid]
                #print ("item is ",item)     #print statements used in testing
                #print ("randomList[x] is ",randomList[x])
                #print ("mid is ", mid)

                if (randomList[x] + item == n) and (randomList[x] != item):
                    print ("SURPRISE, we found two values that add up")
                    return n
                elif (randomList[x] + item > n):
                    high = mid - 1
                else:
                    low = mid + 1
            low = 0
            high = len(randomList) - 1
            x = x + 1
        statement = "Could not find 2 numbers that would sum {}".format(n)
        return statement
            


    greeting()
    iN = promptForNumbers()
    statement = processNums(iN)
    print (statement)
main()
