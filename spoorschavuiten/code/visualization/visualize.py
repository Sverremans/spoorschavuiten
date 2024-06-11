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
    sizes = 30
    color1 = "black"
    color2 = "gray"
# Coordinates Holland
    x = []
    y = []
# Coordinates Netherlands
    xn = []
    yn = []

    plt.figure(figsize=(6,7.5))

    # x, y = makeDots(holland, x,  )
    for station in holland._stations:
        x.append(holland._stations[station]._x)
        y.append(holland._stations[station]._y)

    for station in netherlands._stations:
        xn.append(netherlands._stations[station]._x)
        yn.append(netherlands._stations[station]._y)

    print(x)
    print(y)



    plt.scatter(xn, yn, c= color2, s= sizes)
    plt.scatter(x, y, c= color1, s=sizes)
    
    xConnection = []
    yConnection = []
    print(len(netherlands._connections))
    for connection in netherlands._connections:
        xA = connection._stationA._x
        yA = connection._stationA._y
        xB = connection._stationB._x
        yB = connection._stationB._y

        xConnection.append(xA)
        yConnection.append(yA)
        xConnection.append(xB)
        yConnection.append(yB)
        plt.plot(xConnection, yConnection, c = color2)

        xConnection.clear()
        yConnection.clear()
    plt.grid(False)
    plt.savefig('verbindingenInNederland.png')
    plt.show()

    
    print(len(xConnection))
    print(len(yConnection))

def makeDots(region, x, y):
    for station in region._stations:
        x.append(region._stations[station]._x)
        y.append(region._stations[station]._y)
    return x, y