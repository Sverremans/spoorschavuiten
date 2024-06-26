from code.visualization.visualize import * # makeMap, visualizeMap, drawUsedConnections, outputGraph, makeMapWithNames, onlyLines, drawMapHolland
from code.classes.classes import Region, Schedule
from code.algorithms.random import Random, FixedRandom
from code.algorithms.greedy import FixedGreedy, Greedy
from code.algorithms.hillclimber import HillClimber, HcStopCondition
import geopandas as gpd # type: ignore
import pandas as pd # type: ignore


# -----------------------------------------------------------------------------------------------------------------------------------------------
# score_list1 = []
# df_scores1 = pd.read_csv("data/output/1000000RandomScoresHolland.csv", header = None)
# for l in range(len(df_scores1)):
#         score_list1.append(df_scores1.loc[l, 2])

# score_list2 = []
# df_scores2 = pd.read_csv("data/output/1000000GreedyScoresHolland.csv", header = None)
# for l in range(len(df_scores2)):
#         score_list2.append(df_scores2.loc[l, 2])

# # score_list3 = []
# # df_scores3 = pd.read_csv("data/output/hillclimberHollandScores_3.csv", header = None)
# # for l in range(len(df_scores3)):
# #         score_list3.append(df_scores3.loc[l, 2])

# outputGraphHistMultiple(score_list1, score_list2)
# # outputGraphHist(score_list3)

# -----------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------
score_list1 = []
df_scores1 = pd.read_csv("data/output/1000000RandomScoresNederland.csv", header = None)
for l in range(len(df_scores1)):
        score_list1.append(df_scores1.loc[l, 2])

score_list2 = []
df_scores2 = pd.read_csv("data/output/1000000GreedyScoresNederland_3.csv", header = None)
for l in range(len(df_scores2)):
        score_list2.append(df_scores2.loc[l, 2])

outputGraphHistMultiple(score_list1, score_list2)

# -----------------------------------------------------------------------------------------------------------------------------------------------
# colors = ["red", "blue", "pink", "grey", "yellow",
#         "hotpink", "orange", "violet", "cyan", "purple",
#         "maroon", "indigo", "teal", "magenta", "crimson", "palevioletred", 
#         "salmon", "deepskyblue", "deeppink", "darkviolet", "goldenrod", "red"]          

# routes= [['Beverwijk naar Castricum', 'Zaandam naar Beverwijk', 'Zaandam naar Hoorn', 'Alkmaar naar Hoorn'], 
#           ['Amsterdam Amstel naar Amsterdam Zuid', 'Amsterdam Amstel naar Amsterdam Centraal', 'Amsterdam Centraal naar Amsterdam Sloterdijk', 'Amsterdam Sloterdijk naar Zaandam', 'Zaandam naar Castricum', 'Castricum naar Alkmaar', 'Alkmaar naar Den Helder'], 
#           ['Heemstede-Aerdenhout naar Haarlem', 'Leiden Centraal naar Heemstede-Aerdenhout', 'Den Haag Centraal naar Leiden Centraal', 'Delft naar Den Haag Centraal', 'Schiedam Centrum naar Delft', 'Rotterdam Centraal naar Schiedam Centrum', 'Dordrecht naar Rotterdam Centraal', 'Dordrecht naar Rotterdam Centraal', 'Rotterdam Centraal naar Rotterdam Alexander', 'Rotterdam Alexander naar Gouda'], 
#           ['Den Haag Centraal naar Gouda', 'Gouda naar Alphen a/d Rijn', 'Leiden Centraal naar Alphen a/d Rijn', 'Leiden Centraal naar Schiphol Airport', 'Amsterdam Zuid naar Schiphol Airport', 'Amsterdam Zuid naar Amsterdam Sloterdijk', 'Amsterdam Sloterdijk naar Haarlem', 'Haarlem naar Beverwijk']]

