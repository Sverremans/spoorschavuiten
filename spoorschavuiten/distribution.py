from code.classes.classes import Region, Schedule
# from code.algorithms import randomise, randomise2, randomWithConstraints
from code.algorithms import random as rd
from code.visualization.visualize import *
import time


if __name__ == "__main__":

    holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")

    start = time.time()
    all_outputs = []
    times = 50
    timeList = []
    colors = ["red", "blue", "pink", "black", "yellow",
        "hotpink", "orange", "violet", "cyan", "purple",
        "maroon", "indigo", "teal", "magenta", "crimson", "palevioletred", 
        "salmon", "deepskyblue", "deeppink", "darkviolet", "goldenrod"]

    for i in range(times):
        timeList.append(i + 1)

    for _ in range(times):
        # holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
        # max_trains = 7

        # for i in range(max_trains):
        #     randomise.random_route(holland)
        #     if holland.is_solution():
        #         break
        schedule = Schedule(holland)
        randomSolution = rd.Random(schedule, 120, 7)
        randomSolution.run()
        # onlyLines(holland)
        # drawUsedConnections(holland, colors)
        # visualizeMap(holland, "test.png")

        output = randomSolution.schedule.calculate_value()
        print(schedule.calculate_value())
        all_outputs.append(output)

    # print("Average = " + str(sum(all_outputs) / 100000))
    end = time.time()
    # outputGraph(all_outputs, timeList)
    # print(all_outputs)
    # outputGraphHist(all_outputs, timeList)

    
    print(end - start)
