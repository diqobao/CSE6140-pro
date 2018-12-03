#import BranchAndBound
import MSTApprox as MST
import SimulatedAnnealing as SA
#import Local2
from os.path import isfile
from math import sqrt
import argparse
import sys
import dataparse
import LocalSearch
from dataparse import getdis


class AllWrapper:
    def __init__(self, filename):
        self.file = filename

    def TSP(self, instance='Atlanta', algorithm='BnB', seed=1, cutoff=600):

        if algorithm == 'BnB':
        ## TODO 
            pass

        elif algorithm == 'MSTApprox':
            G = getdis(self.file)
            mst = MST.MSTApprox(graph = G, instance = instance, seed = seed, cutoff=cutoff)
            mst.output()

        elif algorithm == 'SA':
        ## TODO
            data = getdis(self.file)
            sa = SA.SimulatedAnnealing(data=data, cutoff=cutoff, random_seed=seed, city = instance)
            path_best, cost_best, time = sa.solve(verbose=False, check_point=False, filename=file)
            sa.output(path_best, cost_best)


        elif algorithm == 'LS2':
            lc = LocalSearch.localsearch(city=instance, seedNo=seed, time_limit=cutoff)
            lc.main()


        else:
            return None


def main():

    # Argument parser for taking in values from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('-inst', type=str, dest="instance", default='Atlanta', help='The name of the city')
    parser.add_argument('-alg', type=str, dest="algorithm", default='bnb', help='The name of the algorithm')
    parser.add_argument('-seed', type=int, dest="seed", default=1, help='Randomized seed value')
    parser.add_argument('-time', type=int, dest="cutoff", default=1, help='The cutoff time')
    args = parser.parse_args()

    # Checking if the input file exists
    filename = "./DATA/{}.tsp".format(args.instance)
    if not isfile(filename):
        print("The file doesn't exist, please enter the correct name.")
        sys.exit(1)

    ## Try different algorithms
    Wrapper = AllWrapper(filename)
    kwargs = vars(args).copy()
    Wrapper.TSP(args.instance, args.algorithm, args.seed, args.cutoff)

if __name__ == '__main__':
    main()
