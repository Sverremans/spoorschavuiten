import random
from code.classes.classes import Route

# ########################################################### #
# This function takes used vs unused connections into account #
# ########################################################### #
class Random:
    def __init__(self, schedule, maxTime: int, maxTrains: int):
        # self.region = region
        self.schedule = schedule
        self.maxTime = maxTime
        self.maxTrains = maxTrains
        self.time = 0


    def choose_station(self):
        return random.choice(list(self.schedule._stations.values()))


    def get_connections(self, currentStation) -> list:
        connections = []
        # print(self.region._connections)
        for connection in self.schedule._connections:
            # print(connection._stationA)
            # print(connection._stationB)

            if connection._stationA == currentStation:
                connections.append((connection, "f"))
            if connection._stationB == currentStation:
                connections.append((connection, "b"))
        return connections
    

    def choose_connection(self, possibleConnections):
        return random.choice(possibleConnections)


    def add_time(self, extraTime):
        self.time += extraTime
        # return self.time


    def subtract_time(self, extraTime):
        self.time -= extraTime


    def set_connection_is_used(self, connection):
        connection.is_used()


    def set_new_station(self, station, direction, connection):
        if direction == "f":
            station = connection._stationB
        else:
            station = connection._stationA
        return station
    
    
    def run(self):
        # self.reset()
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
        # Herhaal tot time > maxTime bij de volgende stap, of tot er maxTrain aantal trajecten zijn gemaakt.
    