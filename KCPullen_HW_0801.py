# Keiland Pullen
# DSC 430: Python Programming
# Due Date 11/12/2019
# Link to video: https://youtu.be/lHWtXAXAmGk
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Assignment 0801: Plot Generator

import random       

def getNames():
    '''Funtion to open plot_names file and selct a plot name'''

    nameFile = open("plot_names.txt","r")                   # open plot_names file 
    listPlotNames = nameFile.readlines()                    # read file into array of lines
    nameFile.close()
  
    return listPlotNames                                    # return array of plot names


def getAdjectives():
    '''Funtion to open plot_adjectives file and selct a plot adjective'''
    
    adjsFile = open("plot_adjectives.txt","r")              # open plot_adjectives file
    listPlotAdjs = adjsFile.readlines()                     # read file into array of lines
    adjsFile.close()

    return listPlotAdjs                                     # return array of plot adjectives


def getProfessions():
    '''Funtion to open plot_adjectives file and selct a plot adjective'''
                                                            # !!! notice the spelling of the file name !!!
    ProfFile = open("plot_profesions.txt","r")              # open "plot_profesions" file
    listPlotProf = ProfFile.readlines()                     # read file into array of lines
    ProfFile.close()

    return listPlotProf                                     # return array of plot professions


def getVerbs():
    '''Function to open plot_verbs file and select verbs'''

    verbFile = open("plot_verbs.txt","r")                   # open plot_verbs file
    listPlotVerbs = verbFile.readlines()                    # read file into array of lines
    verbFile.close()

    return listPlotVerbs                                    # return array of plot verbs


def getAdjectivesEvil():
    '''Function to open plot_adjectives_evil and select evil plot adjectives'''
    
    evilAdjsFile = open("plot_adjectives_evil.txt","r")     # open plot_adjectives_evil file
    listPlotEvilAdjs = evilAdjsFile.readlines()             # read file into array of lines
    evilAdjsFile.close()

    return listPlotEvilAdjs                                 # return array of evil plot adjectives


def getVillainJob():
    '''Function to open plot villains job and select a career for our villain'''
                                                            # !!! Pay attention to the spelling of "plot_villian_job"
    villainJobFile = open("plot_villian_job.txt","r")       # open plot_villian_job file
    listPlotVillainJob = villainJobFile.readlines()         # read file into array of lines
    villainJobFile.close()

    return listPlotVillainJob                               # return array of plot villains jobs


def getVillains():
    '''Funciton to open plot_villains and select our vile villains'''
    
    villainFile = open("plot_villains.txt","r")             # open plot_villains file
    listPlotVillain = villainFile.readlines()               # read file into array of lines
    villainFile.close()

    return listPlotVillain                                  # return array of plot villains



class SimplePlotGenerator():
    '''Class to create Simple Plot Generator'''
    
    def __init__(self):
        '''Constructor to initiate Simple Plot Generator class'''

    def registerView(self, view):
        '''Function to register our View/Controller'''

        self.view = view
        
        if self.view == "keyboard":                         # The keyboard view will server as our default input/output view
            print ("Default View \n")
            k = keyboardIO()                                # Call keyboardIO class
            aPlot = k.getNameFromUser()
            bPlot = k.getAdjectivesFromUser()
            cPlot = k.getProfFromUser()
            dPlot = k.getVerbsFromUser()
            ePlot = k.getEvilAdjectivesFromUser()
            fPlot = k.getVillainJobFromUser()
            gPlot = k.getVillainsFromUser()
            intStatement = ("{}, a {} {}, must {} the {} {}, {}".format(aPlot.replace("\n",""),bPlot.replace("\n",""),cPlot.replace("\n",""),dPlot.replace("\n",""),ePlot.replace("\n",""),fPlot.replace("\n",""),gPlot.replace("\n","")) )
            print ()
            print (intStatement)
            
        elif self.view == "gui":                            # View for GUI
            print ("There is a GUI")
            
        elif self.view == "app":                            # View for APPs
            print ("There is an APP")
            
        elif self.view == "web":                            # View for Web pages
            print ("There is a Web Page")
            
        else:
            print("Spaceholder for additonal view")         # Spaceholder for future View(s)

        return
        

    def generate(self):                                     
        '''Function to return plot for Simple Plot Generator'''

        msg = "Something happens"

        return msg



