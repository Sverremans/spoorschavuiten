from code.classes.classes import Region
from code.algorithms import randomise, randomise2, randomWithConstraints
from code.visualization.visualize import outputGraph, outputGraphHist
import time


if __name__ == "__main__":

    start = time.time()
    all_outputs = []
    times = 100000
    timeList = []

    for i in range(times):
        timeList.append(i + 1)

    for i in range(times):
        holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
        max_trains = 7

        for i in range(max_trains):
            randomise.random_route(holland)
            if holland.is_solution():
                break
        output = holland.calculate_value()
        all_outputs.append(output)

    print("Average = " + str(sum(all_outputs) / 100000))
    end = time.time()
    # outputGraph(all_outputs, timeList)
    outputGraphHist(all_outputs, timeList)

    
    print(end - start)
