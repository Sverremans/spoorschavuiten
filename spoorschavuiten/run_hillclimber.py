from code.algorithms.hillclimber import HillClimber, HcStopCondition
from code.algorithms.random import FixedRandom, Random
from code.classes.classes import Schedule, Region
from code.visualization.visualize import *


holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
schedule = Schedule(holland)

random = Random(schedule, 120, 7)
random.run()

iterations = 10

for i in range(iterations):
    hillClimber = HcStopCondition(schedule, 120, 7, 1000000)
    hillClimber.run(10, 4)

    outputToFile(hillClimber._newSchedule, f"test_{i + 1}", "data/test123.csv")
    routesToFile(hillClimber._newSchedule, f"test{i + 1}", "data/test456.csv")
    # raise NotImplementedError