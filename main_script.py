from classes import Station
import pandas as pd

if __name__ == "__main__":
    stations = []
    
    # add stations with coordinates
    df_stations = pd.read_csv('csv_files/StationsHolland.csv')
    for l in range(len(df_stations)):
        new_station = Station(df_stations.loc[l, 'station'], df_stations.loc[l, 'x'], df_stations.loc[l, 'y'])
        stations.append(new_station)

    # add connections and distances
    df_connections = pd.read_csv('csv_files/ConnectiesHolland.csv')
    for s in stations:
        for l in range(len(df_connections)):
            if s._name == df_connections.loc[l, 'station1']:
                s.add_connection(df_connections.loc[l, 'station2'], df_connections.loc[l, 'distance'])
            elif s._name == df_connections.loc[l, 'station2']:
                s.add_connection(df_connections.loc[l, 'station1'], df_connections.loc[l, 'distance'])