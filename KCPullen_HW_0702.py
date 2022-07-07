# Keiland Pullen
# DSC 430: Python Programming
# Due Date 11/5/2019
# Link to video: 
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Assignment 0702: Overlapping Ellipses


import KCPullen_HW_0701

class Point():
    '''Class to create points for the Ellipsis'''
    def __init__(self,x,y):
        '''Constructor to initiate class'''

        self.x = x
        self.y = y

        self.createPoint(self.x,self.y)

    def createPoint(self,x,y):
        '''Function to create the point'''
        self.x = x
        self.y = y
        self.point = []
        self.point.append(self.x)
        self.point.append(self.y)
        print("Point is ",self.point)
        

class Ellipse():
    '''Class to create points for the Ellipses'''
    def __init__(self, p1, p2, width):
        '''Constructor to initiate Ellipse class'''
        Point.p1 = p1
        Point.p2 = p2
        self.width = width
        # print (Point.p1.point, Point.p2.point)
        
        self.createEllipse()


    def createEllipse(self):
        '''Function to determine X, X', Y, and Y' of each point'''
        
        self.p1 = []
        self.p2 = []

        for i in range(len(Point.p2.point)):
            print(Point.p2.point[i])
            self.p1.append(Point.p1.point[i])
            self.p2.append(Point.p2.point[i])
        
            
        print ("p1, p2 and width =  {} {} {}".format(Point.p1.point, Point.p2.point, self.width) )


    

