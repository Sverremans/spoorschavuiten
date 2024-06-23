from code.algorithms.depth_first import DepthFirst
from code.algorithms.greedy_lookahead import GreedyLookahead
from code.classes.classes import Schedule, Region
from code.visualization.visualize import *

# holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
netherlands = Region("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv") 
# new_schedule = Schedule(holland)
new_schedule = Schedule(netherlands)
max_trains = 20
max_time = 180

greedy_lookahead = GreedyLookahead(new_schedule, max_time, max_trains, 3)
greedy_lookahead.run()

outputToFile(greedy_lookahead.schedule, "Greedy Lookahead algorithm output, 23/6/2024", "data/greedylookahead_Nederland_ouput.csv")
routesToFile(greedy_lookahead.schedule, "Greedy Lookahead algorithm output, 23/6/2024", "data/greedylookahead_Nederland_route.csv")


# depth_first = DepthFirst(new_schedule, max_time, max_trains)
# depth_first.run()


# outputToFile(depth_first.schedule, "Depht First algorithm output, 19/6/2024", "data/depthfirst_ouput.csv")
# routesToFile(depth_first.schedule, "Depht First algorithm output, 19/6/2024", "data/depthfirst_route.csv")

#TODO
# S = 10000 - (500 + 396) = 9104 score voor depth_first run door Massimo