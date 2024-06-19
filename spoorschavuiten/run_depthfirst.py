from code.algorithms.depth_first import DepthFirst
from code.classes.classes import Schedule, Region
from code.visualization.visualize import *

holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
new_schedule = Schedule(holland)
max_trains = 4
max_time = 120

depth_first = DepthFirst(new_schedule, max_time, max_trains)
depth_first.run()

routesToFile(depth_first.schedule, "Depht First algorithm output, 19/6/2024", "data/depthfirst_route.csv")