# routes2 =[['Amsterdam Amstel naar Amsterdam Zuid', 'Amsterdam Amstel naar Hilversum', 'Hilversum naar Almere Centrum', 'Almere Centrum naar Lelystad Centrum', 'Almere Centrum naar Lelystad Centrum', 'Amsterdam Centraal naar Almere Centrum', 'Amsterdam Centraal naar Amsterdam Sloterdijk'], 
#          ['Helmond naar Venlo', 'Eindhoven naar Helmond', 'Eindhoven naar s-Hertogenbosch', 'Utrecht Centraal naar s-Hertogenbosch', 'Utrecht Centraal naar Alphen a/d Rijn'], 
#          ['Amsterdam Amstel naar Almere Centrum', 'Utrecht Centraal naar Amsterdam Amstel', 'Utrecht Centraal naar Hilversum', 'Utrecht Centraal naar Hilversum', 'Utrecht Centraal naar Amersfoort', 'Apeldoorn naar Amersfoort'],
#          ['Alkmaar naar Hoorn', 'Castricum naar Alkmaar', 'Beverwijk naar Castricum', 'Zaandam naar Beverwijk', 'Zaandam naar Castricum', 'Beverwijk naar Castricum', 'Beverwijk naar Castricum'],
#          ['Breda naar Dordrecht', 'Dordrecht naar Rotterdam Centraal', 'Rotterdam Centraal naar Schiedam Centrum', 'Schiedam Centrum naar Delft', 'Delft naar Den Haag HS', 'Den Haag HS naar Gouda', 'Rotterdam Alexander naar Gouda', 'Rotterdam Blaak naar Rotterdam Alexander', 'Rotterdam Blaak naar Rotterdam Alexander', 'Rotterdam Blaak naar Rotterdam Alexander'], 
#          ['Oss naar Nijmegen', 'Nijmegen naar Arnhem Centraal', 'Arnhem Centraal naar Dieren', 'Zutphen naar Dieren', 'Deventer naar Zutphen', 'Deventer naar Apeldoorn', 'Apeldoorn naar Zutphen', 'Apeldoorn naar Zutphen'], 
#          ['Hilversum naar Almere Centrum', 'Utrecht Centraal naar Hilversum', 'Utrecht Centraal naar Gouda', 'Den Haag Centraal naar Gouda', 'Den Haag Centraal naar Leiden Centraal', 'Den Haag HS naar Leiden Centraal'], 
#          ['Amsterdam Sloterdijk naar Haarlem', 'Heemstede-Aerdenhout naar Haarlem', 'Leiden Centraal naar Heemstede-Aerdenhout', 'Leiden Centraal naar Alphen a/d Rijn', 'Gouda naar Alphen a/d Rijn', 'Den Haag Laan v NOI naar Gouda', 'Den Haag Laan v NOI naar Gouda'], 
#          ['Den Haag HS naar Leiden Centraal', 'Leiden Centraal naar Schiphol Airport', 'Utrecht Centraal naar Schiphol Airport', 'Utrecht Centraal naar Ede-Wageningen', 'Arnhem Centraal naar Ede-Wageningen', 'Arnhem Centraal naar Dieren', 'Arnhem Centraal naar Dieren'], 
#          ['Groningen naar Assen', 'Leeuwarden naar Groningen', 'Leeuwarden naar Heerenveen', 'Heerenveen naar Steenwijk', 'Steenwijk naar Zwolle'], 
#          ['Delft naar Den Haag Centraal', 'Delft naar Den Haag Laan v NOI', 'Den Haag Laan v NOI naar Leiden Centraal', 'Leiden Centraal naar Alphen a/d Rijn', 'Utrecht Centraal naar Alphen a/d Rijn', 'Utrecht Centraal naar Amsterdam Centraal', 'Amsterdam Amstel naar Amsterdam Centraal'], 
#          ['Assen naar Zwolle', 'Zwolle naar Deventer', 'Deventer naar Almelo', 'Almelo naar Hengelo', 'Hengelo naar Enschede', 'Hengelo naar Enschede'],
#          ['Eindhoven naar Tilburg', 'Weert naar Eindhoven', 'Roermond naar Weert', 'Sittard naar Roermond', 'Maastricht naar Sittard', 'Maastricht naar Sittard', 'Sittard naar Heerlen'], 
#          ['Zwolle naar Almelo', 'Zwolle naar Amersfoort', 'Utrecht Centraal naar Amersfoort'],
#          ['Heemstede-Aerdenhout naar Haarlem', 'Haarlem naar Beverwijk'],
#          ['Roosendaal naar Vlissingen', 'Etten-Leur naar Roosendaal', 'Breda naar Etten-Leur', 'Tilburg naar Breda', 's-Hertogenbosch naar Tilburg', 's-Hertogenbosch naar Oss'],
#          ['Schiedam Centrum naar Delft', 'Rotterdam Blaak naar Schiedam Centrum', 'Dordrecht naar Rotterdam Blaak', 'Roosendaal naar Dordrecht', 'Roosendaal naar Dordrecht', 'Dordrecht naar Rotterdam Centraal', 'Rotterdam Centraal naar Rotterdam Alexander', 'Rotterdam Centraal naar Rotterdam Alexander'],
#          ['Amsterdam Zuid naar Schiphol Airport', 'Amsterdam Zuid naar Amsterdam Sloterdijk', 'Amsterdam Sloterdijk naar Zaandam', 'Zaandam naar Hoorn', 'Alkmaar naar Hoorn', 'Alkmaar naar Den Helder']]


