import random
from code.classes.classes import Route, Station, Schedule, Connection


class Random:
    """
    Algorithm that adds routes to schedule. Starting a route in random station and then taking random paths of linked connections.
    """
    def __init__(self, schedule: Schedule, maxTime: int, maxTrains: int) -> None:
        self.schedule = schedule
        self.maxTime = maxTime
        self.maxTrains = maxTrains
        self.time: int = 0

    def choose_station(self) -> Station:
        """
        Chooses randomly from list of stations.
        """
        return random.choice(list(self.schedule.stations.values()))

    def get_connections(self, currentStation: Station) -> list[tuple[Connection, str]]:
        """
        Returns list of available connections and their directions (forwards or backwards) from current station.
        """
        connections = []
        for connection in self.schedule.connections:
            if connection.stationA == currentStation:
                connections.append((connection, "f"))
            if connection.stationB == currentStation:
                connections.append((connection, "b"))
        return connections
    
    def choose_connection(self, possibleConnections: list[tuple[Connection, str]]) -> tuple[Connection, str]:
        """
        Returns a randomly choosen connection and direction.
        """
        return random.choice(possibleConnections)

    def add_time(self, extraTime: int) -> None:
        """
        Adds time used to self.time varaiable.
        """
        self.time += extraTime

    def subtract_time(self, extraTime: int) -> None:
        """
        Subtracts time used to self.time varaiable.
        """
        self.time -= extraTime

    def set_connection_is_used(self, connection: Connection) -> None:
        """
        Calls is_used() method of object of Connection class.
        """
        connection.is_used()

    def set_new_station(self, station: Station, direction: str, connection: Connection) -> Station:
        """
        Returns the new current station based on given direction the connection is traveled on.
        """
        if direction == "f":
            station = connection.stationB
        else:
            station = connection.stationA
        return station
    
    def generate_output(self) -> None:
        """
        Calls generate_output() method of self.schedule object.
        """
        self.schedule.generate_output()

    def run(self) -> None:
        """
        Runs the algorithm.
        """
        for _ in range(self.maxTrains):
            route = Route()
            self.time = 0
            # Kies een random station om met de trein te beginnen.
            currentStation = self.choose_station()
            route.add_station(currentStation)

            # Kies op het station een connectie om berijden
            while self.time <= self.maxTime:
                possibleConnections = self.get_connections(currentStation)
                chosenConnection, direction = self.choose_connection(possibleConnections)
                # Voeg deze connectie toe aan het traject, voeg de afstand toe
                self.add_time(chosenConnection.get_dist())
                if self.time > self.maxTime:
                    self.subtract_time(chosenConnection.get_dist())
                    break
                self.set_connection_is_used(chosenConnection)
                currentStation = self.set_new_station(currentStation, direction, chosenConnection)
                route.add_connection(chosenConnection)
                route.add_station(currentStation)

            self.schedule.add_route(route)
            self.schedule.update_time(self.time)
            # Stop met trajecten leggen als alle verbindingen zijn gemaakt.
            if self.schedule.is_solution():
                break


class FixedRandom(Random):
    """
    A variation on the Random algorithm that returns the same output based on a fixedseed.
    """
    def __init__(self, schedule: Schedule, maxTime: int, maxTrains: int, fixedSeed: int) -> None:
        super().__init__(schedule, maxTime, maxTrains)
        random.seed(fixedSeed)
