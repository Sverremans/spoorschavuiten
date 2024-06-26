import copy, random
from code.algorithms.greedy import Greedy, Termini_Greedy
from code.classes.classes import Schedule


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
        
        self.scores = []
        self.iterations_list = [0]
        self.scoresPoints = []
        self.iterations_listPoints = [0]

    def mutate_train(self) -> None:
        # Plan een nieuwe trein in indien er nog sporen ongebruikt zijn
        unused_connections = []
        for connection in self.newSchedule.connections:
            if not connection.used:
                unused_connections.append(connection)

        if unused_connections:
            new_greedy = Greedy(self.newSchedule, 120, 1)
            new_greedy.run()

    def mutate_schedule(self, nr_of_trains: int = 1) -> None:
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
        """Update de 'used' boolean van connection"""
        used_connections = set()
        for route in self.newSchedule.routes:
            for connection in route.route:
                used_connections.add(connection)
        for connection in self.newSchedule.connections:
            if connection in used_connections:
                connection.is_used()
            else:
                connection.not_used()
            
    def check_solution(self) -> bool:
        # Vergelijk waarden doelfuncties
        calc_value = self.newSchedule.calculate_value()
        
        # Merk op dat we gelijkheden toestaan om onze kans later een betere dienstregeling te vinden laten toenemen
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

            # Doe check_solution()
            if self.check_solution():
                self.scores.append(self._value)
                self.scores.append(self._value)
                self.iterations_list.append(i + 1)
                self.iterations_list.append(i + 1)

                self.scoresPoints.append(self._value)
                self.iterations_listPoints.append(i + 1)

        self.iterations_list.append(self.iterations_list[-1])
        self.scoresPoints.append(self.scoresPoints[-1])
        self.scores.append(self.scores[-1])

        # Laat newSchedule de laatste verbeterde oplossing zijn
        self.newSchedule = self._oldSchedule


class HcStopCondition(HillClimber):
    """
    Laat Hill Climber stoppen als er na een vast aantal iteraties geen verbetering is gevonden.
    """
    def __init__(self, schedule: Schedule, maxTime: int, maxTrains: int, cap: int = 100000) -> None:
        super().__init__(schedule, maxTrains, maxTime)
        self._cap = cap

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

        self.iterations_list.append(self.iterations_list[-1])
        self.scoresPoints.append(self.scoresPoints[-1])
        self.scores.append(self.scores[-1])

        # Laat newSchedule de laatste verbeterde oplossing zijn
        self.newSchedule = self._oldSchedule


class Termini_HillClimber(HillClimber):
    """
    Variatie van Hillclimber waarbij een Termini Greedy algoritme wordt gebruikt bij
    het inplannen van een nieuwe trein i.p.v. een Greedy.
    """
    # NOTE: dit geeft een lagere score dan reguliere Hill Climber
    def mutate_train(self) -> None:
        # Plan een nieuwe trein in indien er nog sporen ongebruikt zijn
        unused_connections = []
        for connection in self.newSchedule.connections:
            if not connection.used:
                unused_connections.append(connection)

        if unused_connections:
            new_greedy = Termini_Greedy(self.newSchedule, 120, 1)
            new_greedy.run()
