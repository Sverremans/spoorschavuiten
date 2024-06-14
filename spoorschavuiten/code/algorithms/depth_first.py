import copy


class DepthFirst:
    """
    A Depth First algorithm that builds a stack of regions with a unique assignment of routes for each instance.
    """
    def __init__(self, region) -> None:
        # sla beste regio met betreffende score op
        self._region = copy.deepcopy(region)
        self.best_solution = region
        self.best_score = region.calculate_value()

    def create_all_possible_regions(self):
    
    
    
    # creeer staten boom
    # neem eerste staat in de boom
    # vergelijk score van staat met beste staat
    # neem volgende staat in de boom


        
    