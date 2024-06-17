from code.classes.classes import Region
from code.algorithms import randomise, randomise2
from code.visualization.visualize import *

if __name__ == "__main__":

    colors = ["red", "blue", "pink", "black", "yellow",
        "hotpink", "orange", "violet", "cyan", "purple",
        "maroon", "indigo", "teal", "magenta", "crimson", "palevioletred", 
        "salmon", "deepskyblue", "deeppink", "darkviolet", "goldenrod"]

    holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
    nederland = Region("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv")

    max_trains = 7

    ### Hier volgt code om hillclimber te testen ###

    schedule = Schedule(holland)

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
