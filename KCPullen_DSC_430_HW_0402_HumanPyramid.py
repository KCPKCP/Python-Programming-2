# Keiland Pullen
# DSC 430: Python Programming
# Due Date 10/15/2019
# Link to video: https://youtu.be/3WeIWlOL_Xg
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Assignment 0402: Human Pyramid


def main():
    ''' This is the main function for the Human Pyramid program. '''

    def greeting():
        ''' This function is to greet the user and explain the task at hand. '''
        print("\nEnter the Row and Column of a person in the Human Pyramid, and receive the total weight\
 on that person's back.\n")


    def promptForNumbers():
        ''' This function will prompt user to enter two numbers '''
        row = int(input("Please enter the Row : ") )
        col = int(input("Please enter the Column : ")  )

        return row, col


    def humanPyramid(row, col):
        ''' This function is where recursion is performed. The total weight is returned as a result. '''

        #print("Row = {} | Col = {}".format(row,col)) # print statement used for testing
        #print("RowCol = {}{}".format(row,col) )      # print statement user for testing
        if (row == 0):
            return 0
        else:
            weight = 0
            
            if ( col == 0):
                weight =  64 + ( humanPyramid(row - 1, col))
                print("weight = ",weight)
                return weight
            else:
                weight =  64 + ( humanPyramid(row - 1, col)) + 64 + (humanPyramid(row - 1, col -1) )          
                #print("row {} - col {} - weight {}".format(row,col,weight))  # print statement used for testing
                return weight
    

    greeting()
    row, col = promptForNumbers()
    weight = humanPyramid(row,col)

    print ("The total on row {} col {} is: {} ".format(row,col,weight) )

main()



