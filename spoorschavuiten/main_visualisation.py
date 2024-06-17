from code.visualization.visualize import * # makeMap, visualizeMap, drawUsedConnections, outputGraph, makeMapWithNames, onlyLines, drawMapHolland
from code.classes.classes import Region, Schedule
from code.algorithms import randomise, randomise2
from code.algorithms.random import Random, FixedRandom
from code.algorithms.greedy import FixedGreedy

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

# random = Random(schedule, 120, 7)
# random.run()

# random = FixedRandom(schedule, 120, 7, 5)
# random.run()

greedy = FixedGreedy(schedule2, 120, 7, 5)
greedy.run()

# random2 = Random(schedule2, 180, 22)
# random2.run()
# schedule2.generate_output()

for i, route in enumerate(schedule2._routes, 1):
        test = str(f'train_{i},"{route._stations}"')
        outputToFile(test)
        outputToFile("\n")
test = str(f"score,{schedule2.calculate_value()}")
outputToFile(test)
outputToFile("\n")


# schedule2.generate_output()

# draw_figure_with_names(schedule2, colors, "data/netherlands_.geojson", "figures/test.jpg")
# draw_figure_without_names(schedule2, colors, "data/netherlands_.geojson", "figures/test.jpg")
# draw_figure_no_stations(schedule, colors, "data/netherlands_.geojson", "figures/connectionsWithStationNames.jpg")

# onlyLines(schedule2)
# drawUsedConnections(schedule2, colors)
# visualizeMap(schedule2, "figures/onlyLines.png")