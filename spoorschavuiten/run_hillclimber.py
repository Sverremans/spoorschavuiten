from code.algorithms.hillclimber import HillClimber, HcStopCondition
from code.algorithms.random import Random
from code.classes.classes import Schedule, Region
from code.visualization.visualize import *
import time

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Het volgende stukje code wordt gebruikt om met een Hill Climber algoritme een dienstregeling te makenvoor Holland.
#
# Eerst wordt een random dienstregeling gemaakt door middel van een random algoritme.
# Deze wordt gemaakt met de een maximale tijd van 120 minuten en maximaal 7 treinen.
#
# Vervolgens wordt er 10000 keer een Hill Climber algoritme uitgevoerd die stopt nadat er 100000 keer geen verbertering in de score is gevonden.
# De Hill Climber verwijdert vanuit de bestaande dienstregeling 4 treinen en maakt deze opnieuw.
# Als de nieuwe score hoger is dan de score van het vorige schema, wordt de score opgeslagen.
# Hierna wordt het algoritme opnieuw uitgevoerd. 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("start")
start = time.time()
holland = Region("data/input/StationsHolland.csv", "data/input/ConnectiesHolland.csv")
schedule = Schedule(holland)

random = Random(schedule, 120, 7)
random.run()

iterations = 10000

for i in range(iterations):
    hillClimber = HcStopCondition(schedule, 120, 7, 100000)
    hillClimber.run(100000, 4)

    outputToFile(hillClimber.newSchedule, f"Holland; 10000 runs; hillclimber die stopt na 100000 keer geen verberering te vinden. 23/06/2024 run_{i + 1}", "data/output/hillclimberHollandOutput_3.csv")
    routesToFile(hillClimber.newSchedule, f"Holland, 10000 runs, hillclimber die stopt na 100000 keer geen verberering te vinden. 23/06/2024 run_{i + 1}", "data/output/hillclimberHollandRoutes_3.csv")
    outputHillClimberGraph(hillClimber.iterations_listPoints, hillClimber.scoresPoints, hillClimber.iterations_list, hillClimber.scores, f"Holland, 10000 runs, hillclimber die stopt na 100000 keer geen verberering te vinden. 23/06/2024 run_{i + 1}", "data/output/hillclimberHollandGraph_3.csv")
    scoresToFile(hillClimber.newSchedule, i, "data/output/hillclimberHollandScores_3.csv")

end = time.time()
print(end - start)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Het volgende stukje code wordt gebruikt om met een Hill Climber algoritme een dienstregeling te maken voor Nederland.
#
# Eerst wordt een random dienstregeling gemaakt door middel van een random algoritme.
# Deze wordt gemaakt met de een maximale tijd van 180 minuten en maximaal 20 treinen.
#
# Vervolgens wordt er 1000 keer een Hill Climber algoritme uitgevoerd die stopt nadat er 50000 keer geen verbertering in de score is gevonden.
# De Hill Climber verwijdert vanuit de bestaande dienstregeling 12 treinen en maakt deze opnieuw.
# Als de nieuwe score hoger is dan de score van het vorige schema, wordt de score opgeslagen.
# Hierna wordt het algoritme opnieuw uitgevoerd. 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("start")
start = time.time()

netherlands = Region("data/input/StationsNationaal.csv", "data/input/ConnectiesNationaal.csv")
schedule2 = Schedule(netherlands)

random = Random(schedule2, 180, 20)
random.run()

iterations = 1000

for i in range(iterations):
    hillClimber = HcStopCondition(schedule2, 180, 20, 50000)
    hillClimber.run(50000, 12)

    outputToFile(hillClimber.newSchedule, f"Nederland; 1000 runs; hillclimber die stopt na 50000 keer geen verberering te vinden. 23/06/2024 run_{i + 1}", "data/output/hillclimberNederlandOutput.csv")
    routesToFile(hillClimber.newSchedule, f"Nederland, 1000 runs, hillclimber die stopt na 50000 keer geen verberering te vinden. 23/06/2024 run_{i + 1}", "data/output/hillclimberNederlandRoutes.csv")
    outputHillClimberGraph(hillClimber.iterations_listPoints, hillClimber.scoresPoints, hillClimber.iterations_list, hillClimber.scores, f"Nederland, 1000 runs, hillclimber die stopt na 50000 keer geen verberering te vinden. 23/06/2024 run_{i + 1}", "data/output/hillclimberNederlandGraph.csv")
    scoresToFile(hillClimber.newSchedule, i, "data/output/hillclimberNederlandScores.csv")

end = time.time()
print(end - start)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Het volgende stukje code wordt gebruikt om met een Hill Climber algoritme een dienstregeling te maken voor Nederland.
#
# Eerst wordt een random dienstregeling gemaakt door middel van een random algoritme.
# Deze wordt gemaakt met de een maximale tijd van 180 minuten en maximaal 16 treinen.
#
# Vervolgens wordt er 100 keer een Hill Climber algoritme uitgevoerd die stopt nadat er 1000000 keer geen verbertering in de score is gevonden.
# De Hill Climber verwijdert vanuit de bestaande dienstregeling 3 treinen en maakt deze opnieuw.
# Als de nieuwe score hoger is dan de score van het vorige schema, wordt de score opgeslagen.
# Hierna wordt het algoritme opnieuw uitgevoerd. 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("start")
start = time.time()

netherlands = Region("data/input/StationsNationaal.csv", "data/input/ConnectiesNationaal.csv")
schedule2 = Schedule(holland)

random = Random(schedule2, 180, 16)
random.run()

iterations = 100

for i in range(iterations):
    hillClimber = HillClimber(schedule2, 16, 180)
    hillClimber.run(1000000, 3)

    outputToFile(hillClimber.newSchedule, f"Nederland; 100 runs; hillclimber die stopt na 1000000. 25/06/2024 run_{i + 1}", "data/output/hillclimberNederlandOutput_new.csv")
    routesToFile(hillClimber.newSchedule, f"Nederland, 100 runs, hillclimber die stopt na 1000000. 25/06/2024 run_{i + 1}", "data/output/hillclimberNederlandRoutes_new.csv")
    outputHillClimberGraph(hillClimber.iterations_listPoints, hillClimber.scoresPoints, hillClimber.iterations_list, hillClimber.scores, f"Nederland, 100 runs, hillclimber die stopt na 1000000. 25/06/2024  run_{i + 1}", "data/output/hillclimberNederlandGraph_new.csv")
    scoresToFile(hillClimber.newSchedule, i, "data/output/hillclimberNederlandScores_new.csv")

end = time.time()
print(end - start)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
