from code.visualization.visualize import * # makeMap, visualizeMap, drawUsedConnections, outputGraph, makeMapWithNames, onlyLines, drawMapHolland
from code.classes.classes import Region, Schedule
from code.algorithms.random import Random, FixedRandom
from code.algorithms.greedy import FixedGreedy, Greedy
from code.algorithms.hillclimber import HillClimber

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

# greedy = FixedGreedy(schedule2, 120, 7, 5)
# greedy.run()

# random2 = Random(schedule2, 180, 22)
# random2.run()
# schedule2.generate_output()

# new_schedule = Schedule(holland)
max_trains = 7
max_time = 120
greedy_schedule = Greedy(schedule2, 8, 20)
greedy_schedule.run()

hillClimber = HillClimber(schedule2, holland, 180, 20)
hillClimber.run(100000, 15)

# hillClimber.generate_output_to_file()
# hillClimber.generate_output()
outputToFile(hillClimber._newSchedule, "Generated output of a hillclimber algorithm, 1000 iterations.")

# schedule2.generate_output()

# draw_figure_with_names(schedule2, colors, "data/netherlands_.geojson", "figures/test.jpg")
draw_figure_without_names(hillClimber._newSchedule, colors, "data/netherlands_.geojson", "figures/test.jpg")
# draw_figure_no_stations(schedule, colors, "data/netherlands_.geojson", "figures/connectionsWithStationNames.jpg")
