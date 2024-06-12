from code.classes.classes import Region
from code.algorithms import randomise, randomise2
#from code.visualization.visualize import visualizeMap

if __name__ == "__main__":

    holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
    nederland = Region("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv")

    max_trains = 7

    for i in range(max_trains):
        randomise2.random_route_2(holland)
        if holland.is_solution():
            break
    holland.generate_output()
    #visualizeMap()
    #test