# holland = Region("data/input/StationsHolland.csv", "data/input/ConnectiesHolland.csv")
# netherlands = Region("data/input/StationsNationaal.csv", "data/input/ConnectiesNationaal.csv")
# new_routes = convert_string_to_used_connections(routes, holland)
# new_routes2 = convert_string_to_used_connections(routes2, netherlands)
# draw_finished_map(holland, colors, "data/holland_2.geojson", "figures/hollandIngevuldDoorHillclimberAlgoritme_9202.jpg", new_routes)
# draw_finished_map(netherlands, colors, "data/netherlands_.geojson", "figures/nederlandIngevuldDoorHillclimberAlgoritme_6289.jpg", new_routes2)
# -----------------------------------------------------------------------------------------------------------------------------------------------

# # Boxplot maker voor Holland

# score_list1 = []
# df_scores1 = pd.read_csv("data/output/1000000RandomScoresHolland.csv", header = None)
# for l in range(len(df_scores1)):
#         score_list1.append(df_scores1.loc[l, 2])

# score_list2 = []
# df_scores2 = pd.read_csv("data/output/1000000GreedyScoresHolland.csv", header = None)
# for l in range(len(df_scores2)):
#         score_list2.append(df_scores2.loc[l, 2])

# score_list3 = []
# df_scores3 = pd.read_csv("data/output/hillclimberHollandScores_3.csv", header = None)
# for l in range(len(df_scores3)):
#         score_list3.append(df_scores3.loc[l, 2])




# data_1 = score_list1 
# data_2 = score_list2
# data_4 = score_list3
# data_3 = []
# data = [data_1, data_2, data_3, data_4]
# data_extra = [data_3, data_4]


# # Volledige data
# fig = plt.figure(figsize =(10, 7))
# plt.boxplot(data, vert = False, flierprops={'marker': 'o', 'markersize': 5, 'markeredgecolor': 'grey'})
# plt.scatter(9104, 3, color = 'black', marker = '*')
# plt.yticks([1, 2, 3, 4], ['Random', 'Greedy', 'Depth-First', 'Hillclimber'])
# plt.title("Holland")
# plt.xlabel("Score")
# plt.savefig("figures/Boxplot_Holland")
# plt.show()

# #Ingezoemde data
# fig = plt.figure(figsize =(10, 7))
# plt.boxplot(data_extra, vert = False, flierprops={'marker': 'o', 'markersize': 5, 'markeredgecolor': 'grey'})
# plt.scatter(9104, 1, color = 'black', marker = '*')
# plt.yticks([1, 2], ['Depth-First', 'Hillclimber'])
# plt.title("Holland (ingezoemd)")
# plt.xlabel("Score")
# plt.savefig("figures/Boxplot_Holland_CloseUp")
# plt.show()
# -----------------------------------------------------------------------------------------------------------------------------------------------

# #Boxplot maker voor Holland

# score_list1 = []
# df_scores1 = pd.read_csv("data/output/1000000RandomScoresNederland.csv", header = None)
# for l in range(len(df_scores1)):
#         score_list1.append(df_scores1.loc[l, 2])

# score_list2 = []
# df_scores2 = pd.read_csv("data/output/1000000GreedyScoresNederland_3.csv", header = None)
# for l in range(len(df_scores2)):
#         score_list2.append(df_scores2.loc[l, 2])

# score_list3 = []
# df_scores3 = pd.read_csv("data/output/hillclimberNederlandScores.csv", header = None)
# for l in range(len(df_scores3)):
#         score_list3.append(df_scores3.loc[l, 2])




# data_1 = score_list1 
# data_2 = score_list2
# data_3 = score_list3
# data = [data_1, data_2, data_3]
# data_extra = [data_3]


# # Volledige data
# fig = plt.figure(figsize =(10, 7))
# plt.boxplot(data, vert = False, flierprops={'marker': 'o', 'markersize': 5, 'markeredgecolor': 'grey'})
# plt.yticks([1, 2, 3], ['Random', 'Greedy', 'Hillclimber'])
# plt.title("Nederland")
# plt.xlabel("Score")
# plt.savefig("figures/Boxplot_Nederland")
# plt.show()

# #Ingezoemde data
# fig = plt.figure(figsize =(10, 7))
# plt.boxplot(data_3, vert = False, flierprops={'marker': 'o', 'markersize': 5, 'markeredgecolor': 'grey'})
# plt.yticks([1], ['Hillclimber'])
# plt.title("Nederland (ingezoemd)")
# plt.xlabel("Score")
# plt.savefig("figures/Boxplot_Nederland_CloseUp")
# plt.show()
# -----------------------------------------------------------------------------------------------------------------------------------------------
colors = ['red', 'blue']
routes = []

holland = Region("data/input/StationsHolland.csv", "data/input/ConnectiesHolland.csv")
new_routes = convert_string_to_used_connections(routes, holland)
draw_finished_map(holland, colors, "data/holland_2.geojson", "figures/hollandIngevuldDoorHillclimberAlgoritme_9202.jpg", new_routes)