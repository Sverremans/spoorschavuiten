import pandas as pd # type: ignore


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
    
    # added to fix depth_first score getting method
    def __eq__(self, other):
        if isinstance(other, Connection):
            return self._stationA._name == other._stationA._name and self._stationB._name == other._stationB._name
        else:
            return False
    
    def __hash__(self):
        return hash(self.__repr__())


class Route:
    """Traject van connecties waar een trein langs komt."""
    def __init__(self) -> None:
        self._route: list[Connection] = []
        self._stations: list[Station] = []
        self.time = 0
        self.current_station = None
    
    def add_time(self, extraTime):
        self.time += extraTime

    def subtract_time(self, extraTime):
        self.time -= extraTime
    
    def add_connection(self, connection) -> None:
        self._route.append(connection)

    def add_station(self, station) -> None:
        self._stations.append(station)

    def get_dist(self) -> int:
        dist = 0
        for connection in self._route:
            dist += connection.get_dist()
        return dist


class Schedule:
    """Maakt lijnvoering voor de regio"""
    def __init__(self, region) -> None:
        self._routes: list[Route] = []
        self._time_used: int = 0
        self._stations: dict[str, Station] = region._stations
        self._connections: list[Connection] = self.clear_connections(region)
    
    def clear_connections(self, region) -> list[Connection]:
        for connection in region._connections:
            connection._used = False
        return region._connections
    
    def add_route(self, route) -> None:
        self._routes.append(route)

    def update_time(self, time) -> None:
        self._time_used += time

    def is_solution(self) -> bool:
        """Returns True if each connection is used, False otherwise."""
        for connection in self._connections:
            if not connection._used:
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
        print("train,stations")
        for i, route in enumerate(self._routes, 1):
            print(f'train_{i},"{route._stations}"')
        print(f"score,{self.calculate_value()}")


class Region:
    """Regio van stations en verbindingen waarin routes lopen."""
    def __init__(self, stations_file: str, connections_file: str) -> None:
        self._stations: dict[str, Station] = self.load_stations(stations_file)
        self._connections: list[Connection] = self.load_connections(connections_file)

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
