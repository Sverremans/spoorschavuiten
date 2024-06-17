import copy

class HillClimber:
    def __init__(self, schedule):
        # Maak een kopie van Schedule-object
        self._schedule = copy.deepcopy(schedule)
        # Bereken de doelfuntie

    #def mutate_train():
        # Plan een nieuwe trein in indien er nog sporen ongebruikt zijn

    #def mutate_schedule(nr_of_trains=1):
        # Verwijder n treinen
        # Doe n keer mutate_train()

    #def check_solution():
        # Vergelijk waarden doelfuncties
        # Sla nieuw Schedule op indien het beter is

    #def run(iterations, nr_of_trains=1):
        # Sla iterations op

        # Loop over de iterations
            # Doe mutate_schedule(nr_of_trains)
            # Doe check_solution()