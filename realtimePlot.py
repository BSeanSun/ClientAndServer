import matplotlib.pyplot as plt
import random
class realtimePlot:
    #xList = list()
    #yList = list()
    
    def __init__(self,xList,yList):
        
        #plt.ion()
        #if plt.fignum_exists('Figure 1') == False:
        plt.ion()
        #fig = plt.figure()
        #while True:
        #for i in range(50):
        y = random.randrange(50)
        xList.append(xList[-1]+1)
        yList.append(y)
            #makeFig()
        plt.scatter(xList, yList)
        plt.draw()
        #if plt.fignum_exists('Figure 1') == False:
         #   pass
            #plt.draw()
        #plt.pause(0.1)