class RandomPlotGenerator(SimplePlotGenerator):         #  Extend SimplePlotGenerator
    '''Class to create a Random Plot Generator'''

    def generate(self):
        '''Function to return random plot'''

        def getPlotNames():
            '''Funtion to open plot_names file and selct a random plot name'''
           
            listPlotNames = getNames()
            randPlotName = random.choice(listPlotNames)     # Use Random function to return random plot name

            return randPlotName.replace("\n","")

        def getPlotAdjectives():
            '''Funtion to open plot_adjectives file and selct a random plot adjective'''
            
            listPlotAdjs = getAdjectives()
            randPlotAdjs = random.choice(listPlotAdjs)      # Use Random function to return random plot adjective

            return randPlotAdjs.replace("\n","")
        

        def getPlotProfessions():
            '''Funtion to open plot_professions file and selct a random plot profession'''

            listPlotProf = getProfessions()
            randPlotProf = random.choice(listPlotProf)      # Use Random function to return random plot profession

            return randPlotProf.replace("\n","")


        def getPlotVerbs():
            '''Funtion to open plot_verbs file and selct a random plot verb'''

            listPlotVerbs = getVerbs()
            randPlotVerbs = random.choice(listPlotVerbs)    # Use Random function to return random plot verb

            return randPlotVerbs.replace("\n","")

        def getPlotAdjectivesEvil():
            '''Funtion to open plot_adjectives_evil file and selct a random plot evil adjective'''

            listPlotEvilAdjs = getAdjectivesEvil()
            randPlotEvilAdjs = random.choice(listPlotEvilAdjs)  # Use Random function to return random evil plot adjective

            return randPlotEvilAdjs.replace("\n","")

        def getPlotVillainJob():
            '''Funtion to open plot_villains_job file and selct a random plot villain job'''
            
            listPlotVillainJob = getVillainJob()
            randPlotVillainJob = random.choice(listPlotVillainJob)  # Use Random function to return random plot villain job

            return randPlotVillainJob.replace("\n","")


        def getPlotVillains():
            '''Funtion to open plot_villains file and selct a random plot villain'''
       
            listPlotVillain = getVillains()
            randPlotVillain = random.choice(listPlotVillain)         # Use Random function to return random plot villain

            return randPlotVillain.replace("\n","")

        rpgPlotName             = getPlotNames()                    # Read plots into variables
        rpgPlotAdjs             = getPlotAdjectives()
        rpgPlotProf             = getPlotProfessions()
        rpgPlotVerbs            = getPlotVerbs()
        rpgPlotAdjectivesEvil   = getPlotAdjectivesEvil()
        rpgPlotVillainJob       = getPlotVillainJob()
        rpgPlotVillains         = getPlotVillains()

        statement = ("{}, a {} {}, must {} the {} {}, {}".format(rpgPlotName,rpgPlotAdjs,rpgPlotProf,rpgPlotVerbs,rpgPlotAdjectivesEvil,rpgPlotVillainJob,rpgPlotVillains) )
        
        return statement   # returns random plot string



class InteractivePlotGenerator(SimplePlotGenerator):                    # Extend SimplePlotGenerator
    '''Class to create the Interactive Plot Generator'''

    def view(self, io):
        '''Function to declare a view'''
        
        self.io = io
        self.registerView(self.io)
             
    def generate(self, io="keyboard"):                      # generate plot with default view as keyboard
        '''Function to return Interactive Plot'''
        
        #io = "keyboard"     # hardcoded views for testing
        #io = "app"
        self.view(io)        # call function to register view



