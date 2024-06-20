from code.algorithms.hillclimber import HillClimber, HcStopCondition
from code.algorithms.random import FixedRandom, Random
from code.classes.classes import Schedule, Region
from code.visualization.visualize import *


holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
netherlands = Region("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv")
schedule = Schedule(netherlands)

random = Random(schedule, 180, 20)
random.run()

iterations = 5

for i in range(iterations):
    # hillClimber = HcStopCondition(schedule, 120, 7, 1000000)
    # hillClimber.run(10, 4)

    hillClimber = HillClimber(schedule, 180, 20)
    hillClimber.run(1000000, 12)

    outputToFile(hillClimber._newSchedule, f"Nederland test_{i + 1}", "data/test123.csv")
    routesToFile(hillClimber._newSchedule, f"Nederland test_{i + 1}", "data/test456.csv")
    outputHillClimberGraph(hillClimber.iterations_listPoints, hillClimber.scoresPoints, hillClimber.iterations_list, hillClimber.scores, f"Nederland test_{i + 1}", "data/test789.csv")

    # raise NotImplementedError