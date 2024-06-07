from spoorschavuiten.code.classes import Region


# if __name__ == "__main__":

holland = Region("spoorschavuiten/csv_files/StationsHolland.csv", "spoorschavuiten/csv_files/ConnectiesHolland.csv")

max_trains = 7

for i in range(max_trains):
    holland.add_route(current_station)
    if holland.is_solution:
        break

minimum_x = holland._stations[0]._x
minimum_y = holland._stations[0]._y
maximum_x = holland._stations[0]._x
maximum_y = holland._stations[0]._y
for s in holland._stations:
    if s._x < minimum_x:
        minimum_x = s._x
    if s._x > maximum_x:
        maximum_x = s._x
    if s._y < minimum_y:
        minimum_y = s._y
    if s._y > maximum_y:
        maximum_y = s._y
print("min x is " + str(minimum_x))
print("min y is " + str(minimum_y))
print("max x is " + str(maximum_x))
print("max y is " + str(maximum_y))
    
    #print(s)

#for c in holland._connections:
    #print(c._stationA + " is verbonden met " + c._stationB + " in " + str(c._dist) + " minuten.")    

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
