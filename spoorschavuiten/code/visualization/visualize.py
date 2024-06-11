import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
from code.classes.classes import Region

def visualizeMap():
    '''
    All stations and connections are imported, stations are made to a dot on the plot.
    Connections are made to be a line between dots on the plot.  
    '''
    holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
    netherlands = Region("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv")

    plt.style.use('_mpl-gallery')
    
# Coordinates Holland
    x = []
    y = []
# Coordinates Netherlands
    xn = []
    yn = []
    xConnection = []
    yConnection = []
    plt.figure(figsize=(6,7.5))

    drawDots(holland, x, y)
    drawLines(holland, xConnection, yConnection)

    # Coordinates Netherlands
    xn = []
    yn = []
    drawDots(netherlands, xn, yn)
    drawLines(netherlands, xConnection, yConnection)

    
    
    

    

    plt.grid(False)
    plt.savefig('verbindingenInNederland.png')
    plt.show()





def drawDots(region: Region, x: list, y: list):
    for station in region._stations:
        x.append(region._stations[station]._x)
        y.append(region._stations[station]._y)
    plt.scatter(x, y, c= "black", s=30)


def drawLines(region: Region, xList: list, yList: list):
    for connection in region._connections:
        xA = connection._stationA._x
        yA = connection._stationA._y
        xB = connection._stationB._x
        yB = connection._stationB._y

        xList.append(xA)
        yList.append(yA)
        xList.append(xB)
        yList.append(yB)
        plt.plot(xList, yList, c = "gray")

        xList.clear()
        yList.clear()