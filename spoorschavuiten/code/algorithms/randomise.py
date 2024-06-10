import random
from code.classes.classes import Route


def random_route(regio) -> None:
    time = 0
    route = Route()
    current_station = random.choice(list(regio._stations.values()))
    route._stations.append(current_station)
    while time <= 120:
        possible_connections = []
        for connection in regio._connections:
            if connection._stationA == current_station:
                possible_connections.append((connection, "f"))
            if connection._stationB == current_station:
                possible_connections.append((connection, "b"))
        # choose randomly from possible connections
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
        route._stations.append(current_station)

    regio._routes.append(route)
    regio._time_used += time

# ########################################################### #
# This function takes used vs unused connections into account #
# ########################################################### #
def random_route_2(regio) -> None:
    time = 0
    route = Route()
    current_station = random.choice(list(regio._stations.values()))
    route._stations.append(current_station)
    while time <= 120:
        possible_connections = []
        unused_connections = []
        
        for connection in regio._connections:
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

        # Ik heb geen flauw idee waarom, maar het volgende blokje code dwingt routes via Almaar:

        #for connection in regio._connections:
        #    if connection._used:
        #        print(connection)
        
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
        route._stations.append(current_station)

    regio._routes.append(route)
    regio._time_used += time