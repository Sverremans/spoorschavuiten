import random
from code.classes.classes import Route

# BASELINE
def random_route(region) -> None:
    ''''
    This function selects a random route for 1 train.
    '''
    time = 0
    route = Route()
    current_station = random.choice(list(region._stations.values()))
    route.add_station(current_station)
    while time <= 120:
        possible_connections = []
        for connection in region._connections:
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
        route.add_station(current_station)

    region.add_route(route)
    region.update_time(time)
