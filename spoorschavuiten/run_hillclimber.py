from code.algorithms.hillclimber import HillClimber, HcStopCondition
from code.algorithms.random import FixedRandom, Random
from code.classes.classes import Schedule, Region
from code.visualization.visualize import *
import time
import argparse

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# print("start")
# start = time.time()
holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
# schedule = Schedule(holland)


# random = Random(schedule, 120, 7)
# random.run()

# iterations = 5000
# printcounter = 0

# for i in range(iterations):
#     hillClimber = HcStopCondition(schedule, 120, 7, 100000)
#     hillClimber.run(100000, 4)

#     # hillClimber = HillClimber(schedule, 120, 7)
#     # hillClimber.run(1000, 4)

#     outputToFile(hillClimber.newSchedule, f"Holland; 10000 runs; hillclimber die stopt na 100000 keer geen verberering te vinden. 23/06/2024 run_{i + 1}", "data/hillclimberHollandOutput_3.csv")
#     routesToFile(hillClimber.newSchedule, f"Holland, 10000 runs, hillclimber die stopt na 100000 keer geen verberering te vinden. 23/06/2024 run_{i + 1}", "data/hillclimberHollandRoutes_3.csv")
#     outputHillClimberGraph(hillClimber.iterations_listPoints, hillClimber.scoresPoints, hillClimber.iterations_list, hillClimber.scores, f"Holland, 10000 runs, hillclimber die stopt na 100000 keer geen verberering te vinden. 23/06/2024 run_{i + 1}", "data/hillclimberHollandGraph_3.csv")
#     scoresToFile(hillClimber.newSchedule, i, "data/hillclimberHollandScores_3.csv")
#     printcounter += 1

#     if printcounter == 10:
#         print("10 keer gedaan")
#         printcounter = 0

# end = time.time()
# print(end - start)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# print("start")
# start = time.time()

# netherlands = Region("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv")
# schedule2 = Schedule(netherlands)


# random = Random(schedule2, 180, 20)
# random.run()

# iterations = 1000
# printcounter = 0

# for i in range(iterations):
#     hillClimber = HcStopCondition(schedule2, 180, 20, 50000)
#     hillClimber.run(50000, 12)

#     # hillClimber = HillClimber(schedule, 180, 20)
#     # hillClimber.run(50000, 12)

#     outputToFile(hillClimber.newSchedule, f"Nederland; 1000 runs; hillclimber die stopt na 50000 keer geen verberering te vinden. 23/06/2024 run_{i + 1}", "data/hillclimberNederlandOutput.csv")
#     routesToFile(hillClimber.newSchedule, f"Nederland, 1000 runs, hillclimber die stopt na 50000 keer geen verberering te vinden. 23/06/2024 run_{i + 1}", "data/hillclimberNederlandRoutes.csv")
#     outputHillClimberGraph(hillClimber.iterations_listPoints, hillClimber.scoresPoints, hillClimber.iterations_list, hillClimber.scores, f"Nederland, 1000 runs, hillclimber die stopt na 50000 keer geen verberering te vinden. 23/06/2024 run_{i + 1}", "data/hillclimberNederlandGraph.csv")
#     scoresToFile(hillClimber.newSchedule, i, "data/hillclimberNederlandScores.csv")
#     printcounter += 1

#     if printcounter == 10:
#         print("10 keer gedaan")
#         printcounter = 0

# end = time.time()
# print(end - start)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("start")
start = time.time()

netherlands = Region("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv")
schedule2 = Schedule(holland)


random = Random(schedule2, 120, 4)
random.run()

iterations = 200
printcounter = 0

for i in range(iterations):
    hillClimber = HillClimber(schedule2, 4, 120)
    hillClimber.run(1000000, 2)

    # hillClimber = HillClimber(schedule, 180, 20)
    # hillClimber.run(50000, 12)

    outputToFile(hillClimber.newSchedule, f"Holland; 1000 runs; hillclimber die stopt na 1000000. 25/06/2024 run_{i + 1}", "data/hillclimberHollandOutput_new.csv")
    routesToFile(hillClimber.newSchedule, f"Holland, 1000 runs, hillclimber die stopt na 1000000. 25/06/2024 run_{i + 1}", "data/hillclimberHollandRoutes_new.csv")
    outputHillClimberGraph(hillClimber.iterations_listPoints, hillClimber.scoresPoints, hillClimber.iterations_list, hillClimber.scores, f"Nederland, 1000 runs, hillclimber die stopt na 1000000 keer. 25/06/2024 run_{i + 1}", "data/hillclimberHollandGraph_new.csv")
    scoresToFile(hillClimber.newSchedule, i, "data/hillclimberHollandScores_new.csv")
    
    print(f'Current iteration: {i + 1} out of {iterations}')
    print(f'Current time: {time.time() - start}')

end = time.time()
print(end - start)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
