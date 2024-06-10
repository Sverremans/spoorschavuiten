from classes import Region


if __name__ == "__main__":

    holland = Region("../csv_files/StationsHolland.csv", "../csv_files/ConnectiesHolland.csv")

    max_trains = 7

    for i in range(max_trains):
        holland.add_route()
        if holland.is_solution():
            break

    # Print output
    print("train,stations")
    for i, route in enumerate(holland._routes, 1):
        print(f"train{i},{route._stations}")
        print(f"score,{holland.calculate_value()}")
