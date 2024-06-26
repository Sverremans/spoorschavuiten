from code.classes.classes import Region, Schedule
from code.algorithms import random as rd
from code.algorithms import greedy as gd
from code.visualization.visualize import *
import time

if __name__ == "__main__":

    holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
    netherlands = Region("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv") 

    start = time.time()
    times = 1000000
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Met de volgende regels code worden 1000000 random dienstregelingen gemaakt voor Holland.
# Deze scores worden opgeslagen in losse bestanden waar vervolgens histogrammen en boxplots mee gemaakt worden. 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Random Holland
    for i in range(times):
        schedule = Schedule(holland)
        randomSolution = rd.Random(schedule, 120, 7)
        randomSolution.run()

        scoresToFile(schedule, i, "data/1000000RandomScoresHolland_2.csv")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Met de volgende regels code worden 1000000 random dienstregelingen gemaakt voor Nederland.
# Deze scores worden opgeslagen in losse bestanden waar vervolgens histogrammen en boxplots mee gemaakt worden. 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Random Nederland
    for i in range(times):
        schedule = Schedule(netherlands)
        randomSolution = rd.Random(schedule, 180, 20)
        randomSolution.run()

        scoresToFile(schedule, i, "data/1000000RandomScoresNederland.csv")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Met de volgende regels code worden 1000000 greedy dienstregelingen gemaakt voor Holland.
# Het greedy algoritme houd rekening met al gebruikte verbindingen en vermijdt deze wanneer het mogelijk is.
# Deze scores worden opgeslagen in losse bestanden waar vervolgens histogrammen en boxplots mee gemaakt worden. 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Greedy Holland
    for i in range(times):
        schedule = Schedule(holland)
        greedySolutionHol = gd.Greedy(schedule, 120, 7)
        greedySolutionHol.run()

        scoresToFile(schedule, i, "data/1000000GreedyScoresHolland_2.csv")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Met de volgende regels code worden 1000000 greedy dienstregelingen gemaakt voor Nederland.
# Het greedy algoritme houd rekening met al gebruikte verbindingen en vermijdt deze wanneer het mogelijk is.
# Deze scores worden opgeslagen in losse bestanden waar vervolgens histogrammen en boxplots mee gemaakt worden. 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Greedy Nederland
    for i in range(times):
        schedule = Schedule(netherlands)
        greedySolutionNed = gd.Greedy(schedule, 180, 20)
        greedySolutionNed.run()

        scoresToFile(schedule, i, "data/1000000GreedyScoresNederland_3.csv")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    end = time.time()
    print(end - start)
