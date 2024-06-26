from code.visualization.visualize import * # makeMap, visualizeMap, drawUsedConnections, outputGraph, makeMapWithNames, onlyLines, drawMapHolland
from code.classes.classes import Region, Schedule
from code.algorithms.random import Random, FixedRandom
from code.algorithms.greedy import FixedGreedy, Greedy
from code.algorithms.hillclimber import HillClimber, HcStopCondition
import geopandas as gpd # type: ignore
import pandas as pd # type: ignore


# -----------------------------------------------------------------------------------------------------------------------------------------------
                        # Maakt een histogram met alle Random en Greedy scores van Holland.
# -----------------------------------------------------------------------------------------------------------------------------------------------

score_list1 = []
df_scores1 = pd.read_csv("data/output/random/1000000RandomScoresHolland.csv", header = None)
for l in range(len(df_scores1)):
        score_list1.append(df_scores1.loc[l, 2])

score_list2 = []
df_scores2 = pd.read_csv("data/output/greedy/1000000GreedyScoresHolland.csv", header = None)
for l in range(len(df_scores2)):
        score_list2.append(df_scores2.loc[l, 2])

outputGraphHistMultiple(score_list1, score_list2, 'figures/randomScoresVSGreedyScoresHolland.jpg', "Holland")
# -----------------------------------------------------------------------------------------------------------------------------------------------
                        # Maakt een histogram met alle Random en Greedy scores van Nederland.
# -----------------------------------------------------------------------------------------------------------------------------------------------
score_list1 = []
df_scores1 = pd.read_csv("data/output/random/1000000RandomScoresNederland.csv", header = None)
for l in range(len(df_scores1)):
        score_list1.append(df_scores1.loc[l, 2])

score_list2 = []
df_scores2 = pd.read_csv("data/output/greedy/1000000GreedyScoresNederland.csv", header = None)
for l in range(len(df_scores2)):
        score_list2.append(df_scores2.loc[l, 2])

outputGraphHistMultiple(score_list1, score_list2, 'figures/randomScoresVSGreedyScoresNederland.jpg', "Nederland")

# -----------------------------------------------------------------------------------------------------------------------------------------------
                        # Teken een kaart van de gereden routes gemaakt door het Hill Climber algoritme
                        # routes tekent Holland
                        # routes2 tekent Nederland
# -----------------------------------------------------------------------------------------------------------------------------------------------
colors = ["red", "blue", "pink", "grey", "yellow",
        "hotpink", "orange", "violet", "cyan", "purple",
        "maroon", "indigo", "teal", "magenta", "crimson", "palevioletred", 
        "salmon", "deepskyblue", "deeppink", "darkviolet", "goldenrod", "red"]  
        
                # Holland
routes= [['Beverwijk naar Castricum', 'Zaandam naar Beverwijk', 'Zaandam naar Hoorn', 'Alkmaar naar Hoorn'], 
          ['Amsterdam Amstel naar Amsterdam Zuid', 'Amsterdam Amstel naar Amsterdam Centraal', 'Amsterdam Centraal naar Amsterdam Sloterdijk', 'Amsterdam Sloterdijk naar Zaandam', 'Zaandam naar Castricum', 'Castricum naar Alkmaar', 'Alkmaar naar Den Helder'], 
          ['Heemstede-Aerdenhout naar Haarlem', 'Leiden Centraal naar Heemstede-Aerdenhout', 'Den Haag Centraal naar Leiden Centraal', 'Delft naar Den Haag Centraal', 'Schiedam Centrum naar Delft', 'Rotterdam Centraal naar Schiedam Centrum', 'Dordrecht naar Rotterdam Centraal', 'Dordrecht naar Rotterdam Centraal', 'Rotterdam Centraal naar Rotterdam Alexander', 'Rotterdam Alexander naar Gouda'], 
          ['Den Haag Centraal naar Gouda', 'Gouda naar Alphen a/d Rijn', 'Leiden Centraal naar Alphen a/d Rijn', 'Leiden Centraal naar Schiphol Airport', 'Amsterdam Zuid naar Schiphol Airport', 'Amsterdam Zuid naar Amsterdam Sloterdijk', 'Amsterdam Sloterdijk naar Haarlem', 'Haarlem naar Beverwijk']]

