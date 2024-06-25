from code.classes.classes import Route, Schedule
from code.algorithms.depth_first import DepthFirst
import copy
import time


class GreedyLookahead(DepthFirst):
    """
    A Greedy algorithm that searches through all possible configurations of a route and adds the highest scoring one to schedule, 
        but prunes the branch of configurations prematurely if after 'x' connections set a new one is not used.
    """

    def __init__(self, schedule: Schedule, maxTime: int, maxTrains: int, lookahead: int):
        super().__init__(schedule, maxTime, maxTrains)
        self.lookahead = lookahead

    def run(self) -> None:
        """
        Runs the algorithm.

        pre: self.schedule is an object of type Schedule and self.max_trains is a positive integer.
        post: adds routes to self.schedule. The amount depends on if all connections are set before self.max_trains.
        """
        step = 0
        start = time.time()

        # for each train find best route
        for _ in range(self.max_trains):

            # search for best route from all starting stations
            for station in self.schedule.stations.values():
                new_route = Route()
                new_route.current_station = station
                self.possible_routes.append(new_route)

                # for each possible starting position, visit all possible routes
                while self.possible_routes:
                    step += 1
                    print(f'Step {step}, current value: {self.best_score}, schedule: {len(self.schedule.routes)}')
                    new_route = self.get_next_state()
                    new_route = self.check_branch(new_route)
                    self.check_score(new_route)
                    current_station = new_route.current_station
                    self.build_children(new_route, current_station)

            # past this point best possible route to add to schedule is found
            print(f"passed this point. Best route is: {self.best_route.route}. Score: {self.best_score}")
            self.schedule.add_route(self.best_route)
            self.best_route = None
            self.best_score = 0

            # check if all connections are already used (so max overall score)
            scheduled_connections = {connection for route in self.schedule.routes for connection in route.route}
            if set(self.schedule.connections) == scheduled_connections:
                break
        
        end = time.time()
        print(f"Duration of algorithm in seconds: {end - start}")

    def check_branch(self, new_route: Route) -> Route:
        """
        If last 'x' additions on the route have not improved score, stop the branch and get next state. 
            Keep doing untill better route is found.

        pre: new_route is an object of type Route.
        post: returns an object of type Route or calls self.get_next_state() and calls itself again.
        """
        connections_used = [connection for connection in new_route.route]
        if len(connections_used) < self.lookahead or len(self.possible_routes) == 0:
            return new_route
        if self.schedule.routes:
            scheduled_connections = [connection for route in self.schedule.routes for connection in route.route]
        else:
            scheduled_connections = []

        not_improved = 0
        for i in range(self.lookahead):
            if i == 1:
                if connections_used[-i] in scheduled_connections or connections_used[-i] in connections_used[:-i]:
                    not_improved += 1
            else:
                if connections_used[-i] in scheduled_connections or connections_used[-i] in (connections_used[:-i] + connections_used[-i+1:]):
                    not_improved += 1

        # keep checking the next branch untill a good one is found
        if not_improved == self.lookahead:
            new_route = self.get_next_state()
            return self.check_branch(new_route)
        else:
            return new_route
