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
    parser.add_argument('-a', '--algorithm', type=str, default='HillClimber', choices=['Random', 'FixedRandom', 'Greedy', 'FixedGreedy', 'Termini_Greedy', 'GreedyLookAhead', 'HillClimber', 'HcStopCondition', 'Termini_HillClimber', 'DepthFirst'], help='Choose between Random, FixedRandom, Greedy, FixedGreedy, Termini_Greedy, GreedyLookAhead, HillClimber, HcStopCondition, Termini_HillClimber, DepthFirst. Chooses HillClimber by default.')
    parser.add_argument('-n', '--nr_of_runs', type=int, default=1, help='Enter the number of runs. Chooses 1 by default.')
    parser.add_argument('-s', '--seed', type=int, default=1234, help='Enter a seed for fixed algorithms. Chooses 1234 by default.')
    parser.add_argument('-r', '--railmap', type=str, default='Holland', choices=['Holland', 'Nederland'], help='Choose between Holland and Nederland. Chooses Holland by default.')
    parser.add_argument('-tr', '--max_trains', type=int, help='Enter the maximum number of trains. Chooses 7 for Holland and 20 for Nederland by default.')
    parser.add_argument('-ti', '--max_time', type=int, help='Enter the maximum time in minutes for the length of each train path. Chooses 120 for Holland and 180 for Nederland by default.')
    parser.add_argument('-i', '--iterations', type=int, default=100000, help='Enter the number of iterations for the hillclimber algorithms. Chooses 100000 by default.')
    parser.add_argument('-c', '--changes', type=int, default=2, help='Enter the number of changes per iteration for the hillclimber algorithms. Chooses 2 by default.')
    parser.add_argument('-ca', '--cap', type=int, default=50000, help='Enter the cap for HcStopCondition. Chooses 50000 by default.')
    args = parser.parse_args()

    # Laad de data in
    holland = Region("data/input/StationsHolland.csv", "data/input/ConnectiesHolland.csv")
    nederland = Region("data/input/StationsNationaal.csv", "data/input/ConnectiesNationaal.csv")

    # Sla de command-line arguments op in variabelen
    algorithm = args.algorithm
    nr_of_runs = args.nr_of_runs
    seed = args.seed
    if args.railmap == 'Holland':
        railmap = holland
        # Zet de default constrains zoals in de opdracht
        max_trains = 7
        max_time = 120
    elif args.railmap == 'Nederland':
        railmap = nederland
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
            new_schedule = Schedule(railmap)
            random_schedule = Random(new_schedule, max_time, max_trains)
            random_schedule.run()

            outputToFile(new_schedule, f'Random {args.railmap} run number {run_nr + 1}', f'data/output/random/random_{args.railmap}_output.csv')
            routesToFile(new_schedule, f'Random {args.railmap} run number {run_nr + 1}', f'data/output/random/random_{args.railmap}_routes.csv')
            scoresToFile(new_schedule, run_nr, f'data/output/random/random_{args.railmap}_scores.csv')


    elif algorithm == 'FixedRandom':
        for run_nr in range(nr_of_runs):
            new_schedule = Schedule(railmap)
            fixed_random_schedule = FixedRandom(new_schedule, max_time, max_trains, seed)
            fixed_random_schedule.run()

            outputToFile(new_schedule, f'FixedRandom {args.railmap} run number {run_nr + 1}', f'data/output/random/fixedrandom_{args.railmap}_output.csv')
            routesToFile(new_schedule, f'FixedRandom {args.railmap} run number {run_nr + 1}', f'data/output/random/fixedrandom_{args.railmap}_routes.csv')
            scoresToFile(new_schedule, run_nr, f'data/output/random/fixedrandom_{args.railmap}_scores.csv')
    
    elif algorithm == 'Greedy':
        for run_nr in range(nr_of_runs):
            new_schedule = Schedule(railmap)
            greedy_schedule = Greedy(new_schedule, max_time, max_trains)
            greedy_schedule.run()

            outputToFile(new_schedule, f'Greedy {args.railmap} run number {run_nr + 1}', f'data/output/greedy/greedy_{args.railmap}_output.csv')
            routesToFile(new_schedule, f'Greedy {args.railmap} run number {run_nr + 1}', f'data/output/greedy/greedy_{args.railmap}_routes.csv')
            scoresToFile(new_schedule, run_nr, f'data/output/greedy/greedy_{args.railmap}_scores.csv')
    
    elif algorithm == 'FixedGreedy':
        for run_nr in range(nr_of_runs):
            new_schedule = Schedule(railmap)
            fixed_greedy_schedule = FixedGreedy(new_schedule, max_time, max_trains, seed)
            fixed_greedy_schedule.run()

            outputToFile(new_schedule, f'FixedGreedy {args.railmap} run number {run_nr + 1}', f'data/output/greedy/fixedgreedy_{args.railmap}_output.csv')
            routesToFile(new_schedule, f'FixedGreedy {args.railmap} run number {run_nr + 1}', f'data/output/greedy/fixedgreedy_{args.railmap}_routes.csv')
            scoresToFile(new_schedule, run_nr, f'data/output/greedy/fixedgreedy_{args.railmap}_scores.csv')
        
    elif algorithm == 'Termini_Greedy':
        for run_nr in range(nr_of_runs):
            new_schedule = Schedule(railmap)
            termini_greedy_schedule = Termini_Greedy(new_schedule, max_time, max_trains)
            termini_greedy_schedule.run()

            outputToFile(new_schedule, f'Termini_Greedy {args.railmap} run number {run_nr + 1}', f'data/output/greedy/termini_greedy_{args.railmap}_output.csv')
            routesToFile(new_schedule, f'Termini_Greedy {args.railmap} run number {run_nr + 1}', f'data/output/greedy/termini_greedy_{args.railmap}_routes.csv')
            scoresToFile(new_schedule, run_nr, f'data/output/greedy/termini_greedy_{args.railmap}_scores.csv')
    
    elif algorithm == 'GreedyLookAhead':
        for run_nr in range(nr_of_runs):
            new_schedule = Schedule(railmap)
            greedy_lookahead_schedule = GreedyLookahead(new_schedule, max_time, max_trains, 3)
            greedy_lookahead_schedule.run()
            
            outputToFile(new_schedule, f'GreedyLookAhead {args.railmap} run number {run_nr + 1}', f'data/output/greedy_lookahead/greedylookahead_{args.railmap}_output.csv')
            routesToFile(new_schedule, f'GreedyLookAhead {args.railmap} run number {run_nr + 1}', f'data/output/greedy_lookahead/greedylookahead_{args.railmap}_routes.csv')
            scoresToFile(new_schedule, run_nr, f'data/output/greedy_lookahead/greedylookahead_{args.railmap}_scores.csv')
    
    elif algorithm == 'HillClimber':
        for run_nr in range(nr_of_runs):
            new_schedule = Schedule(railmap)
            random_schedule = Random(new_schedule, max_time, max_trains)
            random_schedule.run()
            hillclimber_schedule = HillClimber(new_schedule, max_trains, max_time)
            hillclimber_schedule.run(iterations, changes)

            outputToFile(new_schedule, f'HillClimber {args.railmap} run number {run_nr + 1}', f'data/output/hillclimber/hillclimber_{args.railmap}_output.csv')
            routesToFile(new_schedule, f'HillClimber {args.railmap} run number {run_nr + 1}', f'data/output/hillclimber/hillclimber_{args.railmap}_routes.csv')
            scoresToFile(new_schedule, run_nr, f'data/output/hillclimber/hillclimber_{args.railmap}_scores.csv')
            outputHillClimberGraph(hillclimber_schedule.iterations_listPoints, hillclimber_schedule.scoresPoints, hillclimber_schedule.iterations_list, hillclimber_schedule.scores, f'HillClimber {args.railmap} run number {run_nr + 1}', f'data/output/hillclimber/hillclimber_{args.railmap}_graph.csv')
    
    elif algorithm == 'HcStopCondition':
        for run_nr in range(nr_of_runs):
            new_schedule = Schedule(railmap)
            random_schedule = Random(new_schedule, max_time, max_trains)
            random_schedule.run()
            hcstopcondition_schedule = HcStopCondition(new_schedule, max_time, max_trains, cap)
            hcstopcondition_schedule.run(iterations, changes)

            outputToFile(new_schedule, f'HcStopCondition {args.railmap} run number {run_nr + 1}', f'data/output/hillclimber/hcstopcondition_{args.railmap}_output.csv')
            routesToFile(new_schedule, f'HcStopCondition {args.railmap} run number {run_nr + 1}', f'data/output/hillclimber/hcstopcondition_{args.railmap}_routes.csv')
            scoresToFile(new_schedule, run_nr, f'data/output/hillclimber/hcstopcondition_{args.railmap}_scores.csv')
            outputHillClimberGraph(hcstopcondition_schedule.iterations_listPoints, hcstopcondition_schedule.scoresPoints, hcstopcondition_schedule.iterations_list, hcstopcondition_schedule.scores, f'HcStopCondition {args.railmap} run number {run_nr + 1}', f'data/output/hillclimber/hcstopcondition_{args.railmap}_graph.csv')
    
    elif algorithm == 'Termini_HillClimber':
        for run_nr in range(nr_of_runs):
            new_schedule = Schedule(railmap)
            random_schedule = Random(new_schedule, max_time, max_trains)
            random_schedule.run()
            termini_hillclimber_schedule = Termini_HillClimber(new_schedule, max_trains, max_time)
            termini_hillclimber_schedule.run(iterations, changes)

            outputToFile(new_schedule, f'Termini_HillClimber {args.railmap} run number {run_nr + 1}', f'data/output/hillclimber/termini_hillclimber_{args.railmap}_output.csv')
            routesToFile(new_schedule, f'Termini_HillClimber {args.railmap} run number {run_nr + 1}', f'data/output/hillclimber/termini_hillclimber_{args.railmap}_routes.csv')
            scoresToFile(new_schedule, run_nr, f'data/output/hillclimber/termini_hillclimber_{args.railmap}_scores.csv')
            outputHillClimberGraph(termini_hillclimber_schedule.iterations_listPoints, termini_hillclimber_schedule.scoresPoints, termini_hillclimber_schedule.iterations_list, termini_hillclimber_schedule.scores, f'Termini_HillClimber {args.railmap} run number {run_nr + 1}', f'data/output/hillclimber/termini_hillclimber_{args.railmap}_graph.csv')
    
    elif algorithm == 'DepthFirst':
        for run_nr in range(nr_of_runs):
            new_schedule = Schedule(railmap)
            depthfirst_schedule = DepthFirst(new_schedule, max_time, max_trains)
            depthfirst_schedule.run()
            
            outputToFile(new_schedule, f'DepthFirst {args.railmap} run number {run_nr + 1}', f'data/output/depthfirst/depthfirst_{args.railmap}_output.csv')
            routesToFile(new_schedule, f'DepthFirst {args.railmap} run number {run_nr + 1}', f'data/output/depthfirst/depthfirst_{args.railmap}_routes.csv')
            scoresToFile(new_schedule, run_nr, f'data/output/depthfirst/depthfirst_{args.railmap}_scores.csv')