holland = Region("data/input/StationsHolland.csv", "data/input/ConnectiesHolland.csv")
new_routes = convert_string_to_used_connections(routes, holland)
draw_finished_map(holland, colors, "data/holland_2.geojson", "figures/hollandIngevuldDoorHillclimberAlgoritme_9202.jpg", new_routes)

                # Nederland
routes2 =[['Amsterdam Amstel naar Amsterdam Zuid', 'Amsterdam Amstel naar Hilversum', 'Hilversum naar Almere Centrum', 'Almere Centrum naar Lelystad Centrum', 'Almere Centrum naar Lelystad Centrum', 'Amsterdam Centraal naar Almere Centrum', 'Amsterdam Centraal naar Amsterdam Sloterdijk'], 
         ['Helmond naar Venlo', 'Eindhoven naar Helmond', 'Eindhoven naar s-Hertogenbosch', 'Utrecht Centraal naar s-Hertogenbosch', 'Utrecht Centraal naar Alphen a/d Rijn'], 
         ['Amsterdam Amstel naar Almere Centrum', 'Utrecht Centraal naar Amsterdam Amstel', 'Utrecht Centraal naar Hilversum', 'Utrecht Centraal naar Hilversum', 'Utrecht Centraal naar Amersfoort', 'Apeldoorn naar Amersfoort'],
         ['Alkmaar naar Hoorn', 'Castricum naar Alkmaar', 'Beverwijk naar Castricum', 'Zaandam naar Beverwijk', 'Zaandam naar Castricum', 'Beverwijk naar Castricum', 'Beverwijk naar Castricum'],
         ['Breda naar Dordrecht', 'Dordrecht naar Rotterdam Centraal', 'Rotterdam Centraal naar Schiedam Centrum', 'Schiedam Centrum naar Delft', 'Delft naar Den Haag HS', 'Den Haag HS naar Gouda', 'Rotterdam Alexander naar Gouda', 'Rotterdam Blaak naar Rotterdam Alexander', 'Rotterdam Blaak naar Rotterdam Alexander', 'Rotterdam Blaak naar Rotterdam Alexander'], 
         ['Oss naar Nijmegen', 'Nijmegen naar Arnhem Centraal', 'Arnhem Centraal naar Dieren', 'Zutphen naar Dieren', 'Deventer naar Zutphen', 'Deventer naar Apeldoorn', 'Apeldoorn naar Zutphen', 'Apeldoorn naar Zutphen'], 
         ['Hilversum naar Almere Centrum', 'Utrecht Centraal naar Hilversum', 'Utrecht Centraal naar Gouda', 'Den Haag Centraal naar Gouda', 'Den Haag Centraal naar Leiden Centraal', 'Den Haag HS naar Leiden Centraal'], 
         ['Amsterdam Sloterdijk naar Haarlem', 'Heemstede-Aerdenhout naar Haarlem', 'Leiden Centraal naar Heemstede-Aerdenhout', 'Leiden Centraal naar Alphen a/d Rijn', 'Gouda naar Alphen a/d Rijn', 'Den Haag Laan v NOI naar Gouda', 'Den Haag Laan v NOI naar Gouda'], 
         ['Den Haag HS naar Leiden Centraal', 'Leiden Centraal naar Schiphol Airport', 'Utrecht Centraal naar Schiphol Airport', 'Utrecht Centraal naar Ede-Wageningen', 'Arnhem Centraal naar Ede-Wageningen', 'Arnhem Centraal naar Dieren', 'Arnhem Centraal naar Dieren'], 
         ['Groningen naar Assen', 'Leeuwarden naar Groningen', 'Leeuwarden naar Heerenveen', 'Heerenveen naar Steenwijk', 'Steenwijk naar Zwolle'], 
         ['Delft naar Den Haag Centraal', 'Delft naar Den Haag Laan v NOI', 'Den Haag Laan v NOI naar Leiden Centraal', 'Leiden Centraal naar Alphen a/d Rijn', 'Utrecht Centraal naar Alphen a/d Rijn', 'Utrecht Centraal naar Amsterdam Centraal', 'Amsterdam Amstel naar Amsterdam Centraal'], 
         ['Assen naar Zwolle', 'Zwolle naar Deventer', 'Deventer naar Almelo', 'Almelo naar Hengelo', 'Hengelo naar Enschede', 'Hengelo naar Enschede'],
         ['Eindhoven naar Tilburg', 'Weert naar Eindhoven', 'Roermond naar Weert', 'Sittard naar Roermond', 'Maastricht naar Sittard', 'Maastricht naar Sittard', 'Sittard naar Heerlen'], 
         ['Zwolle naar Almelo', 'Zwolle naar Amersfoort', 'Utrecht Centraal naar Amersfoort'],
         ['Heemstede-Aerdenhout naar Haarlem', 'Haarlem naar Beverwijk'],
         ['Roosendaal naar Vlissingen', 'Etten-Leur naar Roosendaal', 'Breda naar Etten-Leur', 'Tilburg naar Breda', 's-Hertogenbosch naar Tilburg', 's-Hertogenbosch naar Oss'],
         ['Schiedam Centrum naar Delft', 'Rotterdam Blaak naar Schiedam Centrum', 'Dordrecht naar Rotterdam Blaak', 'Roosendaal naar Dordrecht', 'Roosendaal naar Dordrecht', 'Dordrecht naar Rotterdam Centraal', 'Rotterdam Centraal naar Rotterdam Alexander', 'Rotterdam Centraal naar Rotterdam Alexander'],
         ['Amsterdam Zuid naar Schiphol Airport', 'Amsterdam Zuid naar Amsterdam Sloterdijk', 'Amsterdam Sloterdijk naar Zaandam', 'Zaandam naar Hoorn', 'Alkmaar naar Hoorn', 'Alkmaar naar Den Helder']]

