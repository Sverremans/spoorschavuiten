import pandas as pd # type: ignore
import functools


class Station:
    '''
    Every station has a name, an x coodinate and an y coordinate.
    These coordinates are used to draw a map of all the stations.
    '''
    def __init__(self, name: str, x: float, y: float) -> None:
        self._name = name
        self._x = x
        self._y = y

    def __repr__(self) -> str:
        return self._name


class Connection:
    '''
    A connection has the attributes to show the two stations the connection is in between.
    A station A and a station B. The dist variable is the distance in minutes between the two stations.
    The last attribute is a boolean, this states if the connections is used or not.

    Pre: It needs two stations and the distance between those station for the object to be made.
    '''
    def __init__(self, stationA: Station, stationB: Station, dist: int) -> None:
        self.stationA = stationA
        self.stationB = stationB
        self._dist = dist
        self.used: bool = False
        self._repr = f"{self.stationA} naar {self.stationB}"

    def get_dist(self) -> int:
        return self._dist

    def is_used(self) -> None:
        self.used = True

    def not_used(self) -> None:
        self.used = False
    
    def __repr__(self) -> str:
        return self._repr
    
    # added to fix depth_first score getting method
    def __eq__(self, other) -> bool:
        if isinstance(other, Connection):
            return self.stationA._name == other.stationA._name and self.stationB._name == other.stationB._name
        else:
            return False
    
    def __hash__(self):
        return hash(self.__repr__())


class Route:
    '''
    A Route object contains a list of the different connections used for one train.
    It also saves the stations it passed on the route in another list
    Lastly it counts the duration of the different connections.
    '''
    def __init__(self) -> None:
        self.route: list[Connection] = []
        self.stations: list[Station] = []
        self.time = 0
        self.current_station = None
    
    def add_time(self, extraTime) -> None:
        self.time += extraTime

    def subtract_time(self, extraTime) -> None:
        self.time -= extraTime
    
    def add_connection(self, connection) -> None:
        self.route.append(connection)

    def add_station(self, station) -> None:
        self.stations.append(station)

    def get_dist(self) -> int:
        dist = 0
        for connection in self.route:
            dist += connection.get_dist()
        return dist


class Schedule:
    '''
    In Schedule there is a list that contains all the routes that are made by an algorithm, these routes are Route objects.
    Schedule keeps a note of all the time passed over all te routes in the list.
    

    Pre: Schedule needs a region to make new routes in.
    '''
    def __init__(self, region) -> None:
        self.routes: list[Route] = []
        self._time_used: int = 0
        self.stations: dict[str, Station] = region.stations
        self.connections: list[Connection] = self.clear_connections(region)
    
    def clear_connections(self, region) -> list[Connection]:
        for connection in region.connections:
            connection.used = False
        return region.connections
    
    def add_route(self, route) -> None:
        self.routes.append(route)

    def update_time(self, time) -> None:
        self._time_used += time

    def is_solution(self) -> bool:
        """Returns True if each connection is used, False otherwise."""
        for connection in self.connections:
            if not connection.used:
                return False
        return True
    
    def calculate_value(self) -> int:
        """Calculates value of configuration of total routes."""      
        nr_of_connections_used = 0

        for connection in self.connections:
            if connection.used == True:
                nr_of_connections_used += 1
        fraction_used = nr_of_connections_used / len(self.connections)
        
        trajectories = len(self.routes)
        
        minutes = self._time_used

        return fraction_used * 10000 - (trajectories * 100 + minutes)
    
    def generate_output(self) -> None:
        print("train,stations")
        for i, route in enumerate(self.routes, 1):
            print(f'train_{i},"{route.stations}"')
        print(f"score,{self.calculate_value()}")

    @functools.cache
    def get_connections(self, current_station: Station) -> list[tuple[Connection, str]]:
        possible_connections = []
        
        for connection in self.connections:
            if connection.stationA == current_station:
                possible_connections.append((connection, "f"))
            if connection.stationB == current_station:
                possible_connections.append((connection, "b"))
        
        return possible_connections


class Region:
    """Regio van stations en verbindingen waarin routes lopen."""
    def __init__(self, stations_file: str, connections_file: str) -> None:
        self.stations: dict[str, Station] = self.load_stations(stations_file)
        self.connections: list[Connection] = self.load_connections(connections_file)

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
            stationA = self.stations[df_connections.loc[l, 'station1']]
            stationB = self.stations[df_connections.loc[l, 'station2']]
            new_connection = Connection(stationA, stationB, df_connections.loc[l, 'distance'])
            connections.append(new_connection)

        return connections
