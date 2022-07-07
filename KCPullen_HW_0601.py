# Keiland Pullen
# DSC 430: Python Programming
# Due Date 10/29/2019
# Link to video: https://youtu.be/4rDMQUpYcdU
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Assignment 0601: Avocados


import statistics

from decimal import *

def main():
    ''' Main function for this program'''

    def getData():
        '''This function will open the .csv file, collect the data, then close the file'''
        fileName = "avocado.csv"                     # Declare file name - relational location
        
        inFile = open(fileName, "r")                 # Open file and read into lists
        listFile = inFile.readlines()
        inFile.close()                               # Always close the file

        totalVolume = []
        
        for item in listFile:                        # This loop will take the Total Volume column and place into a list
            avocadoList = item.split(',')
            totalVolume.append(avocadoList[3])

        totalVolume = totalVolume[1:]                # Remove "Total Volume" header
            #print(totalVolume)
            
        return totalVolume

    
        
    def readAndComputeMean_SM(totalVolume):
        '''This function will use the Statistics module to calculate the Mean of 'Total Volume'. '''
        
        for i in range(0, len(totalVolume) ):
            totalVolume[i] = Decimal(totalVolume[i])  # convert numbers in list from string to decimal format
            #totalVolume[i] = int(totalVolume[i])
            
        
        total = sum(totalVolume)        
        average = statistics.mean(totalVolume)         # uses mean function from statistics module
        
        # for testing - print("Sum is {} ".format(total) )
        # for testing - print("Mean is {0:.2f}".format(average) )

        return average                                   # returns the mean
        

    def readAndComputeSD_SM(totalVolume):
        '''This function will use the Statistics module to calculate the Standard Deviation of 'Total Volume'. '''
         
        for i in range(0, len(totalVolume) ):
            totalVolume[i] = Decimal(totalVolume[i])           # convert numbers in list from string to decimal format
            
        total = sum(totalVolume)
        stanDev = statistics.stdev(totalVolume)                # uses standard deviation function from statistics module

        # for testing - print("Standard Deviation is {0:.2f}".format(stanDev) )

        return stanDev                                        # returns the standard deviation


    def readAndComputeMedian_SM(totalVolume):
        '''This function will use the Statistics module to calculate the Median of 'Total Volume'. '''
    
        for i in range(0, len(totalVolume) ):
            totalVolume[i] = Decimal(totalVolume[i])          # convert numbers in list from string to decimal format
  
        total = sum(totalVolume)
        statMedian = statistics.median(totalVolume)           # uses the median function from the statistics module
        
        # for testing - print("The Median is {0:.2f}".format(statMedian) )

        return statMedian                                      # returns the median

    
    def readAndComputeMean_HG(totalVolume):
        '''This function will calculate the Mean of 'Total Volume' by a yet to be patented Home Grown solution '''

        totalNum = len(totalVolume)
        
        for i in range(0, len(totalVolume) ):
            totalVolume[i] = Decimal(totalVolume[i])            # convert numbers in list from string to decimal format

        total = sum(totalVolume)                                # use SUM function to calculate total

        hgMean = total / totalNum                               # Home Grown Mean calculation

        # for testing - print ("Homegrown Mean = {}".format(hgMean) )

        return hgMean                                            # returns Home Grown Mean value
        


    def readAndComputeSD_HG(totalVolume):
        '''This function will calculate the Mean of 'Total Volume' by a yet to be
patented Home Grown Standard Deviation solution. '''

        import math                                              # import math module if needed for Stand Dev calculations
        
        totalNum = len(totalVolume)
        
        for i in range(0, len(totalVolume) ):
            totalVolume[i] = Decimal(totalVolume[i])            # convert numbers in list from string to decimal format

        total = sum(totalVolume)                                # use SUM function to calculate total

        hgMean = total / totalNum                                # Home Grown Mean calculation

        var = sum(pow(x - hgMean,2) for x in totalVolume) / (totalNum-1)   # pt.1 Home Grown Standard deviation calculation

        std = math.sqrt(var)                                    # pt.2 Home Grown Standard deviation calculation

        # for testing - print("Home grown Standard Deviation is {}".format(std) )

        return std                                              # return Home Grown Standard Deviation

        

    def readAndComputeMedian_HG(totalVolume):
        '''This function will use the Mean of 'Total Volume' by a Home Grown solution'''
        
        totalNum = len(totalVolume)
        
        for i in range(0, len(totalVolume) ):
            totalVolume[i] = Decimal(totalVolume[i])         # convert numbers in list from string to decimal format

        total = sum(totalVolume)

        hgMean = total / totalNum

        totalVolume.sort()                                  # We opted to use the sort (linear) function here

        if totalNum%2 == 0:                                 # Home Grown calculation to find the median
            median1 = totalVolume[totalNum//2]
            median2 = totalVolume[totalNum//2 -1]
            median = (median1 + median2)/2
        else:
            median = totalVolume[totalNum//2]

        # for testing - print ("Median med is " + str(median))

        return median                                        # return the Home Grown Median



    def readAndComputeMean_MML():
        '''This function will calculate the Mean of 'Total Volume' without memory loss '''

        count = 0
        total = 0
        fileName = "avocado.csv"                     # Declare file name - relational location

        with open(fileName) as inFile:                 # read file in one line at a time
            next(inFile)                                    # skip first line in file, which is header file
            for line in inFile:
                count += 1                                  # counter
                numLine = line.split(',')                   # convert each line to a list item
                total += Decimal(numLine[3])                # get total of 4th column

                                                            # for testing --- print(count, total)
        return total/count

        

    def readAndComputeSD_MML():
        '''This function will calculate the Standard Deviation without memory loss'. '''

        import math
        
        m = 0
        S = 0
        n = 0
        fileName = "avocado.csv"                     # Declare file name - relational location

        with open(fileName) as inFile:                 # read file in one line at a time
            next(inFile)                                    # skip first line in file, which is header file
            for line in inFile:
                numLine = line.split(',')                   # convert each line to a list item
                prev_mean = m
                n = n + 1
                m = m + (Decimal(numLine[3])-m)/n
                S = S + (Decimal(numLine[3])-m)*(Decimal(numLine[3])-prev_mean)

        return math.sqrt(S/(n-1) )



    def readAndComputeMedian_MML():
        '''This function will use the bin method to determine the median '''

        fileName = "avocado.csv"                     # Declare file name - relational location

        inFile = open(fileName, "r")
        listFile = inFile.readlines()
        inFile.close()

        totalVolume = []
        n = 0
        for item in listFile:
            avocadoList = item.split(',')
            totalVolume.append(avocadoList[3])
            n += 1

        totalVolume = totalVolume[1:]  # remove header row
        
        def findMed(totalVolume):
            ''' Function to define and populate bins ''' 

            if len(totalVolume) == 1:
                #print (" Total volume => {}".format(totalVolume) )
                return totalVolume
            
            counts = []   
            maxVal = max(totalVolume)
            minVal = min(totalVolume)

            floatTotal = []
            for item in totalVolume:
                floatTotal.append(float(item))

            temp = 0
            tempJ = 0
            
            sumVal = sum(floatTotal) 
            
            a = len(totalVolume)
            n = int( a / 10 )

            for i in range(0, 10):
                arr = []
                for j in range(i * n, (i + 1) *n ):
                    if j>=a:
                        break
                    arr = arr + [float(totalVolume[j]) ]
                    
                    SumValue = sum(arr)

                medVal = (SumValue / sumVal)

                if medVal > temp:       # check if median value of array is less than previous array value
                    temp = medVal       # if value is bigger, then temp is new array value
                    tempJ = arr         # tempJ becomes array with bigger median value
            
            findMed(tempJ)

        findMed(totalVolume)       
        return totalVolume

            
    totalVolume = getData()

    mean_SM = readAndComputeMean_SM(totalVolume)
    

    sd_SM = readAndComputeSD_SM(totalVolume)
   
    
    median_SM = readAndComputeMedian_SM(totalVolume)
    

    mean_HG = readAndComputeMean_HG(totalVolume)
    

    sd_HG = readAndComputeSD_HG(totalVolume)
   

    median_HG = readAndComputeMedian_HG(totalVolume)
  

    mean_MML = readAndComputeMean_MML()
   

    sd_MML = readAndComputeSD_MML()
   

    median_MML = readAndComputeMedian_MML()
    #print (median_MML)
    
    mean_MML = readAndComputeMean_MML()
    
  

    print (" Method \t Mean \t\t Stan Dev \t Median")
    print (" Python \t {:7.2f} \t {:7.2f} \t {:7.2f}".format(mean_SM, sd_SM, median_SM) )
    print (" HG \t\t {:7.2f} \t {:7.2f} \t {:7.2f}".format(mean_HG, sd_HG, median_HG) )
    print (" MML \t\t {:7.2f} \t {:7.2f} \t {:7.2f}".format(mean_MML, sd_MML, mean_MML) )

main()    


    

