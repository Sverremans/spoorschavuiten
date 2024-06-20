import matplotlib # type: ignore
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt # type: ignore
from code.classes.classes import Schedule
from adjustText import adjust_text # type: ignore
import geopandas as gpd # type: ignore


def draw_figure_with_names(schedule: Schedule, colors: list, geojson: str, file_name: str):
    '''
    This function starts with drawing the desired region, the geojson file, with station names.
    It uses the schedule that is made to draw the used connections of the routes.
    The last step it takes in plotting the drawing and saving it as a picture.
    '''
    make_map_with_names(schedule, geojson)
    draw_used_connections(schedule, colors)
    visualize_map(file_name)


def draw_figure_without_names(schedule: Schedule, colors: list, geojson: str, file_name: str):
    '''
    This function starts with drawing the desired region, the geojson file, without station names.
    It uses the schedule that is made to draw the used connections of the routes.
    The last step it takes in plotting the drawing and saving it as a picture.
    '''
    make_map(schedule, geojson)
    draw_used_connections(schedule, colors)
    visualize_map(file_name)


def draw_figure_no_stations(schedule: Schedule, colors: list, geojson: str, file_name: str):
    '''
    This function starts with drawing the desired region, the geojson file, without station, only connections.
    It uses the schedule that is made to draw the used connections of the routes.
    The last step it takes in plotting the drawing and saving it as a picture.
    '''
    only_lines(schedule, geojson)
    draw_used_connections(schedule, colors)
    visualize_map(file_name)


def draw_map_background(file_name: str):
    '''
    Imports a geojason file, and uses geopandas to read and plot the file.
    '''
    mapPlaces = gpd.read_file(file_name)
    mapPlaces.plot(color = "white", edgecolor = "grey")


def make_map(schedule: Schedule, geojson: str) -> None:
    '''
    All stations and connections are imported, stations are made to be a dot on the plot.
    Connections are made to be a dotted line between dots on the plot.  
    '''
    xConnection = []
    yConnection = []
    x = []
    y = []

    draw_map_background(geojson)

    draw_dots(schedule, x, y)
    draw_lines(schedule, xConnection, yConnection)
    plt.grid(False)


def make_map_with_names(schedule: Schedule, geojson: str) -> None:
    '''
    All stations and connections are imported, stations are made to a dot on the plot.
    Connections are made to be a line between dots on the plot.
    Names of the different stations are added in the plot.  
    '''
    xConnection = []
    yConnection = []
    x = []
    y = []
    draw_map_background(geojson)

    draw_dots_with_names(schedule, x, y)
    draw_lines(schedule, xConnection, yConnection)

    plt.grid(False)


def only_lines(schedule: Schedule, geojson: str) -> None:
    '''
    All connections are imported, connections are made to be a dotted line between stations on the plot.
    The stations themselves are not shown in this plot.  
    '''
    xConnection = []
    yConnection = []

    draw_map_background(geojson)

    draw_lines(schedule, xConnection, yConnection)
    plt.grid(False)


def visualize_map(name: str) -> None:
    '''
    Draws a map of the train network of the desired region, it saves this picture in a file.
    '''
    plt.axis('off')
    plt.savefig(name)
    plt.show()


def draw_dots(schedule: Schedule, x: list, y: list) -> None:
    '''
    Draws all stations as dots on the map.
    '''
    for station in schedule._stations:
        x.append(schedule._stations[station]._x)
        y.append(schedule._stations[station]._y)
    plt.scatter(x, y, c= "black", s=30)
    plt.axis("off")


def draw_dots_with_names(schedule: Schedule, x: list, y: list) -> None:
    '''
    Draws all stations as dots on the map, also adds the name of the station to the plot.
    '''
    z = []
    for station in schedule._stations:
        x.append(schedule._stations[station]._x)
        y.append(schedule._stations[station]._y)
        z.append(schedule._stations[station]._name)
    plt.scatter(x, y, c= "black", s=30)

    for i, txt in enumerate(z):
        plt.annotate(txt, (x[i], y[i]))

    # label = [plt.annotate(txt, (x[i], y[i])) for i, txt in enumerate(z)]
    # adjust_text(label)
    plt.axis("off")


def draw_lines(schedule: Schedule, xList: list, yList: list) -> None:
    '''
    Draws all connections as lines on the map.
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


def draw_used_connections(schedule: Schedule, color: list) -> None:
    '''
    Draws all connections used in a route, all routes in the schedule get a different color. 
    '''
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


def writeInFile(text: str, file: str):
    file = open(file, "a")
    file.write(text)
    file.close()


def outputToFile(schedule: Schedule, title: str, file: str):
    '''
    Writes the generated output in a desired textfile.
    title: The name of the used algorithm.
    '''
    writeInFile(title, file)
    writeInFile("\n", file)
    writeInFile("\n", file)
    writeInFile("train,stations", file)
    writeInFile("\n", file)
    for i, route in enumerate(schedule._routes, 1):
        writeInFile(f'train_{i},"{route._stations}"', file)
        writeInFile("\n", file)
    writeInFile(f"score,{schedule.calculate_value()}", file)
    writeInFile("\n", file)
    writeInFile("\n", file)
    writeInFile("\n", file)


def makeHillClimberGraph(x: list, y: list, xpoints: list, ypoints:list):
    plt.scatter(x, y, c= "black", s=30)
    
    plt.plot(xpoints, ypoints)

    plt.title("Hill Climber-Algoritme")
    plt.xlabel("Iteraties")
    plt.ylabel("Score")
    # plt.yscale("log")
    plt.xscale("log")
    plt.savefig("data/hillClimber.jpg")
    plt.show()


def outputHillClimberGraph(x: list, y: list, xpoints: list, ypoints:list, title: str, file: str):
    writeInFile(title, file)
    writeInFile("\n", file)
    writeInFile("\n", file)
    writeInFile(f'"x, punten voor lijn tekenen", "{x}"', file)
    writeInFile("\n", file)
    writeInFile(f'"y, punten voor lijn tekenen", "{y}"', file)
    writeInFile("\n", file)
    writeInFile(f'"x, punten van verbetering", "{xpoints}"', file)
    writeInFile("\n", file)
    writeInFile(f'"y, punten van verbetering", "{ypoints}"', file)
    writeInFile("\n", file)
    writeInFile("\n", file)
    writeInFile("\n", file)


def routesToFile(schedule: Schedule, title, file):
    writeInFile(title, file)
    writeInFile("\n", file)
    writeInFile("\n", file)
    for i, route in enumerate(schedule._routes, 1):
        writeInFile(f'train_{i},"{route._route}"', file)
        writeInFile("\n", file)
    writeInFile("\n", file)
    writeInFile("\n", file)
    writeInFile("\n", file)