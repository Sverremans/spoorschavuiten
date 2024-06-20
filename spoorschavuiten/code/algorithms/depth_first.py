from code.classes.classes import Route
import copy
import time


class DepthFirst():
    """
    A Depth First algorithm that builds a stack of schedules with a unique assignment of routes for each instance.
    """

    def __init__(self, schedule, maxTime: int, maxTrains: int):
        self.schedule = schedule
        self.maxTime = maxTime
        self.max_trains = maxTrains

        self.possible_routes = []
        self.best_route = None
        self.best_score = 0

    def run(self):
        step = 0
        start = time.time()

        # for each train find best route
        for _ in range(1):

            # search for best route from all starting stations
            for station in self.schedule.stations.values():
                new_route = Route()
                new_route.current_station = station
                self.possible_routes.append(new_route)

                # for each possible starting position, visit all possible routes
                while self.possible_routes:
                    step += 1
                    print(f'Step {step}, with {len(self.possible_routes)} states, current value: {self.best_score}')
                    new_route = self.get_next_state()
                    self.check_score(new_route)
                    current_station = new_route.current_station
                    self.build_children(new_route, current_station)

            # past this point best possible route to add to schedule is found
            print(f"passed this point. Best route is: {self.best_route._route}. Score: {self.best_score}")
            self.schedule.add_route(self.best_route)
            self.best_route = None
            self.best_score = 0

            # check if all connections are already used (so max overall score)
            scheduled_connections = {connection for route in self.schedule.routes for connection in route.route}
            if set(self.schedule.connections) == scheduled_connections:
                break
        
        end = time.time()
        print(f"Duration of algorithm in seconds: {end - start}")

    def get_next_state(self):

        return self.possible_routes.pop()
    
    def check_score(self, new_route):
        """
        Check if new route has better score than best route
        """
        new_score = self.get_score(new_route)
        if new_score > self.best_score:
            self.best_route = new_route
            self.best_score = new_score

    def get_score(self, new_route):
        """
        Returns score for the potential route
        """
        if self.schedule.routes:
            scheduled_connections = {connection for route in self.schedule.routes for connection in route.route}
        else:
            scheduled_connections = set()
        connections_used = {connection for connection in new_route.route}
        added_connections = connections_used - scheduled_connections
        fraction = len(added_connections) / len(self.schedule.connections)

        return fraction * 10000 - (100 + new_route.time)

    def build_children(self, route, current_station):
        possible_connections = self.get_connections(current_station)
        for possible_connection in possible_connections:
            connection, direction = possible_connection
            new_route = copy.deepcopy(route)
            new_route.add_time(connection.get_dist())
            if new_route.time > self.maxTime:
                new_route.subtract_time(connection.get_dist())
                continue
            new_route.add_connection(connection)
            new_route.current_station = self.get_new_station(current_station, direction, connection)
            self.possible_routes.append(new_route)

    def get_connections(self, currentStation) -> list:
        connections = []
        for connection in self.schedule._connections:
            if connection.stationA == currentStation:
                connections.append((connection, "f"))
            if connection.stationB == currentStation:
                connections.append((connection, "b"))
        return connections

    def get_new_station(self, station, direction, connection):
        if direction == "f":
            station = connection.stationB
        else:
            station = connection.stationA
        return station
