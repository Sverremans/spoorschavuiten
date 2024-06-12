from code.classes.classes import Region
from code.algorithms import randomise, randomise2
from code.visualization.visualize import outputGraph
import time


if __name__ == "__main__":

    start = time.time()
    all_outputs = []
    times = 10000
    timeList = []

    for i in range(times):
        timeList.append(i + 1)

    for i in range(times):
        holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
        max_trains = 7

        for i in range(max_trains):
            randomise2.random_route_2(holland)
            if holland.is_solution():
                break
        output = holland.calculate_value()
        all_outputs.append(output)

    end = time.time()
    outputGraph(all_outputs, timeList)

    
    print(end - start)
    # outputGraph(times, test)
