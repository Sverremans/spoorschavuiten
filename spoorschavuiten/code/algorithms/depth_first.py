import copy


class DepthFirst:
    """
    A Depth First algorithm that builds a stack of regions with a unique assignment of routes for each instance.
    """
    def __init__(self, schedule) -> None:
        # sla beste schedule met betreffende score op
        self._stack = []
        self.best_solution = schedule
        self.best_score = schedule.calculate_value()

    def create_all_possible_schedules(self):
        # creeer staten boom

    
    
        # neem eerste staat in de boom
        next_schedule = self._stack.pop()

        # vergelijk score van staat met beste staat
        if next_schedule.calculate_value() > 
        # neem volgende staat in de boom

class DepthFirst:
    """
    A Depth First algorithm that builds a stack of schedules with a unique assignment of routes for each instance.
    """
    def __init__(self, schedule) -> None:
        # initialiseer lijst van mogelijke schedules
        # sla beste schedule met betreffende score op

    def create_all_possible_schedules(self):
        # creeer staten boom en voeg toe aan lijst

    def get_next_schedule(self:)
        # neem eerste staat in de boom

    def check_scores(self:)
        # vergelijk score van staat met beste staat
        # sla de beste op

    def run(self):
        # create_all_possible_schedules()
        # totdat de lijst met schedules leeg is doe:
            # get_next_schedule()
            # check_scores()