netherlands = Region("data/input/StationsNationaal.csv", "data/input/ConnectiesNationaal.csv")
new_routes2 = convert_string_to_used_connections(routes2, netherlands)
draw_finished_map(netherlands, colors, "data/netherlands_.geojson", "figures/nederlandIngevuldDoorHillclimberAlgoritme_6289.jpg", new_routes2)
# -----------------------------------------------------------------------------------------------------------------------------------------------
                        # Boxplot maker voor Holland
# -----------------------------------------------------------------------------------------------------------------------------------------------
score_list1_Holland = []
df_scores1_Holland = pd.read_csv("data/output/random/1000000RandomScoresHolland.csv", header = None)
for l in range(len(df_scores1_Holland)):
        score_list1_Holland.append(df_scores1_Holland.loc[l, 2])

score_list2_Holland = []
df_scores2_Holland = pd.read_csv("data/output/greedy/1000000GreedyScoresHolland.csv", header = None)
for l in range(len(df_scores2_Holland)):
        score_list2_Holland.append(df_scores2_Holland.loc[l, 2])

score_list3_Holland = []
df_scores3_Holland = pd.read_csv("data/output/hillclimber/run_3/hillclimberHollandScores_3.csv", header = None)
for l in range(len(df_scores3_Holland)):
        score_list3_Holland.append(df_scores3_Holland.loc[l, 2])

data_1 = score_list1_Holland 
data_2 = score_list2_Holland
data_4 = score_list3_Holland
data_3 = []
data = [data_1, data_2, data_3, data_4]
data_extra = [data_3, data_4]

                # Volledige data
