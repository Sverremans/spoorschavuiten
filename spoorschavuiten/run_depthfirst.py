from code.algorithms.depth_first import DepthFirst
from code.classes.classes import Schedule, Region
from code.visualization.visualize import *

# Parameters
holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
netherlands = Region("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv") 
new_schedule = Schedule(netherlands)
max_trains = 20
max_time = 180

depth_first = DepthFirst(new_schedule, max_time, max_trains)
depth_first.run()

outputToFile(depth_first.schedule, "Depht First algorithm output, 19/6/2024", "data/output/depthfirst/depthfirst_ouput.csv")
routesToFile(depth_first.schedule, "Depht First algorithm output, 19/6/2024", "data/output/depthfirst/depthfirst_route.csv")
