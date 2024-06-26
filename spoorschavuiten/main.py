import argparse
from code.classes.classes import Region, Schedule
from code.algorithms.random import Random, FixedRandom
from code.algorithms.greedy import Greedy, FixedGreedy, termini_Greedy
from code.algorithms.greedy_lookahead import GreedyLookahead
from code.algorithms.hillclimber import HillClimber, HcStopCondition, termini_HillClimber
from code.algorithms.depth_first import DepthFirst

if __name__ == "__main__":
    
    # Initialiseer de parser
    parser = argparse.ArgumentParser(description='runs the algorithm')
    parser.add_argument('-a', '--algorithm', type=str, default='HillClimber', choices=['Random', 'FixedRandom', 'Greedy', 'FixedGreedy', 'termini_Greedy', 'GreedyLookahead', 'HillClimber', 'hcStopCondition', 'termini_HillClimber', 'DepthFirst'], help='choose between Random, FixedRandom, Greedy, FixedGreedy, termini_Greedy, GreedyLookahead, HillClimber, hcStopCondition, termini_HillClimber, DepthFirst')
    parser.add_argument('-r', '--nr_of_runs', type=int, default=1, help='enter the number of runs')
    args = parser.parse_args()

    # Laad de data in
    holland = Region("data/StationsHolland.csv", "data/ConnectiesHolland.csv")
    nederland = Region("data/StationsNationaal.csv", "data/ConnectiesNationaal.csv")

    algorithm = args.algorithm
    nr_of_runs = args.nr_of_runs

    max_trains = 7
    max_time = 120

    # TODO: doe hier if, elif, elif, etcetera
    if algorithm == 'Random':
        new_schedule = Schedule(holland)
        random_schedule = Random(new_schedule, max_time, max_trains)
        random_schedule.run()
        random_schedule.generate_output()
    elif algorithm == 'FixedRandom':
        pass
    elif algorithm == 'Greedy':
        pass
    elif algorithm == 'FixedGreedy':
        pass
    elif algorithm == 'termini_Greedy':
        pass
    elif algorithm == 'GreedyLookAhead':
        pass
    elif algorithm == 'HillClimber':
        pass
    elif algorithm == 'hcStopCondition':
        pass
    elif algorithm == 'termini_HillClimber':
        pass
    elif algorithm == 'DepthFirst':
        pass