fig = plt.figure(figsize =(10, 7))
plt.boxplot(data, vert = False, flierprops={'marker': 'o', 'markersize': 5, 'markeredgecolor': 'grey'})
plt.scatter(9104, 3, color = 'black', marker = '*')
plt.yticks([1, 2, 3, 4], ['Random', 'Greedy', 'Depth-First', 'Hillclimber'], fontsize=15)
plt.xticks(fontsize=15)
plt.title("Holland", fontsize=20)
plt.xlabel("Score", fontsize=16)
plt.savefig("figures/Boxplot_Holland")
plt.show()

                #Ingezoemde data
fig = plt.figure(figsize =(10, 7))
plt.boxplot(data_extra, vert = False, flierprops={'marker': 'o', 'markersize': 5, 'markeredgecolor': 'grey'})
plt.scatter(9104, 1, color = 'black', marker = '*')
plt.yticks([1, 2], ['Depth-First', 'Hillclimber'], fontsize=15)
plt.xticks(fontsize=15)
plt.title("Holland (ingezoemd)", fontsize=20)
plt.xlabel("Score", fontsize=16)
plt.savefig("figures/Boxplot_Holland_CloseUp")
plt.show()
# -----------------------------------------------------------------------------------------------------------------------------------------------
                        # Boxplot maker voor Holland
# -----------------------------------------------------------------------------------------------------------------------------------------------
score_list1_Nederland = []
df_scores1_Nederland = pd.read_csv("data/output/random/1000000RandomScoresNederland.csv", header = None)
for l in range(len(df_scores1_Nederland)):
        score_list1_Nederland.append(df_scores1_Nederland.loc[l, 2])

score_list2_Nederland = []
df_scores2_Nederland = pd.read_csv("data/output/greedy/1000000GreedyScoresNederland.csv", header = None)
for l in range(len(df_scores2_Nederland)):
        score_list2_Nederland.append(df_scores2_Nederland.loc[l, 2])

score_list3_Nederland = []
df_scores3_Nederland = pd.read_csv("data/output/hillclimber/run_1/hillclimberNederlandScores.csv", header = None)
for l in range(len(df_scores3_Nederland)):
        score_list3_Nederland.append(df_scores3_Nederland.loc[l, 2])

data_1 = score_list1_Nederland 
data_2 = score_list2_Nederland
data_3 = score_list3_Nederland
data = [data_1, data_2, data_3]

                # Volledige data
fig = plt.figure(figsize =(10, 7))
plt.boxplot(data, vert = False, flierprops={'marker': 'o', 'markersize': 5, 'markeredgecolor': 'grey'})
plt.yticks([1, 2, 3], ['Random', 'Greedy', 'Hillclimber'], fontsize=15)
plt.xticks(fontsize=15)
plt.title("Nederland", fontsize=20)
plt.xlabel("Score", fontsize=16)
plt.savefig("figures/Boxplot_Nederland")
plt.show()

                #Ingezoemde data
fig = plt.figure(figsize =(10, 7))
plt.boxplot(data_3, vert = False, flierprops={'marker': 'o', 'markersize': 5, 'markeredgecolor': 'grey'})
plt.yticks([1], ['Hillclimber'], fontsize=15)
plt.xticks(fontsize=15)
plt.title("Nederland (ingezoemd)", fontsize=20)
plt.xlabel("Score", fontsize=16)
plt.savefig("figures/Boxplot_Nederland_CloseUp")
plt.show()
# -----------------------------------------------------------------------------------------------------------------------------------------------
                        # Hill Climber grafiek maken - Holland
