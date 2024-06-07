import pandas as pd


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
    def __init__(self, stationA: str, stationB: str, dist: int) -> None:
        self._stationA = stationA
        self._stationB = stationB
        self._dist = dist
        self._used: bool = False

    def get_dist(self) -> int:
        return self._dist


class Route:
    """Traject van connecties waar een trein langs komt."""
    def __init__(self) -> None:
        self._route: list[Connection] = []
    
    def add_station(self, connection) -> None:
        self._route.append(connection)

    def get_dist(self) -> int:
        dist = 0
        for connection in self._route:
            dist += connection.get_dist()
        return dist


class Region:
    """Regio van stations en verbindingen waarin routes lopen."""
    def __init__(self, stations_file: str, connections_file: str) -> None:
        self._stations: list[Station] = self.load_stations(stations_file)
        self._connections: list[Connection] = self.load_connections(connections_file)
        self._routes: list[Route] = []
        self._time_used: int = 0
    
    def load_stations(self, stations_file: str) -> list:
        stations = []

        # add stations with coordinates
        df_stations = pd.read_csv(stations_file)
        for l in range(len(df_stations)):
            new_station = Station(df_stations.loc[l, 'station'], df_stations.loc[l, 'x'], df_stations.loc[l, 'y'])
            stations.append(new_station)

        return stations

    def load_connections(self, connections_file: str) -> list:
        connections = []

        # add connections and distances
        df_connections = pd.read_csv(connections_file)
        for l in range(len(df_connections)):
            new_connection = Connection(df_connections.loc[l, 'station1'], df_connections.loc[l, 'station2'], df_connections.loc[l, 'distance'])
            connections.append(new_connection)

        return connections

    def is_solution(self):
        """Returns True if each connection is used, False otherwise."""
        for connection in self._connections:
            if not connection._used():
                return False
        return True
    
    def calculate_value(self):
        """Calculates value of configuration of total routes."""
        nr_of_connections_used = 0
        for connection in self._connections:
            if connection._used == True:
                nr_of_connections_used += 1
        fraction_used = nr_of_connections_used / len(self._connections)

        trajectories = len(self._routes)

        minutes = 0
        for route in self._routes:
            minutes += route.get_dist()

        return fraction_used * 10000 - (trajectories * 100 + minutes)