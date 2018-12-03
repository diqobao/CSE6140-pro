"""
MST Approximation

"""

import numpy as np
import sys
import time
from dataparse import getdis


class MSTApprox:

    def __init__(self, instance, graph, cutoff=600, randomseed = 1):
        self.city = instance
        self.G = graph
        self.time_cutoff = cutoff
        self.random_seed = randomseed
        self.tour = []
        self.total_dist = 0.0

    """
    MSTtsp(self):
    Firstly, use Prim's Algorithm to generate MST. Then double the MST to get a full walk.
    
    A full walk lists all vertices when they are first visited in preorder,
    it also lists vertices when they are returned after a subtree is visited in preorder. 
    
    """

    def MSTtsp(self):
        MST = []
        visited = [0]
        Graph = np.array(self.G)
        n = len(self.G)

        while len(visited) < n:
            (row, col) = np.unravel_index(Graph[visited].argmin(), Graph[visited].shape)
            ## find the minimum path length from current node to next node
            ## (row, col) is the position of the next node

            visited.append(col)
            ## add the node which has the minimum path length from the current node

            MST.append((visited[row], col))
            ## update the path

            visited_edge = [(v, col) for v in visited]
            ## record the visited edge.

            for (u,v) in visited_edge:
            ## set the length of visited edge to infinite to avoid add duplicate path
                Graph[u][v] = float("inf")
                Graph[v][u] = float("inf")

        returnMST = [(v, u) for (u, v) in MST]
        # According to the property of MST approximation, an edge will be visited double times to complete a full walk.

        MST.extend(returnMST)

        return MST

    """
    tour_generator(self, MST, parent):
    use preorder to generate the order of the travel path.
    depth first search in the tree and output each node the first time that you enter it.
    
    """
    def tour_generator(self, MST, r):
        if r not in self.tour:
            self.tour.append(r)
            ## for the current node, find its next node then append it to the path.
            next = [node[1] for node in MST if node[0] == r]
            if len(next) > 0:
                for n in next:
                    self.tour_generator(MST, n)
            return

    """
    def travel(self):

    Traverse the tour we generated, and sum up the distance to get the total distance of this tour.
    Note that we need to return to the start node to complete the tour,
    we use  "final_dist" variable for the distance of this path.

    """
    def travel(self):
        for i in range(0,len(self.tour)-1):
            dist = self.G[self.tour[i]][self.tour[i+1]]
            self.total_dist += dist
        final_dist = self.G[self.tour[-1]][self.tour[0]]
        self.total_dist+=final_dist

    """
    def write_sol(self):

    Output the solution to the Output document.
    The first line of output file is the total distance of the tour.
    The second line of the output file is the tour v1, v2, ..., vn. Each node is separated by ','.
    
    """

    def write_sol(self):
        total_dist = (str)((int)(self.total_dist))
        with open(self.city + "_MSTApprox_" + str(self.time_cutoff) + '.sol',
                  'w') as f:
            f.write(total_dist)
            f.write('\n')
            data = (",".join(str(i) for i in self.tour))
            f.write(str(data))

    """
    def write_sol(self):

    Output the trace to the Output document.
    The MSTApprox is not randomized, hence we only output one line into the file.
    The data is the runtime of the method and the total distance of the tour.

    """
    def write_trace(self, runtime):
        total_dist = (str)((int)(self.total_dist))
        with open(self.city + "_MSTApprox_" + str(self.time_cutoff) +'.trace','w') as f:
            f.write('{:.2f} {}\n'.format(runtime, total_dist))

    """
    def out(self):

    It's an overall output function for executing the method and generating results.

    """
    def output(self):
        start = time.time() * 1000
        self.total_dist = 0.0
        self.tour = []
        MST = self.MSTtsp()
        self.tour_generator(MST, self.random_seed)
        self.travel()
        runtime = (time.time() * 1000) - start
        if runtime > self.time_cutoff:
            print("runtime > 10 mins! ")
        self.write_trace(runtime)
        self.write_sol()

    """
    def main():

    Main function.
    Run this program in CMD, input 
    >>python MSTApprox.py <city>
    Then a .sol file and a .trace file are generated in the current directory.

    """
def main():

    num_args = len(sys.argv)

    if num_args < 2:
        print("error: not enough input arguments")
        exit(1)

    city = sys.argv[1]

    filename = "./DATA/DATA/{}.tsp".format(city)
    G = getdis(filename)
    mst = MSTApprox(instance = city, graph = G)
    mst.output()

if __name__ == '__main__':
    main()
