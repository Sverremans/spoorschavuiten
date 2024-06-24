from code.classes.classes import Region, Schedule
# from code.algorithms import randomise, randomise2, randomWithConstraints
from code.algorithms import random as rd
from code.algorithms import greedy as gd
from code.visualization.visualize import *
import time

colors = ["red", "blue", "pink", "black", "yellow",
        "hotpink", "orange", "violet", "cyan", "purple",
        "maroon", "indigo", "teal", "magenta", "crimson", "palevioletred", 
        "salmon", "deepskyblue", "deeppink", "darkviolet", "goldenrod"]

if __name__ == "__main__":

    holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
    netherlands = Region("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv") 

    start = time.time()
    all_outputs = []
    times = 1000000
    timeList = []

    for i in range(times):
        timeList.append(i + 1)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # # Random Holland
    # for i in range(times):
    #     schedule = Schedule(holland)
    #     randomSolution = rd.Random(schedule, 120, 7)
    #     randomSolution.run()

    #     output = randomSolution.schedule.calculate_value()
    #     scoresToFile(schedule, i, "data/1000000RandomScores.csv")
    #     # print(schedule.calculate_value())
    #     all_outputs.append(output)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # # Random Nederland
    # for i in range(times):
    #     schedule = Schedule(netherlands)
    #     randomSolution = rd.Random(schedule, 180, 20)
    #     randomSolution.run()

    #     output = randomSolution.schedule.calculate_value()
    #     scoresToFile(schedule, i, "data/1000000RandomScoresNederland.csv")
    #     # print(schedule.calculate_value())
    #     all_outputs.append(output)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # # Greedy Holland
    # for i in range(times):
    #     schedule = Schedule(holland)
    #     greedySolutionHol = gd.Greedy(schedule, 120, 7)
    #     greedySolutionHol.run()

    #     output = greedySolutionHol.schedule.calculate_value()
    #     scoresToFile(schedule, i, "data/1000000GreedyScoresHolland.csv")
    #     # print(schedule.calculate_value())
    #     all_outputs.append(output)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Greedy Nederland
    for i in range(times):
        schedule = Schedule(netherlands)
        greedySolutionNed = gd.Greedy(schedule, 180, 20)
        greedySolutionNed.run()

        output2 = greedySolutionNed.schedule.calculate_value()
        scoresToFile(schedule, i, "data/1000000GreedyScoresNederland_2.csv")
        # print(schedule.calculate_value())
        # all_outputs.append(output2)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    end = time.time()
    print(end - start)
