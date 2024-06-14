from code.visualization.visualize import makeMap, visualizeMap, drawUsedConnections, outputGraph, makeMapWithNames, onlyLines, drawMapHolland
from code.classes.classes import Region, Schedule
from code.algorithms import randomise, randomise2
from code.algorithms.random import Random

# import geopandas as gpd # type: ignore
# from spoorschavuiten.code.algorithms import random

holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
netherlands = Region("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv")
schedule = Schedule(holland)
schedule2 = Schedule(netherlands)
colors = ["red", "blue", "pink", "grey", "yellow",
        "hotpink", "orange", "violet", "cyan", "purple",
        "maroon", "indigo", "teal", "magenta", "crimson", "palevioletred", 
        "salmon", "deepskyblue", "deeppink", "darkviolet", "goldenrod", "red"]

random = Random(schedule, 120, 7)
random.run()

random2 = Random(schedule2, 180, 22)
random2.run()

schedule.generate_output()
schedule2.generate_output()

# makeMapWithNames(schedule)
# drawUsedConnections(schedule, colors)


# visualizeMap(schedule, "figures/connectionsWithStationNames.png")

# makeMap(schedule)
# drawUsedConnections(schedule, colors)
# visualizeMap(schedule, "figures/connectionsInTheNetherlands.png")

# onlyLines(schedule2)
# drawUsedConnections(schedule2, colors)
# visualizeMap(schedule2, "figures/onlyLines.png")