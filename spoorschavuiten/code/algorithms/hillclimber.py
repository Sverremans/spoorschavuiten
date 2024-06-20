import copy, random
from code.algorithms.greedy import Greedy
from code.classes.classes import Schedule

# NOTE de theoretisch maximaal haalbare score is 1*10000 - (4 * 100 + 381) = 9219 -> 9214 misschien mogelijk (-5). 
# Dit komt zeer in de buurt (9202).
# NOTE voor Nederland is dit 7549.
# TODO kijk eens naar deze manual: https://realpython.com/python-property/

class HillClimber:
    """
    Neemt een ingevulde dienstregeling en plant steeds n treinen opnieuw in.
    Slaat verbeteringen op en gooit verslechteringen weg.
    """
    def __init__(self, schedule: Schedule, maxTrains: int, maxTime: int) -> None:
        # Maak een kopie van Schedule-object
        self._oldSchedule = schedule
        self.newSchedule = copy.deepcopy(schedule)
        # Bereken de doelfuntie
        self._value = schedule.calculate_value()
        self._maxTrains = maxTrains
        self._maxTime = maxTime
        
        self.scores = [schedule.calculate_value()]
        self.iterations_list = []
        self.scoresPoints = []
        self.iterations_listPoints = []

    def mutate_train(self) -> None:
        # Plan een nieuwe trein in indien er nog sporen ongebruikt zijn
        unused_connections = []
        for connection in self.newSchedule.connections:
            if not connection.used:
                unused_connections.append(connection)

        if unused_connections:
            new_greedy = Greedy(self.newSchedule, 120, 1)
            new_greedy.run()

    def mutate_schedule(self, nr_of_trains=1) -> None:
        # Verwijder n treinen
        if nr_of_trains > len(self.newSchedule.routes):
            nr_of_trains = len(self.newSchedule.routes)

        for _ in range(nr_of_trains):
            nr_of_routes = len(self.newSchedule.routes)
            remove = random.choice(range(nr_of_routes))

            # Trek minuten van te verwijderen trajecten van totaal af
            for connection in self.newSchedule.routes[remove].route:
                self.newSchedule._time_used -= connection.get_dist()

            self.newSchedule.routes.pop(remove)

        # Zet de booleans weer goed
        self.update_used_connections()

        # Doe n keer mutate_train()
        for _ in range(nr_of_trains):
            self.mutate_train()

    def update_used_connections(self) -> None:
        """Updates the 'used' boolean of connection"""
        used_connections = []
        for route in self.newSchedule.routes:
            for connection in route.route:
                used_connections.append(connection)
        for connection in self.newSchedule.connections:
            if connection in used_connections:
                connection.is_used()
            else:
                connection.not_used()
            
    def check_solution(self) -> bool:
        # Vergelijk waarden doelfuncties
        calc_value = self.newSchedule.calculate_value()
        
        # Note that we allow equality to increase our chances of finding a better schedule later
        if calc_value >= self._value:
            # Sla nieuw Schedule op indien het beter is
            self._value = calc_value
            self._oldSchedule = self.newSchedule
            self.newSchedule = copy.deepcopy(self._oldSchedule)
            return True
        return False

    def generate_output(self) -> None:
        self.newSchedule.generate_output()

    def run(self, iterations: int, nr_of_trains: int = 1) -> None:
        # Sla iterations op
        self._iterations = iterations

        # Loop over de iterations
        for i in range(self._iterations):
            # Doe mutate_schedule(nr_of_trains)
            self.mutate_schedule(nr_of_trains)

            # TODO: lees over generators https://realpython.com/introduction-to-python-generators/
            # Doe check_solution()
            if self.check_solution():
                self.scores.append(self._value)
                self.scores.append(self._value)
                self.iterations_list.append(i + 1)
                self.iterations_list.append(i + 1)

                self.scoresPoints.append(self._value)
                self.iterations_listPoints.append(i + 1)

        self.iterations_list.append(self._iterations)

        # Set newSchedule to be the last improving solution
        self.newSchedule = self._oldSchedule


class HcStopCondition(HillClimber):
    """
    Laat Hill Climber stoppen als er na een vast aantal iteraties geen verbetering is gevonden
    """
    def __init__(self, schedule: Schedule, maxTime: int, maxTrains: int, cap: int = 100000) -> None:
        # Maak een kopie van Schedule-object
        self._oldSchedule = schedule
        self.newSchedule = copy.deepcopy(schedule)
        # Bereken de doelfuntie
        self._value = schedule.calculate_value()
        self._maxTrains = maxTrains
        self._maxTime = maxTime

        self._cap = cap
        
        self.scores = [schedule.calculate_value()]
        self.iterations_list = []
        self.scoresPoints = []
        self.iterations_listPoints = []

    def run(self, iterations: int, nr_of_trains: int = 1) -> None:
        # Sla iterations op
        self._iterations = iterations

        # Initialiseer stopconditie
        no_improvement_counter = 0

        # Loop over de iterations
        for i in range(self._iterations):
            # Stop als er geen verbetering is na 100000 iteraties
            if no_improvement_counter >= self._cap:
                break
            
            # Doe mutate_schedule(nr_of_trains)
            self.mutate_schedule(nr_of_trains)

            # TODO: lees over generators https://realpython.com/introduction-to-python-generators/
            # Doe check_solution()
            if self.check_solution():
                self.scores.append(self._value)
                self.scores.append(self._value)
                self.iterations_list.append(i + 1)
                self.iterations_list.append(i + 1)

                self.scoresPoints.append(self._value)
                self.iterations_listPoints.append(i + 1)

                no_improvement_counter = 0
            else:
                no_improvement_counter += 1

        self.iterations_list.append(self._iterations)

        # Set newSchedule to be the last improving solution
        self.newSchedule = self._oldSchedule