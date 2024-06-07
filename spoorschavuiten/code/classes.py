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

    def add_route(self, current_station):
        time = 0
        current_station = current_station
        route = Route()
        while time <= 120:
            possible_connections = []
            for connection in self._connections:
                if connection._stationA == current_station or connection._stationB == current_station:
                    possible_connections.append(connection)
            # choose randomly from possible connections
            connection = random.choice(possible_connections)
            route.add_station(connection)
<<<<<<< HEAD
            #current_station = connection
            #for connection in self._connections:
            #    if connection._stationA == current_station:
            #        route.add_station(connection)
            #        current_station = connection._stationB
            #        time += connection.get_dist()
            #    elif connection._stationB == current_station:
            #        route.add_station(connection)
=======
            current_station = connection
            for connection in self._connections:
                if connection._stationA == current_station:
                    route.add_station(connection)
                    current_station = connection._stationB
                    time += connection.get_dist()
                elif connection._stationB == current_station:
                    route.add_station(connection)
>>>>>>> b631c8243d16eff6c4b047273f340432ece561eb
        self._routes.append(route)
        return current_station

        


    def is_solution(self) -> bool:
        """Returns True if each connection is used, False otherwise."""
        for connection in self._connections:
            if not connection._used():
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

        minutes = 0
        for route in self._routes:
            minutes += route.get_dist()

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