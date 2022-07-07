# Keiland Pullen
# DSC 430: Python Programming
# Due Date 10/22/2019
# Link to video: https://youtu.be/sYKDPXbRdgQ
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Assignment 0501: Dice and Cups



import random     #import function for a random shuffle. Shuffle will function as a dice roll. 

class SixSidedDie:
    '''This class will represent the action of rolling the die and the value rolled.'''
  
    sidesOfDie = 6           # The number of sides on the die

    def __init__(self, sides=sidesOfDie):
        ''' Constructor that allows the class to create an instance/object and initialize the attributes'''
        
        self.sides = sides    # initial list containing each side of the die

  
    def roll(self):
        ''' Class Function or Method to roll the die '''
        self.side = random.randint(1,self.sides)  # random roll of die, from 1 to number of die-sides
        return self.side


    def getFaceValue(self):
        ''' Class Method to get the Face Value of the rolled die '''
        side = self.side
        return side


    def __repr__(self):
        ''' Special Method to return the canonical string representation of the object ''' 
        return 'SixSidedDie({})'.format(self.side)

            

class TenSidedDie(SixSidedDie):
    '''This class will represent the action of rolling a 10-sided die and the value rolled.'''

    sidesOfDie = 10
    
    def __init__(self, sides = 10):
        ''' Constructor that allows the class to create an instance/object and initialize the attributes'''
        self.sides = sides

    def __repr__(self):
        ''' Special Method to return the canonical string representation of the object ''' 
        return 'TenSidedDie({})'.format(self.side)   
    


class TwentySidedDie(SixSidedDie):
    '''This class will represent the action of rolling a 20-sided die and the value rolled.'''

    sidesOfDie = 20   
    
    def __init__(self, sides = 20):
        ''' Constructor that allows the class to create an instance/object and initialize the attributes'''
        self.sides = sides

    def __repr__(self):
        ''' Special Method to return the canonical string representation of the object ''' 
        return 'TwentySidedDie({})'.format(self.side)



class Cup:
    ''' This class will represent the cup that will hold the dice.'''

    def __init__(self, six=1, ten=1, twenty=1):
        ''' Constructor that allows the class to create an instance/object and initialize the attributes'''
        self.six    = six        # number of 6-sided die, initialized to 1 in constructor
        self.ten    = ten        # number of 10-sided die, initialized to 1 in constructor
        self.twenty = twenty     # number of 20-sided die, initialized to 1 in constructor

        self.die_SixSided = SixSidedDie()
        self.die_TenSided = TenSidedDie()
        self.die_TweSided = TwentySidedDie()

        

    def roll(self):
        ''' This method will allow the user-selected number of dice, in the cup to roll. '''
        ''' This method uses composition to access the methods from the earlier 6-sided, 10-sided and 20-sided dice functions.'''

        self.list_six = []
        self.list_ten = []
        self.list_twenty = []
        self.cupTotal = []
        
        for _ in range(self.six): #  Roll dice the number of time user enters.
            self.ans_six = self.die_SixSided.roll()
            self.list_six.append(self.ans_six)
            self.cupTotal.append("SixSidedDie({})".format(self.ans_six) )
            #print("List six -->",self.list_six)     #print statement used for testing.

        for _ in range(self.ten):  #  Roll dice the number of time user enters.  
            self.ans_ten = self.die_TenSided.roll()
            self.list_ten.append(self.ans_ten)
            self.cupTotal.append("TenSidedDie({})".format(self.ans_ten) )
            #print("List ten --> ", self.list_ten)  #print statement used for testing.

        for _ in range(self.twenty): #  Roll dice the number of time user enters.  
            self.ans_twe = self.die_TweSided.roll()
            self.list_twenty.append(self.ans_twe)
            self.cupTotal.append("TwentySidedDie({})".format(self.ans_twe) )
            #print("List twenty --> ", self.list_twenty)  #print statement used for testing.
        
            self.Value = sum (self.list_six) + sum(self.list_ten) + sum(self.list_twenty)  # return total value of all dice
        #return self.Value
        return sum (self.list_six) + sum(self.list_ten) + sum(self.list_twenty)
  

    def getSum(self):
        ''' This method will print the total face value of the dice '''
        
        self.diceValue = sum (self.list_six) + sum(self.list_ten) + sum(self.list_twenty)
        #print(self.diceValue)
        return self.diceValue


    def __repr__(self):
        ''' Special Method to return the canonical string representation of the object '''

        return 'Cup( {} )'.format(self.cupTotal).replace("[","").replace("]","")

