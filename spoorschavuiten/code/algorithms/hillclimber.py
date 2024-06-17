import copy, random
from code.algorithms.greedy import Greedy

class HillClimber:
    def __init__(self, schedule, region, maxTrains, maxTime):
        # Maak een kopie van Schedule-object
        self._schedule = copy.deepcopy(schedule)
        # Bereken de doelfuntie
        self._value = schedule.calculate_value()
        self._region = region
        self._maxTrains = maxTrains
        self._maxTime = maxTime

    def mutate_train(self):
        # Plan een nieuwe trein in indien er nog sporen ongebruikt zijn
        unused_connections = []
        for connection in self._schedule._connections:
            if not connection._used:
                unused_connections.append(connection)

        if unused_connections:
            # starting_connection = random.choice(unused_connections)
            # print(starting_connection)
            # starting_station = random.choice([starting_connection._stationA, starting_connection._stationB])
            # print(starting_station)
            
            new_greedy = Greedy(self._schedule, 120, 1)
            new_greedy.run()
            new_greedy.generate_output()


    def mutate_schedule(self, nr_of_trains=1):
        # Verwijder n treinen
        if nr_of_trains > len(self._schedule._routes):
            nr_of_trains = len(self._schedule._routes)

        for _ in range(nr_of_trains):
            nr_of_routes = len(self._schedule._routes)
            remove = random.choice(range(nr_of_routes))

            time_remove = 0
            for connection in self._schedule._routes[remove]._route:
                time_remove += connection.get_dist()
            self._schedule._time_used -= time_remove

            self._schedule._routes.pop(remove)

        # Zet de booleans weer goed
        self.update_used_connections()

        # Doe n keer mutate_train()
        self.mutate_train()

    def update_used_connections(self):
        """Updates the 'used' boolean of connection"""
        used_connections = set()
        for route in self._schedule._routes:
            for connection in route._route:
                used_connections.add(connection)
        for connection in self._schedule._connections:
            if connection in used_connections:
                connection.is_used()
            else:
                connection.not_used()
            

    #def check_solution():
        # Vergelijk waarden doelfuncties
        # Sla nieuw Schedule op indien het beter is

    #def run(iterations, nr_of_trains=1):
        # Sla iterations op

        # Loop over de iterations
            # Doe mutate_schedule(nr_of_trains)
            # Doe check_solution()