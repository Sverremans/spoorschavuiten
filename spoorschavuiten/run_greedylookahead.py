from code.algorithms.greedy_lookahead import GreedyLookahead
from code.classes.classes import Schedule, Region
from code.visualization.visualize import *

# Parameters
holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
netherlands = Region("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv") 
new_schedule = Schedule(netherlands)
max_trains = 20
max_time = 180
lookahead = 3

greedy_lookahead = GreedyLookahead(new_schedule, max_time, max_trains, lookahead)
greedy_lookahead.run()

outputToFile(greedy_lookahead.schedule, "Greedy Lookahead algorithm output_Nederland, 23/6/2024", "data/output/greedy_lookahead/greedylookahead_ouput.csv")
routesToFile(greedy_lookahead.schedule, "Greedy Lookahead algorithm output_Nederland, 23/6/2024", "data/output/greedy_lookahead/greedylookahead_route.csv")
