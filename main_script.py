from classes import Region


if __name__ == "__main__":

    holland = Region("csv_files/StationsHolland.csv", "csv_files/ConnectiesHolland.csv")

    for s in holland._stations:
        print(s)
    for c in holland._connections:
        print(c._stationA + " is verbonden met " + c._stationB + " in " + str(c._dist) + " minuten.")
    
    # trains = [] # max 7
    # time = 120min
    # all connections on True
    # train = [object(station), object(station),...]
    # current_station = random.stations

    # while connections < 0 or trains < 8:
    #     time = 0
    #     while time < 120:
    #         train.append(current_station)
    #         # get one of stations which is connected from connections variable
    #         # remove that connection from connections variable
    #         time += connection._dist
    #     trains.append(train)
