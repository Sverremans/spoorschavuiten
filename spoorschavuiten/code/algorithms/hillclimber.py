import copy, random
from code.algorithms.greedy import Greedy

# NOTE de theoretisch maximaal haalbare score is 1*10000 - (4 * 100 + 381) = 9219. Dit komt zeer in de buurt (9190).
# TODO kijk eens naar deze manual: https://realpython.com/python-property/

class HillClimber:
    def __init__(self, schedule, region, maxTrains, maxTime) -> None:
        # Maak een kopie van Schedule-object
        self._oldSchedule = schedule
        self._newSchedule = copy.deepcopy(schedule)
        # Bereken de doelfuntie
        self._value = schedule.calculate_value()
        self._region = region
        self._maxTrains = maxTrains
        self._maxTime = maxTime
        self.scores = []
        self.iterations = []

    def mutate_train(self) -> None:
        # Plan een nieuwe trein in indien er nog sporen ongebruikt zijn
        unused_connections = []
        for connection in self._newSchedule._connections:
            if not connection._used:
                unused_connections.append(connection)

        if unused_connections:
            new_greedy = Greedy(self._newSchedule, 120, 1)
            new_greedy.run()


    def mutate_schedule(self, nr_of_trains=1) -> None:
        # Verwijder n treinen
        if nr_of_trains > len(self._newSchedule._routes):
            nr_of_trains = len(self._newSchedule._routes)

        for _ in range(nr_of_trains):
            nr_of_routes = len(self._newSchedule._routes)
            remove = random.choice(range(nr_of_routes))

            time_remove = 0
            for connection in self._newSchedule._routes[remove]._route:
                time_remove += connection.get_dist()
            self._newSchedule._time_used -= time_remove

            self._newSchedule._routes.pop(remove)

        # Zet de booleans weer goed
        self.update_used_connections()

        # Doe n keer mutate_train()
        for _ in range(nr_of_trains):
            self.mutate_train()

    def update_used_connections(self) -> None:
        """Updates the 'used' boolean of connection"""
        used_connections = set()
        for route in self._newSchedule._routes:
            for connection in route._route:
                used_connections.add(connection)
        for connection in self._newSchedule._connections:
            if connection in used_connections:
                connection.is_used()
            else:
                connection.not_used()
            

    def check_solution(self) -> bool:
        # Vergelijk waarden doelfuncties
        calc_value = self._newSchedule.calculate_value()
        
        # Note that we allow equality to increase our chances of finding a better schedule later
        if calc_value >= self._value:
            # Sla nieuw Schedule op indien het beter is
            self._value = calc_value
            self._oldSchedule = self._newSchedule
            self._newSchedule = copy.deepcopy(self._oldSchedule)
            # print("Verbetering gevonden")
            return True
        return False

    def generate_output(self) -> None:
        self._newSchedule.generate_output()

    def run(self, iterations, nr_of_trains=1) -> None:
        # Sla iterations op
        self._iterations = iterations

        # Loop over de iterations
        for i in range(self._iterations):
            # Doe mutate_schedule(nr_of_trains)
            self.mutate_schedule(nr_of_trains)

            # Doe check_solution()
            if self.check_solution():
                self.scores.append(self._value)
                self.iterations.append(i + 1)

        # Set newSchedule to be the last improving solution
        self._newSchedule = self._oldSchedule