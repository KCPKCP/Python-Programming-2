# Keiland Pullen
# DSC 430: Python Programming
# Due Date: 10/ 8 /2019
# Link to video: https://youtu.be/bn5pTGvhL1U 
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Assignment 0301: Goldbach's Conjecture

def main():
    ''' Assignment to take in an integer (less than 100) as input, then return a single line displaying
        how two primes can sum to the integer.
    '''

    def greeting():
        ''' Function to greet user '''
        print (' Hello, for this assignment, the user will enter any number/integer between (and including) 2 - 100')
        print (' The result will be a line of two primes whose sum is the integer. \n')


    def getInput():
        ''' Function to prompt user input. If the entered number is less than 2 or greater than 100, prompt the user
            to enter again
        '''
        checkNum = True

        while checkNum:
            try:
                getNumber = int(input(' Please enter a number between 2 and 100 : \n') )
                if getNumber >= 2 and getNumber <= 100:
                    checkNum = False
            except (Exception, TypeError, ValueError):
                print (' DANGER!!! That was not an integer, your number was less than 2 or greater than 100... Please try again. \n')

        return getNumber


    def getPrimes(thisNumber):
        ''' Function to calculate the Prime numbers '''

        listNum = []
        primeListNum = [1]
        i = 0

        
        for num in range(2, thisNumber + 1):
            for i in range(2, num):
                if ( num %i) == 0:
                    
                    break
            else:
                primeListNum.append(num)

        return primeListNum
                   

    def doCalculation(primeListNum, num):
        ''' Function to do the full calculation '''

        listNum = primeListNum
        listSums = []
        
        while num > 0:
            for x in range(1, len(listNum) ):
                primeNum = num - listNum[x]
                if primeNum in listNum:
                    if (num == primeNum + listNum[x]):
                        listSums.append("{} {} {}".format(num, listNum[x], primeNum) ) 
                        break
            num = num - 2

        listSums.reverse()
        return listSums


    def printList(listSums):
        ''' Function to print the list, function will print (2 = 1 + 1) as default value for 2 '''

        number = []
        print()
        print ('2  = 1 + 1')
        for x in range(0, len(listSums) ):
            number.append(listSums[x].split(' ') )
            print ( '{:2s} = {} + {}'.format(number[x][0], number[x][1], number[x][2] ) )


    greeting()
    
    getNumber = getInput()
    
    primeListNum = getPrimes(getNumber)
    
    listSums = doCalculation(primeListNum, getNumber)

    printList(listSums)

    
    
    
main()


