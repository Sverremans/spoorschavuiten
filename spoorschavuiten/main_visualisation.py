from code.visualization.visualize import * # makeMap, visualizeMap, drawUsedConnections, outputGraph, makeMapWithNames, onlyLines, drawMapHolland
from code.classes.classes import Region, Schedule
from code.algorithms.random import Random, FixedRandom
from code.algorithms.greedy import FixedGreedy, Greedy
from code.algorithms.hillclimber import HillClimber, HcStopCondition
import geopandas as gpd # type: ignore
import pandas as pd


# -----------------------------------------------------------------------------------------------------------------------------------------------
score_list = []
df_scores = pd.read_csv("data/1000000RandomScores.csv", header = None)
for l in range(len(df_scores)):
        score_list.append(df_scores.loc[l, 2])
outputGraphHist(score_list)

# -----------------------------------------------------------------------------------------------------------------------------------------------
            





# holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
# netherlands = Region("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv")
# schedule = Schedule(holland)
# schedule2 = Schedule(netherlands)
# colors = ["red", "blue", "pink", "grey", "yellow",
#         "hotpink", "orange", "violet", "cyan", "purple",
#         "maroon", "indigo", "teal", "magenta", "crimson", "palevioletred", 
#         "salmon", "deepskyblue", "deeppink", "darkviolet", "goldenrod", "red"]

# make_map_with_names(schedule, "data/holland_2.geojson")
# visualize_map("figures/test2.jpg")

# random = Random(schedule, 120, 7)
# random.run()

# # random = FixedRandom(schedule, 120, 7, 5)
# # random.run()

# # greedy = FixedGreedy(schedule2, 120, 7, 5)
# # greedy.run()

# # random2 = Random(schedule2, 180, 22)
# # random2.run()
# # schedule2.generate_output()

# new_schedule = Schedule(holland)
# greedy_schedule = Greedy(schedule, 120, 7)
# greedy_schedule.run()

# hillClimber = HillClimber(schedule, 120, 7)
# hillClimber.run(1000, 4)
# hillClimber = HcStopCondition(schedule, 120, 7)
# hillClimber.run(10000000, 4)



# # hillClimber.generate_output_to_file()
# # hillClimber.generate_output()
# outputToFile(hillClimber.newSchedule, "Generated output of a hillclimber algorithm, Netherlands, 100000 iterations. 20-06-24", "data/test.csv")
# # print(hillClimber.scores)
# # print(hillClimber.iterations)
# routesToFile(hillClimber.newSchedule, "test", "data/test.csv")

# outputHillClimberGraph(hillClimber.iterations_listPoints, hillClimber.scoresPoints, hillClimber.iterations_list, hillClimber.scores, "Test, x", "data/test.csv")

# makeHillClimberGraph(hillClimber.iterations_listPoints, hillClimber.scoresPoints, hillClimber.iterations_list, hillClimber.scores)



# # draw_figure_with_names(schedule2, colors, "data/netherlands_.geojson", "figures/test.jpg")
# draw_figure_without_names(hillClimber.newSchedule, colors, "data/holland_2.geojson", "figures/test.jpg")
# draw_figure_no_stations(schedule, colors, "data/netherlands_.geojson", "figures/connectionsWithStationNames.jpg")
