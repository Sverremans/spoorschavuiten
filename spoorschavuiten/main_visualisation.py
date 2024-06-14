from code.visualization.visualize import makeMap, visualizeMap, drawUsedConnections, outputGraph, makeMapWithNames, onlyLines
from code.classes.classes import Region
from code.algorithms import randomise, randomise2, randomWithConstraints
from code.algorithms.randomWithConstraints import Random

holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")

max_trains = 7
# xConnections = []
# yConnections = []
colors = ["red", "blue", "pink", "black", "yellow",
        "hotpink", "orange", "violet", "cyan", "purple",
        "maroon", "indigo", "teal", "magenta", "crimson", "palevioletred", 
        "salmon", "deepskyblue", "deeppink", "darkviolet", "goldenrod"]

# for i in range(max_trains):
#     randomise2.random_route_2(holland)
#     if holland.is_solution():
#         break

# randomWithConstraints.createRandomSolution(holland, 120, 7)
random = Random(holland, 120, 7)
random.run()

holland.generate_output()
makeMapWithNames(holland)
drawUsedConnections(holland, colors)
visualizeMap(holland, "figures/connectionsWithStationNames.png")

# makeMap(holland)
# drawUsedConnections(holland, colors)
# visualizeMap(holland, "figures/connectionsInTheNetherlands.png")

# onlyLines(holland)
# drawUsedConnections(holland, colors)
# visualizeMap(holland, "figures/onlyLines.png")
# print(len(colors))