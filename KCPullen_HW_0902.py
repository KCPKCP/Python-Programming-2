# Keiland Pullen
# DSC 430: Python Programming
# Due Date 11/19/2019
# Link to video: https://youtu.be/Vc-OYU2Hr6I
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Assignment 0902: Game of Life

import numpy as np                                 # import NumPy module


def conway(s, p):
    '''Conway function to generate a board.'''

    p1 = p
    p2 = 1 - p1
    board = np.random.choice([1, 0], size=s * s, p=[p1, p2])
    board = board.reshape(s,s)
    # print(board)                                  # print BOARD for testing
    # print (p1)                                    # print for testing
    # print (p2)                                    # print for testing

    advance(board, 5)                               # pass board and time to advance function
    
    return 

def advance(b, t):
    '''Function that will accept a Conway board and advances it in t-time via the rules'''

    board = b
    print ("Time is hard-coded at ",t)
    
    print("Initial Board \n",board)

    # print ("Length of board = ",len(board) )          # print for testing
    # print ("Board[x,y] 2,3 = ",board[2,3] )           # print for testing
    
    length = ( len(board) )

    while 0 < t:                                        # while loop for time value
        
        for x in range(length):                         # loops to calculate the values of surrounding plots
            for y in range(length):
                total = int(  board[x,(y-1)%length] + board[x,(y+1)%length]
                            + board[(x-1)%length,y] + board[(x+1)%length,y] 
                            + board[(x-1)%length,(y-1)%length] + board[(x-1)%length,(y+1)%length]
                            + board[(x+1)%length,(y-1)%length] + board[(x+1)%length,(y+1)%length] )

                if board[x,y] == 1:                     # implement Conway rules
                    if (total < 2) or (total > 3):
                        board[x,y] = 0
                else:
                    if (total == 2) or (total == 3):
                        board[x,y] = 1

                if board[x,y] == 0:
                    if total == 3:
                        board[x,y] = 1

        print ("New Board \n",board)
        #print(t)
        t = t - 1                                       # decrement While (time) loop

    
            

    
