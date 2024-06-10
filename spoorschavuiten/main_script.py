from code.classes.classes import Region


if __name__ == "__main__":

    holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")

    max_trains = 7

    for i in range(max_trains):
        holland.add_route()
        if holland.is_solution():
            break

    holland.generate_output()
