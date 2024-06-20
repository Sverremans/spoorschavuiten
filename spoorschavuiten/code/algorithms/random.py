import random
from code.classes.classes import Route, Station
from typing import Any


class Random:
    """
    Fully random algorithm.
    """
    def __init__(self, schedule, maxTime: int, maxTrains: int) -> None:
        self.schedule = schedule
        self.maxTime = maxTime
        self.maxTrains = maxTrains
        self.time = 0

    def choose_station(self) -> Station:
        return random.choice(list(self.schedule.stations.values()))

    def get_connections(self, currentStation) -> list:
        connections = []
        for connection in self.schedule.connections:
            if connection.stationA == currentStation:
                connections.append((connection, "f"))
            if connection.stationB == currentStation:
                connections.append((connection, "b"))
        return connections
    
    def choose_connection(self, possibleConnections) -> Any:
        return random.choice(possibleConnections)

    def add_time(self, extraTime) -> None:
        self.time += extraTime

    def subtract_time(self, extraTime) -> None:
        self.time -= extraTime

    def set_connection_is_used(self, connection) -> None:
        connection.is_used()

    def set_new_station(self, station, direction, connection) -> Station:
        if direction == "f":
            station = connection.stationB
        else:
            station = connection.stationA
        return station
    
    def generate_output(self) -> None:
        self.schedule.generate_output()

    def run(self) -> None:
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
    def __init__(self, schedule, maxTime: int, maxTrains: int, fixedSeed: int) -> None:
        self.schedule = schedule
        self.maxTime = maxTime
        self.maxTrains = maxTrains
        self.time = 0
        random.seed(fixedSeed)