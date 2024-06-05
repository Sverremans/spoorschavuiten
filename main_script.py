from classes import Station
from classes import Connection
import pandas as pd

def load_stations(stations_file: str) -> list:
    stations = []

    # add stations with coordinates
    df_stations = pd.read_csv(stations_file)
    for l in range(len(df_stations)):
        new_station = Station(df_stations.loc[l, 'station'], df_stations.loc[l, 'x'], df_stations.loc[l, 'y'])
        stations.append(new_station)

    return stations

def load_connections(connections_file: str) -> list:
    connections = []

    # add connections and distances
    df_connections = pd.read_csv(connections_file)
    for l in range(len(df_connections)):
        new_connection = Connection(df_connections.loc[l, 'station1'], df_connections.loc[l, 'station2'], df_connections.loc[l, 'distance'])
        connections.append(new_connection)

    return connections

if __name__ == "__main__":
    stations = load_stations('csv_files/StationsHolland.csv')
    connections = load_connections('csv_files/ConnectiesHolland.csv')
    for s in stations:
        print(s._name)
    for c in connections:
        print(c._stationA + " is verbonden met " + c._stationB + " in " + str(c._dist) + " minuten.")