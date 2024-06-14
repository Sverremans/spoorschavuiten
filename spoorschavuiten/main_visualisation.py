from code.visualization.visualize import makeMap, visualizeMap, drawUsedConnections, outputGraph, makeMapWithNames, onlyLines
from code.classes.classes import Region, Schedule
from code.algorithms import randomise, randomise2, randomWithConstraints
from code.algorithms.randomWithConstraints import Random

holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
schedule = Schedule(holland)
max_trains = 7
colors = ["red", "blue", "pink", "black", "yellow",
        "hotpink", "orange", "violet", "cyan", "purple",
        "maroon", "indigo", "teal", "magenta", "crimson", "palevioletred", 
        "salmon", "deepskyblue", "deeppink", "darkviolet", "goldenrod"]

random = Random(schedule, 120, 7)
random.run()

schedule.generate_output()
makeMapWithNames(schedule)
drawUsedConnections(schedule, colors)
visualizeMap(schedule, "figures/connectionsWithStationNames.png")

makeMap(schedule)
drawUsedConnections(schedule, colors)
visualizeMap(schedule, "figures/connectionsInTheNetherlands.png")

onlyLines(schedule)
drawUsedConnections(schedule, colors)
visualizeMap(schedule, "figures/onlyLines.png")
print(len(colors))