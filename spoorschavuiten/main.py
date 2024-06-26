import argparse
from code.classes.classes import Region, Schedule
from code.algorithms.random import Random, FixedRandom
from code.algorithms.greedy import Greedy, FixedGreedy, Termini_Greedy
from code.algorithms.greedy_lookahead import GreedyLookahead
from code.algorithms.hillclimber import HillClimber, HcStopCondition, Termini_HillClimber
from code.algorithms.depth_first import DepthFirst

if __name__ == "__main__":
    
    # Initialiseer de parser
    parser = argparse.ArgumentParser(description='runs the algorithm')
    parser.add_argument('-a', '--algorithm', type=str, default='HillClimber', choices=['Random', 'FixedRandom', 'Greedy', 'FixedGreedy', 'Termini_Greedy', 'GreedyLookAhead', 'HillClimber', 'HcStopCondition', 'Termini_HillClimber', 'DepthFirst'], help='choose between Random, FixedRandom, Greedy, FixedGreedy, Termini_Greedy, GreedyLookAhead, HillClimber, HcStopCondition, Termini_HillClimber, DepthFirst')
    parser.add_argument('-r', '--nr_of_runs', type=int, default=1, help='enter the number of runs')
    parser.add_argument('-s', '--seed', type=int, default=1234, help='enter a seed for fixed algorithms')
    parser.add_argument('-m', '--map', type=str, default='Holland', choices=['Holland', 'Nederland'], help='choose between Holland and Nederland')
    parser.add_argument('-tr', '--max_trains', type=int, help='enter the maximum number of trains')
    parser.add_argument('-ti', '--max_time', type=int, help='enter the maximum time in minutes for the length of each train path')
    parser.add_argument('-i', '--iterations', type=int, default=100000, help='enter the number of iterations for the hillclimber algorithms')
    parser.add_argument('-c', '--changes', type=int, default=2, help='enter the number of changes per iteration for the hillclimber algorithms')
    parser.add_argument('-ca', '--cap', type=int, default=50000, help='enter the cap for HcStopCondition')
    args = parser.parse_args()

    # Laad de data in
    holland = Region("data/input/StationsHolland.csv", "data/input/ConnectiesHolland.csv")
    nederland = Region("data/input/StationsNationaal.csv", "data/input/ConnectiesNationaal.csv")

    # Sla de command-line arguments op in variabelen
    algorithm = args.algorithm
    nr_of_runs = args.nr_of_runs
    seed = args.seed
    if args.map == 'Holland':
        map = holland
        # Zet de default constrains zoals in de opdracht
        max_trains = 7
        max_time = 120
    elif args.map == 'Nederland':
        map = nederland
        # Zet de default constrains zoals in de opdracht
        max_trains = 20
        max_time = 180
    iterations = args.iterations
    changes = args.changes
    cap = args.cap
    
    # Overschrijf de constraints indien gewenst
    if args.max_trains:
        max_trains = args.max_trains
    if args.max_time:
        max_time = args.max_time

    # TODO: doe hier if, elif, elif, etcetera
    if algorithm == 'Random':
        new_schedule = Schedule(map)
        random_schedule = Random(new_schedule, max_time, max_trains)
        random_schedule.run()
        random_schedule.generate_output()

    elif algorithm == 'FixedRandom':
        new_schedule = Schedule(map)
        fixed_random_schedule = FixedRandom(new_schedule, max_time, max_trains, seed)
        fixed_random_schedule.run()
        fixed_random_schedule.generate_output()
    
    elif algorithm == 'Greedy':
        new_schedule = Schedule(map)
        greedy_schedule = Greedy(new_schedule, max_time, max_trains)
        greedy_schedule.run()
        greedy_schedule.generate_output()
    
    elif algorithm == 'FixedGreedy':
        new_schedule = Schedule(map)
        fixed_greedy_schedule = FixedGreedy(new_schedule, max_time, max_trains, seed)
        fixed_greedy_schedule.run()
        fixed_greedy_schedule.generate_output()
    
    elif algorithm == 'Termini_Greedy':
        new_schedule = Schedule(map)
        termini_greedy_schedule = Termini_Greedy(new_schedule, max_time, max_trains)
        termini_greedy_schedule.run()
        termini_greedy_schedule.generate_output()
    
    elif algorithm == 'GreedyLookAhead':
        new_schedule = Schedule(map)
        greedy_lookahead_schedule = GreedyLookahead(new_schedule, max_time, max_trains, 3)
        greedy_lookahead_schedule.run()
        # TODO: wegschrijven
    
    elif algorithm == 'HillClimber':
        new_schedule = Schedule(map)
        random_schedule = Random(new_schedule, max_time, max_trains)
        random_schedule.run()
        for run_nr in range(nr_of_runs):
            hillclimber_schedule = HillClimber(new_schedule, max_trains, max_time)
            hillclimber_schedule.run(iterations, changes)
            hillclimber_schedule.generate_output()
    
    elif algorithm == 'HcStopCondition':
        new_schedule = Schedule(map)
        random_schedule = Random(new_schedule, max_time, max_trains)
        random_schedule.run()
        for run_nr in range(nr_of_runs):
            hcstopcondition_schedule = HcStopCondition(new_schedule, max_time, max_trains, cap)
            hcstopcondition_schedule.run(iterations, changes)
            hcstopcondition_schedule.generate_output()
    
    elif algorithm == 'Termini_HillClimber':
        new_schedule = Schedule(map)
        random_schedule = Random(new_schedule, max_time, max_trains)
        random_schedule.run()
        for run_nr in range(nr_of_runs):
            termini_hillclimber_schedule = Termini_HillClimber(new_schedule, max_trains, max_time)
            termini_hillclimber_schedule.run(iterations, changes)
            termini_hillclimber_schedule.generate_output()
    
    elif algorithm == 'DepthFirst':
        new_schedule = Schedule(map)
        depthfirst_schedule = DepthFirst(new_schedule, max_time, max_trains)
        depthfirst_schedule.run()
        # TODO: wegschrijven