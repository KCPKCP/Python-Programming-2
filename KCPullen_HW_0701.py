# Keiland Pullen
# DSC 430: Python Programming
# Due Date 11/5/2019
# Link to video: https://www.youtube.com/watch?v=gmDAaZsxj1U
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Assignment 0701: 


class WarAndPeacePseudoRandomNumberGenerator():
    '''Main class for Random Number Generator'''
    
    def __init__(self, seed=500):
        '''Initialize the class along with variable declaraions'''
        self
        self.seed = seed
        #print (self.seed)                 # print statement for testing
        self.openWarAndPeace(self.seed)    # pass seed to function to open and read file
     
   
    def openWarAndPeace(self, seed):
        '''Function to open War-and-Peace file, goto seed character and read in x amount of characters'''

        self.seedy = seed                 # seed value from class
        #print("Seed =", seed)            # print statement for testing
        war = []                          # list to contain characters
        Y = 32                            # value to execute loop for 32 characters
        
        while Y > 0:                      # open file, read seed character, then every 1000th character until 32 characters
            
            for x in range(self.seedy, self.seedy+1000, 1000-1):
                infile = open ("war-and-peace.txt","r")
                warPeace = infile.read()[x]
                war.append(warPeace)
                infile.close()
                self.seedy += 1000
              
            Y = Y - 1                     # counter decrement
            
        self.Xcharacters(war)             # send list to Xcharacters function 
        self.seedy = 0                    # reset seed in this function
        war = []                          # reset list
        return


    def Xcharacters(self,lstOfLetters):
        '''Function to compare characters then assign a value of 0 or 1 to the comparison'''

        listLetters = lstOfLetters
        # print(listLetters)             #  print for testing

        x = 0
        listNums = []
        
        while x < 64:                    # Loop decrements from 64 because there are 32 pairs of chars.
            
            if listLetters[x] > listLetters[x + 1]:  #For loop to compare chars and assign value
                num = 0              
            else:
                num = 1
            listNums.append(num)        # assign bit values to list
            x = x + 2

        self.calculate(listNums)        # send list to Calculate function
        return


    def calculate(self, listNums):
        ''' Calculate the values of the 1-bits in their location'''

        num = 1
        x = 0
        self.ranNumb = 0
        lstRan = []
        for i in range(1, 33):           
            num = 1 / 2**i               # calculate 32 values between 0 and 1, that are each 1/2 of each other
            # print (num, listNums[x])   # print statement for testing
            self.ranNumb = self.ranNumb + (num * listNums[x])  #calcuate the value for each 1-bit
            if listNums[x] == 1:
                lstRan.append(num)       # assign each random number to a list
            x = x +1

        # print ("Random number is ",self.ranNumb)  # print each random number for testing
        # print (lstRan)                # print list of randoms for testing
        


    def random(self, num=1):
        ''' Random function to generate the random numbers'''

        self.seedy = self.seed
        
        #print ("num =", num)       # print statement for testing
        
        self.ranDict = {}
        
        while 0 < num:              # using while loop to do 10,000 calculations
    
            self.openWarAndPeace(self.seedy + num)
            num = num - 1
            #print(num)                                 # print statement for testing
            #print ("self ranNumb = ",self.ranNumb)     # print statemetn for testing
            self.ranDict[num] = self.ranNumb
            self.seedy = self.seedy + 505

        # print (self.ranDict)
        
        #self.stats()

        return self.ranDict

        

    def stats(self):
        ''' Calculate the Min, Max and Mean of the 10,000 random numbers '''
        import statistics
        
        
        randomDict = self.ranDict

        ranMax  = max(randomDict, key=randomDict.get)  
        ranMin  = min(randomDict, key=randomDict.get)
        ranMean = statistics.mean(randomDict[x] for x in randomDict)

        print ()
        print ("Max : ",randomDict[ranMax])
        print ("Min : ",randomDict[ranMin])
        print ("Mean : ",ranMean)




        
        
    
        
