from code.classes.classes import Region, Schedule
from code.algorithms.random import Random
from code.algorithms.greedy import Greedy
from code.algorithms.greedy import Termini_Greedy
from code.algorithms.depth_first import DepthFirst
from code.visualization.visualize import *
from code.algorithms.hillclimber import HillClimber as hc
from code.algorithms.hillclimber import HcStopCondition as hcStop
from code.algorithms.hillclimber import Termini_HillClimber as terHc
import time

start_time = time.time()
if __name__ == "__main__":

    colors = ["red", "blue", "pink", "black", "yellow",
        "hotpink", "orange", "violet", "cyan", "purple",
        "maroon", "indigo", "teal", "magenta", "crimson", "palevioletred", 
        "salmon", "deepskyblue", "deeppink", "darkviolet", "goldenrod"]

    holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
    nederland = Region("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv")

    # new_schedule = Schedule(holland)
    # max_trains = 7
    # max_time = 120

    # greedy_schedule = Greedy(new_schedule, max_time, max_trains)
    # greedy_schedule.run()
    # greedy_schedule.generate_output()

    ### Hier volgt code om hillclimber te testen ###

    # new_schedule = Schedule(nederland)
    max_trains = 20
    max_time = 180

    total_iterations = 100
    for iteration in range(total_iterations):
        new_schedule = Schedule(nederland)
        greedy_schedule = Greedy(new_schedule, max_time, max_trains)
        greedy_schedule.run()

        hillClimber = terHc(new_schedule, max_time, max_trains)
        hillClimber.run(50000, 12)
        # hillClimber.generate_output()

        outputToFile(hillClimber.newSchedule, f'termini_hillclimber run {iteration + 1}', "data/termini_hillclimber.csv")
        routesToFile(hillClimber.newSchedule, f'termini_hillclimber run {iteration + 1}', "data/termini_hillclimber_routes.csv")
        if (iteration + 1) % 5 == 0:
            print(f'Current iteration: {iteration + 1} out of {total_iterations}')

    print("--- %s seconds ---" % (time.time() - start_time))
    
    # depth_first = DepthFirst(new_schedule, max_time, max_trains)
    # depth_first.run()

    ### Hier eindigt code om hillclimber te testen ###

    # for i in range(max_trains):
    #     randomise2.random_route(holland)
    #     if holland.is_solution():
    #         break
    # holland.generate_output()

    #makeMapWithNames(holland)
    #drawUsedConnections(holland, colors)
    #visualizeMap(holland, "figures/test.png")
    #test
