import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from code.classes.classes import Region

def makeMap(region: Region) -> None:
    '''
    All stations and connections are imported, stations are made to a dot on the plot.
    Connections are made to be a line between dots on the plot.  
    '''

    plt.style.use('_mpl-gallery')
    plt.figure(figsize=(6,7.5))
    xConnection = []
    yConnection = []

# Coordinates Holland
    x = []
    y = []
    drawDots(region, x, y)
    drawLines(region, xConnection, yConnection)

# Coordinates Netherlands
    # xn = []
    # yn = []
    # drawDots(region, xn, yn)
    # drawLines(region, xConnection, yConnection)

    plt.grid(False)


def visualizeMap(region: Region) -> None:
    '''
    Draws a map of the train network of the Netherlands.
    '''
    # makeMap(region)
    # drawUsedConnections(region)
    plt.savefig('verbindingenInNederland.png')
    plt.show()


def drawDots(region: Region, x: list, y: list) -> None:
    '''
    Draw all stations as dots on the map.
    '''
    for station in region._stations:
        x.append(region._stations[station]._x)
        y.append(region._stations[station]._y)
    plt.scatter(x, y, c= "black", s=30)


def drawLines(region: Region, xList: list, yList: list) -> None:
    '''
    Draw all connections as lines on the map.
    '''
    for connection in region._connections:
        xA = connection._stationA._x
        yA = connection._stationA._y
        xB = connection._stationB._x
        yB = connection._stationB._y

        xList.append(xA)
        yList.append(yA)
        xList.append(xB)
        yList.append(yB)
        plt.plot(xList, yList, "-", c = "gray")

        xList.clear()
        yList.clear()

def drawUsedConnections(region: Region, xList: list, yList: list, color: str) -> None:
# def drawUsedConnections(region: Region) -> None:
    xList = []
    yList = []
    for route in region._routes:
        for connection in route._route:
            xA = connection._stationA._x
            yA = connection._stationA._y
            xB = connection._stationB._x
            yB = connection._stationB._y

            xList.append(xA)
            yList.append(yA)
            xList.append(xB)
            yList.append(yB)
            plt.plot(xList, yList, c = color)
            # print(color)
            xList.clear()
            yList.clear()
