from code.algorithms.random import Random
from code.classes.classes import Route, Station, Connection, Schedule
import random
import functools


class Greedy(Random):
    """
    Algorithm that adds routes to schedule. Starting a route in random station and then taking paths of linked connections. 
    Connections are set with preference for unused ones.
    """
    def get_connections(self, current_station: Station) -> tuple[list[tuple[Connection, str]], list[tuple[Connection, str]]]:
        """
        Returns tuple of lists of available connections and their directions (forwards or backwards) from current station. 
        The first list is of all possible connections. The second list is of all unused possible connections.
        """
        possible_connections = self.schedule.get_connections(current_station)
        unused_connections = []
        
        for connection, direction in possible_connections:
             if not connection.used:
                    unused_connections.append((connection, direction))

        return possible_connections, unused_connections

    def choose_connection(self, possible_connections: list[tuple[Connection, str]], unused_connections: list[tuple[Connection, str]]) -> tuple[Connection, str]:
        """
        Returns a randomly choosen unused connection and direction, but if there is none 
        it returns a randomly choosen used connection and direction.
        """
        if unused_connections:
            return random.choice(unused_connections)
        else:    
            return random.choice(possible_connections)

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
                possible_connections, unused_connections = self.get_connections(currentStation)
                chosenConnection, direction = self.choose_connection(possible_connections, unused_connections)
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


class FixedGreedy(Greedy):
    """
    A variation on the Greedy algorithm that returns the same output based on a fixedseed.
    """
    def __init__(self, schedule: Schedule, maxTime: int, maxTrains: int, fixedSeed: int) -> None:
        super().__init__(schedule, maxTime, maxTrains)
        random.seed(fixedSeed)

class Termini_Greedy(Greedy):
    """
    A variation on the Greedy algorithm that preferrably chooses start stations with only one connection, 
    if none it chooses a random start station again. This heuristic prevents some use of connections twice.
    """
    def run(self) -> None:
        """
        Runs the algorithm.
        """
        # Bepaal welke stations kopstations zijn
        self._termini = []
        self._unused_termini = []
        for station in self.schedule.stations.values():
            if len(self.get_connections(station)[0]) == 1:
                self._termini.append(station)
                self._unused_termini.append(station)

        for _ in range(self.maxTrains):
            route = Route()
            self.time = 0
            
            # Kies eerst kopstations als beginpunten, daarna random andere stations
            if self._unused_termini:
                currentStation = self._unused_termini.pop()
            else:
                currentStation = self.choose_station()
                while currentStation in self._termini:
                    currentStation = self.choose_station()
            route.add_station(currentStation)

            # Kies op het station een connectie om berijden
            while self.time <= self.maxTime:
                possible_connections, unused_connections = self.get_connections(currentStation)
                chosenConnection, direction = self.choose_connection(possible_connections, unused_connections)
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
