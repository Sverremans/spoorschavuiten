from code.algorithms.random import Random
from code.classes.classes import Route
import random


class Greedy(Random):
    """
    Routes starts at random locations, but the rest is searched for in greedy way.
    """
    def get_connections(self, current_station) -> list:
        possible_connections = []
        unused_connections = []
        
        for connection in self.schedule.connections:
            if connection._stationA == current_station:
                possible_connections.append((connection, "f"))
                if not connection.used:
                    unused_connections.append((connection, "f"))
            if connection._stationB == current_station:
                possible_connections.append((connection, "b"))
                if not connection.used:
                    unused_connections.append((connection, "b"))
        
        return possible_connections, unused_connections

    def choose_connection(self, possible_connections, unused_connections):
        if len(unused_connections) > 0:
            return random.choice(unused_connections)
        else:    
            return random.choice(possible_connections)

    def run(self):
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
    def __init__(self, schedule, maxTime: int, maxTrains: int, fixedSeed: int):
        self.schedule = schedule
        self.maxTime = maxTime
        self.maxTrains = maxTrains
        self.time = 0
        random.seed(fixedSeed)