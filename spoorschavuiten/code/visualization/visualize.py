import matplotlib # type: ignore
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt # type: ignore
from code.classes.classes import Region
from adjustText import adjust_text # type: ignore

#test
def makeMap(region: Region) -> None:
    '''
    All stations and connections are imported, stations are made to a dot on the plot.
    Connections are made to be a line between dots on the plot.  
    '''

    plt.style.use('_mpl-gallery')
    plt.figure(figsize=(6,7.5))
    xConnection = []
    yConnection = []

    x = []
    y = []
    drawDots(region, x, y)
    drawLines(region, xConnection, yConnection)

    plt.grid(False)


def onlyLines(region):
    plt.style.use('_mpl-gallery')
    plt.figure(figsize=(6,7.5))
    xConnection = []
    yConnection = []

    drawLines(region, xConnection, yConnection)
    plt.grid(False)

def makeMapWithNames(region: Region) -> None:
    '''
    All stations and connections are imported, stations are made to a dot on the plot.
    Connections are made to be a line between dots on the plot.  
    '''
    plt.style.use('_mpl-gallery')
    plt.figure(figsize=(6,7.5))
    xConnection = []
    yConnection = []
    x = []
    y = []
    drawDotsWithNames(region, x, y)
    drawLines(region, xConnection, yConnection)

    plt.grid(False)


def visualizeMap(region: Region, name: str) -> None:
    '''
    Draws a map of the train network of the Netherlands.
    '''
    # makeMap(region)
    # drawUsedConnections(region)
    plt.savefig(name)
    plt.show()


def drawDots(region: Region, x: list, y: list) -> None:
    '''
    Draw all stations as dots on the map.
    '''
    z = []
    for station in region._stations:
        x.append(region._stations[station]._x)
        y.append(region._stations[station]._y)
        # z.append(region._stations[station]._name)
    plt.scatter(x, y, c= "black", s=30)
    plt.axis("off")


def drawDotsWithNames(region: Region, x: list, y: list) -> None:
    '''
    Draw all stations as dots on the map.
    '''
    z = []
    for station in region._stations:
        x.append(region._stations[station]._x)
        y.append(region._stations[station]._y)
        z.append(region._stations[station]._name)
    plt.scatter(x, y, c= "black", s=30)

    # for i, txt in enumerate(z):
    #     plt.annotate(txt, (x[i], y[i]))

    label = [plt.annotate(txt, (x[i], y[i])) for i, txt in enumerate(z)]
    adjust_text(label)
    plt.axis("off")


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
        plt.plot(xList, yList, ":", c = "gray")

        xList.clear()
        yList.clear()


def drawUsedConnections(region: Region, color: list) -> None:
# def drawUsedConnections(region: Region) -> None:
    xList = []
    yList = []
    for i, route in enumerate(region._routes):
        for connection in route._route:
            xA = connection._stationA._x
            yA = connection._stationA._y
            xB = connection._stationB._x
            yB = connection._stationB._y

            xList.append(xA)
            yList.append(yA)
            xList.append(xB)
            yList.append(yB)
            plt.plot(xList, yList, c = color[i])
            # print(color)
            xList.clear()
            yList.clear()


def outputGraph(outputs: list, time: list) -> None:
    y = outputs
    y.sort()
    x = time
    plt.bar(x, y)
    plt.savefig('aantalPuntenMetRandom.png')
    plt.show()


def outputGraphHist(outputs: list, time: list) -> None:
    y = outputs
    y.sort()
    x = time
    plt.hist(y, bins=10)
    plt.savefig('figures/scoreVerdeling.png')
    plt.show()