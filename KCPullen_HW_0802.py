# Keiland Pullen
# DSC 430: Python Programming
# Due Date 11/12/2019
# Link to video: https://youtu.be/bZKcgTuVNKo
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Assignment 0802: Plot Generator


import KCPullen_HW_0801                                 # import HW_0801 assignment

from KCPullen_HW_0801 import SimplePlotGenerator        # import Classes from HW_0801 python file
from KCPullen_HW_0801 import RandomPlotGenerator
from KCPullen_HW_0801 import InteractivePlotGenerator


class PlotViewer():
    '''Class to create Plot Viewer class'''
    
    def __init__(self):
        '''Constructor to initiate Plot viewer class'''

        

    def registerPlotGenerator(self, pg):
        '''Function to register Plot Generators, default standard io is keyboard '''

        self.pg = pg                                    # we need to register the type of class
        
        return

    def view(self, io):
        '''Function to declare a view'''                # This function can be used to register the different views.

        self.io = io
        
        
    def generate(self):
        '''Function to return plot'''                   # In this function, we will use If-Else statements to determine
                                                        # which class is being called, then we will execute that clause.
        

        if type(self.pg) == KCPullen_HW_0801.SimplePlotGenerator:
            print("Simple Plot Generator")
            msg = KCPullen_HW_0801.SimplePlotGenerator.generate(self)
            print (msg)
            
        elif type(self.pg) == KCPullen_HW_0801.RandomPlotGenerator:
            print("Random Plot Generator")
            msg = KCPullen_HW_0801.RandomPlotGenerator.generate(self)
            print (msg)
            
        elif type(self.pg) == KCPullen_HW_0801.InteractivePlotGenerator:
            print("Interactive Plot Generator")
            msg = KCPullen_HW_0801.InteractivePlotGenerator()
            msg.generate()                              # The default view is Keyboard
            #msg.generate("app")                        # The app view can be called here as an option
            #msg.generate("gui")                        # The gui view can be called here as an option
            
               

        return

        