def computeOverlapOfEllipses(e1,e2):
    '''Function to calculate the over lapping area of 2 ellipses'''

    Ellipse.e1 = e1
    Ellipse.e2 = e2

    e1Width = str(Ellipse.e1.width)
    e2Width = str(Ellipse.e2.width)
    
    
    print("E1 width = ",e1Width)
    print("E2 width = ",e2Width)

    x1       = ''
    x2       = ''
    x1Prime  = ''
    x2Prime  = ''
    y1       = ''
    y2       = ''
    y1Prime  = ''
    y2Prime  = ''
    listX = []
    listY = []
    listW = []
    listW.append(int(e1Width))
    listW.append(int(e2Width))
    
    print()
    
    for i in range(0, len(Ellipse.e1.p1)) :
        print(" i = ",i)
        if i == 0:
            x1 = Ellipse.e1.p1[i]
            x2 = Ellipse.e1.p2[i]
            listX.append(x1)
            listX.append(x2)
        else:
            y1 = Ellipse.e1.p1[i]
            y2 = Ellipse.e1.p2[i]
            listY.append(y1)
            listY.append(y2)

    print("x1 = {}, x2 = {}, y1 = {}, y2 = {}".format(x1, x2, y1, y2) )

    print()
    
    for j in range(0,len(Ellipse.e2.p1)):   
        if j == 0:
            x1Prime = Ellipse.e2.p1[j]
            x2Prime = Ellipse.e2.p2[j]
            listX.append(x1Prime)
            listX.append(x2Prime)
        else:
            y1Prime = Ellipse.e2.p1[j]
            y2Prime = Ellipse.e2.p2[j]
            listY.append(y1Prime)
            listY.append(y2Prime)

    print("x1Prime = {}, x2Prime = {}, y1Prime = {}, y2Prime = {}".format(x1Prime, x2Prime, y1Prime, y2Prime) )

    print("List x: ",listX)
    print("List y: ",listY)
    print("List w: ",listW)

    minX = min(listX)
    maxX = max(listX)
    minY = min(listY)
    maxY = max(listY)
    minW = min(listW)
    maxW = max(listW)
    

    print ("Min x = {}, Max X = {}, Min Y = {}, Max Y = {}".format(minX, maxX, minY, maxY) )

    leftSide = int(minX) - (int(maxW)/2)  # Calculate left edge of box
    print ("leftSide",leftSide)

    rightSide = int(maxX) + (int(maxW)/2) # Calculate right edge of box
    print ("rightSide",rightSide)

    topSide = int(maxY) + (int(maxW)/2)   # Calculate top edge of box
    print ("topSide", topSide)

    bottomSide = int(minY) - (int(maxW)/2) # Calulate bottom edge of box
    print ("bottomSide", bottomSide)

    height = abs(topSide - bottomSide)     # Calculate height of box
    
    length = abs(rightSide - leftSide)     # Calculate length of box

    print ("Height = ",height)
    print ("length = ",length)

    #For X, Now multiply random number by Length then add by leftSide...
    #For Y, Now multiply random number by Height then add by topSide...

    listRand = ''
    listRand = randomCall()
    print (listRand)
    print (type(listRand))
    print (listRand[1] )

    print (listRand.values() )

    xyPoint = []
    
    for key in range(1, len(listRand) + 1):
        print(listRand.get(key))
        randPoint = listRand.get(key)
        xPoint = (randPoint * length) + leftSide
        yPoint = (randPoint * height) + bottomSide
        xyPoint.append( (xPoint, yPoint)  )

    print (xyPoint)

    def inEllipse(x1, x2, x1Prime, x2Prime, y1, y2, y1Prime, y2Prime, e1Width, e2Width, points):
        ''' Helper function to determine if point is in ellipse'''
        import math
        
        print("Calculation")
        print("Points", points)
        print("Length of Points = ",len(points) )

        count = 0
        inCount = 0
        inEone = True
        inEtwo = True
        
        for a in range(0, len(points)):
            print(points[a])
            ranXY = points[a]
            ranX, ranY = ranXY[:len(ranXY)//2], ranXY[len(ranXY)//2:]
            print("x = ",ranX)
            print("y = ",ranY)
            #ranX.replace("(","").replace(",","").replace(")","")
            #''.join(ranX)
            ranX = ranX[0]
            ranX = float(ranX)
            #ranY.replace("(","").replace(",","").replace(")","")
            #''.join(ranY)
            ranY = ranY[0]
            ranY = float(ranY)
            print("X = ",ranX)
            print("Y = ",ranY)
        
            distance1 = math.sqrt( (ranX - x1)**2 + (ranY - y1)**2 )
            distance2 = math.sqrt( (ranX - x2)**2 + (ranY - y2)**2 )

            distance1Prime = math.sqrt( (ranX - x1Prime)**2 + (ranY - y1Prime)**2 )
            distance2Prime = math.sqrt( (ranX - x2Prime)**2 + (ranY - y2Prime)**2 )

            distance12 = distance1 + distance2
            distance12Prime = distance1Prime + distance2Prime
            print ("Distance between points in 1st ellipse...", distance1 + distance2)
            print ("Distance between points in 2nd ellipse...", distance1Prime + distance2Prime)

            if (float(e1Width) > distance12):
                print ("Yes, point is in Ellipse 1")
                inEone = True
            else:
                inEone = False

            if (float(e2Width) > distance12Prime):
                print ("Yes, point is in Ellipse 2")
                inEtwo = True
            else:
                inEtwo = False
                
            if (inEone == True) and (inEtwo == True):
                count = 1
            else:
                count = 0


            inCount = inCount + count

        return inCount


    inCount = inEllipse(x1, x2, x1Prime, x2Prime, y1, y2, y1Prime, y2Prime, e1Width, e2Width, xyPoint)

    n = 3
    
    print ("inCount = ",inCount)
    
    areaEllipses = (height * length) * (inCount / n)

    print ("Area of overlap is ",areaEllipses)
        
    


    

def randomCall():
    ''' Call Random function from War-and-Peace to create darts'''
    ''' This should be just a function call... '''
    
    randNumbs = []
    nums = KCPullen_HW_0701.WarAndPeacePseudoRandomNumberGenerator()
    randNumbs = nums.random()

    #print("Random number dictionary --> ",randNumbs)  # print for testing

    return randNumbs

    
