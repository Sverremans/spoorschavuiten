from classes import Region


if __name__ == "__main__":

    holland = Region("../csv_files/StationsHolland.csv", "../csv_files/ConnectiesHolland.csv")

    max_trains = 7

    for i in range(max_trains):
        holland.add_route()
        if holland.is_solution():
            break
    
    holland.generate_output()
