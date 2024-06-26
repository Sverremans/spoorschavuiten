from code.algorithms.random import Random
from code.classes.classes import Route
import random
from typing import Any
import functools

class Greedy(Random):
    """
    Routes starts at random locations, but the rest is searched for in greedy way.
    """
    def get_connections(self, current_station) -> list:
        possible_connections = self.schedule.get_connections(current_station)
        unused_connections = []
        
        for connection, direction in possible_connections:
             if not connection.used:
                    unused_connections.append((connection, direction))

        return possible_connections, unused_connections

    def choose_connection(self, possible_connections, unused_connections) -> Any:
        if unused_connections:
            return random.choice(unused_connections)
        else:    
            return random.choice(possible_connections)

    def run(self) -> None:
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
    def __init__(self, schedule, maxTime: int, maxTrains: int, fixedSeed: int) -> None:
        self.schedule = schedule
        self.maxTime = maxTime
        self.maxTrains = maxTrains
        self.time = 0
        random.seed(fixedSeed)

class Termini_Greedy(Greedy):
    """
    Kiest eerst de stations met slechts één verbinding als startpunten.
    Deze heuristiek voorkomt het onnodig dubbel berijden van sporen.
    """
    def run(self) -> None:
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
