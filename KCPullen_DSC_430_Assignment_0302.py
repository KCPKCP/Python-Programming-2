# Keiland Pullen
# DSC 430: Python Programming
# Due Date: 10/ 8 /2019
# Link to video: https://youtu.be/YbYB0qFTFa4
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Assignment 0302: Happy Primes

def happyPrimes():
    '''This program will take any positive integer, replace the number by the sum of the squares of its digits and will
       repeat the process until the integer equals 1 or loops in a cycle that does not include 1.  For numbers that end
       the process with 1, label answer Happy Prime.  Those do not end in 1 are Sad Prime. Then there are Happy non-prime
       and Sad non-primes.
       '''

    def greetUser():
        ''' Function to greet User and provide instructions '''
        print('\n Hello, this program will determine if a number is a Happy Prime or a Sad Prime. \n')


    def getNumber():
        ''' Function to prompt user to enter an integer. '''
        
        checkNum = True

        while checkNum:
            try:
                getInt = int(input(' Please enter an integer: ') )
                if getInt > 0:
                    checkNum = False
            except:
                print ('\n DANGER!!!  You entered something that was not a positive integer.  Please try again! \n')
        return getInt


    def splitNumber(myNum):
        ''' Function to split the integer.    '''
        listMyNum = []

        strNum = str(myNum)

        listMyNum = [num for num in strNum] 
        return listMyNum


    def squareNumber(splNum):
        ''' Function to square the numbers '''
        sqList = []
        for x in range(0, len(splNum) ) :
            sqNum = int( splNum[x] )
            sqNum = sqNum**2
            sqList.append(sqNum)
        newVal = 0
        
        for x in range(0, len(sqList)):
            newVal = newVal + int(sqList[x] )
        splNum.append(newVal)
        return splNum 


    def printLine(allNum):
        ''' Function to print return sentence and stuff'''
        
        add = '+'
        equ = '='

        listLen = len(allNum)
        int(listLen)
        lastVal = allNum[-1]

        printList = []

        listLen = listLen -1
        for x in range(0, len(allNum) ):
            if (lastVal == allNum[x] ):
                print(equ, end = ' ')
                print(allNum[x])
                printList.append(equ)
                printList.append(allNum[x])
            else:               
                print(' {} squared '.format( allNum[x]), end = '')
                printList.append(allNum[x])
                printList.append(add)
                listLen = listLen -1
                if (listLen >= 1):
                    print(add, end = '')
        return lastVal


    def mainBody():
        ''' Function to execute main body of this program '''

        finalVal = getNumber()
        loopCounter = 0
        while True:
            splNum = splitNumber(finalVal)
            allNum = squareNumber(splNum)
            finalVal = printLine(allNum)
            
            if finalVal == 1:
                print('\n This number is a HAPPY PRIME')
                return False
                

            loopCounter = loopCounter + 1
            if loopCounter == 25:
                return False


               

                    
    greetUser()
    mainBody()
     
happyPrimes()
                    

        


    
