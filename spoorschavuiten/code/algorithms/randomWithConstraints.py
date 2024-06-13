import random
from code.classes.classes import Route

# ########################################################### #
# This function takes used vs unused connections into account #
# ########################################################### #
def trajects(region, used):
    max_trains = 7

    for i in range(max_trains):
        random_route(region, used)
        if region.is_solution():
            break   

def random_route(region, usedStations) -> None:
    maxTrains = 7
    for i in range(maxTrains):
        time = 0
        route = Route()
        # usedStations = set()
        current_station = random.choice(list(region._stations.values()))
        while current_station in usedStations:
            current_station = random.choice(list(region._stations.values()))
        usedStations.add(current_station)
        route.add_station(current_station)
        while time <= 120:
            possible_connections = []
            unused_connections = []
            
            
            for connection in region._connections:
                if connection._stationA == current_station:
                    possible_connections.append((connection, "f"))
                    if not connection._used:
                        unused_connections.append((connection, "f"))
                if connection._stationB == current_station:
                    possible_connections.append((connection, "b"))
                    if not connection._used:
                        unused_connections.append((connection, "b"))

            # choose randomly from (unused) possible connections
            if len(unused_connections) > 0:
                connection, direction = random.choice(unused_connections)
            else:    
                connection, direction = random.choice(possible_connections)

            time += connection.get_dist()
            
            # check if max time exceeded
            if time > 120:
                time -= connection.get_dist()
                break
            connection.is_used()
            # check to move forwards or backwards
            if direction == "f":
                current_station = connection._stationB
            else:
                current_station = connection._stationA

            route.add_connection(connection)
            route.add_station(current_station)

        region.add_route(route)
        region.update_time(time)
        if region.is_solution():
            break 
    