from code.visualization.visualize import * # makeMap, visualizeMap, drawUsedConnections, outputGraph, makeMapWithNames, onlyLines, drawMapHolland
from code.classes.classes import Region, Schedule
from code.algorithms.random import Random, FixedRandom
from code.algorithms.greedy import FixedGreedy, Greedy
from code.algorithms.hillclimber import HillClimber, HcStopCondition
import geopandas as gpd # type: ignore
import pandas as pd


# -----------------------------------------------------------------------------------------------------------------------------------------------
score_list1 = []
df_scores1 = pd.read_csv("data/1000000RandomScoresHolland_2.csv", header = None)
for l in range(len(df_scores1)):
        score_list1.append(df_scores1.loc[l, 2])
print(len(score_list1))
score_list2 = []
df_scores2 = pd.read_csv("data/1000000GreedyScoresHolland_2.csv", header = None)
for l in range(len(df_scores2)):
        score_list2.append(df_scores2.loc[l, 2])
print(len(score_list2))
score_list3 = []
df_scores3 = pd.read_csv("data/hillclimberHollandScores_3.csv", header = None)
for l in range(len(df_scores3)):
        score_list3.append(df_scores3.loc[l, 2])
print(len(score_list3))
outputGraphHistMultiple(score_list1, score_list2, score_list3)
# outputGraphHist(score_list3)

# -----------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------
# score_list1 = []
# df_scores1 = pd.read_csv("data/1000000RandomScoresNederland.csv", header = None)
# for l in range(len(df_scores1)):
#         score_list1.append(df_scores1.loc[l, 2])

# score_list2 = []
# df_scores2 = pd.read_csv("data/1000000GreedyScoresNederland.csv", header = None)
# for l in range(len(df_scores2)):
#         score_list2.append(df_scores2.loc[l, 2])

# outputGraphHistMultiple(score_list1, score_list2)

# -----------------------------------------------------------------------------------------------------------------------------------------------
# colors = ["red", "blue", "pink", "grey", "yellow",
#         "hotpink", "orange", "violet", "cyan", "purple",
#         "maroon", "indigo", "teal", "magenta", "crimson", "palevioletred", 
#         "salmon", "deepskyblue", "deeppink", "darkviolet", "goldenrod", "red"]          

# routes= [['Beverwijk naar Castricum', 'Zaandam naar Beverwijk', 'Zaandam naar Hoorn', 'Alkmaar naar Hoorn'], 
#           ['Amsterdam Amstel naar Amsterdam Zuid', 'Amsterdam Amstel naar Amsterdam Centraal', 'Amsterdam Centraal naar Amsterdam Sloterdijk', 'Amsterdam Sloterdijk naar Zaandam', 'Zaandam naar Castricum', 'Castricum naar Alkmaar', 'Alkmaar naar Den Helder'], 
#           ['Heemstede-Aerdenhout naar Haarlem', 'Leiden Centraal naar Heemstede-Aerdenhout', 'Den Haag Centraal naar Leiden Centraal', 'Delft naar Den Haag Centraal', 'Schiedam Centrum naar Delft', 'Rotterdam Centraal naar Schiedam Centrum', 'Dordrecht naar Rotterdam Centraal', 'Dordrecht naar Rotterdam Centraal', 'Rotterdam Centraal naar Rotterdam Alexander', 'Rotterdam Alexander naar Gouda'], 
#           ['Den Haag Centraal naar Gouda', 'Gouda naar Alphen a/d Rijn', 'Leiden Centraal naar Alphen a/d Rijn', 'Leiden Centraal naar Schiphol Airport', 'Amsterdam Zuid naar Schiphol Airport', 'Amsterdam Zuid naar Amsterdam Sloterdijk', 'Amsterdam Sloterdijk naar Haarlem', 'Haarlem naar Beverwijk']]

# holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
# # netherlands = Region("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv")

# new_routes = convert_string_to_used_connections(routes, holland)
# draw_figure_without_names(holland, colors, "data/holland_2.geojson", "figures/test.jpg", new_routes)
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