class keyboardIO():                          # Class for keyboard view, which is our default basic I/O view
    '''Class for KeyBoard Input Output'''

    def __init__(self):
        '''Constructor to initiate Simple Plot Generator class'''

    def getNameFromUser(self):
        '''Function to prompt user and get name'''

        getPlotName = getNames()                           # Call function to read plot names from file
        intPlotName =  random.sample(getPlotName, k=5)     # Read 5 random plot names 
        print ("Plot Names:")
        
        for x in range(0, len(intPlotName)):               # Loop to print 5 plot names and prompt user to select one
            print(x+1, intPlotName[x])
            
        getIntPlotName = int(input("Please select one of the names from the above list of plot name - enter a number: "  ))

        #print (intPlotName[getIntPlotName - 1])
        return intPlotName[getIntPlotName - 1]
    

    def getAdjectivesFromUser(self):
        '''Function to prompt user to select an adjective'''

        getPlotAdj = getAdjectives()                        # Call function to read plot names from file
        intAdjectives = random.sample(getPlotAdj, k=5)      # Read 5 random plot names 
        print ("Plot Adjectives:")

        for x in range(0, len(intAdjectives)):              # Loop to print 5 plot adjectives and prompt user to select one
            print(x+1, intAdjectives[x])

        getIntAdjectives = int(input("Please select a plot adjective from the above list - enter a number: "))
        #print (intAdjectives[getIntAdjectives - 1])
        return intAdjectives[getIntAdjectives - 1]

    def getProfFromUser(self):
        '''Function to prompt user to select a plot profession'''

        getPlotProf = getProfessions()                      # Call function to read plot professions from file
        intProfessions = random.sample(getPlotProf, k=5)    # Read 5 random plot professions
        print ("Plot Professions:")

        for x in range(0, len(intProfessions)):             # Loop to print 5 plot professions and prompt user to select one
            print(x+1, intProfessions[x])

        getIntProfessions = int(input("Please select a Plot Profession from the above list - enter a number: "))
        #print (intProfessions[getIntProfessions - 1])
        return (intProfessions[getIntProfessions - 1])

    def getVerbsFromUser(self):
        '''Function to prompt user to select a plot verg'''

        getPlotVb = getVerbs()                          # Call function to read plot verbs from file
        intVerbs = random.sample(getPlotVb, k=5)        # Read 5 random plot professions
        print ("Plot Verbs:")
                
        for x in range(0, len(intVerbs)):
            print(x+1, intVerbs[x])

        getIntVerbs = int(input("Please select a Plot Verb from the above list - enter a number: "))
        #print (intVerbs[getIntVerbs - 1])
        return (intVerbs[getIntVerbs - 1])

    def getEvilAdjectivesFromUser(self):
        '''Function to prompt user to select an evil adjective for our vile villain'''
        
        getPlotEvilAdj = getAdjectivesEvil()            # Call function to read evil plot adjectives from file
        intEvilAdj = random.sample(getPlotEvilAdj, k=5) # Read 5 random evill plot adjectives
        print ("Plot Evil Adjectives:")
    
        for x in range(0, len(intEvilAdj)):
            print(x+1, intEvilAdj[x])

        getIntEvilAdj = int(input("Please select an Evil Plot Adjective from the above list - enter a number: "))
        #print(intEvilAdj[getIntEvilAdj - 1])
        return(intEvilAdj[getIntEvilAdj - 1])

    def getVillainJobFromUser(self):
        '''Function to prompt user to select a job for our evil villain'''
        
        getPlotVillainJob = getVillainJob()                     # Call function to read evil plot villain jobs from file
        intVillainJob = random.sample(getPlotVillainJob, k=5)   # Read 5 random evil plot jobs
        print ("Plot Villain Jobs:")

        for x in range(0, len(intVillainJob)):
            print(x+1, intVillainJob[x])

        getIntVillainJob = int(input("Please select a job for the evil villain from the above list - enter a number; "))
        #print(intVillainJob[getIntVillainJob -1])
        return (intVillainJob[getIntVillainJob -1])
        
    def getVillainsFromUser(self):
        '''Function to prompt user to select a villain'''
        
        getPlotVillain = getVillains()                          # Call function to read plot villains from file
        intPlotVillain = random.sample(getPlotVillain, k=5)     # Read 5 random plot villains
        print ("Plot Villains:")

        for x in range(0, len(intPlotVillain)):
            print(x+1, intPlotVillain[x])

        getIntPlotVillain = int(input("Please select a plot villain from the above list - enter a number: "))
        #print(intPlotVillain[getIntPlotVillain - 1])
        return (intPlotVillain[getIntPlotVillain -1])
        

        

        
            
    
    
