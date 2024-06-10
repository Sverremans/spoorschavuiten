from code.classes.classes import Region
from code.algorithms import randomise


if __name__ == "__main__":

    holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")

    max_trains = 7

    for i in range(max_trains):
        randomise.random_route(holland)
        if holland.is_solution():
            break

    holland.generate_output()
