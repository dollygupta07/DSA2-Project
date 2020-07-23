import copy
import math
import random
import os


# The Karger's Mincut algorithm
def MinCut(graph: dict, t: int):
    '''
    Input:
        graph: A dictionary having the vertices and the corresponding edges
        t: An integer which keeps track of upto when MinCut should be run recursively
    Output:
        graph: The modified graph, after removing the edge and merging the 2 vertices it connected
    Variables:
        start: A randomly chosen vertex from the graph
        end: An other random vertex which makes an edge with start in the graph
        mincut: Hold the current value of mincut (no of cutting edges) in various iterations of the algorithm
        cuts: A list which keeps track of all the mincut values in every iteration
    '''
    while len(graph) > t:
        start = random.choice(list(graph.keys()))
        finish = random.choice(graph[start])
        # print(start, finish)

        # Adding the edges from the absorbed node:
        for edge in graph[finish]:
            # Stops from making a self-loop
            if edge != start:  
                graph[start].append(edge)

        # Deleting the references to the absorbed node and changing them to the source node:
        for edge in graph[finish]:
            graph[edge].remove(finish)
            # Stops from re-adding all the edges in start
            if edge != start:
                graph[edge].append(start)
        del graph[finish]

    # Calculating and recording the mincut
    mincut = len(graph[list(graph.keys())[0]])
    cuts.append(mincut)
    # print(graph)
    return graph


# Karger-Stein's recursive Fast MinCut algorithm
def FastMinCut(graph: dict):
    '''
    Input:
        graph: A dictionary having the vertices and the corresponding edges
    Output:
        recursively calls the MinCut or FastMinCut methods based on the number 
        of vertices present in the graph
    Variables:
        t: An integer which keeps track of upto when FastMinCut should be run recursively
        graph_1 and graph_2: Contracted graphs returned by MinCut
    '''
    if len(graph) < 6:
        return MinCut(graph, 2)
    else:
        t = 1 + int(len(graph) / math.sqrt(2))
        graph_1 = MinCut(graph, t)
        graph_2 = MinCut(graph, t)
        if len(graph_1) > len(graph_2):
            return FastMinCut(graph_2)
        else:
            return FastMinCut(graph_1)

# return min(FastMinCut(graph_1), FastMinCut(graph_2))

# Main Driver function
def main(filename):
    graph_file = open(filename)
    graph = {}
    global cuts
    cuts = []
    edge_num = 0
    edge_list = []

    print(f"Loading graph from: {filename}")

    for line in graph_file:
        node = int(line.split()[0])
        edges = []
        for edge in line.split()[1:]:
            edges.append(int(edge))
        graph[node] = edges
        edge_num = edge_num + len(edges)
        edge_list.append(len(edges))
    graph_file.close()

    print(f"Graph initialized!\n")

    # Print the general info of the graph
    print("Total edges:     ", edge_num / 2)
    print("Total vertices:  ", len(graph))
    print("Maximum degree:  ", max(edge_list))
    print("Minimum degree:  ", min(edge_list))
    print("Average degree:  ", sum(edge_list) / len(edge_list))

    # Creating the adjacency matrix of the graph (for refrence)
    f = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/matrix.txt'), 'w')
    for j in range(1, len(graph) + 1):
        for i in range(1, 201):
            if i not in graph[j]:
                f.write('0 ')
            else:
                f.write('1 ')
        f.write('\n')
    f.close()

    count = 200
    i = 0
    while i < count:
        graph1 = copy.deepcopy(graph)
        g = FastMinCut(graph1)
        i += 1

    print("\nResults")
    print('-'*20)
    print("Running times: ", len(cuts))
    print("Mincut of the graph is: ", min(cuts))
