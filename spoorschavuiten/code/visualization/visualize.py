import matplotlib # type: ignore
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt # type: ignore
from code.classes.classes import Schedule
from adjustText import adjust_text # type: ignore
import geopandas as gpd # type: ignore

# TODO
# Schrijf een paar functies om zadat deze logische gebruikt kunnen woprden


def makeMap(schedule: Schedule) -> None:
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

    drawMapHolland()
    drawDots(schedule, x, y)
    drawLines(schedule, xConnection, yConnection)

    plt.grid(False)


def onlyLines(schedule):
    # plt.style.use('_mpl-gallery')
    # plt.figure(figsize=(6,7.5))
    xConnection = []
    yConnection = []

    # drawMapHolland()
    drawMapNetherlands()
    drawLines(schedule, xConnection, yConnection)
    plt.grid(False)

def makeMapWithNames(schedule: Schedule) -> None:
    '''
    All stations and connections are imported, stations are made to a dot on the plot.
    Connections are made to be a line between dots on the plot.  
    '''
    # plt.style.use('_mpl-gallery')
    # plt.figure(figsize=(6,7.5))
    xConnection = []
    yConnection = []
    x = []
    y = []
    # drawMapHolland()
    drawMapNetherlands()
    drawDotsWithNames(schedule, x, y)
    drawLines(schedule, xConnection, yConnection)

    plt.grid(False)


def visualizeMap(schedule: Schedule, name: str) -> None:
    '''
    Draws a map of the train network of the Netherlands.
    '''
    # makeMap(schedule)
    # drawUsedConnections(schedule)
    plt.savefig(name)
    plt.show()


def drawDots(schedule: Schedule, x: list, y: list) -> None:
    '''
    Draw all stations as dots on the map.
    '''
    z = []
    for station in schedule._stations:
        x.append(schedule._stations[station]._x)
        y.append(schedule._stations[station]._y)
        # z.append(schedule._stations[station]._name)
    plt.scatter(x, y, c= "black", s=30)
    plt.axis("off")


def drawDotsWithNames(schedule: Schedule, x: list, y: list) -> None:
    '''
    Draw all stations as dots on the map.
    '''
    z = []
    for station in schedule._stations:
        x.append(schedule._stations[station]._x)
        y.append(schedule._stations[station]._y)
        z.append(schedule._stations[station]._name)
    plt.scatter(x, y, c= "black", s=30)

    # for i, txt in enumerate(z):
    #     plt.annotate(txt, (x[i], y[i]))

    label = [plt.annotate(txt, (x[i], y[i])) for i, txt in enumerate(z)]
    adjust_text(label)
    plt.axis("off")


def drawLines(schedule: Schedule, xList: list, yList: list) -> None:
    '''
    Draw all connections as lines on the map.
    '''
    for connection in schedule._connections:
        xA = connection._stationA._x
        yA = connection._stationA._y
        xB = connection._stationB._x
        yB = connection._stationB._y

        xList.append(xA)
        yList.append(yA)
        xList.append(xB)
        yList.append(yB)
        plt.plot(xList, yList, ":", c = "black")

        xList.clear()
        yList.clear()


def drawUsedConnections(schedule: Schedule, color: list) -> None:
# def drawUsedConnections(schedule: schedule) -> None:
    xList = []
    yList = []
    for i, route in enumerate(schedule._routes):
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


def drawMapHolland():
    mapPlaces = gpd.read_file("data/holland_.geojson")
    mapPlaces.plot(color = "white", edgecolor = "grey")


def drawMapNetherlands():
    mapPlaces = gpd.read_file("data/netherlands_.geojson") 
    mapPlaces.plot(color = "white", edgecolor = "grey")