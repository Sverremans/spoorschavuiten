from code.visualization.visualize import makeMap, visualizeMap, drawUsedConnections, outputGraph
from code.classes.classes import Region
from code.algorithms import randomise, randomise2

holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")

max_trains = 7
makeMap(holland)
xConnections = []
yConnections = []
colors = ["red", "blue", "pink", "black", "yellow", "hotpink", "orange"]

for i in range(max_trains):
    randomise2.random_route_2(holland)
    if holland.is_solution():
        break
    drawUsedConnections(holland, xConnections, yConnections, colors[i])
    # print("-----------------------kleurtje-----------------------")
    # print(colors[i])
    # print("-----------------------kleurtje-----------------------")

visualizeMap(holland)
holland.generate_output()
