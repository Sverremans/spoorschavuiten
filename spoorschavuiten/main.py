import argparse
from code.classes.classes import Region, Schedule
from code.algorithms.random import Random, FixedRandom
from code.algorithms.greedy import Greedy, FixedGreedy, Termini_Greedy
from code.algorithms.greedy_lookahead import GreedyLookahead
from code.algorithms.hillclimber import HillClimber, HcStopCondition, Termini_HillClimber
from code.algorithms.depth_first import DepthFirst
from code.visualization.visualize import *

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

    # Voer het gekozen algoritme uit
    if algorithm == 'Random':
        for run_nr in range(nr_of_runs):
            new_schedule = Schedule(map)
            random_schedule = Random(new_schedule, max_time, max_trains)
            random_schedule.run()

            outputToFile(new_schedule, f'Random {args.map} run number {run_nr + 1}', f'data/output/random/random_{args.map}_output.csv')
            routesToFile(new_schedule, f'Random {args.map} run number {run_nr + 1}', f'data/output/random/random_{args.map}_routes.csv')
            scoresToFile(new_schedule, run_nr, f'data/output/random/random_{args.map}_scores.csv')


    elif algorithm == 'FixedRandom':
        for run_nr in range(nr_of_runs):
            new_schedule = Schedule(map)
            fixed_random_schedule = FixedRandom(new_schedule, max_time, max_trains, seed)
            fixed_random_schedule.run()

            outputToFile(new_schedule, f'FixedRandom {args.map} run number {run_nr + 1}', f'data/output/random/fixedrandom_{args.map}_output.csv')
            routesToFile(new_schedule, f'FixedRandom {args.map} run number {run_nr + 1}', f'data/output/random/fixedrandom_{args.map}_routes.csv')
            scoresToFile(new_schedule, run_nr, f'data/output/random/fixedrandom_{args.map}_scores.csv')
    
    elif algorithm == 'Greedy':
        for run_nr in range(nr_of_runs):
            new_schedule = Schedule(map)
            greedy_schedule = Greedy(new_schedule, max_time, max_trains)
            greedy_schedule.run()

            outputToFile(new_schedule, f'Greedy {args.map} run number {run_nr + 1}', f'data/output/greedy/greedy_{args.map}_output.csv')
            routesToFile(new_schedule, f'Greedy {args.map} run number {run_nr + 1}', f'data/output/greedy/greedy_{args.map}_routes.csv')
            scoresToFile(new_schedule, run_nr, f'data/output/greedy/greedy_{args.map}_scores.csv')
    
    elif algorithm == 'FixedGreedy':
        for run_nr in range(nr_of_runs):
            new_schedule = Schedule(map)
            fixed_greedy_schedule = FixedGreedy(new_schedule, max_time, max_trains, seed)
            fixed_greedy_schedule.run()

            outputToFile(new_schedule, f'FixedGreedy {args.map} run number {run_nr + 1}', f'data/output/greedy/fixedgreedy_{args.map}_output.csv')
            routesToFile(new_schedule, f'FixedGreedy {args.map} run number {run_nr + 1}', f'data/output/greedy/fixedgreedy_{args.map}_routes.csv')
            scoresToFile(new_schedule, run_nr, f'data/output/greedy/fixedgreedy_{args.map}_scores.csv')
        
    elif algorithm == 'Termini_Greedy':
        for run_nr in range(nr_of_runs):
            new_schedule = Schedule(map)
            termini_greedy_schedule = Termini_Greedy(new_schedule, max_time, max_trains)
            termini_greedy_schedule.run()

            outputToFile(new_schedule, f'Termini_Greedy {args.map} run number {run_nr + 1}', f'data/output/greedy/termini_greedy_{args.map}_output.csv')
            routesToFile(new_schedule, f'Termini_Greedy {args.map} run number {run_nr + 1}', f'data/output/greedy/termini_greedy_{args.map}_routes.csv')
            scoresToFile(new_schedule, run_nr, f'data/output/greedy/termini_greedy_{args.map}_scores.csv')
    
    elif algorithm == 'GreedyLookAhead':
        for run_nr in range(nr_of_runs):
            new_schedule = Schedule(map)
            greedy_lookahead_schedule = GreedyLookahead(new_schedule, max_time, max_trains, 3)
            greedy_lookahead_schedule.run()
            
            outputToFile(new_schedule, f'GreedyLookAhead {args.map} run number {run_nr + 1}', f'data/output/greedy_lookahead/greedylookahead_{args.map}_output.csv')
            routesToFile(new_schedule, f'GreedyLookAhead {args.map} run number {run_nr + 1}', f'data/output/greedy_lookahead/greedylookahead_{args.map}_routes.csv')
            scoresToFile(new_schedule, run_nr, f'data/output/greedy_lookahead/greedylookahead_{args.map}_scores.csv')
    
    elif algorithm == 'HillClimber':
        for run_nr in range(nr_of_runs):
            new_schedule = Schedule(map)
            random_schedule = Random(new_schedule, max_time, max_trains)
            random_schedule.run()
            hillclimber_schedule = HillClimber(new_schedule, max_trains, max_time)
            hillclimber_schedule.run(iterations, changes)

            outputToFile(new_schedule, f'HillClimber {args.map} run number {run_nr + 1}', f'data/output/hillclimber/hillclimber_{args.map}_output.csv')
            routesToFile(new_schedule, f'HillClimber {args.map} run number {run_nr + 1}', f'data/output/hillclimber/hillclimber_{args.map}_routes.csv')
            scoresToFile(new_schedule, run_nr, f'data/output/hillclimber/hillclimber_{args.map}_scores.csv')
    
    elif algorithm == 'HcStopCondition':
        for run_nr in range(nr_of_runs):
            new_schedule = Schedule(map)
            random_schedule = Random(new_schedule, max_time, max_trains)
            random_schedule.run()
            hcstopcondition_schedule = HcStopCondition(new_schedule, max_time, max_trains, cap)
            hcstopcondition_schedule.run(iterations, changes)

            outputToFile(new_schedule, f'HcStopCondition {args.map} run number {run_nr + 1}', f'data/output/hillclimber/hcstopcondition_{args.map}_output.csv')
            routesToFile(new_schedule, f'HcStopCondition {args.map} run number {run_nr + 1}', f'data/output/hillclimber/hcstopcondition_{args.map}_routes.csv')
            scoresToFile(new_schedule, run_nr, f'data/output/hillclimber/hcstopcondition_{args.map}_scores.csv')
    
    elif algorithm == 'Termini_HillClimber':
        for run_nr in range(nr_of_runs):
            new_schedule = Schedule(map)
            random_schedule = Random(new_schedule, max_time, max_trains)
            random_schedule.run()
            termini_hillclimber_schedule = Termini_HillClimber(new_schedule, max_trains, max_time)
            termini_hillclimber_schedule.run(iterations, changes)

            outputToFile(new_schedule, f'Termini_HillClimber {args.map} run number {run_nr + 1}', f'data/output/hillclimber/termini_hillclimber_{args.map}_output.csv')
            routesToFile(new_schedule, f'Termini_HillClimber {args.map} run number {run_nr + 1}', f'data/output/hillclimber/termini_hillclimber_{args.map}_routes.csv')
            scoresToFile(new_schedule, run_nr, f'data/output/hillclimber/termini_hillclimber_{args.map}_scores.csv')
    
    elif algorithm == 'DepthFirst':
        for run_nr in range(nr_of_runs):
            new_schedule = Schedule(map)
            depthfirst_schedule = DepthFirst(new_schedule, max_time, max_trains)
            depthfirst_schedule.run()
            
            outputToFile(new_schedule, f'DepthFirst {args.map} run number {run_nr + 1}', f'data/output/depthfirst/depthfirst_{args.map}_output.csv')
            routesToFile(new_schedule, f'DepthFirst {args.map} run number {run_nr + 1}', f'data/output/depthfirst/depthfirst_{args.map}_routes.csv')
            scoresToFile(new_schedule, run_nr, f'data/output/depthfirst/depthfirst_{args.map}_scores.csv')