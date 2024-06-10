import pandas as pd
import random


class Station:
    """Station met bijbehorende coordinaten."""
    def __init__(self, name: str, x: float, y: float) -> None:
        self._name = name
        self._x = x
        self._y = y

    def __repr__(self) -> str:
        return self._name


class Connection:
    """Verbinding tussen twee stations met bijbehorende duur in minuten."""
    def __init__(self, stationA: Station, stationB: Station, dist: int) -> None:
        self._stationA = stationA
        self._stationB = stationB
        self._dist = dist
        self._used: bool = False

    def get_dist(self) -> int:
        return self._dist

    def is_used(self):
        self._used = True
    
    def __repr__(self) -> str:
        return f"{self._stationA} naar {self._stationB}"


class Route:
    """Traject van connecties waar een trein langs komt."""
    def __init__(self) -> None:
        self._route: list[Connection] = []
        self._stations: list[Station] = []
    
    def add_connection(self, connection) -> None:
        self._route.append(connection)

    def get_dist(self) -> int:
        dist = 0
        for connection in self._route:
            dist += connection.get_dist()
        return dist


class Region:
    """Regio van stations en verbindingen waarin routes lopen."""
    def __init__(self, stations_file: str, connections_file: str) -> None:
        self._stations: dict[str, Station] = self.load_stations(stations_file)
        self._connections: list[Connection] = self.load_connections(connections_file)
        self._routes: list[Route] = []
        self._time_used: int = 0
        self._current_station = random.choice(list(self._stations.values()))
    
    def load_stations(self, stations_file: str) -> list:
        stations = {}

        # add stations with coordinates
        df_stations = pd.read_csv(stations_file)
        for l in range(len(df_stations)):
            new_station = Station(df_stations.loc[l, 'station'], df_stations.loc[l, 'x'], df_stations.loc[l, 'y'])
            stations[new_station._name] = new_station

        return stations

    def load_connections(self, connections_file: str) -> list:
        connections = []

        # add connections and distances
        df_connections = pd.read_csv(connections_file)
        for l in range(len(df_connections)):
            stationA = self._stations[df_connections.loc[l, 'station1']]
            stationB = self._stations[df_connections.loc[l, 'station2']]
            new_connection = Connection(stationA, stationB, df_connections.loc[l, 'distance'])
            connections.append(new_connection)

        return connections

    def add_route(self) -> None:
        time = 0
        route = Route()
        current_station = self._current_station
        route._stations.append(current_station)
        while time <= 120:
            possible_connections = []
            for connection in self._connections:
                if connection._stationA == current_station:
                    possible_connections.append((connection, "f"))
                if connection._stationB == current_station:
                    possible_connections.append((connection, "b"))
            # choose randomly from possible connections
            connection, direction = random.choice(possible_connections)
            time += connection.get_dist()
            connection.is_used()
            # check to move forewards or backwards
            if direction == "f":
                current_station = connection._stationB
            else:
                current_station = connection._stationA

            route.add_connection(connection)
            route._stations.append(current_station)

        self._current_station = current_station
        self._routes.append(route)
        self._time_used += time

    def is_solution(self) -> bool:
        """Returns True if each connection is used, False otherwise."""
        for connection in self._connections:
            if not connection.is_used():
                return False
        return True
    
    def calculate_value(self) -> int:
        """Calculates value of configuration of total routes."""
        nr_of_connections_used = 0
        for connection in self._connections:
            if connection._used == True:
                nr_of_connections_used += 1
        fraction_used = nr_of_connections_used / len(self._connections)

        trajectories = len(self._routes)

        minutes = self._time_used

        return fraction_used * 10000 - (trajectories * 100 + minutes)
    
    def generate_output(self) -> None:
        route = [holland._connections[1], holland._connections[0], holland._connections[-1]]
        #1 maak empty list van stations
        station_list = []
        #2 check welk station erin moet en voeg toe

        #3 doe dit voor elke trein

        #4 bereken score

        #5 print header

        #6 print treinen

        #7 print score