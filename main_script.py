from classes import Station
import pandas as pd

def load_data(stations_file: str, connections_file: str) -> list:
    stations = []

    # add stations with coordinates
    df_stations = pd.read_csv(stations_file)
    for l in range(len(df_stations)):
        new_station = Station(df_stations.loc[l, 'station'], df_stations.loc[l, 'x'], df_stations.loc[l, 'y'])
        stations.append(new_station)

    # add connections and distances
    df_connections = pd.read_csv(connections_file)
    for s in stations:
        for l in range(len(df_connections)):
            if s._name == df_connections.loc[l, 'station1']:
                s.add_connection(df_connections.loc[l, 'station2'], df_connections.loc[l, 'distance'])
            elif s._name == df_connections.loc[l, 'station2']:
                s.add_connection(df_connections.loc[l, 'station1'], df_connections.loc[l, 'distance'])

    return stations

if __name__ == "__main__":
    stations = load_data('csv_files/StationsHolland.csv', 'csv_files/ConnectiesHolland.csv')
    #print(stations[0]._name)

    # deze code berekent het maximale aantal verbindingen van een station
    #maximum_nr = 0
    #max_stat = ''
    #for s in stations:
    #    if len(s._connections) > maximum_nr:
    #        maximum_nr = len(s._connections)
    #        max_stat = s._name
    #print(maximum_nr)
    #print(max_stat)