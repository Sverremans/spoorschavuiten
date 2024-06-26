from code.classes.classes import Route, Schedule, Station, Connection
import copy
import time


class DepthFirst():
    """
    A Depth First search algorithm that searches through all possible configurations of a route and 
    adds the highest scoring one to schedule.
    """

    def __init__(self, schedule: Schedule, maxTime: int, maxTrains: int):
        self.schedule = schedule
        self.maxTime = maxTime
        self.max_trains = maxTrains

        self.possible_routes: list[Route] = []
        self.best_route: Route = None
        self.best_score: int = 0

    def run(self) -> None:
        """
        Runs the algorithm.

        pre: self.schedule is an object of type Schedule and self.max_trains is a positive integer.
        post: adds routes to self.schedule. The amount depends on if all connections are set before self.max_trains.
        """
        step = 0
        start = time.time()

        # for each train find best route
        for _ in range(self.max_trains):

            # search for best route from all starting stations
            for station in self.schedule.stations.values():
                new_route = Route()
                new_route.current_station = station
                self.possible_routes.append(new_route)

                # for each possible starting position, visit all possible routes
                while self.possible_routes:
                    step += 1
                    print(f'Step {step}, current value: {self.best_score}, schedule: {len(self.schedule._routes)}')
                    new_route = self.get_next_state()
                    self.check_score(new_route)
                    current_station = new_route.current_station
                    self.build_children(new_route, current_station)

            # past this point best possible route to add to schedule is found
            self.schedule.add_route(self.best_route)
            self.best_route = None
            self.best_score = 0

            # check if all connections are already used (so max overall score)
            scheduled_connections = {connection for route in self.schedule.routes for connection in route.route}
            if set(self.schedule.connections) == scheduled_connections:
                break
        
        end = time.time()
        print(f"Duration of algorithm in seconds: {end - start}")

    def get_next_state(self) -> Route:
        """
        Pops next configuration of route.

        pre: self.possible_routes is not empty.
        post: deletes and returns an object of type Route from self.possible_routes.
        """

        return self.possible_routes.pop()
    
    def check_score(self, new_route: Route) -> None:
        """
        Check if new route has better score than best route.

        pre: new_route is an object of type Route.
        post: if new_score is higher than current, then self.best_route and self.best_score are assigned a new value, 
            otherwise nothing changes.
        """

        new_score = self.get_score(new_route)
        if new_score > self.best_score:
            self.best_route = new_route
            self.best_score = new_score

    def get_score(self, new_route: Route) -> int:
        """
        Returns score for the potential route

        pre: new_route is an object of type Route.
        post: returns the score for the route.
        """
        if self.schedule.routes:
            scheduled_connections = {connection for route in self.schedule.routes for connection in route.route}
        else:
            scheduled_connections = set()
        connections_used = {connection for connection in new_route.route}
        added_connections = connections_used - scheduled_connections
        fraction = len(added_connections) / len(self.schedule.connections)

        return fraction * 10000 - (100 + new_route.time)

    def build_children(self, current_route: Route, current_station: Station) -> None:
        """
        Adds the children configuration states of current route to self.possible_routes stack.

        pre: route is an object of type Route and current_station is an object of type Station.
        post: appends self.possible_routes with children configuration states of current route.
        """
        possible_connections = self.get_connections(current_station)
        for possible_connection in possible_connections:
            connection, direction = possible_connection
            new_route = copy.deepcopy(current_route)
            new_route.add_time(connection.get_dist())
            if new_route.time > self.maxTime:
                new_route.subtract_time(connection.get_dist())
                continue
            new_route.add_connection(connection)
            new_route.current_station = self.get_new_station(current_station, direction, connection)
            self.possible_routes.append(new_route)

    def get_connections(self, currentStation: Station) -> list[tuple[Station, str]]:
        """
        Returns possible directions the route can go from current station.

        pre: current station is an object of type Station.
        post: returns a list of tuples of connection objects of type connection with a string 
            which indicates forwards or backwards.
        """
        connections = []
        for connection in self.schedule.connections:
            if connection.stationA == currentStation:
                connections.append((connection, "f"))
            if connection.stationB == currentStation:
                connections.append((connection, "b"))
        return connections

    def get_new_station(self, station: Station, direction: str, connection: Connection) -> Station:
        """
        Returns the station to which the connection leads.

        pre: station is an object of type Station, direction is a string and connection is an object of type Connection.
        post: returns an object of type Station.
        """
        if direction == "f":
            station = connection.stationB
        else:
            station = connection.stationA
        return station
