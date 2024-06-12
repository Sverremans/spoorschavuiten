from code.classes.classes import Region
from code.algorithms import randomise


if __name__ == "__main__":

    all_outputs = []
    for i in range(100):
        holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
        max_trains = 7

        for i in range(max_trains):
            randomise.random_route_2(holland)
            if holland.is_solution():
                break
        output = holland.calculate_value()
        all_outputs.append(output)
    print(all_outputs)