# -----------------------------------------------------------------------------------------------------------------------------------------------
x_Holland  = [0, 1, 2, 18, 23, 27, 29, 38, 59, 111, 132, 172, 289, 474, 916, 2909, 3364, 5991, 6540, 9020, 9285, 18437, 20946, 21917, 42716]
y_Holland  = [7807.714285714286, 8516.0, 8527.0, 8712.0, 8720.0, 8923.0, 8927.0, 8933.0, 8935.0, 8940.0, 8952.0, 8961.0, 8974.0, 8979.0, 9135.0, 9145.0, 9153.0, 9154.0, 9158.0, 9159.0, 9163.0, 9163.0, 9190.0, 9202.0, 9202.0]
xpoints_Holland = [0, 1, 1, 2, 2, 18, 18, 23, 23, 27, 27, 29, 29, 38, 38, 59, 59, 111, 111, 132, 132, 172, 172, 289, 289, 474, 474, 916, 916, 2909, 2909, 3364, 3364, 5991, 5991, 6540, 6540, 9020, 9020, 9285, 9285, 18437, 18437, 20946, 20946, 21917, 21917, 42716, 42716]
ypoints_Holland  = [7807.714285714286, 7807.714285714286, 8516.0, 8516.0, 8527.0, 8527.0, 8712.0, 8712.0, 8720.0, 8720.0, 8923.0, 8923.0, 8927.0, 8927.0, 8933.0, 8933.0, 8935.0, 8935.0, 8940.0, 8940.0, 8952.0, 8952.0, 8961.0, 8961.0, 8974.0, 8974.0, 8979.0, 8979.0, 9135.0, 9135.0, 9145.0, 9145.0, 9153.0, 9153.0, 9154.0, 9154.0, 9158.0, 9158.0, 9159.0, 9159.0, 9163.0, 9163.0, 9163.0, 9163.0, 9190.0, 9190.0, 9202.0, 9202.0, 9202.0]
makeHillClimberGraph(x_Holland , y_Holland , xpoints_Holland , ypoints_Holland )
# -----------------------------------------------------------------------------------------------------------------------------------------------
                        # Hill Climber grafiek maken - Nederland
# -----------------------------------------------------------------------------------------------------------------------------------------------
x_Nederland  = [0, 1, 4, 8, 14, 30, 58, 94, 243, 532, 1279, 1436, 2242, 2253, 2437, 3712, 22233, 22312]
y_Nederland = [4074.044943820225, 4939.483146067416, 4952.483146067416, 5053.483146067416, 5234.202247191011, 5238.202247191011, 5322.561797752809, 5359.561797752809, 5393.561797752809, 5394.561797752809, 5485.921348314607, 5514.921348314607, 5549.2808988764045, 5632.2808988764045, 5715.640449438202, 5720.640449438202, 6193.0, 6193.0]
xpoints_Nederland = [0, 1, 1, 4, 4, 8, 8, 14, 14, 30, 30, 58, 58, 94, 94, 243, 243, 532, 532, 1279, 1279, 1436, 1436, 2242, 2242, 2253, 2253, 2437, 2437, 3712, 3712, 22233, 22233, 22312, 22312]
ypoints_Nederland = [4074.044943820225, 4074.044943820225, 4939.483146067416, 4939.483146067416, 4952.483146067416, 4952.483146067416, 5053.483146067416, 5053.483146067416, 5234.202247191011, 5234.202247191011, 5238.202247191011, 5238.202247191011, 5322.561797752809, 5322.561797752809, 5359.561797752809, 5359.561797752809, 5393.561797752809, 5393.561797752809, 5394.561797752809, 5394.561797752809, 5485.921348314607, 5485.921348314607, 5514.921348314607, 5514.921348314607, 5549.2808988764045, 5549.2808988764045, 5632.2808988764045, 5632.2808988764045, 5715.640449438202, 5715.640449438202, 5720.640449438202, 5720.640449438202, 6193.0, 6193.0, 6193.0]

makeHillClimberGraph(x_Nederland, y_Nederland, xpoints_Nederland, ypoints_Nederland)
# -----------------------------------------------------------------------------------------------------------------------------------------------